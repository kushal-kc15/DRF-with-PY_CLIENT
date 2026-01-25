from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from . import validators
from api.serializers import UserPublicSerializer

class ProductInlineSerializer(serializers.Serializer):
  url=serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )
  title=serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user',read_only=True)
    related_products=ProductInlineSerializer(source='user.product_set.all',read_only=True,many=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    
    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'edit_url',
            'pk',
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
            'related_products'
        ]

    def get_user(self, obj):
        return obj.user.username if obj.user else None

    def validate_title(self, value):
        request = self.context.get('request')
        user = request.user
        qs = Product.objects.filter(user=user, title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name.")
        return value

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'get_discount_price'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount_price()
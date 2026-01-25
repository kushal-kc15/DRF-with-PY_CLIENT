from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from . import validators


class ProductSerializer(serializers.ModelSerializer):
  my_discount=serializers.SerializerMethodField(read_only=True)
  edit_url=serializers.SerializerMethodField(read_only=True)
  url=serializers.HyperlinkedIdentityField(
    view_name="product-detail",
    lookup_field="pk"
    )
  title=serializers.CharField(validators=[validators.validate_title_no_hello,validators.unique_product_title])
  # name=serializers.CharField(source='title',read_only=True)
  class Meta:
    model = Product
    fields = ['url','edit_url','pk','id','title', 'content', 'price','sale_price','my_discount']
  
  def validate_title(self,value):
    request=self.context.get('request')
    user=request.user
    qs=Product.objects.filter(user=user,title__iexact=value)
    if qs.exists():
      raise serializers.ValidationError("This title has already been used")
    return value

  def get_edit_url(self,obj):
    request=self.context.get('request')
    if request is None:
      return None
    return reverse("product-detail",kwargs={"pk":obj.pk},request=request)
    # return request.build_absolute_uri(obj.get_api_url())

  def get_my_discount(self,obj):
    if not hasattr(obj,'get_discount_price'):
      return None
    if not isinstance(obj,Product):
      return None
    return obj.get_discount_price()
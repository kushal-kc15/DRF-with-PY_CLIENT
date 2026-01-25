from rest_framework import generics
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    UserQuerySetMixin,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or title
        serializer.save(user=self.request.user, content=content)

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(    
    StaffEditorPermissionMixin,
    UserQuerySetMixin,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    UserQuerySetMixin,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            instance.save() # Fixed: Added missing save()

product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    UserQuerySetMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()
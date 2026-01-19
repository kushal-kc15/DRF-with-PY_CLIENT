from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
  queryset=Product.objects.all()
  serializer_class=ProductSerializer
  #lookup_field="pk"
  
class ProductListCreateView(generics.ListCreateAPIView):
  queryset=Product.objects.all()
  serializer_class=ProductSerializer

  def perform_create(self,serializer):
    title=serializer.validated_data.get("title")
    content=serializer.validated_data.get("content") or None
    if content is None:
      content=title
    serializer.save(content=content)


#not using this method instead we are using ProductListCreateView above
class ProductListView(generics.ListAPIView):
  queryset=Product.objects.all()
  serializer_class=ProductSerializer

from rest_framework import mixins,viewsets
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):

  """
  get->list-> queryset
  get->retrieve-> queryset
  post->create-> queryset
  put->update-> queryset
  patch->partial_update-> queryset
  delete->destroy-> queryset
  """
  queryset=Product.objects.all()
  serializer_class=ProductSerializer
  lookup_field="pk" #default


class ProductGenericViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
 queryset=Product.objects.all()
 serializer_class=ProductSerializer
 lookup_field="pk"
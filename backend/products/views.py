from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework import mixins,permissions,authentication
from .permissions import IsStaffEditorPermission
from api.authentication import TokenAuthentication

#generics view
# class ProductListCreate(generics.ListCreateAPIView):
#   queryset=Product.objects.all()
#   serializer_class=ProductSerializer

#   def perform_create(self,serializer):
#     title=serializer.validated_data.get("title")
#     content=serializer.validated_data.get("content") or None
#     if content is None:
#       content=title
#     serializer.save(content=content)

# class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#   queryset=Product.objects.all()
#   serializer_class=ProductSerializer
#   lookup_field="pk"

#   def perform_update(self,serializer):
#     instance=serializer.save()
#     if instance.title and not instance.content:
#       instance.content=instance.title
#     instance.save()

#not using this method instead we are using ProductListCreateView above
# class ProductListView(generics.ListAPIView):
#   queryset=Product.objects.all()
#   serializer_class=ProductSerializer

class ProductListCreateView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
  queryset=Product.objects.all()
  serializer_class=ProductSerializer
  authentication_classes=[
    authentication.SessionAuthentication,
    TokenAuthentication,
    ]
  permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]

  def get(self,request,*args,**kwargs):
    return self.list(request,*args,**kwargs)  

  def post(self,request,*args,**kwargs):
    return self.create(request,*args,**kwargs)  


#Mixin and generic api view
class ProductRetrieveUpdateDestroyView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
  queryset=Product.objects.all()
  serializer_class=ProductSerializer
  lookup_field="pk"
  

  def get(self,request,*args,**kwargs):
    return self.retrieve(request,*args,**kwargs)  

  def put(self,request,*args,**kwargs):
    return self.update(request,*args,**kwargs)  

  def delete(self,request,*args,**kwargs):
    return self.destroy(request,*args,**kwargs)   
    
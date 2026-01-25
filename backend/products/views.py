from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermission

class ProductListCreateView(generics.ListCreateAPIView):
    """
    Handles List (GET) and Create (POST) operations.
    Restricted to Staff Editors.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer):
        # Auto-fill content with title if it's not provided
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or title
        serializer.save(content=content)

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles Retrieve (GET), Update (PUT/PATCH), and Destroy (DELETE) operations.
    Using 'pk' as the lookup field.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            instance.save()
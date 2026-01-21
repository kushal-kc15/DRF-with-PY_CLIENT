from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDestroy

urlpatterns=[
    path("", ProductListCreateView.as_view(), name='product-list-create'),
    path("<int:pk>/", ProductRetrieveUpdateDestroy.as_view(), name='product-detail'),
]

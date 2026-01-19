from django.urls import path
from .views import ProductDetailView,ProductListCreateView

urlpatterns=[
    path("<int:pk>/",ProductDetailView.as_view()),
    path("",ProductListCreateView.as_view())
]

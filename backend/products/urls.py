from django.urls import path
from .views import ProductDetailView,ProductCreateView

urlpatterns=[
    path("<int:pk>/",ProductDetailView.as_view()),
    path("create/",ProductCreateView.as_view())
]

from django.urls import path
from . import views
#from .views import api_view
urlpatterns=[
  path('',views.api_home)#localhost:8000/api/
]
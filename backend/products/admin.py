from django.contrib import admin
from . models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
  list_display=['title','content','price']
  list_filter=['price']
  search_fields=['title','content']
admin.site.register(Product,ProductAdmin)
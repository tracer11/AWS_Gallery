from django.urls import path
from .views import ProductList

urlpaths = {
  path('products', ProductList.as_view())
}
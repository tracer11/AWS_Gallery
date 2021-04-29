from django.shortcuts import render
from rest_framework import generics
from .models import Product, Category, Seller
from .serializers import ProductSerializer, CategorySerilaizer, SellerSerializer
from rest_framework.response import Response

# Create your views here.

class ProductList(generics.ListCreateApiView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Category(models.Model):
  
  name = models.CharField(max_length=250)

class Seller(models.Model):
  
  name = models.CharField(max_length=250)

class Product(models.Model):

  photo = models.URLField(max_length=500)
  asin = models.CharField(unique=True, max_length=100)
  seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='products')
  price = models.FloatField(validators=[MinValueValidator(0)])
  title = models.CharField(max_length=500)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
  updated = models.DateTimeField(auto_now_add=True)

    
    
from rest_framework.serializers import ModelSerializer, SerializersMethodField
from .models import Category, Seller, Product

class CategorySerilaizer(ModelSerializer):
  
  photo = SerializersMethodField()

  def get_photo(self, obj):
    try:
      return obj.products.first().photo
    except:
      return ''
  class Meta:
    model = Category
    fields = ['__all__']



class SellerSerializer(ModelSerializer):
 class Meta:
  model = Category
  fields = ['__all__']


class ProductSerializer(ModelSerializer):
  category = CategorySerilaizer()
  seller = SellerSerializer()

  fields = ['__all__']
 
    

    
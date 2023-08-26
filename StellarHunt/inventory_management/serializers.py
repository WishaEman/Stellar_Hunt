from .models import Category, Product, Subcategory
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    """ Serializer for the Category model.  """

    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    """ Serializer for the Subcategory model.   """

    class Meta:
        model = Subcategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """ Serializer for the Product model.   """

    subcategory = SubcategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'subcategory', 'title', 'description', 'price', 'available', 'image', 'quantity']

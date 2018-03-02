from rest_framework import serializers
from productos.models import Products, ProductsDetail 

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class ProductsDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsDetail
        fields = '__all__'
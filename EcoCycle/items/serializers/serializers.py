from rest_framework import serializers
from items.models import Products, ProductImages


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ('id', 'images')

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Products
        fields = '__all__'


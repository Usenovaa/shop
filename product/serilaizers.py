from rest_framework import serializers
from .models import Category, Product, ProductImage

class CategorySerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['images'] = ProductImageSerilaizer(instance.images.all(), many=True).data
        return representation


class ProductListSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'image', 'price')


class ProductImageSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
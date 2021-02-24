from rest_framework import serializers
from parser_site.models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = '__all__'


class ProductSubCategorySerializer(serializers.ModelSerializer):

    product = serializers.SerializerMethodField()

    class Meta:
        model = Subcategory
        fields = '__all__'

    @staticmethod
    def get_product(obj):
        return ProductSerializer(CardProduct.objects.filter(subcategory=obj), many=True).data


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CardProduct
        fields = '__all__'


class ProductListRetrieveSerializer(serializers.ModelSerializer):

    subcategory = SubCategorySerializer(many=True, read_only=True)


    class Meta:
        model = CardProduct
        fields = '__all__'


class SubCategoryListRetrieveSerializer(serializers.ModelSerializer):

    category = CategorySerializer()


    class Meta:
        model = Subcategory
        fields = '__all__'

from rest_framework import serializers
from .models import Product, Category, Tag



class ProductSerializer(serializers.ModelSerializer):
    # tags = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = 'title category price description tags'.split()

    # def get_tags(self, product):
    #     return [i.name for i in product.tags.all()]

    # def get_tags(self, product):
    #     l = []
    #     for i in product.tags.all():
    #         l.append(i.name)
    #
    #     return l

class CategorySerializer(serializers.ModelSerializer):
    models = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = 'id name models'.split()








from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Product, Category, Tag



class ProductSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = 'title category price description tags'.split()

    def get_tags(self, product):
        return [i.name for i in product.tags.all()]

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


class ProductCreateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=100)
    description = serializers.CharField(min_length=2, max_length=100)
    price = serializers.IntegerField()
    category_id = serializers.IntegerField()
    tags = serializers.ListField(child=serializers.IntegerField())


    def validate_title(self, title):
        print(title)
        products = Product.objects.filter(title=title)
        if products.count() > 0:
            raise ValidationError('Takoi product uje sushestvuet')

    def validate(self, attrs):
        id = attrs['category_id']
        if Category.objects.filter(id=id).count() == 0:
             raise ValidationError('Incorrect Category')
        return attrs

class ProductUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=100)
    description = serializers.CharField(min_length=2, max_length=100)
    price = serializers.IntegerField()
    category_id = serializers.IntegerField()
    tags = serializers.ListField(child=serializers.IntegerField())


    def validate_title(self, title):
        print(title)
        products = Product.objects.filter(title=title)
        if products.count() > 0:
            raise ValidationError('Takoi product uje sushestvuet')

    def validate(self, attrs):
        id = attrs['category_id']
        if Category.objects.filter(id=id).count() == 0:
             raise ValidationError('Incorrect Category')
        return attrs

class LoginValidateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)


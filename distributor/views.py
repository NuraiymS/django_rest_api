
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response

from .models import Category, Tag, Product
# Create your views here.



# def product_list_view(request):
#     products = Product.objects.all()
#     product_list = []
#     for i in products:
#         product_list.append(
#             {
#                 'title': i.title,
#                 'description': i.description,
#                 'price': i.price,
#                 'category': i.category,
#             }
#         )
#     data = {
#         'title': product_list
#     }
#     return JsonResponse(data=data, safe=False)


from rest_framework.decorators import api_view
from .serializers import ProductSerializer, CategorySerializer


# @api_view(['GET', 'POST'])
# def product_rest_list_view(request):
#     products = Product.objects.all()
#     data = ProductSerializer(products, many=True).data
#     return Response(data=data)

@api_view(['GET', 'POST'])
def product_rest_list_view(request):
    return Response(data=ProductSerializer(Product.objects.all(), many=True).data)

@api_view(['GET'])

def product_item(request,id):
    products = Product.objects.get(id=id)
    data = ProductSerializer(products, many=False).data
    return Response(data=data)

@api_view(['GET', 'POST'])
def categories_list(request):
    categories = Category.objects.all()
    data = CategorySerializer(categories, many=True).data
    return Response(data=data)

@api_view(['GET'])
def categories_id(request, id):
    categories =Category.objects.get(id=id)
    data = CategorySerializer(categories).data
    return Response(data=data)



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
from .serializers import ProductSerializer


# @api_view(['GET', 'POST'])
# def product_rest_list_view(request):
#     products = Product.objects.all()
#     data = ProductSerializer(products, many=True).data
#     return Response(data=data)

@api_view(['GET', 'POST'])
def product_rest_list_view(request):
    return Response(data=ProductSerializer(Product.objects.all(), many=True).data)

@api_view(['GET', 'POST'])
def product_item(request):
    products = Product.objects.all(id=id)
    data = ProductSerializer(products, many=True).data
    return Response(data=data)
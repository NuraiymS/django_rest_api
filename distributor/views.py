
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
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


from rest_framework.decorators import api_view, permission_classes
from .serializers import ProductSerializer, CategorySerializer, ProductCreateSerializer, ProductUpdateSerializer, \
    LoginValidateSerializer


# @api_view(['GET', 'POST'])
# def product_rest_list_view(request):
#     products = Product.objects.all()
#     data = ProductSerializer(products, many=True).data
#     return Response(data=data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def product_rest_list_view(request):
    if request.method == "GET":
        print(request.user)
        return Response(data=ProductSerializer(Product.objects.all(), many=True).data)
    elif request.method == "POST":
        serializer = ProductCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={
                    'message': 'error',
                    'errors': serializer.errors
                }
            )
        title = request.data['title']
        description = request.data['description']
        price = request.data['price']
        category_id = request.data['category_id']
        product = Product.objects.create(
            title=title, description=description, price=price,
             category_id=category_id)
        tags = request.data['tags']
        for i in tags:
            product.tags.add(i)
        product.save()
        return Response(data={'message': 'OK',
                              'product': ProductSerializer(product).data})


@api_view(['GET', 'PUT'])
def product_item(request,id):
    try:
        products = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'message': 'Takogo producta net'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ProductUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={
                    'message': 'error',
                    'errors': serializer.errors
                }
            )
        products.title = request.data['title']
        products.description = request.data['description']
        products.price = request.data['price']
        products.category_id = request.data['category_id']
        products.tags.clear()
        for i in request.data['tags']:
            products.tags.add(i)
        products.save()
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

@api_view(['POST'])
def test(request):
    title = request.data.get('title', 'Mango')
    Product.objects.create(title=title)
    return Response(data={'massage': 'received'})

from django.contrib import auth
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        serializer = LoginValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={
                    'message': 'error',
                    'errors': serializer.errors
                },
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        print(serializer.validated_data)
        user = auth.authenticate(**serializer.validated_data)
        if user:
            try:
                token = Token.objects.get(user=user)
                print('GET TOKEN')
            except Token.DoesNotExist:
                print('CREATE TOKEN')
                token = Token.objects.create(user=user)
            return Response(data={'key': token.key})
        else:
            return Response(
                data={'message': 'User not found!!!'},
                status=status.HTTP_404_NOT_FOUND
            )


            # Token.objects.filter(user=user).delete()   - ЭТОТ ИСПОЛЬЗУЕМ TOKEN ЕСЛИ НУЖЕН 1 ПОЛЬЗОВАТЕЛЬ - ОДНО ПРИЛОЖЕНИЕ
            # token = Token.objects.create(user=user)
            # return Response(data={'key': token.key})





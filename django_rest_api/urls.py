"""django_rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from distributor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/products/', views.product_list_view),
    path('api/v2/products/', views.product_rest_list_view),
    path('api/v1/product/<int:id>/', views.product_item),
    path('api/v3/categories/', views.categories_list),
    path('api/v1/categories/<int:id>/', views.categories_id),
    path('api/v1/test/', views.test),
    path('api/v1/login/', views.login)
]

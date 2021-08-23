from django.contrib import admin
from distributor.models import Category, Tag, Product
# Register your models here.

class CategoryModelInLine(admin.StackedInline):
    model = Category
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Category
    inLines = [CategoryModelInLine]




admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product, ProductAdmin)
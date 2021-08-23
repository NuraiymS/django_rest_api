from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, related_name= 'models',  on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    is_publish = models.BooleanField(default=True)

    def __str__(self):
        return self.title



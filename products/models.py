from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=64)
    sku = models.CharField(max_length=128)
    description = models.TextField()    
    image = CloudinaryField('image', blank=True, null=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

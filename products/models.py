from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=64)
    sku =  models.CharField(max_length=128)
    description = models.TextField()    
    image = CloudinaryField('image', blank=True, null=True)
    price = models.CharField(max_length=32)
    category = models.CharField(max_length=64)


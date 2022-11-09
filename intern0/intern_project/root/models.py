from django.db import models

# Create your models here.
class Product(models.Model):
    Product_Name = models.CharField(max_length=100)
    Price = models.IntegerField()
    Quantity = models.IntegerField()
    
    
from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.CharField(max_length=255)
    image_url = models.FileField(upload_to='media/images/')

    def __str__(self):
        return self.name
    
class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

    def __str__(self):
        return self.code

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image_url = models.FileField(upload_to='media/images/categories/')
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'



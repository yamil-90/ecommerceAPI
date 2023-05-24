from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=Product.objects.all())])
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    stock = serializers.IntegerField(min_value=0, max_value=1000)
    description = serializers.CharField(max_length=500)
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'stock', 'description', 'image_url')
        
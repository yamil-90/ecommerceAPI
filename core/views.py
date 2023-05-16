from django.shortcuts import render
from .models import Product
from rest_framework.views import APIView
import json
from .serializers import ProductSerializer
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ProductList(APIView):
    model = Product

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    
class ProductDetail(APIView):
    model = Product

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data, safe=False)

class ProductCreate(APIView, LoginRequiredMixin):
    model = Product

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False)
    
class ProductUpdate(APIView, LoginRequiredMixin):
    model = Product

    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False, status=400)
    
class ProductDelete(APIView, LoginRequiredMixin):
    model = Product

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return JsonResponse({'message': 'The product does not exist'}, status=404)
        product.delete()
        return JsonResponse({'message': 'Product was deleted successfully!'}, status=204)
    
class ProductUpdateStock(APIView, LoginRequiredMixin):
    model = Product

    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        stock = request.POST.get('stock')
        product.stock = int(stock)
        product.save()
        return JsonResponse({'message': f"Stock was updated successfully! new stock: {product.stock}"}, status=200)

    def put(self, request, pk):
        product = Product.objects.get(pk=pk)   
        stock = request.POST.get('stock')
        print(stock)
        product.stock += int(stock)
        product.save()
        return JsonResponse({'message': f"Stock was updated successfully! new stock: {product.stock}"}, status=200)
    
class CartBuy(APIView, LoginRequiredMixin):
    model = Product

    def post(self, request):
        body = request.body.decode('utf-8')
        cart = json.loads(body)
        cart = cart['items']
        for item in cart:
            product = Product.objects.get(pk=item['id'])
            product.stock -= item['quantity']
            if product.stock < 0:
                return JsonResponse({'message': 'The product is out of stock'}, status=400)
            product.save()

        return JsonResponse({'message': 'purchase was successfull'}, safe=False)
    
    

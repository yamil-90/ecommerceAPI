from django.shortcuts import render
from ..models import Product
from rest_framework.views import APIView
import json
from ..serializers import ProductSerializer
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import sys
from rest_framework.parsers import MultiPartParser

# Create your views here.


class ProductList(APIView):
    model = Product

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        response = {
            'products': serializer.data,
            'message': f'user {request.user}'
        }
        return JsonResponse(response,  safe=False)
    
class ProductDetail(APIView):
    model = Product

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data, safe=False)

class ProductCreate(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    model = Product

    def post(self, request):
        print('idduno')
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'product created'}, safe=False)
        return JsonResponse(serializer.errors, safe=False, status=400)
    
class ProductUpdate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    model = Product

    def patch(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False)

    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False, status=400)
    
class ProductDelete(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    model = Product

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return JsonResponse({'message': 'The product does not exist'}, status=404)
        product.delete()
        return JsonResponse({'message': 'Product was deleted successfully!'}, status=204)
    
class ProductUpdateStock(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
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
    
class CartBuy(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
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
    
    

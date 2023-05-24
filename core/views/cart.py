from ..models import Product
from rest_framework.views import APIView
import json
from django.http import JsonResponse

def checkStock(cart):
    for item in cart:
        product = Product.objects.get(pk=item['id'])
        if product.stock < item['quantity']:
            return JsonResponse({
                'message': f'The product "{product.name}" is out of stock, delete it from cart and try again',
                'product': product.name
            }, status=400)


class CartBuy(APIView):
    model = Product

    def post(self, request):
        body = request.body.decode('utf-8')
        cart = json.loads(body)
        cart = cart['cart']
        checkStock(cart)
        total = 0
        for item in cart:
            product = Product.objects.get(pk=item['id'])
            total += product.price * item['quantity']
            product.stock -= item['quantity']
            product.save()

        return JsonResponse({
            'message': 'purchase was successfull',
            'total': total
            }, safe=False)
    
    

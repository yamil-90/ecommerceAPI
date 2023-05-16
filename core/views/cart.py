from ..models import Product
from rest_framework.views import APIView
import json
from django.http import JsonResponse


class CartBuy(APIView):
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
    
    

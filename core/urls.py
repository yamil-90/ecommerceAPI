from django.urls import path
from .views import products, cart, login


app_name = 'core'

urlpatterns = [
    path('products', products.ProductList.as_view(), name='product_list'),
    path('products/<int:pk>', products.ProductDetail.as_view(), name='product_detail'),
    path('products/create', products.ProductCreate.as_view(), name='product_create'),
    path('products/<int:pk>/update', products.ProductUpdate.as_view(), name='product_update'),
    path('products/<int:pk>/stock/update', products.ProductUpdateStock.as_view(), name='product_update_stock'),
    path('products/<int:pk>/delete', products.ProductDelete.as_view(), name='product_delete'),
    path('cart/buy', cart.CartBuy.as_view(), name='cart_buy'),
    path('login', login.Login.as_view(), name='login'),
    path('restricted', login.RestrictedView.as_view(), name='restricted'),
]
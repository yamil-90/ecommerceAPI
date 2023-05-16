from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('products', views.ProductList.as_view(), name='product_list'),
    path('products/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('products/create', views.ProductCreate.as_view(), name='product_create'),
    path('products/<int:pk>/update', views.ProductUpdate.as_view(), name='product_update'),
    path('products/<int:pk>/stock/update', views.ProductUpdateStock.as_view(), name='product_update_stock'),
    path('products/<int:pk>/delete', views.ProductDelete.as_view(), name='product_delete'),
    path('cart/buy', views.CartBuy.as_view(), name='cart_buy'),

]
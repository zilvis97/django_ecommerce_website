from django.urls import path
from .views import item_list, checkout_page, products_page

app_name = 'core'

urlpatterns = [
    path('', item_list, name='item-list'),
    path('/checkout/', checkout_page, name='checkout-page'),
    path('/products/', products_page, name='product-page')
]
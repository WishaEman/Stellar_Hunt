from django.urls import path

from .views import (AddToCartView, CartItemDetailView, CartItemListView,
                    CheckoutView, TotalQuantityAPIView)

app_name = 'cart_handler'

urlpatterns = [
    path('cart-items/', CartItemListView.as_view(), name='cart-list'),
    path('cart-items/<int:product_id>/', CartItemDetailView.as_view(), name='cart-item-detail'),
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('total-quantity/', TotalQuantityAPIView.as_view(), name='total_quantity_api'),

]

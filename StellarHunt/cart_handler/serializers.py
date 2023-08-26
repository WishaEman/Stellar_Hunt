from rest_framework import serializers

from .models import Cart, CartItem

from inventory_management.models import Product
from inventory_management.serializers import ProductSerializer


class ListCartItemSerializer(serializers.ModelSerializer):
    """  Serializer for listing multiple CartItems, including related Product details. """

    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ('cart', 'product', 'quantity', 'subtotal')


class CartItemSerializer(serializers.ModelSerializer):
    """  Serializer for single CartItem, handles creation with associated Cart, Product, and quantity. """

    class Meta:
        model = CartItem
        fields = ('cart', 'product', 'quantity', 'subtotal')
        extra_kwargs = {
            'cart': {'read_only': True},
            'subtotal': {'read_only': True},
        }

    def create(self, validated_data):
        product_id = self.context['request'].data.get('product')
        quantity = self.context['request'].data.get('quantity', 1)

        user = self.context['request'].user

        if user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=user, completed=False)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product not found.")

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity = int(quantity)
        cart_item.save()

        return cart_item


class CartSerializer(serializers.ModelSerializer):
    """ Serializer for Cart model, including related CartItems and total_price field.   """

    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'completed', 'cart_items', 'total_price')

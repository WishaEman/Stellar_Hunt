from rest_framework import serializers

from .models import Cart, CartItem

from inventory_management.models import Product


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('cart', 'product', 'quantity', 'subtotal')
        extra_kwargs = {
            'cart': {'read_only': True},
            'subtotal': {'read_only': True}
        }

    def create(self, validated_data):
        product_id = self.context['request'].data.get('product')
        quantity = self.context['request'].data.get('quantity', 1)

        user = self.context['request'].user

        if user.is_authenticated:
            completed_cart = Cart.objects.filter(user=user, completed=True).first()
            if completed_cart:
                completed_cart.cartitem_set.all().delete()

            cart, created = Cart.objects.get_or_create(user=user, completed=False)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product not found.")

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if created:
            cart_item.quantity = int(quantity)
        else:
            cart_item.quantity += int(quantity)
        cart_item.save()

        return cart_item


class CartSerializer(serializers.ModelSerializer):
    """
     the cart_items attribute provides information about the
     related CartItem instances associated with the Cart.
    """

    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'completed', 'cart_items', 'total_price')

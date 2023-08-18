from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import Cart, CartItem, CartItemSerializer


class CartItemListView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_cart = Cart.objects.get(user=self.request.user, completed=False)
        return CartItem.objects.filter(cart=user_cart)


class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'product_id'

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        user_cart = Cart.objects.get(user=user, completed=False)
        return CartItem.objects.filter(cart=user_cart, product_id=product_id)


class AddToCartView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            cart = Cart.objects.get(user=user, completed=False)
            total_price = cart.total_price

            cart.completed = True
            cart.save()

            return Response({
                'message': 'Checkout successful',
                'total_price': total_price,
                'status': 200
            })
        except Cart.DoesNotExist:
            return Response({'message': 'No active cart found'}, status=400)

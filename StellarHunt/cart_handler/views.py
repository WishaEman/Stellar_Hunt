from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

from .serializers import Cart, CartItem, CartItemSerializer, ListCartItemSerializer


class CartItemListView(generics.ListAPIView):
    """ API view to list cart items for the authenticated user. """

    serializer_class = ListCartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_cart = Cart.objects.get(user=self.request.user, completed=False)
        return CartItem.objects.select_related('product').filter(cart=user_cart)


class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ API view to retrieve, update, and delete a specific cart item.  """

    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'product_id'

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        user_cart = Cart.objects.get(user=user, completed=False)
        return CartItem.objects.filter(cart=user_cart, product_id=product_id)


class AddToCartView(generics.CreateAPIView):
    """ API view to add a new item to the cart. """

    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CheckoutView(APIView):
    """ API view for the checkout process.  """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            cart = Cart.objects.get(user=user, completed=False)
            if cart.cartitem_set.count() > 0:
                cart.cartitem_set.all().delete()
                cart.save()
                return JsonResponse({
                    'message': 'Checkout successful',
                    'status': 200
                }, status=200)
            else:
                return JsonResponse({
                    'message': 'No Cart Items Selected',
                    'status': 400
                }, status=400)
        except Cart.DoesNotExist:
            return JsonResponse({
                'message': 'No active cart found',
                'status': 400
            }, status=400)


class TotalQuantityAPIView(APIView):
    """ API view to get the total quantity of items in the user's cart. """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            cart = Cart.objects.get(user=user, completed=False)
        except Cart.DoesNotExist:
            return Response({"totalQuantity": 0})

        total_quantity = sum(item.quantity for item in cart.cartitem_set.all())

        return Response({"totalQuantity": total_quantity})

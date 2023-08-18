import uuid

from django.db import models

from authentication.models import User
from inventory_management.models import Product


class Cart(models.Model):
    """
    The Cart model represents a user's shopping cart, associating it with a user
    """
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    completed = models.BooleanField(default=False)

    @property
    def total_price(self):
        return sum(item.subtotal for item in self.cartitem_set.all())


class CartItem(models.Model):
    """
    The CartItem model represents a product and its quantity in the cart
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.product.price * self.quantity
        super().save(*args, **kwargs)

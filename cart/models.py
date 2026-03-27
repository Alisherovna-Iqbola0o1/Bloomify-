from django.db import models
from django.conf import settings
from products.models import Product

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cart_items"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")  # bitta user bitta productni bir martadan ko'p qo‘shmasin

    def __str__(self):
        return f"{self.quantity} x {self.product.title} for {self.user.email}"

    @property
    def total_price(self):
        return self.product.price * self.quantity
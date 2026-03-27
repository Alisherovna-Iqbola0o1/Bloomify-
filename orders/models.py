from django.db import models
from django.conf import settings
from products.models import Product

class PaymentType(models.TextChoices):
    CASH = "cash", "Cash"
    CARD = "card", "Card"

class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(
        max_length=10,
        choices=PaymentType.choices,
        default=PaymentType.CASH
    )
    card_number = models.CharField(max_length=12, blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Automatic total_price calculation
        self.total_price = self.product.price * self.quantity
        if self.payment_type == PaymentType.CARD and not self.card_number:
            from rest_framework.exceptions import ValidationError
            raise ValidationError("Card number is required for card payments.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} by {self.user.email}"
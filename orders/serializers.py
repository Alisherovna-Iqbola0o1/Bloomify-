from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id", "user", "product", "quantity", "total_price",
            "payment_type", "card_number", "is_paid", "created_at", "updated_at"
        ]
        read_only_fields = ["id", "total_price", "is_paid", "created_at", "updated_at"]
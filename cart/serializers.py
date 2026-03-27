from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = ["id", "user", "product", "quantity", "total_price", "added_at"]
        read_only_fields = ["id", "user", "total_price", "added_at"]
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id", "category", "title", "slug", "description",
            "price", "image", "seen_count", "created_at", "updated_at"
        ]
        read_only_fields = ["id", "slug", "seen_count", "created_at", "updated_at"]
from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product", "quantity", "total_price", "payment_type", "is_paid", "created_at")
    list_filter = ("payment_type", "is_paid")
    search_fields = ("user__email", "product__title")
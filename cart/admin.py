from django.contrib import admin
from .models import Cart

# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product", "quantity", "total_price", "added_at")
    list_filter = ("user", "added_at", "product")
    search_fields = ("user__email", "product__title")
    readonly_fields = ("total_price", "added_at")
    ordering = ("-added_at",)
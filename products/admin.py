from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price", "seen_count", "created_at")
    list_filter = ("category",)
    search_fields = ("title", "category__name")
    prepopulated_fields = {"slug": ("title",)}
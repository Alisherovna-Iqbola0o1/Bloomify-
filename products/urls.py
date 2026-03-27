from django.urls import path
from .views import ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("create/", ProductCreateView.as_view(), name="product-create"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="product-detail"),
    path("<slug:slug>/update/", ProductUpdateView.as_view(), name="product-update"),
]
from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer

# Admin/Seller product yaratadi
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role not in ["admin", "seller"]:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("You do not have permission to create products.")
        serializer.save()

# Product list — barcha userlar ko‘radi
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

# Product detail
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    permission_classes = [permissions.AllowAny]

# Product update — Admin/Seller
class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user.role not in ["admin", "seller"]:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("You do not have permission to update products.")
        serializer.save()
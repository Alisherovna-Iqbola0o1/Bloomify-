from rest_framework import generics, permissions
from .models import Category
from .serializers import CategorySerializer

# Create your views here.

# Admin/Seller category yaratadi
class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role not in ["admin", "seller"]:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("You do not have permission to create categories.")
        serializer.save()

# Category list (all users)
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

# Category detail (optional)
class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"
    permission_classes = [permissions.AllowAny]
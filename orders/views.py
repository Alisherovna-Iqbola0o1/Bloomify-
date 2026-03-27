from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatic total_price handled in model save()
        serializer.save(user=self.request.user, is_paid=True)  # Simulate payment confirmed

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Faqat o‘z user’ning buyurtmalari ko‘rinadi
        return Order.objects.filter(user=self.request.user)
from django.urls import path
from .views import RegisterView, ProfileView, UserListView, UserTokenObtainView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="user-register"),
    path("profile/", ProfileView.as_view(), name="user-profile"),
    path("users/", UserListView.as_view(), name="user-list"),  # faqat  admin  uchun
    path("login/", UserTokenObtainView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
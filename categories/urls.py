from django.urls import path
from .views import CategoryCreateView, CategoryListView, CategoryDetailView

urlpatterns = [
    path("", CategoryListView.as_view(), name="category-list"),
    path("create/", CategoryCreateView.as_view(), name="category-create"),
    path("<slug:slug>/", CategoryDetailView.as_view(), name="category-detail"),
]
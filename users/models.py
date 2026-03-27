from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = "admin", "Admin"
        SELLER = "seller", "Seller"
        CUSTOMER = "customer", "Customer"
        USER = "user", "User"

    role = models.CharField(
        max_length=10,
        choices=RoleChoices.choices,
        default=RoleChoices.USER
    )
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)

    REQUIRED_FIELDS = ["email", "role"]

    def __str__(self):
        return f"{self.username} ({self.role})"
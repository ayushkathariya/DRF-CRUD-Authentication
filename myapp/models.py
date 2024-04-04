from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    objects = CustomUserManager()
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"id: {self.id} || email: {self.email}"


class Todo(models.Model):
    task = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"id:{self.id} || task: {self.task}"

from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


class CustomUserManager(BaseUserManager):
    """Manager for CustomUser model"""

    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_admin", True)

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    
    objects = CustomUserManager()  # Assign the custom manager

    def __str__(self):
        return self.username

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
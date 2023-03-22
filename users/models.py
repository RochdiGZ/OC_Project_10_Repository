# users/models.py
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    """The CustomUserManager class inherits from BaseUserManager class."""
    def create_user(self, email, password=None, first_name=None, last_name=None):
        if not email:
            raise ValueError('The given email must be set.')
        # Verify that email is valid with normalize_email method
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        # Modify the password with set_password method
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, first_name=None, last_name=None):
        user = self.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """The CustomUser class inherits from AbstractBaseUser class."""
    email = models.EmailField(max_length=128, unique=True, blank=False)
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)  # auto_now_add=True
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = "Utilisateur"

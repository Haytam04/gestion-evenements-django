from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, unique=True)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name="User"
        verbose_name_plural="Users"

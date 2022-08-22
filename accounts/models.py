from django.db import models
from django.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=200, blank=True, null=True)
    address = models.TextField
    photo = models.ImageField(null=True, blank=True, upload_to='users')

    class Meta:
        db_table = 'users'





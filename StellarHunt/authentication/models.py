from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)


class User(AbstractUser):
    """ Custom User model inheriting from AbstractUser  """
    full_name = models.CharField(
        max_length=255,
        blank=False,
        default=''
    )
    email = models.EmailField(
        unique=True,
        blank=False
    )
    address = models.CharField(
        max_length=200,
        blank=False
    )
    phone_number = models.CharField(
        max_length=11,
        blank=False
    )
    gender = models.CharField(
        max_length=10,
        blank=False,
        choices=GENDER_CHOICES)

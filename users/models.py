from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    title = models.CharField(max_length=120)
    # address_1 = models.DateField(default=date.today)
    # address_2 = models.CharField(
    #     widget=models.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    # # )
    # city = models.CharField()

    def __str__(self):
        return self.email

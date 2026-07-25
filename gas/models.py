from django.db import models
from django.contrib.auth.models import User


class GasBill(models.Model):

    PROVIDER_CHOICES = [
        ("Indane", "Indane"),
        ("HP Gas", "HP Gas"),
        ("Bharat Gas", "Bharat Gas"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    consumer_number = models.CharField(max_length=20)

    provider = models.CharField(
        max_length=30,
        choices=PROVIDER_CHOICES
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.consumer_number
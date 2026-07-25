from django.db import models
from django.contrib.auth.models import User


class Recharge(models.Model):

    OPERATOR_CHOICES = [
        ("Jio", "Jio"),
        ("Airtel", "Airtel"),
        ("Vi", "Vi"),
        ("BSNL", "BSNL"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    mobile_number = models.CharField(max_length=10)

    operator = models.CharField(
        max_length=20,
        choices=OPERATOR_CHOICES
    )

    amount = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mobile_number} - {self.operator}"
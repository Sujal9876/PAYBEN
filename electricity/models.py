from django.db import models
from django.contrib.auth.models import User


class ElectricityBill(models.Model):

    BOARD_CHOICES = [
        ("BSES", "BSES"),
        ("Tata Power", "Tata Power"),
        ("UPPCL", "UPPCL"),
        ("MSEB", "MSEB"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    consumer_number = models.CharField(max_length=20)

    board = models.CharField(
        max_length=30,
        choices=BOARD_CHOICES
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.consumer_number
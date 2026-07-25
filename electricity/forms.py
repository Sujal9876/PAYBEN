from django import forms
from .models import ElectricityBill


class ElectricityBillForm(forms.ModelForm):

    class Meta:

        model = ElectricityBill

        fields = [
            "consumer_number",
            "board",
            "amount",
        ]

        widgets = {

            "consumer_number": forms.TextInput(

                attrs={

                    "class": "form-control form-control-lg",

                    "placeholder": "Enter Consumer Number"

                }

            ),

            "board": forms.Select(

                attrs={

                    "class": "form-select form-select-lg"

                }

            ),

            "amount": forms.NumberInput(

                attrs={

                    "class": "form-control form-control-lg",

                    "placeholder": "Enter Bill Amount"

                }

            )

        }
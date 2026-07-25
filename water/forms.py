from django import forms
from .models import WaterBill


class WaterBillForm(forms.ModelForm):

    class Meta:

        model = WaterBill

        fields = [
            "provider",
            "consumer_number",
            "amount",
        ]

        widgets = {

            "provider": forms.Select(

                attrs={

                    "class": "form-select form-select-lg"

                }

            ),

            "consumer_number": forms.TextInput(

                attrs={

                    "class": "form-control form-control-lg",

                    "placeholder": "Enter Consumer Number"

                }

            ),

            "amount": forms.NumberInput(

                attrs={

                    "class": "form-control form-control-lg",

                    "placeholder": "Enter Bill Amount"

                }

            ),

        }
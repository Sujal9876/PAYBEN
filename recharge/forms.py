from django import forms
from .models import Recharge


class RechargeForm(forms.ModelForm):

    class Meta:
        model = Recharge

        fields = [
            "mobile_number",
            "operator",
            "amount",
        ]

        widgets = {

            "mobile_number": forms.TextInput(

                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Enter 10-digit Mobile Number"
                }

            ),

            "operator": forms.Select(

                attrs={
                    "class": "form-select form-select-lg"
                }

            ),

            "amount": forms.NumberInput(

                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Enter Recharge Amount"
                }

            ),

        }
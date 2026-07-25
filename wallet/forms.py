from django import forms


class AddMoneyForm(forms.Form):

    amount = forms.DecimalField(

        max_digits=10,

        decimal_places=2,

        min_value=1,

        widget=forms.NumberInput(

            attrs={

                "class": "form-control form-control-lg",

                "placeholder": "Enter Amount"

            }

        )

    )
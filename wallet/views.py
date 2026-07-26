from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Wallet
from .forms import AddMoneyForm


@login_required(login_url="/login/")
def wallet(request):

    wallet, created = Wallet.objects.get_or_create(
        user=request.user
    )

    return render(
        request,
        "wallet.html",
        {
            "wallet": wallet
        }
    )


@login_required(login_url="/login/")
def add_money(request):

    wallet, created = Wallet.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = AddMoneyForm(request.POST)

        if form.is_valid():

            wallet.balance += form.cleaned_data["amount"]

            wallet.save()

            return redirect("/wallet/")

    else:

        form = AddMoneyForm()

    return render(
        request,
        "add_money.html",
        {
            "form": form
        }
    )
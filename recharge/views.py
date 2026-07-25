from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import RechargeForm
from .models import Recharge
from wallet.models import Wallet


@login_required
def recharge(request):

    wallet, created = Wallet.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = RechargeForm(request.POST)

        if form.is_valid():

            recharge = form.save(commit=False)

            recharge.user = request.user

            amount = recharge.amount

            if wallet.balance < amount:

                return render(
    request,
    "recharge.html",
    {
        "form": form,
        "wallet": wallet,
        "error": "Insufficient Wallet Balance"
    }
)

            wallet.balance -= amount
            wallet.save()

            recharge.save()

            return redirect("/wallet/")

    else:

        form = RechargeForm()

    return render(
    request,
    "recharge.html",
    {
        "form": form,
        "wallet": wallet
    }
)


@login_required
def recharge_history(request):

    recharges = Recharge.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "recharge_history.html",
        {
            "recharges": recharges
        }
    )
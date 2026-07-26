from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import WaterBillForm
from .models import WaterBill
from wallet.models import Wallet


@login_required(login_url="/login/")
def water(request):

    wallet, created = Wallet.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = WaterBillForm(request.POST)

        if form.is_valid():

            bill = form.save(commit=False)

            bill.user = request.user

            if wallet.balance < bill.amount:

                return render(
                    request,
                    "water.html",
                    {
                        "form": form,
                        "error": "Insufficient Wallet Balance"
                    }
                )

            wallet.balance -= bill.amount
            wallet.save()

            bill.save()

            return redirect("/dashboard/")

    else:

        form = WaterBillForm()

    return render(
        request,
        "water.html",
        {
            "form": form
        }
    )
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ElectricityBillForm
from .models import ElectricityBill

from wallet.models import Wallet


@login_required
def electricity(request):

    wallet, created = Wallet.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = ElectricityBillForm(request.POST)

        if form.is_valid():

            bill = form.save(commit=False)

            bill.user = request.user

            if wallet.balance < bill.amount:

                return render(
                    request,
                    "electricity.html",
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

        form = ElectricityBillForm()

    return render(
        request,
        "electricity.html",
        {
            "form": form
        }
    )
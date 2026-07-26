from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from wallet.models import Wallet
from recharge.models import Recharge
from electricity.models import ElectricityBill
from water.models import WaterBill
from gas.models import GasBill


@login_required(login_url="/login/")
def profile(request):

    wallet, created = Wallet.objects.get_or_create(
        user=request.user
    )

    context = {

        "wallet": wallet,

        "recharge_count":
            Recharge.objects.filter(
                user=request.user
            ).count(),

        "electricity_count":
            ElectricityBill.objects.filter(
                user=request.user
            ).count(),

        "water_count":
            WaterBill.objects.filter(
                user=request.user
            ).count(),

        "gas_count":
            GasBill.objects.filter(
                user=request.user
            ).count(),

    }

    return render(
        request,
        "profile.html",
        context
    )
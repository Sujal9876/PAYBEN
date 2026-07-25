from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from recharge.models import Recharge
from electricity.models import ElectricityBill
from water.models import WaterBill
from gas.models import GasBill


@login_required
def transactions(request):

    recharge_list = Recharge.objects.filter(
        user=request.user
    )

    electricity_list = ElectricityBill.objects.filter(
        user=request.user
    )

    water_list = WaterBill.objects.filter(
        user=request.user
    )

    gas_list = GasBill.objects.filter(
        user=request.user
    )

    return render(
        request,
        "transactions.html",
        {
            "recharges": recharge_list,
            "electricity": electricity_list,
            "water": water_list,
            "gas": gas_list,
        },
    )
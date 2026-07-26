from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from itertools import chain
from operator import attrgetter

from .forms import RegisterForm

from wallet.models import Wallet
from recharge.models import Recharge
from electricity.models import ElectricityBill
from water.models import WaterBill
from gas.models import GasBill


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            return redirect("/login/")
        else:
            return render(request, "register.html", {
                "form": form
            })

    else:
        form = RegisterForm()

    return render(request, "register.html", {
        "form": form
    })


def login_user(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            next_url = request.GET.get("next")

            if next_url:
                return redirect(next_url)

            return redirect("/dashboard/")

        return render(request, "login.html", {
            "error": "Invalid username or password."
        })

    return render(request, "login.html")


@login_required(login_url="/login/")
def dashboard(request):

    wallet, created = Wallet.objects.get_or_create(
        user=request.user
    )

    recharge_count = Recharge.objects.filter(
        user=request.user
    ).count()

    electricity_count = ElectricityBill.objects.filter(
        user=request.user
    ).count()

    water_count = WaterBill.objects.filter(
        user=request.user
    ).count()

    gas_count = GasBill.objects.filter(
        user=request.user
    ).count()

    recent_transactions = sorted(
        chain(
            Recharge.objects.filter(user=request.user),
            ElectricityBill.objects.filter(user=request.user),
            WaterBill.objects.filter(user=request.user),
            GasBill.objects.filter(user=request.user),
        ),
        key=attrgetter("created_at"),
        reverse=True,
    )[:5]

    context = {
        "wallet": wallet,
        "recharge_count": recharge_count,
        "electricity_count": electricity_count,
        "water_count": water_count,
        "gas_count": gas_count,
        "recent_transactions": recent_transactions,
        "chart_labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "chart_data": [500, 1200, 700, 1500, 900, 2200],
    }

    return render(request, "dashboard.html", context)


def logout_user(request):
    logout(request)
    return redirect("/")
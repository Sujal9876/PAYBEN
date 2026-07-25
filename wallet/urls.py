from django.urls import path
from . import views

urlpatterns = [

    path("", views.wallet, name="wallet"),

    path(
        "add/",
        views.add_money,
        name="add_money"
    ),

]
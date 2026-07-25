from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.recharge,
        name="recharge"
    ),

    path(
        "history/",
        views.recharge_history,
        name="recharge_history"
    ),

]
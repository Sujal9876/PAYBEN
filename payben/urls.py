from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("accounts.urls")),

    path("recharge/", include("recharge.urls")),

    path("wallet/", include("wallet.urls")),

    path("electricity/", include("electricity.urls")),

    path("water/", include("water.urls")),

    path("gas/", include("gas.urls")),

    path("transactions/", include("transactions.urls")),

    path("profile/", include("profile_app.urls")),
]
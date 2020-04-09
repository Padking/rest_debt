from django.urls import path

from .views import DebtorView

app_name = "debt_api"


urlpatterns = [
    path('debtors/', DebtorView.as_view()),  # для GET, POST
    path('debtors/<int:pk>', DebtorView.as_view()),  # для PUT
]

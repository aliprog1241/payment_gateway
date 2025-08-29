from django.urls import path

from finance.views import ChargeWalletView, VerifyView

urlpatterns = [
    path('charge/', ChargeWalletView.as_view()),
    path('verify/', VerifyView.as_view()),

]
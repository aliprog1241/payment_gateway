from django.urls import path

from finance.views import ChargeWalletView, VerifyView, PaymentView, PaymenyGatewayView

urlpatterns = [
    path('charge/', ChargeWalletView.as_view()),
    path('verify/', VerifyView.as_view()),
    path('pay/<str:invoice_number>/', PaymentView.as_view(), name='payment-link'),
    path('pay/<str:invoice_number>/<str:gateway_code>/', PaymenyGatewayView.as_view(), name='payment-gateway'),


]
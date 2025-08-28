from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
from finance.forms import ChargeWalletForm
from finance.utils.zarinpal import zpal_request_handler, zpal_payment_checker


class ChargeWalletView(View):
    template_name = 'charge_wallet.html'
    form_class = ChargeWalletForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class()})


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            payment_link, authority = zpal_request_handler(
                settings.ZARINPAL['merchant_id'],
                form.cleaned_data['amount'],
                "wallet_charge",
                "miri03369@gmail.com",
                "",
                settings.ZARINPAL['gateway_callback_url']
            )

            if payment_link is not None:
                return redirect(payment_link)
        return render(request, self.template_name, {'form': form})


class VerifyView(View):
    template_name = 'callback.html'

    def get(self, request, *args, **kwargs):
        status = request.GET.get("Status")
        authority = request.GET.get("Authority")

        if status != "OK":
            return render(request, self.template_name, {
                "is_paid": False,
                "ref_id": None,
                "message": "❌ پرداخت انجام نشد یا توسط کاربر لغو شد."
            })

        amount = 10000

        is_paid, ref_id = zpal_payment_checker(
            settings.ZARINPAL["merchant_id"], amount, authority
        )

        return render(request, self.template_name, {
            "is_paid": is_paid,
            "ref_id": ref_id,
            "message": "✅ پرداخت موفق!" if is_paid else "❌ پرداخت ناموفق"
        })

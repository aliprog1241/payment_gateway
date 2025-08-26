from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
from finance.forms import ChargeWalletForm
from finance.utils import zpal_request_handler


class ChargeWalletView(View):
    template_name = 'charge_wallet.html'
    form_class = ChargeWalletForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class()})
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.views import View

import purchase
from package.models import Package
from purchase.models import Purchase


class PurchaseCrateView(LoginRequiredMixin, View):

    def get(self, request, package_id, *args, **kwargs):
        try:
            package = Package.objects.get(id=package_id)

        except Package.DoesNotExist:
            raise Http404


        purchase = Purchase.create(package, request.user)
        return render(request, 'purchase/create.html', {'purchase': purchase})


class PurchaseListView(View):
    def get( self, request, *args, **kwargs):
        purchases = Purchase.objects.all()
        return render(request, 'purchase/list.html', {'purchases': Purchases})

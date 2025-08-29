from django.shortcuts import render
from django.views import View

from package.models import Package


class PurchaseCrateView(View):

    def post(self, request, package_id, *args, **kwargs):
        try:
            package = Package.objects.get(id=package_id)



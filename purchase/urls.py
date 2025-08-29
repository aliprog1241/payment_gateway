from django.urls import path

from purchase.views import PurchaseCrateView

urlpatterns = [

    path('creat/<int:package_id>',  PurchaseCrateView.as_view(), name='create-purchase'),

]
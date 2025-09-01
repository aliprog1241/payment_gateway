from django.urls import path

from purchase.views import PurchaseCrateView, PurchaseListView

urlpatterns = [

    path('creat/<int:package_id>/',  PurchaseCrateView.as_view(), name='create-purchase'),
    path('list/',  PurchaseListView.as_view(), name='list-purchase'),

]
from django.urls import path

from purchase.views import PurchaseCrateView, purchases_list

urlpatterns = [

    path('creat/<int:package_id>/',  PurchaseCrateView.as_view(), name='create-purchase'),
    path('list/',  purchases_list, name='list-purchase'),
    path('list/<str:username>/',  purchases_list, name='list-purchase'),

]
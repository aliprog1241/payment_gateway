from  django.urls import path
from package.views import PricingView




urlpatterns = [
    path('pricing/', PricingView.as_view()),
]
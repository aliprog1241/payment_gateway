from  django.urls import path
from django.views.generic import TemplateView
from package.views import PricingView




urlpatterns = [
    path('pricing', PricingView.as_view()),
]
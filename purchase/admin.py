from multiprocessing.reduction import register

from django.contrib import admin
from django.contrib.admin import register

from purchase.models import Purchase


@register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['user', 'package', 'price', 'status']
    list_filter = ['status']


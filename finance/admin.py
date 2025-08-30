from django.contrib import admin
from django.contrib.admin import register

from finance.models import Gateway, Payment

admin.site.register(Payment)
admin.site.register(Gateway)

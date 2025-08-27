import json
import uuid
from django.db import models
from django.conf import settings
from django.template.defaultfilters import title
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from finance.utils.zarinpal import zpal_request_handler, zpal_payment_checker


class Gateway(models.Model):
    FUNCTION_SAMAN = "saman"
    FUNCTION_SHAPARAK = "shaparak"
    FUNCTION_FINOTECH = "finotech"
    FUNCTION_ZARRINPAL = "zarrinpal"
    FUNCTION_PARSIAN = "parsian"
    GATEWAY_FUNCTIONS = (
        (FUNCTION_SAMAN, _("Saman")),
        (FUNCTION_SHAPARAK, _("Shaparak")),
        (FUNCTION_FINOTECH, _("Finotech")),
        (FUNCTION_ZARRINPAL, _("Zarrinpal")),
        (FUNCTION_PARSIAN, _("Parsian")),
    )

    title = models.CharField(max_length=100, verbose_name=_("gateway title"))
    gateway_request_url = models.CharField(
        max_length=150, verbose_name=_("request url"), null=True, blank=True
    )
    gateway_verify_url = models.CharField(
        max_length=150, verbose_name=_("verify url"), null=True, blank=True
    )
    gateway_code = models.CharField(
        max_length=12, verbose_name=_("gateway code"), choices=GATEWAY_FUNCTIONS
    )
    is_enable = models.BooleanField(verbose_name=_("is enabled"), default=True)
    auth_data = models.TextField(verbose_name=_("auth data"), null=True, blank=True)


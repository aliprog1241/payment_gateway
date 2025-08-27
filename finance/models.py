import json
import uuid

from django.conf import settings
from django.utils import timezone
from django.db import models

from finance.utils import zpal_request_handler, zpal_payment_checker



class Gateway(models.Model):

    
    FUNCTION_SAMAN = 'saman'
    FUNCTION_SHAPARAK = 'shaparak'
    FUNCTION_FINOTECH = 'fintech'
    FUNCTION_ZARINPAL = 'zarinpal'
    FUNCTION_PARSIAN = 'parsian'
    FUNCTION_SAMAN = 'saman'
    GATWAY_FUNCTIANS = (
        (FUNCTION_SAMAN, -('saman')),
        (FUNCTION_SHAPARAK, -('shaparak')),
        (FUNCTION_FINOTECH, -('fintech')),
        (FUNCTION_ZARINPAL, -('zarinpal')),
        (FUNCTION_PARSIAN, -('parsian')),
        (FUNCTION_SAMAN, -('saman')),
    )


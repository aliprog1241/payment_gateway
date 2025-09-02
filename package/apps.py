from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class PackageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'package'
    reversed_name = _('package')
    verbose_name_plural = _('packages')

from django.db import models
from django.utils.translation import gettext_lazy as _

class Package(models.Model):
    title = models.CharField(max_length=48, verbose_name=_('title'))
    price = models.PositiveBigIntegerField(verbose_name=_('price'))
    description = models.TextField(blank=True)
    days = models.PositiveSmallIntegerField()
    is_enabled = models.BooleanField(default=True)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Packages")
        verbose_name_plural = _("Packages")

    def __str__(self):
        return self.title

class PackageAttribute(models.Model):
    package = models.ForeignKey(Package, related_name='attribute',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
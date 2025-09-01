from django.db import models
from django.utils.translation import gettext

class Package(models.Model):
    title = models.CharField(max_length=48, verbose_name=gettext('title'))
    price = models.PositiveBigIntegerField(verbose_name=gettext('price'))
    description = models.TextField(blank=True)
    days = models.PositiveSmallIntegerField()
    is_enabled = models.BooleanField(default=True)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = gettext("Packages")
        verbose_name_plural = gettext("Packages")

    def __str__(self):
        return self.title

class PackageAttribute(models.Model):
    package = models.ForeignKey(Package, related_name='attribute',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
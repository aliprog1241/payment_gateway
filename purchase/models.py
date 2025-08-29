from django.contrib.auth.models import User
from django.db import models

from package.admin import PackageModelAdmin


class Purchase(models.Model):
    user = models.ForeignKey(User, related_name='purchases', on_delete=models.SET_NULL, null=True )
    package = models.ForeignKey(PackageModelAdmin, related_name='purchases', on_delete=models.SET_NULL, null=True )

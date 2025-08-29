from django.contrib.auth.models import User
from django.db import models
from package.models import Package
from package.admin import PackageModelAdmin


class Purchase(models.Model):
    user = models.ForeignKey(User, related_name='purchases', on_delete=models.SET_NULL, null=True )
    package = models.ForeignKey(Package, related_name='purchases', on_delete=models.SET_NULL, null=True )
    price = models.PositiveBigIntegerField()

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.package}'


    @classmethod
    def create(cls, package, user):
        if package.is_enabled:
            return cls.objects.create(
                user=user, package=package, price=package.price,

            )
        return None


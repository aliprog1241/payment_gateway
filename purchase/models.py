from django.contrib.auth.models import User
from django.db import models, transaction

from finance.models import Payment
from package.models import Package
from package.admin import PackageModelAdmin


class Purchase(models.Model):
    PAID = 10
    NO_PAID = -10

    STATUS_CHOICES = (
        (PAID, 'Paid'),
        (NO_PAID, 'No Paid'),

    )
    user = models.ForeignKey(User, related_name='purchases', on_delete=models.SET_NULL, null=True )
    package = models.ForeignKey(Package, related_name='purchases', on_delete=models.SET_NULL, null=True )
    price = models.PositiveBigIntegerField()
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=NO_PAID)
    payment =models.ForeignKey(Payment, related_name='purchases', on_delete=models.PROTECT, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.package}'


    @staticmethod
    def creat_payment( package, user ):
        return Payment.objects.create(amount=package.price, user=user)



    @classmethod
    def create(cls, package, user):
        if package.is_enabled:
            with transaction.atomic():
                payment = cls.creat_payment(package, user)
                purchase =  cls.objects.create(
                    user=user, package=package, price=package.price, payment=payment

                )
            return purchase
        return None


from django.db.models.signals import post_save, pre_init, post_init
from django.dispatch import receiver

from finance.models import Payment
from purchase.models import Purchase


@receiver(post_save, sender=Payment)
def callback(sender, instance, created, **kwargs):
    if instance.is_paid and  not instance._b_is_paid:
        print('purchase signals fired!!!')
        if instance.purchase.exists():
            purchase = instance.purchases.first()
            purchase.status = Purchase.PAID
            purchase.save()


@receiver(post_init, sender=Payment)
def store_is_paid_data(sender, instance, **kwargs):
    # print(' post_init signal called!!!')
    instance._b_is_paid = instance.is_paid

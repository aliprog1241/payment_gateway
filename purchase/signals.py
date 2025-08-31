from django.db.models.signals import post_save
from django.dispatch import receiver

from finance.models import Payment
from purchase.models import Purchase


@receiver(post_save, sender=Payment)
def callback(sender, instance, created, **kwargs):
    print('signal called!!!')
    if instance.is_paid:
        purchase = instance.purchase.first()
        purchase.status = Purchase.STATUS_PAID
        purchase.save()
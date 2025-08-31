from itertools import count

from django.core.management import BaseCommand
from django.db.models import Sum, Count

from finance.models import Payment


class Command(BaseCommand):

    def handle(self, *args, **options):
        payment = Payment.objects.aggregate(total=Sum('amount'), count=Count('id'))
        print(payment)

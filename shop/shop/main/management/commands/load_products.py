from django.core.management.base import BaseCommand, CommandError
from main.models import Product

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Start loading products')
        Product.objects.all().delete()
        for n in range(1,1000):
            p = Product()
            p.name = 'Super car'
            p.desc = 'To implement the command, edit polls/management/commands/closepoll.py to look like this:'
            p.save()
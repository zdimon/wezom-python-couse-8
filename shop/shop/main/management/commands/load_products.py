from django.core.management.base import BaseCommand, CommandError
from main.models import Product, Category
import random
from django.core.files import File
from shop.settings import BASE_DIR
class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Start loading products')
        Category.objects.all().delete()
        Product.objects.all().delete()
        for category in ['food', 'cars', 'animals']:
            c = Category()
            c.name = category
            c.save()

            for n in range(1,50):
                rnd = random.randint(1,3)
                image_name = '%s.jpeg' % rnd
                image_path = '%s/init_data/images/%s' % (BASE_DIR, image_name)
                p = Product()
                p.name = 'Super car %s' % c.name
                p.desc = 'To implement the command, edit polls/management/commands/closepoll.py to look like this:'
                p.category = c
                p.save()
                p.image.save(image_name,File(open(image_path, 'rb')))
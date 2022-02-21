from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()

    def __str__(self):
        return "[%s] %s" % (self.id, self.name)
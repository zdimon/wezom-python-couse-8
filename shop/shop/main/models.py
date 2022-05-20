from django.db import models
from django.contrib.auth.models import User


class Profile(User):
    phone = models.CharField(max_length=250)

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    image = models.ImageField(upload_to='media', null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "[%s] %s" % (self.id, self.name)



class Busket(models.Model):
    sessionid = models.CharField(max_length=250)
    phone = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return self.sessionid
class Busketitems(models.Model):
    basket = models.ForeignKey(Busket, on_delete=models.CASCADE)
    count = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
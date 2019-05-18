from django.db import models
from products.models import Product

class Magacin(models.Model):
     products    = models.ManyToManyField(Product, blank=True)
     stanje     = models.IntegerField(default=0)


from re import I
from django.db import models
from generics import mixins

class Product(mixins.GenericModelMixin):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.name 
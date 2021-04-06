from typing import Type
from django.db import models
from django.contrib.auth.models import User


class PizzaSize(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Topping(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

TYPE = (
    ('regular', 'Regular pizza'),
    ('square', 'Square pizza'),
)
    
class Pizza(models.Model):
    type = models.CharField(max_length=13, choices=TYPE)
    size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)
    
    def __str__(self):
        toppings_associated = ", ".join(str(spe.name) for spe in self.toppings.all())
        return f'{self.size} {self.type} pizza with {toppings_associated} $'


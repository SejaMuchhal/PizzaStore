from django.contrib import admin
from .models import Topping, Pizza, PizzaSize


Models = (Topping, Pizza, PizzaSize)

admin.site.register(Models)


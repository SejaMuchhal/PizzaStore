from rest_framework import serializers
from .models import Topping, Pizza, PizzaSize

class ToppingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Topping
        fields = '__all__'

class PizzaSizeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PizzaSize
        fields = '__all__'

class ListPizzaSerializer(serializers.ModelSerializer):
    size = PizzaSizeSerializer(read_only=True)
    toppings = ToppingSerializer(read_only=True, many=True)
    
    class Meta:
        model = Pizza
        fields = ('id', 'type', 'size', 'toppings')
        
class CreatePizzaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pizza
        fields = '__all__' 

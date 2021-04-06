from rest_framework import generics, status
from rest_framework.response import Response
from .models import Topping, Pizza, PizzaSize
from .serializers import ListPizzaSerializer, CreatePizzaSerializer,ToppingSerializer, PizzaSizeSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class PizzaCreateView(generics.CreateAPIView):
    """
    View for creating regular pizza or square pizza.
    """
    serializer_class = CreatePizzaSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        item = Pizza.objects.create(
            type = serializer.data['type'],
            size = PizzaSize.objects.get(id=serializer.data['size']),
            )
        item.toppings.clear()
        for topping in serializer.data['toppings']:
            item.toppings.add(topping)
            
        result = ListPizzaSerializer(item)
        return Response(result.data, status=status.HTTP_201_CREATED)

class PizzaDetailView(APIView):
    """
    View for retrieving, updating or deleting any pizza from the database.
    """
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Pizza, pk=kwargs['id'])
        serializer = ListPizzaSerializer(item)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        item = get_object_or_404(Pizza, pk=kwargs['id'])
        serializer = CreatePizzaSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            item = serializer.save()
            return Response(ListPizzaSerializer(item).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        item = get_object_or_404(Pizza, pk=kwargs['id'])
        item.delete()
        return Response("Pizza deleted", status=status.HTTP_204_NO_CONTENT)
    
class PizzaListView(generics.ListAPIView):
    """
    View for listing a pizzas in database .
    Optionally also restricts the returned pizzas,
    by filtering against a `size` and `type'.
    """
    serializer_class = ListPizzaSerializer

    def get_queryset(self):
        queryset = Pizza.objects.all()
        size = self.request.data.get("size")
        if size is not None:
            queryset = queryset.filter(size=size)
        type = self.request.data.get("type")
        if type is not None:
            queryset = queryset.filter(type=type)
        return queryset


class PizzaSizeView(generics.ListCreateAPIView):
    """
    View for listing all pizza-sizes in database or add new pizza-size.
    """
    serializer_class = PizzaSizeSerializer
    queryset = PizzaSize.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        item = PizzaSize.objects.create(
            name =serializer.data['name'],
            )
        result = PizzaSizeSerializer(item)
        return Response(result.data, status=status.HTTP_201_CREATED)
    
class ToppingView(generics.ListCreateAPIView):
    """
    View for listing all toppings in database or add new topping.
    """
    serializer_class = ToppingSerializer
    queryset = Topping.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        item = Topping.objects.create(
            name =serializer.data['name'],
            )
        result = PizzaSizeSerializer(item)
        return Response(result.data, status=status.HTTP_201_CREATED)
    



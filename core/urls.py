from .views import PizzaCreateView, PizzaDetailView, PizzaListView, PizzaSizeView, ToppingView
from django.urls import path

urlpatterns = [
    path('pizza-create', PizzaCreateView.as_view(), name='pizza_create_view'),
    path('pizza-list', PizzaListView.as_view(), name='pizza_list_view'),
    path('pizzas/<int:id>', PizzaDetailView.as_view(), name='pizza_update_view'),
    path('pizza-size', PizzaSizeView.as_view(), name='pizza_size_list_or_create_view'),
    path('pizza-topping', ToppingView.as_view(), name='pizza_topping_list_or_create_view'), 
]

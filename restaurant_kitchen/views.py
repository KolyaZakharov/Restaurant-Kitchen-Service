
from django.shortcuts import render

from restaurant_kitchen.models import Dish, DishType, Cook, Ingredient


def index(request):
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()
    num_cooks = Cook.objects.count()
    num_ingredients = Ingredient.objects.count()

    context = {
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_cooks": num_cooks,
        "num_ingredients": num_ingredients
    }

    return render(request, "restaurant_kitchen/index.html", context=context)
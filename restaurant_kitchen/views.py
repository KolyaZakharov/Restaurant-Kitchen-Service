
from django.shortcuts import render
from django.views import generic

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

    return render(
        request,
        "restaurant_kitchen/index.html",
        context=context)


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.all().select_related("dish_type")


class DishDitailView(generic.DetailView):
    model = Dish
    queryset = Dish.objects.all().prefetch_related(
        "ingredients",
        "cooks"
    )


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "restaurant_kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"


class DishTypeDetailView(generic.DetailView):
    model = DishType
    template_name = "restaurant_kitchen/dish_type_detail.html"
    context_object_name = "dishtype"


class IngredientListView(generic.ListView):
    model = Ingredient
    paginate_by = 15


class CookListView(generic.ListView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes__dish_type")


class CookDetailView(generic.DetailView):
    model = Cook
    # queryset = Cook.objects.all().prefetch_related("dishes")


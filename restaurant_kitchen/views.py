from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from restaurant_kitchen.models import Dish, DishType, Cook, Ingredient


@login_required
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


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    queryset = Dish.objects.all().select_related("dish_type")


class DishDitailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    queryset = Dish.objects.all().prefetch_related(
        "ingredients",
        "cooks"
    )


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "restaurant_kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    template_name = "restaurant_kitchen/dish_type_detail.html"
    context_object_name = "dishtype"


class DishTypeCreateView(generic.CreateView):
    template_name = "restaurant_kitchen/dish_type_form.html"
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("restaurant_kitchen:dish-type-list")


class DishTypeUpdateView(generic.UpdateView):
    template_name = "restaurant_kitchen/dish_type_form.html"
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("restaurant_kitchen:dish-type-list")


class DishTypeDeleteView(generic.DeleteView):
    template_name = "restaurant_kitchen/dish_type_delete.html"
    model = DishType
    success_url = reverse_lazy("restaurant_kitchen:dish-type-list")


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    paginate_by = 15


class IngredientCreateView(generic.CreateView):
    fields = "__all__"
    template_name = "restaurant_kitchen/ingredient_form.html"
    model = Ingredient
    success_url = reverse_lazy("restaurant_kitchen:ingredient-list")


class IngredientUpdateView(generic.UpdateView):
    fields = "__all__"
    template_name = "restaurant_kitchen/ingredient_form.html"
    model = Ingredient
    success_url = reverse_lazy("restaurant_kitchen:ingredient-list")


class IngredientDeleteView(generic.DeleteView):
    template_name = "restaurant_kitchen/ingredient_delete.html"
    model = Ingredient
    success_url = reverse_lazy("restaurant_kitchen:ingredient-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes__dish_type")


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    # queryset = Cook.objects.all().prefetch_related("dishes")


from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from restaurant_kitchen.forms import (
    DishForm,
    CookForm,
    CookSearchForm,
    SearchForm,
)

from restaurant_kitchen.models import (
    Dish,
    DishType,
    Cook,
    Ingredient,
)


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


class SearchMixin:
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchMixin, self).get_context_data(
            object_list=object_list, **kwargs
        )

        name = self.request.GET.get("name", "")

        context["search_form"] = SearchForm(initial={"name": name},)

        return context

    def get_queryset(self):
        query_set = super().get_queryset()
        search_request = self.request.GET.get("name")
        if search_request:
            return query_set.filter(name__icontains=search_request)

        return query_set


class DishListView(LoginRequiredMixin, SearchMixin, generic.ListView):
    model = Dish
    queryset = Dish.objects.all().select_related("dish_type")
    paginate_by = 15


class DishDitailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    queryset = Dish.objects.all().prefetch_related(
        "ingredients",
        "cooks"
    )


class DishCreateView(generic.CreateView):
    model = Dish
    template_name = "restaurant_kitchen/dish_form.html"
    success_url = reverse_lazy("restaurant_kitchen:dish-list")
    form_class = DishForm


class DishUpdateView(generic.UpdateView):
    model = Dish
    template_name = "restaurant_kitchen/dish_form.html"
    form_class = DishForm


class DishDeleteView(generic.DeleteView):
    model = Dish
    template_name = "restaurant_kitchen/dish_delete.html"
    success_url = reverse_lazy("restaurant_kitchen:dish-list")


class DishTypeListView(LoginRequiredMixin, SearchMixin, generic.ListView):
    model = DishType
    template_name = "restaurant_kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 15


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
    success_url = reverse_lazy("restaurant_kitchen:dish-type-list")
    model = DishType
    fields = "__all__"


class DishTypeDeleteView(generic.DeleteView):
    template_name = "restaurant_kitchen/dish_type_delete.html"
    model = DishType
    success_url = reverse_lazy("restaurant_kitchen:dish-type-list")


class IngredientListView(LoginRequiredMixin, SearchMixin, generic.ListView):
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
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        name_user = self.request.GET.get("username", "")
        context["search_form"] = CookSearchForm(
            initial={"name_user": name_user}
        )

        return context

    def get_queryset(self):
        queryset = Cook.objects.all()

        form = CookSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                username__contains=form.cleaned_data["username"]
            )
        return queryset


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes__dish_type")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookForm
    template_name = "restaurant_kitchen/cook_form.html"
    success_url = reverse_lazy("restaurant_kitchen:cook-list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookForm
    template_name = "restaurant_kitchen/cook_form.html"


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    template_name = "restaurant_kitchen/cook_delete.html"
    success_url = reverse_lazy("restaurant_kitchen:cook-list")

@login_required
def toggle_assign_to_dish(request, pk):
    cook = Cook.objects.get(id=request.user.id)
    if (
        Dish.objects.get(id=pk) in cook.dishes.all()
    ):
        cook.dishes.remove(pk)
    else:
        cook.dishes.add(pk)
    return HttpResponseRedirect(reverse_lazy("restaurant_kitchen:dish-detail", args=[pk]))

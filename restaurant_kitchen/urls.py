from django.urls import path

from restaurant_kitchen.views import (
    index,
    DishListView,
    DishTypeListView,
    IngredientListView,
    CookListView,
    DishDitailView,
    DishTypeDetailView,
    CookDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list"),
    path(
        "dish-types/",
        DishTypeListView.as_view(),
        name="dish-type-list"
         ),
    path("ingredients/",
         IngredientListView.as_view(),
         name="ingredient-list",
         ),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list"
         ),
    path(
        "dish/<int:pk>/",
        DishDitailView.as_view(),
        name="dish-detail"
        ),
    path(
        "dish-type/<int:pk>",
        DishTypeDetailView.as_view(),
        name="dish-type-detail"
    ),
    path(
        "cook/<int:pk>",
        CookDetailView.as_view(),
        name="cook-detail"
    ),

]


app_name = "restaurant_kitchen"

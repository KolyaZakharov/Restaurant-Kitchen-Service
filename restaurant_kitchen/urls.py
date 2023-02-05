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
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    CookCreateView,
    CookDeleteView,
    CookUpdateView,
    toggle_assign_to_dish,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list"),
    path(
        "dish/<int:pk>/",
        DishDitailView.as_view(),
        name="dish-detail"
    ),
    path(
        "dish/create",
        DishCreateView.as_view(),
        name="dish-create"
    ),
    path(
        "dish/<int:pk>/update",
        DishUpdateView.as_view(),
        name="dish-update"
    ),
    path(
        "dish/<int:pk>/delete",
        DishDeleteView.as_view(),
        name="dish-delete"
    ),
    path(
        "dish-types/",
        DishTypeListView.as_view(),
        name="dish-type-list"
    ),
    path(
        "dish/<int:pk>/toggle-assign/",
        toggle_assign_to_dish,
        name="toggle-dish-assign",
    ),
    path(
        "dish-types/<int:pk>",
        DishTypeDetailView.as_view(),
        name="dish-type-detail"
    ),
    path(
        "dish-types/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create",
    ),
    path(
        "dish-types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dish-types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
    path(
        "ingredients/",
        IngredientListView.as_view(),
        name="ingredient-list",
    ),
    path(
        "ingredients/create/",
        IngredientCreateView.as_view(),
        name="ingredient-create",
    ),
    path(
        "ingredients/<int:pk>/update/",
        IngredientUpdateView.as_view(),
        name="ingredient-update",
    ),
    path(
        "ingredients/<int:pk>/delete/",
        IngredientDeleteView.as_view(),
        name="ingredient-delete",
    ),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list"
    ),
    path(
        "cook/<int:pk>",
        CookDetailView.as_view(),
        name="cook-detail"
    ),
    path(
        "cook/create",
        CookCreateView.as_view(),
        name="cook-create"
    ),
    path(
        "cook/<int:pk>/update",
        CookUpdateView.as_view(),
        name="cook-update"
    ),
    path(
        "cook/<int:pk>/delete",
        CookDeleteView.as_view(),
        name="cook-delete"
    ),


]


app_name = "restaurant_kitchen"

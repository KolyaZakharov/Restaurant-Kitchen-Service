from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from restaurant_kitchen.models import Cook, Dish, DishType, Ingredient


class SearchTest(TestCase):
    NUM_OBJECTS = 4

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="new_user",
            years_of_experience=1
        )
        self.client.force_login(self.user)

    def test_search_dish_type_by_name(self):
        for dish_type_num in range(self.NUM_OBJECTS):
            DishType.objects.create(
                name=f"Pizza{dish_type_num}"
            )
            DishType.objects.create(name="Salat")

        response = self.client.get(
            reverse("restaurant_kitchen:dish-type-list") + "?name=Pizza"
        )
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(DishType.objects.filter(name__icontains="Pizza")),
        )

    def test_search_dish_by_name(self):
        dish_type1 = DishType.objects.create(name="cake")
        dish_type2 = DishType.objects.create(name="pasta")

        Dish.objects.create(
            name="Napaleon",
            dish_type=dish_type1,
            price=2
        )

        for dish_num in range(self.NUM_OBJECTS):
            Dish.objects.create(
                name=f"Carbonara{self.NUM_OBJECTS}",
                dish_type=dish_type2,
                price=2
            )

        response = self.client.get(reverse("restaurant_kitchen:dish-list") + "?name=Carb")
        self.assertEqual(
            list(response.context["dish_list"]),
            list(Dish.objects.filter(name__icontains="Carbonara")),
        )

    def test_search_ingredient_by_name(self):
        Ingredient.objects.create(name="salt")

        for ingredient_num in range(self.NUM_OBJECTS):
            Ingredient.objects.create(name=f"Becon{ingredient_num}")

        response = self.client.get(reverse("restaurant_kitchen:ingredient-list") + "?name=Becon")
        self.assertEqual(
            list(response.context["ingredient_list"]),
            list(Ingredient.objects.filter(name__icontains="Becon"))
        )

    def test_search_cook_by_username(self):
        user1 = get_user_model().objects.create_user(
            username="Petro",
            years_of_experience=2
        )
        for user_num in range(self.NUM_OBJECTS):
            get_user_model().objects.create_user(
                username=f"test{user_num}",
                years_of_experience=user_num + 1
            )

        response = self.client.get(
            reverse("restaurant_kitchen:cook-list") + "?username=test"
        )
        self.assertEqual(
            list(response.context["cook_list"]),
            list(Cook.objects.filter(username__icontains="test")),
        )



from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant_kitchen.models import DishType, Ingredient, Dish, Cook


class DishTypeModelTest(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="test")
        self.assertEqual(str(dish_type), dish_type.name)


class IngredientModelTest(TestCase):
    def test_ingredient_str(self):
        ingredient = Ingredient.objects.create(name="test")
        self.assertEqual(str(ingredient), ingredient.name)


class DishModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        dish_type = DishType.objects.create(name="test")
        cls.dish = Dish.objects.create(
            name="test",
            price=10,
            dish_type=dish_type)

    def test_dish_str(self):
        self.assertEqual(str(self.dish), "test (price:10, dish type:test)")

    def test_dish_get_absolute_url(self):
        self.assertEqual(self.dish.get_absolute_url(), "/dish/1/")


class CookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cook = get_user_model().objects.create(
            username="Testusername",
            first_name="Testfirstname",
            last_name="Testlastname",
            password="password1234",
            email="test@gmail.com",
            years_of_experience=1
        )

    def test_cook_str(self):
        self.assertEqual(str(self.cook), "Testusername (Testfirstname Testlastname)")

    def test_cook_get_absolute_url(self):
        self.assertEqual(self.cook.get_absolute_url(), "/cook/1")





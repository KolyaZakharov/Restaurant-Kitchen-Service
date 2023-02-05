from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from django.urls import reverse

from restaurant_kitchen.models import DishType

DISH_TYPE_URL = reverse("restaurant_kitchen:dish-type-list")


class PublicDishTypeFormatTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(DISH_TYPE_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeFormatTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "password123",
        )
        self.client.force_login(self.user)

    def test_retrieve_manufacturer(self):
        DishType.objects.create(name="Testtype1")
        DishType.objects.create(name="Testype2")

        response = self.client.get(DISH_TYPE_URL)
        dishtypes = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dishtypes)
        )
        self.assertTemplateUsed(response, "restaurant_kitchen/dish_type_list.html")
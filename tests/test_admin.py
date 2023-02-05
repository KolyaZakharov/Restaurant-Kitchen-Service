from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345"
        )

        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="Vasil",
            password="vasil123",
            years_of_experience=1
        )

    def test_years_of_experience_listed(self):
        url = reverse("admin:restaurant_kitchen_cook_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.cook.years_of_experience)

    def test_years_of_experience_detailed_listed(self):
        url = reverse("admin:restaurant_kitchen_cook_change", args=[self.cook.id])
        res = self.client.get(url)

        self.assertContains(res, self.cook.years_of_experience)

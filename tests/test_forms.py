from django.test import TestCase

from restaurant_kitchen.forms import CookForm


class FormsTests(TestCase):
    def test_cook_form_with_adds_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "user1234test",
            "password2": "user1234test",
            "first_name": "Firsttest",
            "last_name": "Lasttest",
            "years_of_experience": 1,
        }
        form = CookForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def tests_years_of_experience_validation_with_invalid_data(self):
        form_data = {
            "username": "new_user1",
            "password1": "user1234test",
            "password2": "user1234test",
            "first_name": "Firsttest",
            "last_name": "Lasttest",
            "years_of_experience": 0,
        }
        form = CookForm(data=form_data)
        self.assertFalse(form.is_valid())

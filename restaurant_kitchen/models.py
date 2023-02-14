from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"

    class Meta:
        ordering = ["username"]

    def get_absolute_url(self) -> str:
        return reverse(
            "restaurant_kitchen:cook-detail", kwargs={"pk": self.pk}
        )


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE,)
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="dishes"
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name="dishes"
    )

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "dishes"

    def __str__(self) -> str:
        return f"{self.name}" \
               f" (price:{self.price}, dish type:{self.dish_type.name})"

    def get_absolute_url(self) -> str:
        return reverse(
            "restaurant_kitchen:dish-detail",
            kwargs={"pk": self.pk}
        )

from django.urls import path

from restaurant_kitchen.views import index

urlpatterns = [
    path("", index)
]
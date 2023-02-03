from django import forms


from restaurant_kitchen.models import Dish, DishType, Ingredient


# class DishTypeForm(forms.ModelForm):
#     dishes = forms.ModelMultipleChoiceField(
#         queryset=Dish.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=False
#     )
#
#     class Meta:
#         model = DishType
#         fields = "__all__"
#
#     def save(self, commit=True):
#         form = super().save(commit=False)
#         self.cleaned_data["dishes"].update(dish_type=form)
#         form.save()
#
#         return form

class DishForm(forms.ModelForm):
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Dish
        fields = "__all__"

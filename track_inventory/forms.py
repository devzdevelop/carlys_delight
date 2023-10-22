from django import forms
from .models import Ingredients, RecipeRequirements, MenuItem, PurchaseLog


# Create Form
class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = "__all__"


class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"


class RecipeReqCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirements
        fields = ("__all__")


class PurchaseLogCreateForm(forms.ModelForm):
    class Meta:
        model = PurchaseLog
        fields = ("item_name",)


# Update form
class MenuItemUpdateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"


class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = "__all__"


class RecipeReqUpdateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirements
        fields = "__all__"


class PurchaseLogUpdateForm(forms.ModelForm):
    class Meta:
        model = PurchaseLog
        fields = "__all__"


# Delete Form
class MenuItemDeleteForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"


class IngredientDeleteForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = "__all__"


class RecipeRequirementsDeleteForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirements
        fields = "__all__"


class PurchaseLogDeleteForm(forms.ModelForm):
    class Meta:
        model = PurchaseLog
        fields = "__all__"
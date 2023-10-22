from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ingredients, PurchaseLog, MenuItem, RecipeRequirements
from .forms import MenuItemCreateForm, MenuItemUpdateForm, MenuItemDeleteForm, IngredientCreateForm, \
    IngredientUpdateForm, RecipeReqUpdateForm, PurchaseLogUpdateForm, RecipeReqCreateForm, PurchaseLogCreateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def logout_view(request):
    logout(request)
    return redirect("home")


# List Views
class HomeView(LoginRequiredMixin, ListView):
    model = Ingredients  # You can set any model here; it doesn't have to be Ingredients.
    template_name = "track_inventory/home.html"
    context_object_name = 'ingredients_list'  # This sets the context variable name for Ingredients

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add data from the second model to the context
        context['items2'] = PurchaseLog.objects.all()
        context['items3'] = RecipeRequirements.objects.all()
        context['items4'] = MenuItem.objects.all()
        return context


class IngredientsView(LoginRequiredMixin, ListView):
    model = Ingredients
    template_name = "track_inventory/ingredients.html"


class MenuItemView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "track_inventory/menu_item.html"


class RecipeRequirementsView(LoginRequiredMixin, ListView):
    model = RecipeRequirements
    template_name = "track_inventory/recipe_requirements.html"


class PurchaseLogView(LoginRequiredMixin, ListView):
    model = PurchaseLog
    template_name = "track_inventory/purchase_log.html"


# Add Views
class AddIngredient(LoginRequiredMixin, CreateView):
    model = Ingredients
    template_name = "track_inventory/add_ingredient.html"
    form_class = IngredientCreateForm
    success_url = "/ingredients/"


class AddMenuItem(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = "track_inventory/add_menu_item.html"
    form_class = MenuItemCreateForm
    success_url = "/menu_item/"


class AddRecipeReq(LoginRequiredMixin, CreateView):
    model = RecipeRequirements
    template_name = "track_inventory/add_recipe_requirement.html"
    form_class = RecipeReqCreateForm
    success_url = "/recipe_requirements/"


class AddPurchaseLog(LoginRequiredMixin, CreateView):
    model = PurchaseLog
    template_name = "track_inventory/add_purchase_log.html"
    form_class = PurchaseLogCreateForm
    success_url = "/purchase_log/"


# Update Select/Dropdown Views
class MenuItemUpdateSelect(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "track_inventory/upselect_menu_item.html"


class IngredientUpdateSelect(LoginRequiredMixin, ListView):
    model = Ingredients
    template_name = "track_inventory/upselect_ingredient.html"


class RecipeReqUpdateSelect(LoginRequiredMixin, ListView):
    model = RecipeRequirements
    template_name = "track_inventory/upselect_recipe_requirement.html"
"""
    def post(self, request, *args, **kwargs):
        menu_item_name = request.POST.get('menu_item')

        # Perform the deletion
        try:
            menu_item = MenuItem.objects.get(id=menu_item_id)
            menu_item.delete()
        except MenuItem.DoesNotExist:
            # Handle the case where the menu item doesn't exist
            pass

        return HttpResponseRedirect(reverse('menuitem'))"""


class PurchaseLogUpdateSelect(LoginRequiredMixin, ListView):
    model = PurchaseLog
    template_name = "track_inventory/upselect_puchase_log.html"


# Update Views
class UpdateMenuItem(LoginRequiredMixin, UpdateView):
    model = MenuItem
    template_name = "track_inventory/update_menu_item.html"
    form_class = MenuItemUpdateForm
    success_url = "/menu_item/"


class UpdateIngredient(LoginRequiredMixin, UpdateView):
    model = Ingredients
    template_name = "track_inventory/update_ingredient.html"
    form_class = IngredientUpdateForm
    success_url = "/ingredients/"


class UpdateRecipeReq(LoginRequiredMixin, UpdateView):
    model = RecipeRequirements
    template_name = "track_inventory/update_recipe_requirement.html"
    form_class = RecipeReqUpdateForm
    success_url = "/recipe_requirements/"


class UpdatePurchaseLog(LoginRequiredMixin, UpdateView):
    model = PurchaseLog
    template_name = "track_inventory/update_purchaselog.html"
    form_class = PurchaseLogUpdateForm
    success_url = "/purchase_log/"  #


# Delete Select/DropDown
class MenuItemDeleteSelect(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "track_inventory/delselect_menu_item.html"


class IngredientDeleteSelect(LoginRequiredMixin, ListView):
    model = Ingredients
    template_name = "track_inventory/deselect_ingredient.html"


class RecipeReqDeleteSelect(LoginRequiredMixin, ListView):
    model = RecipeRequirements
    template_name = "track_inventory/deselect_recipe_requirement.html"


class PurchaseLogDeleteSelect(LoginRequiredMixin, ListView):
    model = PurchaseLog
    template_name = "track_inventory/deselect_purchase_log.html"


# Delete Views
class DeleteMenuItemView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        menu_item_id = request.POST.get('menu_item')

        # Perform the deletion
        try:
            menu_item = MenuItem.objects.get(id=menu_item_id)
            menu_item.delete()
        except MenuItem.DoesNotExist:
            # Handle the case where the menu item doesn't exist
            pass

        return HttpResponseRedirect(reverse('menuitem'))


class DeleteIngredient(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        ingredient = request.POST.get('ingredient')

        # Perform the deletion
        try:
            ingredient = Ingredients.objects.get(id=ingredient)
            ingredient.delete()
        except MenuItem.DoesNotExist:
            # Handle the case where the menu item doesn't exist
            print("Doesn't exist")
            pass

        return HttpResponseRedirect(reverse('ingredients'))


class DeleteRecipeReq(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        recipe_req_id = request.POST.get('recipe_req')

        # Perform the deletion
        try:
            recipe_req = RecipeRequirements.objects.get(id=recipe_req_id)
            recipe_req.delete()
        except MenuItem.DoesNotExist:
            # Handle the case where the menu item doesn't exist
            pass

        return HttpResponseRedirect(reverse('reciperequirements'))


class DeletePurchaseLog(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        purchase_log_id = request.POST.get('purchase_log')

        # Perform the deletion
        try:
            purchase_log = PurchaseLog.objects.get(id=purchase_log_id)
            purchase_log.delete()
        except MenuItem.DoesNotExist:
            # Handle the case where the menu item doesn't exist
            pass

        return HttpResponseRedirect(reverse('purchaselog'))



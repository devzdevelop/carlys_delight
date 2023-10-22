"""
URL configuration for carlys_delight project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path, include
from . import views

urlpatterns = [
    # list view
    path("", views.HomeView.as_view(), name="home"),
    path("accounts/", include("django.contrib.auth.urls"), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.SignUp.as_view(), name="signup"),

    path("menu_item/", views.MenuItemView.as_view(), name="menuitem"),
    path("ingredients/", views.IngredientsView.as_view(), name="ingredients"),
    path("recipe_requirements/", views.RecipeRequirementsView.as_view(), name="reciperequirements"),
    path("purchase_log/", views.PurchaseLogView.as_view(), name="purchaselog"),

    # add view
    path("menu_item/add/", views.AddMenuItem.as_view(), name="addmenuitem"),
    path("ingredients/add/", views.AddIngredient.as_view(), name="addingredient"),
    path("reciperequirement/add/", views.AddRecipeReq.as_view(), name="addreciperequirement"),
    path("purchase_log/add/", views.AddPurchaseLog.as_view(), name="addpurchaselog"),

    # update select
    path("menu_item_upselect/", views.MenuItemUpdateSelect.as_view(), name="menuitemupselect"),
    path("ingredient_upselect/", views.IngredientUpdateSelect.as_view(), name="ingredientupselect"),
    path("recipe_requirement_upselect/", views.RecipeReqUpdateSelect.as_view(), name="reciperequirementupselect"),
    path("purchase_log_upselect/", views.PurchaseLogUpdateSelect.as_view(), name="purchaselogupselect"),

    # delete select
    path("menu_item_delselect/", views.MenuItemDeleteSelect.as_view(), name="menuitemdelselect"),
    path("ingredient_delselect/", views.IngredientDeleteSelect.as_view(), name="ingredientdelselect"),
    path("recipe_requirement_delselect/", views.RecipeReqDeleteSelect.as_view(), name="reciperequirementdelselect"),
    path("purchase_log_delselect/", views.PurchaseLogDeleteSelect.as_view(), name="purchaselogdelselect"),

    # update view
    path("menu_item/update/<pk>/", views.UpdateMenuItem.as_view(), name="updatemenuitem"),
    path("ingredients/update/<pk>/", views.UpdateIngredient.as_view(), name="updateingredient"),
    path("recipe_requirements/update/<pk>/", views.UpdateRecipeReq.as_view(), name="updatereciperequirement"),
    path("purchase_log/update/<pk>/", views.UpdatePurchaseLog.as_view(), name="updatepurchaselog"),

    # delete view
    path('deletemenuitem/', views.DeleteMenuItemView.as_view(), name='deletemenuitem'),
    path('deleteingredient/', views.DeleteIngredient.as_view(), name='deleteingredient'),
    path('deletereciperequirement/', views.DeleteRecipeReq.as_view(), name='deletereciperequirement'),
    path('deletepurchaselog/', views.DeletePurchaseLog.as_view(), name='deletepurchaselog'),

]

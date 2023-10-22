from django.contrib import admin
from .models import Ingredients,MenuItem,RecipeRequirements,PurchaseLog
# Register your models here.
admin.site.register(Ingredients)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirements)
admin.site.register(PurchaseLog)
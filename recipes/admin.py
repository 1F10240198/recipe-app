from django.contrib import admin
from .models import User, Recipe, Ingredient, Seasoning, RecipeIngredient, RecipeSeasoning

# Register your models here.
admin.site.register(User)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Seasoning)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeSeasoning)

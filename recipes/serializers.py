from rest_framework import serializers
from .models import User, Recipe, Ingredient, Seasoning, RecipeIngredient, RecipeSeasoning

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class SeasoningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seasoning
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
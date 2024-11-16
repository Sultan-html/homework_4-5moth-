from django.contrib import admin
from .models import Recipe
# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id','name','ingredients','instructions','prep_time','is_vegetarian','created_at']
    search_fields = ['id','name']
    list_filter = ['id','name']
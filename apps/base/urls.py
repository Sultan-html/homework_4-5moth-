from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('api_recipe',RecipeAPI,basename='api_and_mixins_recipe')

urlpatterns = [

]

urlpatterns += router.urls
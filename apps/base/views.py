from django.shortcuts import render

from .models import *
from .serializers import RecipeSerializers

from rest_framework import mixins,viewsets
from rest_framework.viewsets import GenericViewSet
# Create your views here.
from rest_framework.pagination import PageNumberPagination

class Pagination(PageNumberPagination):
    page_size = 10
    max_page_size = 10

# class RecipeAPI(GenericViewSet,
#                 mixins.CreateModelMixin,
#                 mixins.DestroyModelMixin,
#                 mixins.ListModelMixin,
#                 mixins.RetrieveModelMixin,
#                 mixins.UpdateModelMixin):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializers

class RecipeAPI(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializers
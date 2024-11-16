from django.shortcuts import render

from .models import *
from .serializers import RecipeSerializers

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
# Create your views here.
class RecipeAPI(GenericViewSet,
                mixins.CreateModelMixin,
                mixins.DestroyModelMixin,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializers
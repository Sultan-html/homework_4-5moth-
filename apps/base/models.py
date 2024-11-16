from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.TextField()
    instructions = models.TextField()
    prep_time = models.IntegerField(default=1)
    is_vegetarian = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
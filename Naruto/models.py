from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from authenticate.models import User

class Card(models.Model):
    name = models.CharField(max_length = 33)
    description = models.CharField(max_length=300, null=False, blank=True)
    
    level = models.IntegerField(default=1)
    attack = models.IntegerField(default=1)
    defense = models.IntegerField(default=1)

    image = models.ImageField(upload_to='card_image', null=True, blank=True)

    user = models.ForeignKey("authenticate.User", on_delete=models.CASCADE, related_name='cards', blank=False,
                            null=True)
    def __str__(self):
        return self.name
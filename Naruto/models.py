from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from authenticate.models import User

class Card(models.Model):
    name = models.CharField(max_length = 33)
    description = models.CharField(max_length = 300)
    
    level = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(10),MinValueValidator(1)])
    attack = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(1000),MinValueValidator(0)])
    defense = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(1000),MinValueValidator(0)])

    image = models.ImageField(upload_to='card_image', null=True, blank=True)

    user = models.ForeignKey("authenticate.User", on_delete=models.CASCADE, related_name='cards', blank=False,
                            null=True)
    def __str__(self):
        return self.name
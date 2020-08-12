from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    level = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(33),MinValueValidator(0)])
    cash = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

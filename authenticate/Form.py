from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User

class userSignUpForm(UserCreationForm):
    ''' Formulario para cadastro de um usuario'''
    level = forms.PositiveIntegerField(default=0, validators=[MaxValueValidator(33),MinValueValidator(0)])

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.level = 0
        user.save()
        return user
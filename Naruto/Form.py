from django import forms
from .models import Card
from .validations import *

class formCard(forms.ModelForm):


    class Meta:
        model = Card
        fields = {'description', 'level', 'attack', 'name', 'defense', 'image'}

    def clean(self):
        level = self.cleaned_data.get('level')
        attack = self.cleaned_data.get('attack')
        defense = self.cleaned_data.get('defense')
        image = self.cleaned_data.get('image')

        list_errors = {}
        level_invalid_value('level',level,list_errors)
        attack_or_defense_invalid_value('attack', attack, list_errors)
        attack_or_defense_invalid_value('defense', defense, list_errors)

        if list_errors is not None:
            for erro in list_errors:
                erro_message = list_errors[erro]
                self.add_error(erro, erro_message)
        return self.cleaned_data



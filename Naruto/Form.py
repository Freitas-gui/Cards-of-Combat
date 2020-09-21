from django import forms
from .models import Card
from .validations import *

class formCard(forms.ModelForm):

    class Meta:
        model = Card
        fields = {'description', 'level', 'attack', 'name', 'defense', 'image'}

    def clean(self):
        name = self.cleaned_data.get('name')
        description = self.cleaned_data.get('description')
        level = self.cleaned_data.get('level')
        attack = self.cleaned_data.get('attack')
        defense = self.cleaned_data.get('defense')
        image = self.cleaned_data.get('image')

        list_errors = {}
        name_invalid_value('name', name, list_errors)
        description_invalid_value('description', description, list_errors)
        level_invalid_value('level', level, list_errors)
        attack_or_defense_invalid_value('attack', attack, list_errors)
        attack_or_defense_invalid_value('defense', defense, list_errors)

        if list_errors is not None:
            for error in list_errors:
                error_message = list_errors[error]
                self.add_error(error, "⚠ "+error_message)

        return self.cleaned_data


from django import forms
from .models import Type, Flower

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']

class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ['name', 'type', 'description']

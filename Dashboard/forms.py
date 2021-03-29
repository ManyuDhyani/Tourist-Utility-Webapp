from django import forms
from .models import City

class cityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ('city',)
        widgets = {
            'city': forms.TextInput(attrs={
                'class': 'form-control my-3 city-input w-75 mx-auto',
                'placeholder': 'Enter the City name....'
            })
        }
from django import forms
from .models import PredictionModel
class PredictionForm(forms.Form):
	
	image = forms.CharField(widget=forms.TextInput(attrs={'id': 'link', 'hidden': 'hidden'}), label='')

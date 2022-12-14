from django import forms
from django.forms import ModelForm
from .models import *


class PlayForm(ModelForm):
    class Meta:
        model = Play
        fields = ('title', 'genre', 'time', 'date', 'description', 'artists', 'price')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input', 'type': 'text', 'placeholder': 'Title'}),
            'genre': forms.TextInput(attrs={'class': 'input', 'type': 'text', 'placeholder': 'Genre'}),
            'time': forms.TimeInput(attrs={'class': 'input', 'type': 'time', 'placeholder': 'Time'}),
            'date': forms.DateInput(attrs={'class': 'input', 'type': 'date', 'placeholder': 'Date'}),
            'description': forms.Textarea(attrs={'class': 'textarea', 'type': 'text', 'placeholder': 'Description', 'rows': '10'}),
            'artists': forms.Select(attrs={'class': 'input', 'type': 'select', 'placeholder': 'Description', 'rows': '10'}),
            'price': forms.TextInput(attrs={'class': 'input', 'type': 'text', 'placeholder': 'Price'}),
        }


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ('first_name', 'last_name', 'bio')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input', 'type': 'text', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'input', 'type': 'text', 'placeholder': 'Last Name'}),
            'bio': forms.Textarea(attrs={'class': 'textarea', 'type': 'text', 'placeholder': 'Bio'}),
        }


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ('title', 'time', 'date', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input', 'type': 'text', 'placeholder': 'Title'}),
            'time': forms.TimeInput(attrs={'class': 'input', 'type': 'time', 'placeholder': 'Time'}),
            'date': forms.DateInput(attrs={'class': 'input', 'type': 'date', 'placeholder': 'Date'}),
            'content': forms.Textarea(attrs={'class': 'textarea', 'type': 'text', 'placeholder': 'Content', 'rows': '10'}),
        }
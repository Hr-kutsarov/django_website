from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, UserManager
from django import forms


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name',)







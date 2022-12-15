from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, UserManager
from django import forms


class DefaultUserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email',)

    def save(self, commit=True):
        user = super(DefaultUserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ModeratorRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email',)

    def save(self, commit=True):
        user = super(ModeratorRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user







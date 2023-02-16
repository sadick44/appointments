from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "Les deux mots de passe ne sont pas identiques",
    }

    first_name = forms.CharField(
        label="Votre Prenom",
        widget=forms.TextInput(attrs={"class": "form-control", "name": "first_name"})
    )

    last_name = forms.CharField(
        label="Votre Nom",
        widget=forms.TextInput(attrs={"class": "form-control", "name": "last_name"})
    )

    email = forms.CharField(
        label="Votre Email",
        widget=forms.TextInput(attrs={"class": "form-control", "name": "email"})
    )

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control", "name": "password1"
    }), label="Votre mot de passe")

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control", "name": "confirm_password"
    }), label="Confirmer votre mot de passe")

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

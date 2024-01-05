from django import forms
from . import models

class UserForm(forms.ModelForm):
    class Meta:
        model = usuario

        widgets = {
            'password': forms.PasswordInput(),
        }
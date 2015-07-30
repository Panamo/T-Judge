from django import forms
from .models import User


class SignupModelForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'first_name': "First Name",
            'last_name': "Last Name",
            'email': "Email",
            'phone_number': "Phone Number",
            'university': "University",
            'major': "Major",
            'password': "Password"
        }
        exclude = []


class LoginModelForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput, label="Email", max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
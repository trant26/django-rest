from django import forms
from django.forms import CharField
from django.core import validators
from django.core.validators import validate_email
from .models import SignUp



class MultilEmailField(forms.Field):
    def to_python(self, value):
        if not value:
            return []
        return value.split(',')

    def validate(self, value):
        super(MultilEmailField, self).validate(value)
        for email in value:
            validate_email(email)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email']
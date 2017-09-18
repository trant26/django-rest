from django import forms
from .models import SignUp
from django.core.validators import validate_email


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email', 'full_name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "edu" in email:
            raise forms.ValidationError("Please use a valid .EDU email address")
        return email
    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        # 
        return full_name
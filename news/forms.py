from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class RegistrationForm(forms.Form):
    username = forms.CharField(label='User name', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Enter Email", widget=forms.EmailInput(attrs={'class': "form-control my-input"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control my-input"}),
                                label="Enter Password",)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control my-input"}),
                                label="Confirm Password")

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        user = User.objects.filter(username=username)
        if user.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        email = User.objects.filter(email=email)
        if email.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

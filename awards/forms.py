from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import *


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image', 'description', 'link')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email',)


class ProfileUpdateForm(forms.ModelForm):
    bio = forms.Textarea()
    class Meta:
        model = Profile
        fields = ('image', 'bio',)

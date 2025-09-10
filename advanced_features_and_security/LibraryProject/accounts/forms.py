from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    profile_photo = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo')

class CustomUserChangeForm(UserChangeForm):
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    profile_photo = forms.ImageField(required=False)

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo', 'is_active', 'is_staff', 'is_superuser')

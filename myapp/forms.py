from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required = True)
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student')
    )
    role = forms.ChoiceField(choices = ROLE_CHOICES, required = True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
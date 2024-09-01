from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Custom form that extends Django's UserCreationForm
class SignUpForm(UserCreationForm):
    #Add an email field to the form
    email = forms.EmailField(required = True)
    
    #Define choices for the role field
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student')
    )
    #Add a role field to the form with the defined choices
    role = forms.ChoiceField(choices = ROLE_CHOICES, required = True)
    
    #Meta class to specify model and fields
    class Meta:
        model = User
        #Fields to include in the form
        fields = ['username', 'email', 'password1', 'password2', 'role']
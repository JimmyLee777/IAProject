from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.tokens import default_token_generator
#from django.utils.http import urlsafe_base64_decode
from .forms import SignUpForm
from .models import Profile
#from .models import TemporaryUser, 
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView
)
from django.urls import reverse_lazy
#from .utils import send_verification_email, generate_token

User = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.role = form.cleaned_data.get('role')
            user.save()
            return redirect('login')
        else:
            messages.error(request, "There was an error with your signup. Please check the form and try again.")
    else:
        form = SignUpForm()
    return render(request, 'myapp/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            profile = Profile.objects.get(user = user)
            role = profile.role
            if role == "teacher":
                return redirect("teacher_dashboard")
            elif role == "student":
                return redirect("student_dashboard")
            else:
                return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

def home_view(request):
    return render(request, 'myapp/home.html')

'''def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        temp_user = TemporaryUser.objects.get(pk=uid, token=token)
        user = User.objects.create_user(
            username=temp_user.username,
            email=temp_user.email,
            password=temp_user.password  # Ensure to store hashed passwords
        )
        Profile.objects.create(user=user, role=temp_user.role)
        temp_user.delete()
        messages.success(request, 'Your email has been verified! You can now log in.')
        return redirect('login')
    
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        messages.error(request, 'The verification link is invalid or expired.')
        return render(request, 'activation_failed.html')
'''    
class CustomPasswordResetView(PasswordResetView):
    template_name = 'myapp/registration/password_reset_form.html'
    email_template_name = 'myapp/registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'myapp/registration/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'myapp/registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'myapp/registration/password_reset_complete.html'    

def dashboard_view(request):
    user = request.user
    if hasattr(user, 'profile'):
        role = user.profile.role
        if role == 'teacher':
            return redirect('teacher_dashboard')
        elif role == 'student':
            return redirect('student_dashboard')
    return redirect('default_dashboard')

@login_required
def teacher_dashboard_view(request):
    return render(request, 'myapp/teacher_dashboard.html')

@login_required
def student_dashboard_view(request):
    return render(request, 'myapp/student_dashboard.html')


from django.db import models
from django.contrib.auth.models import User

#Model for storing temporary user data during email verification
class TemporaryUser(models.Model):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    username = models.CharField(max_length = 150, unique = True)
    email = email = models.EmailField(unique = True)
    password = models.CharField(max_length = 128)
    token = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length = 10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

#Model for extending User model with a role
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length = 10, choices = ROLE_CHOICES, default = 'student')
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"
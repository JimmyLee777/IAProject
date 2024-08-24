from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .models import TemporaryUser
import hashlib
import random

def generate_token():
    """Generates a unique token for email verification."""
    return hashlib.sha256(str(random.random()).encode()).hexdigest()

def send_verification_email(temp_user):
    """
    Sends a verification email to the newly registered temporary user.
    """
    token = temp_user.token
    uid = urlsafe_base64_encode(force_bytes(temp_user.pk))
    verification_link = reverse('activate', kwargs={'uidb64': uid, 'token': token})
    verification_url = f"{settings.SITE_URL}{verification_link}"
    subject = 'Verify your email'
    message = f"Hi {temp_user.username}, please verify your email by clicking the link below:\n{verification_url}"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [temp_user.email])

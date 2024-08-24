from django.urls import path
from .views import signup_view, login_view, home_view, teacher_dashboard_view, student_dashboard_view 
from .views import (
    CustomPasswordResetView, 
    CustomPasswordResetDoneView, 
    CustomPasswordResetConfirmView, 
    CustomPasswordResetCompleteView
)
urlpatterns = [
    path('', home_view, name = 'home'),
    path('signup/', signup_view, name = 'signup'),
    path('login/', login_view, name = 'login'),
    #path('activate/<uidb64>/<token>/', activate, name = 'activate'),
    path('password_reset/', CustomPasswordResetView.as_view(), name = 'password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name = 'password_reset_done'),
    #path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
    path('teacher_dashboard/', teacher_dashboard_view, name='teacher_dashboard'),
    path('student_dashboard/', student_dashboard_view, name='student_dashboard'),
]

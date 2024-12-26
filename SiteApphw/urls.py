from django.urls import path
from . import views

urlpatterns = [
    path('send-password-reset-emails/', views.send_reset_password_emails, name='send_reset_password_emails'),
]

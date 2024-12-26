from django.urls import path
from . import views

urlpatterns = [
    path('send-password-reset-emails/', views.send_reset_password_emails, name='send_reset_password_emails'),
    path('users/', views.UserListView.as_view(), name='user-list'),  # Для списка всех пользователей
    path('users/detail/', views.UserDetailView.as_view(), name='user-detail'),  # Для детального просмотра
]

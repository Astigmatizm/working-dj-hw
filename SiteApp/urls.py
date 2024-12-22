from django.urls import path
# from .views import register  # is_login
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('register/', register, name='register'),
    path('', index, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]

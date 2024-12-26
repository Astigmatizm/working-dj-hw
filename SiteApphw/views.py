from django.contrib.auth.views import LoginView

from .mixins import AdminRequiredMixin
from .utils import send_password_reset_email
from SiteApphw.models import CustomUser  # Импортируем кастомную модель CustomUser

from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404


class AdminRequiredMixin:
    """
    Миксин, который проверяет, что пользователь является администратором
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            # Перенаправить на страницу с ошибкой или на другую страницу
            return redirect('home')  # Например, если не администратор, перенаправить на главную страницу
        return super().dispatch(request, *args, **kwargs)


def send_reset_password_emails(request):
    users = CustomUser.objects.filter(is_active=True)

    for user in users:
        send_password_reset_email(user)

    return HttpResponse("Письма с восстановлением пароля отправлены.")


class UserListView(ListView):
    model = User
    template_name = 'main/user_list.html'  # Шаблон для отображения
    context_object_name = 'users'  # Имя переменной для передачи в шаблон


class UserDetailView(TemplateView):
    template_name = 'main/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get('username')  # Получение параметра из формы
        if username:
            user = get_object_or_404(User, username=username)
            context['user'] = user
        return context


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

    # Указываем, что если пользователь не авторизован, он будет перенаправлен на страницу входа
    login_url = '/login/'


class AdminUserListView(AdminRequiredMixin, ListView):
    model = User
    template_name = 'admin_user_list.html'
    context_object_name = 'users'


class CustomLoginView(LoginView):
    template_name = 'main/login.html'  # Шаблон для формы логина

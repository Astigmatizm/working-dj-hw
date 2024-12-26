from .utils import send_password_reset_email
from SiteApphw.models import CustomUser  # Импортируем кастомную модель CustomUser

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404


def send_reset_password_emails(request):
    # Получаем всех пользователей, которым нужно отправить письмо
    users = CustomUser.objects.filter(is_active=True)  # Вы можете фильтровать по нужным критериям

    # Отправляем письмо каждому пользователю
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

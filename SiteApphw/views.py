from django.shortcuts import render
from django.http import HttpResponse
from .utils import send_password_reset_email
from SiteApphw.models import CustomUser  # Импортируем кастомную модель CustomUser

def send_reset_password_emails(request):
    # Получаем всех пользователей, которым нужно отправить письмо
    users = CustomUser.objects.filter(is_active=True)  # Вы можете фильтровать по нужным критериям

    # Отправляем письмо каждому пользователю
    for user in users:
        send_password_reset_email(user)

    return HttpResponse("Письма с восстановлением пароля отправлены.")

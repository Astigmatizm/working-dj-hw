from django.template.loader import render_to_string
from django.core.mail import send_mail

def send_password_reset_email(user):
    reset_link = f'http://yourwebsite.com/reset-password/{user.id}/'
    subject = 'Восстановление пароля'

    # Используем шаблон для генерации письма
    message = render_to_string('main/password_reset.html', {'user': user, 'reset_link': reset_link})

    from_email = 'no-reply@yourwebsite.com'
    send_mail(subject, message, from_email, [user.email], html_message=message)

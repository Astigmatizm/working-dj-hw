from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib import messages


def show_request_params(request):
    get_params = request.GET
    post_params = request.POST

    get_params_str = ', '.join([f"{key}: {value}" for key, value in get_params.items()]) # метод items() позволяет получить все ключи и значения в параметрах запроса.

    post_params_str = ', '.join([f"{key}: {value}" for key, value in post_params.items()])

    response_content = f"""
    <html>
        <body>
            <h2>GET Parameters:</h2>
            <p>{get_params_str if get_params else "Нету GET параметр"}</p>
            <h2>POST Parameters:</h2>
            <p>{post_params_str if post_params else "Нету POST параметр"}</p>
        </body>
    </html>
    """

    return HttpResponse(response_content)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Создаем нового пользователя
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, email=email, password=password)

            # Сообщение об успешной регистрации
            messages.success(request, "Регистрация прошла успешно! Теперь вы можете войти в систему.")

            # Перенаправление на страницу входа
            return redirect('login')
        else:
            # Если форма невалидна, отображаем ошибки
            messages.error(request, "В вашей форме произошла ошибка. Пожалуйста, попробуйте еще раз.")
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Проверка аутентификации (упрощенная)
        if username == 'admin' and password == 'password':
            # Перенаправляем на страницу профиля
            return HttpResponseRedirect(reverse('profile'))
        else:
            # Перенаправляем на страницу входа с ошибкой
            return HttpResponseRedirect(reverse('login') + '?error=1')

    return render(request, 'login.html')


def profile_view(request):
    # Страница профиля доступна только для авторизованных пользователей
    if not request.user.is_authenticated:
        # Перенаправление на страницу входа, если пользователь не авторизован
        return HttpResponseRedirect(reverse('login'))

    return render(request, 'profile.html')
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Record, Blog


from django.http import HttpResponseRedirect
from .forms import LoginUserForm, MyForm, UserDataForm
from django.urls import reverse
from django.contrib.auth import authenticate, login


def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'layout/index.html/', context=data)


def profile(request):
    return render(request, 'main/profile.html')


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('profile'))
    else:
        form = LoginUserForm()
    return render(request, 'main/login.html', {'form': form})


def send_squares(request):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squares = [x**2 for x in numbers]
    return JsonResponse({'squares': squares})


def record_detail(request, id):
    record = get_object_or_404(Record, pk=id)
    return render(request, 'main/record_detail.html', {'record': record})


def all_records(request):
    records = Record.objects.all()
    return render(request, 'main/all_records.html', {'records': records})


def form_view(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            # Если форма прошла валидацию, сохраняем данные в базу
            form.save()
            # Перенаправляем на другую страницу с успешным сообщением
            return render(request, 'main/forma.html', {'form': form, 'success': True})
        else:
            # Если форма невалидна, возвращаем ошибку
            return render(request, 'main/forma.html', {'form': form, 'error': 'Ошибка валидации данных'})

    # Если форма не отправлена, показываем пустую форму
    form = UserDataForm()
    return render(request, 'main/forma.html', {'form': form})


def user_info(request):
    if request.user.is_authenticated:
        user_data = f'Пользователь: {request.user.username}\n'
        user_data += f'Полное имя: {request.user.get_full_name()}\n'
        user_data += f'Email: {request.user.email}\n'
        user_data += f'Группы: {", ".join([group.name for group in request.user.groups.all()])}\n'
        return HttpResponse(user_data)
    else:
        return HttpResponse('Пользователь не авторизован.')


def blog_list(request):
    blogs = Blog.objects.prefetch_related('tags').all()
    return render(request, 'main/blog_list.html', {'blogs': blogs})

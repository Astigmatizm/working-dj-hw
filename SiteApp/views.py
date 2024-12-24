from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Record


from django.http import HttpResponseRedirect
from .forms import LoginUserForm, MyForm
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
        form = MyForm(request.POST)
        if form.is_valid():
            return render(request, 'main/forma.html', {'form': form, 'success': True}) # Если форма валидна, выводим успешный результат
        else:
            return render(request, 'main/forma.html', {'form': form, 'error': 'Ошибка валидации данных'}) # Если форма невалидна, выводим ошибки
    form = MyForm() # Если форма еще не отправлена, просто отобразим пустую форму
    return render(request, 'main/forma.html', {'form': form})

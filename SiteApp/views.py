from django.db import transaction
from .models import User, Document
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Record, IceCream, User
from .forms import IceCreamForm, LoginUserForm, CustomForm, DocumentForm
from django.contrib.auth.models import Group, User

from django.http import HttpResponseRedirect
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


def create_ice_cream(request):
    if request.method == 'POST':
        form = IceCreamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ice_cream_list')
    else:
        form = IceCreamForm()

    return render(request, 'main/create_ice_cream.html', {'form': form})


def ice_cream_list(request):
    ice_creams = IceCream.objects.all()
    return render(request, 'main/ice_cream_list.html', {'ice_creams': ice_creams})


def manage_transaction(request):
    if request.method == 'POST':
        # Начинаем транзакцию
        try:
            with transaction.atomic():
                # Создаем записи с использованием метода .create()
                User.objects.create(name='Alice')
                User.objects.create(name='Bob')

                # Логика для отмены транзакции
                user_choice = request.POST.get('action')
                if user_choice == 'rollback':
                    raise Exception("Транзакция отменена пользователем.")

                # Подтверждаем транзакцию
                return HttpResponse("Транзакция завершена успешно.")

        except Exception as e:
            return HttpResponse(f"Ошибка: {e}. Выполняем откат транзакции.")

    return render(request, 'main/manage_transaction.html')


def handle_form(request):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            user = User(name=name, email=email)
            user.save()

            return HttpResponse("Данные успешно сохранены в базе данных.")
        else:
            return HttpResponse("Ошибка: данные формы некорректны.")

    else:
        form = CustomForm()

    return render(request, 'main/form_template.html', {'form': form})


def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Сохраняем загруженный файл в базе данных
            return redirect('document_list')  # Перенаправляем на страницу со списком документов
    else:
        form = DocumentForm()
    return render(request, 'main/upload_document.html', {'form': form})


def document_list(request):
    documents = Document.objects.all()  # Получаем все документы
    return render(request, 'main/document_list.html', {'documents': documents})


def create_group_and_add_users(request):
    # Создание новой группы (если она еще не существует)
    group_name = "New Group"
    group, created = Group.objects.get_or_create(name=group_name)

    # Добавление пользователей в группу
    # Для примера, добавим всех пользователей с username 'user1' и 'user2'
    users_to_add = User.objects.filter(username__in=['user1', 'user2'])

    # Добавление пользователей в группу
    for user in users_to_add:
        group.user_set.add(user)

    return HttpResponse(f'Группа "{group_name}" создана и пользователи добавлены!')


def view_groups(request):
    # Получаем текущего пользователя
    user = request.user

    # Получаем список групп текущего пользователя
    user_groups = user.groups.all()

    # Преобразуем группы в список имен
    group_names = [group.name for group in user_groups]

    # Передаем данные в контекст
    context = {
        'user_groups': group_names,  # Данные о группах пользователя
        'user': user,  # Дополнительная информация о пользователе (опционально)
    }

    # Возвращаем ответ с контекстом
    return render(request, 'main/groups.html', context)

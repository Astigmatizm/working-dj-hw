from .models import Record, IceCream, User, Document
from .forms import IceCreamForm, LoginUserForm, CustomForm, DocumentForm

from django.core.signing import Signer, BadSignature
from django.db import transaction
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login
from django.contrib import messages


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
    documents = Document.objects.all()
    return render(request, 'main/document_list.html', {'documents': documents})


def create_group_and_add_users(request):
    group_name = "New Group"
    group, created = Group.objects.get_or_create(name=group_name)

    users_to_add = User.objects.filter(username__in=['user1', 'user2'])

    for user in users_to_add:
        group.user_set.add(user)

    return HttpResponse(f'Группа "{group_name}" создана и пользователи добавлены!')


def view_groups(request):
    user = request.user

    user_groups = user.groups.all()

    group_names = [group.name for group in user_groups]

    context = {
        'user_groups': group_names,
        'user': user,
    }

    return render(request, 'main/groups.html', context)


def sign_data(request):
    signer = Signer()
    data_to_sign = "data_to_sign"
    signed_data = signer.sign(data_to_sign)
    verify_url = reverse('verify_data') + f'?signed_data={signed_data}'
    return HttpResponse(
        f"Подписанные данные: {signed_data}. Перейдите по <a href='{verify_url}'>этой ссылке</a> для проверки.")


def verify_data(request):
    signer = Signer()
    signed_data = request.GET.get('signed_data', '')

    try:
        original_data = signer.unsign(signed_data)
        return HttpResponse(f"Проверка успешна! Исходные данные: {original_data}")
    except BadSignature:
        return HttpResponse("Подпись неверна!")

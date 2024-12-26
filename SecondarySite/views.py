from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError, HttpResponseBadRequest, \
    HttpResponseForbidden, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse

from SecondarySite.forms import LoginUserForm

menu = [{"title": "О сайте", "url_name": "about"},

        {"title": "Добавить обьявление", "url_name": "add_page"},

        {"title": "Обратная связь", "url_name": "contact"},

        {"title": "Войти", "url_name": "login"}
]


data_db = [
    {'id': 1, 'title': 'fttf ffff', 'content': 'biografy fttf ffff', 'is_published': True},
    {'id': 2, 'title': 'fddf ffff', 'content': 'biografy fddf ffff', 'is_published': False},
    {'id': 3, 'title': 'fyyf ffff', 'content': 'biografy fyyf ffff', 'is_published': True}
]

def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }

    return render(request, 'layout/index.html/', context=data)

def about(request):
    return render(request, 'layout/about.html/', {'title': 'О сайте', 'menu': menu})

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьти с id = {post_id}')

def add_page(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Обратная связь')

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
    return render(request, 'layout/login.html', {'form': form})

def bad_request(request, exception):    # error400
    return HttpResponseBadRequest('<h1>error 400. Некорректный Запрос</h1>')

def forbidden_page(request, exception):     # error403
    return HttpResponseForbidden('<h1>error 403. Доступ запрещен</h1>')

def page_not_found(request, exception):     # error404
    return HttpResponseNotFound("<h1>error 404. Страница не найдена</h1>")

def server_error(request):     # error500
    return HttpResponseServerError('<h1>error 500. Внутренняя ошибка сервера</h1>')
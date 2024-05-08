from audioop import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавление нового проекта', 'url_name': 'addproject'},
    {'title': 'Обратная связь', 'url_name': 'feedback'},
    {'title': 'Авторизация', 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'Первый Квартал', 'content': 'Застройщик Брусника', 'is_published': True},
    {'id': 2, 'title': 'Экография', 'content': 'Застройщик Охта Групп', 'is_published': True},
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'realty/index.html', context=data)


def about(request):
    return render(request, 'realty/about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request, post_id):
    return HttpResponse(f'Отображение проекта с id = {post_id}')


def addproject(request):
    return HttpResponse('Добавление нового проекта')


def feedback(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Аторизация')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404
from django.template.defaultfilters import title
from datetime import datetime


MENU = [
        {'title': 'Главная страница', 'url_name': 'index'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Калькуляторы', 'url_name': 'calculators'},
        {'title': 'Создать калькулятор', 'url_name': 'add'},
        {'title': 'Обратная связь', 'url_name': 'feedback'},
        {'title': 'Войти', 'url_name': 'login'},
        ]

CALCS = [
    {'title': 'Расчет веса металлопроката', 'slug': 'weight', 'published': True},
    {'title': 'Расчет раскроя листового проката', 'slug': 'sheet-metal', 'published': False},
    {'title': 'Расчёт длины развёртки гнутого профиля', 'slug': 'length-bent-profile', 'published': False},
    {'title': 'Расчёт себестоимости раскроя', 'slug': 'cost', 'published': True},
]
DATA = {'title': 'Главная страница',
        'menu': MENU,
        'calcs': CALCS,
        'year': datetime.now().year,
        'calc_selected': None,}

def index(request):
    return render(request, 'calc/index.html', context=DATA)

def calcs(request, calc_slug: str):
    return HttpResponse(f'Calculators {calc_slug} page')

def page_not_found(request: HttpRequest, exception: Http404):
    return HttpResponseNotFound(f'Страница не найдена: {exception}')

def about(request):
    return render(request, 'calc/about.html', context={'title': 'О сайте', 'menu': MENU})

def calculators(request):
    return HttpResponse(f'Страница с калькулятором')

def add(request):
    return HttpResponse(f'Создать калькулятор')

def feedback(request):
    return HttpResponse(f'Обратная связь')

def login(request):
    return HttpResponse(f'Кабинет пользователя')

def show_calculators(request, calc_slug):
    DATA = {'title': 'Главная страница',
            'menu': MENU,
            'calcs': CALCS,
            'year': datetime.now().year,
            'calc_selected': calc_slug, }
    return render(request, 'calc/calculators.html', context=DATA)

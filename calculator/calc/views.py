from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404
from django.template.defaultfilters import title
from datetime import datetime


MENU = [
        {'title': 'Home page', 'url_name': 'index'},
        {'title': 'About site', 'url_name': 'about'},
        {'title': 'Calculators', 'url_name': 'calculators'},
        {'title': 'Add calculator', 'url_name': 'add'},
        {'title': 'Feedback', 'url_name': 'feedback'},
        {'title': 'Login', 'url_name': 'login'},
        ]

CALCS = [
    {'title': 'Weight Calculator', 'slug': 'weight', 'published': True},
    {'title': 'Sheet metal Calculator', 'slug': 'sheet-metal', 'published': False},
    {'title': 'Length of the bent profile Calculator', 'slug': 'length-bent-profile', 'published': False},
    {'title': 'Cost Calculator', 'slug': 'cost', 'published': True},
]
DATA = {'title': 'Main Page',
        'menu': MENU,
        'calcs': CALCS,
        'year': datetime.now().year,
        'calc_selected': None,}

def index(request):
    return render(request, 'calc/index.html', context=DATA)

def calcs(request, calc_slug: str):
    return HttpResponse(f'Calculators {calc_slug} page')

def page_not_found(request: HttpRequest, exception: Http404):
    return HttpResponseNotFound(f'Page not found: {exception}')

def about(request):
    return render(request, 'calc/about.html', context={'title': 'About site', 'menu': MENU})

def calculators(request):
    return HttpResponse(f'Calculators page')

def add(request):
    return HttpResponse(f'Add-calculator page')

def feedback(request):
    return HttpResponse(f'Feedback page')

def login(request):
    return HttpResponse(f'Login')

def show_calculators(request, calc_slug):
    DATA = {'title': 'Main Page',
            'menu': MENU,
            'calcs': CALCS,
            'year': datetime.now().year,
            'calc_selected': calc_slug, }
    return render(request, 'calc/calculators.html', context=DATA)

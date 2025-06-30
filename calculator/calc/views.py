from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404
from django.template.defaultfilters import title

menu = [ 'About site', 'Calculators', 'Add calculator', 'Feedback', 'Login']

calcs = [
    {'title': 'Weight Calculator', 'slug': 'weight', 'published': True},
    {'title': 'Sheet metal Calculator', 'slug': 'sheet-metal', 'published': False},
    {'title': 'Length of the bent profile Calculator', 'slug': 'length-bent-profile', 'published': False},
    {'title': 'Cost Calculator', 'slug': 'cost', 'published': True},
]
data = {'title': 'Main Page',
        'menu': menu,
        'calcs': calcs,}

def index(request):
    return render(request, 'calc/index.html', context=data)

def calcs(request, calc_slug: str):
    return HttpResponse(f'Calculators {calc_slug} page')

def page_not_found(request: HttpRequest, exception: Http404):
    return HttpResponseNotFound(f'Page not found: {exception}')

def about(request):
    return render(request, 'calc/about.html', context={'title': 'About site', 'menu': menu})
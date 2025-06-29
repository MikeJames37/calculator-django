from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404

def index(request):
    return HttpResponse('Home page calc')

def calcs(request, calc_slug: str):
    return HttpResponse(f'Calculators {calc_slug} page')

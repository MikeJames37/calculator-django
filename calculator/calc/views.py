from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404

def index(request):
    return HttpResponse('Home page calc')

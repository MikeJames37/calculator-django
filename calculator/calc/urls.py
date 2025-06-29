from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('calcs/<slug:calc_slug>/', views.calcs),
]
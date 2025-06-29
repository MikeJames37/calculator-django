from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('calcs/<slug:calc_slug>/', views.calcs, name='calcs'),
    path('about/', views.about, name='about')
]
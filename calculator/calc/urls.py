from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('calc/<slug:calc_slug>/', views.calcs, name='calc'),
    path('about/', views.about, name='about'),
    path('calculators/', views.calculators, name='calculators'),
    path('add/', views.add, name='add'),
    path('feedback/', views.feedback, name='feedback'),
    path('login/', views.login, name='login'),
]
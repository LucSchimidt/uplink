from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home, name="home"),
    path('teste/', views.teste, name="teste"),
    path('personalizar/', views.personalizar, name="personalizar"),
    path('conta/', views.conta, name="conta"),
    path('temas/', views.temas, name="temas"),

    #URLS de fora:
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('salvar-dados-formulario/', views.salvar_dados_formulario, name='salvar_dados_formulario'),
    path('temas/aplica_tema/', views.aplica_tema, name="aplica_tema"),
]
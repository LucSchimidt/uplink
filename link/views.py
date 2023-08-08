from django.shortcuts import render, redirect
from django.http import HttpResponse
from ulplataform.models import Uplink, UplinkTheme
import json

# Create your views here.

def link(request, username):
    usuario_up = username
    print(usuario_up)

    uplink = Uplink.objects.get(uplink_name=usuario_up)
    links = json.loads(uplink.links)

    for item in uplink.links_redes:
        print(item['icon'])


    selected_theme = uplink.tema

    tema = UplinkTheme.objects.get(nome_tema = selected_theme)

    return render(request, 'html/main.html', {'uplink': uplink, 'tema': tema, 'links':links})
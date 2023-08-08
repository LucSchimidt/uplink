from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.sessions.backends.signed_cookies import SessionStore
import json
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required
def home(request):
    return render(request, 'html/conta.html')


def teste(request):
    usuario_logado = request.user.id

    uplink = Uplink.objects.get(usuario=usuario_logado)
    links = json.loads(uplink.links)

    for item in uplink.links_redes:
        print(item['icon'])


    selected_theme = uplink.tema

    tema = UplinkTheme.objects.get(nome_tema = selected_theme)

    return render(request, 'html/teste.html', {'uplink': uplink, 'tema': tema, 'links':links})



#VIEW DA PÁGINA DE CONTAS DO UPLINK:
@login_required
def conta(request):
    usuario = request.user

    return render(request, 'html/conta.html',{'user':usuario})

#VIEW DA PÁGINA DE PERSONALIZAÇÃO DO UPLINK:
@login_required
def personalizar(request): 
    usuario_logado = request.user.id
    uplink = Uplink.objects.get(usuario=usuario_logado)
    
    return render(request, 'html/personalizar.html',{'uplink': uplink})

def temas(request):
    temas = UplinkTheme.objects.all()

    return render(request, 'html/temas.html', {'temas': temas})





#LÓGICA DE SALVAR AS INFORMAÇÕES DO FORMULÁRIO DO UPLINK NO MODEL:
@login_required
def salvar_dados_formulario(request):
    if request.method == 'POST':

        # Acessando o Model do usuario logado:
        
        usuario_logado = request.user.id
        uplink = Uplink.objects.get(usuario=usuario_logado)

        titulo = request.POST.get("title")
        #print(request.FILES.items)
        foto = request.FILES.get("photo")

        # Lidando com a parte de links:
        links = []

        #Lógica que pega os campos dos links:
        for key, value in request.POST.items():
                if key.startswith('link-'):

                    link_number = key.split('-')[1]
                    titulo_key = f'titulo-{link_number}'
                    link_titulo = request.POST.get(titulo_key)

                    if link_titulo != '':

                        visible_value = request.POST.get(f'eye_input_{link_number}')
                        if visible_value:
                            checked = 'True'
                        else:
                            checked = 'False'
                        
                        if link_titulo and value:
                            link_obj = {'titulo': link_titulo, 'link': value, 'visible': checked}

                            http = 'https://'

                            if http in link_obj['link']:
                                link_obj['link'] = link_obj['link'].replace('https://', '')
                                links.append(link_obj)
                            else:
                                links.append(link_obj)
                            


                    else:
                        print('Campo não está completo.')

                    

        # Verifica se o campo não está vazio antes de atualizar o modelo
        if titulo != '':
            uplink.titulo = titulo

        if foto is not None:
            uplink.foto = foto

        if links:
            # Cria o JSON com os links coletados
            json_data = json.dumps({'links': links})
            uplink.links = json_data
            #print(json_data)

        # Lidando com a parte de links das redes sociais:
        redes = [
            {"nome": "insta", "link": request.POST.get("insta-link"), "visible": request.POST.get("eye_input_insta"), "icon": 'bi bi-instagram'},
            {"nome": "face", "link": request.POST.get("face-link"), "visible": request.POST.get("eye_input_face"), "icon": 'bi bi-facebook'},
            {"nome": "tiktok", "link": request.POST.get("tiktok-link"), "visible": request.POST.get("eye_input_tiktok"), "icon": 'bi bi-tiktok'},
            {"nome": "youtube", "link": request.POST.get("youtube-link"), "visible": request.POST.get("eye_input_youtube"), "icon": 'bi bi-youtube'},
            {"nome": "twitter", "link": request.POST.get("twitter-link"), "visible": request.POST.get("eye_input_twitter"), "icon": 'bi bi-twitter'},
            {"nome": "threads", "link": request.POST.get("threads-link"), "visible": request.POST.get("eye_input_threads"), "icon": 'bi bi-threads'},
        ]

        redes_validas = [rede for rede in redes if rede["link"]]

        http="https://"

        for rede in redes_validas:
            if http in rede['link']:
                rede['link'] = rede['link'].replace(http, '')
            else:
                pass

        # Atualizando apenas as redes sociais válidas na lista de JSONs existente (uplink.links_redes)
        for nova_rede in redes_validas:
            nome_rede = nova_rede["nome"]
            for item in uplink.links_redes:
                if item["nome"] == nome_rede:
                    item.update(nova_rede)
                    break
            else:
                uplink.links_redes.append(nova_rede)

        # Salvando as informações do form no modelo
        uplink.save()







        messages.success(request, 'UpLink atualizado com sucesso!')
        return redirect('/plataform/personalizar/')


#VIEW QUE APLICA O TEMA NA PÁGINA DO UPLINK:
@login_required
def aplica_tema(request):
    if request.method == 'POST':
        usuario_logado = request.user.id
        uplink = Uplink.objects.get(usuario=usuario_logado)

        tema = request.POST.get('selected-theme-input')

        uplink.tema = tema

        uplink.save()

        messages.success(request, 'Tema aplicado com sucesso!')
        return redirect('/plataform/temas/')
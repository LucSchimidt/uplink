from django import forms
from allauth.account.forms import SignupForm
from django.forms import Select
from django.forms import SelectMultiple


class CustomSignupForm(SignupForm):
    personal_link = forms.CharField(max_length=30, label='URL do UpLink(final do link)', widget=forms.TextInput(attrs={'placeholder': 'ul.upsys.app/seu_url_personalizado'}))

    b_types = [
        ('loja online', 'Loja Online'),
        ('criador de conteudo', 'Criador de Conteúdo'),
        ('prestador', 'Prestador de Serviços'),
        ('pessoal', 'Pessoal')
    ]
    bussiness_type = forms.MultipleChoiceField(choices=b_types, 
                                               label='Finalidade do UpLink',
                                               widget=Select(attrs={'class': 'form-control'}),
                                               required=False
                                               )
    phone_number = forms.CharField(max_length=15, label='Número de Telefone', widget=forms.TextInput(attrs={'placeholder': '+55(19)99999-9999'}))

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .services import coisas_service 
from .forms import CoisasForm
from .entidades.Coisa import Coisa 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.list import ListView
from .models import Coisa
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "app/home.html"



# Parte de cadastro,login, logout do Usuario cadastrado
# TODO:usar CBV para processo de auth do usuario.
def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('login_usuario')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'usuario/form.html', {"form_usuario": form_usuario})

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            messages.error(request, 'As credencias do usuário estão incorretas ou usuário não cadastrado')
            return redirect('login_usuario')
    else:
        form_login = AuthenticationForm()
    return render(request, 'usuario/login.html', {"form_login": form_login})

def deslogar_usuario(request):
    logout(request)
    return redirect('login_usuario')



class CoisasListView( ListView):
    model = Coisa
    



class CoisaCreateView(CreateView):
    model = Coisa
    fields =  [
            'item', 
            'data_emprestimo', 
            'data_devolucao', 
            'contato_amigo', 
            ]

class CoisaUpdateView(UpdateView):
    model = Coisa
    fields = [
            'item',
            'data_emprestimo',
            'data_devolucao',
            'contato_amigo',
            'retorno'
            ]
    template_name_suffix = '_update_form'
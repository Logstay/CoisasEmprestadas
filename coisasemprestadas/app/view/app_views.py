from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..services import coisas_service 
from ..forms import CoisasForm
from ..entidades import Coisas_usr


@login_required()
def home(request):
    return render(request, 'app/home.html')


def cadastrar_coisa(request):
    if request.method == "POST":
        form_coisa = CoisasForm(request.POST)
        if form_coisa.is_valid():
            titulo = form_coisa.cleaned_data["titulo"]

            descricao = form_coisa.cleaned_data["descricao"]

            data_expiracao = form_coisa.cleaned_data["data_expiracao"]

            prioridade = form_coisa.cleaned_data["prioridade"]

            nova_coisa = Coisas_usr(
                item_usr= item_usr, 
                data_emprestimo_usr= data_emprestimo_usr, 
                data_devolucao_usr= data_devolucao_usr, 
                contato_amigo_usr= contato_amigo_usr,  
                usuario=request.user
            )

            coisas_service.cadastrar_coisa(nova_coisa)
            return redirect('listar_tarefas')
    else:
        form_coisa = CoisasForm()
    return render(request, 'app/form_tarefa.html', {"form_tarefa": form_tarefa})

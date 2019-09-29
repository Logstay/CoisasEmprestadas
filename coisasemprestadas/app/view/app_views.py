from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

@login_required()
def home(request):
    return render(request, 'app/home.html')


def cadastrar_coisa(request):
    if request.method == "POST":
        form_tarefa = TarefaForm(request.POST)
        if form_tarefa.is_valid():
            titulo = form_tarefa.cleaned_data["titulo"]

            descricao = form_tarefa.cleaned_data["descricao"]

            data_expiracao = form_tarefa.cleaned_data["data_expiracao"]

            prioridade = form_tarefa.cleaned_data["prioridade"]
            
            tarefa_nova = Coisas_usr(
                titulo=titulo,
                descricao=descricao,
                data_expiracao=data_expiracao, 
                prioridade=prioridade, 
                usuario=request.user)

            tarefa_service.cadastrar_tarefa(tarefa_nova)
            return redirect('listar_tarefas')
    else:
        form_tarefa = TarefaForm()
    return render(request, 'tarefas/form_tarefa.html', {"form_tarefa": form_tarefa})

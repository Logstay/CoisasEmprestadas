from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('login')
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
            messages.error(request, 'As credencias do usuário estão incorretas')
            return redirect('login')
    else:
        form_login = AuthenticationForm()
    return render(request, 'usuario/login.html', {"form_login": form_login})

def deslogar_usuario(request):
    logout(request)
    return redirect('login')
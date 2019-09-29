from django.urls import path
from .view.app_views import *
from .view.usuario_views import *

urlpatterns = [
    
    path('login_usuario', logar_usuario , name='login' ),

    path('logout_usuario', deslogar_usuario , name='logout' ),

    path('cadastro_usuario', cadastrar_usuario , name='cadastro' ),

]

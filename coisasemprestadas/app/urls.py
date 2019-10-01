from django.urls import path
from .views import *

urlpatterns = [
    
    path('login_usuario', logar_usuario , name='login_usuario' ),

    path('logout_usuario', deslogar_usuario , name='logout_usuario' ),

    path('cadastro_usuario', cadastrar_usuario , name='cadastrar' ),

    path('home', HomeTemplateView.as_view(), name='home'),

    path('cadastrar_coisa', CoisaCreateView.as_view(model=Coisa, success_url="/listar"), name='cadastrar_coisa'),

    # path('listar/<int:id>', listar_coisas_id, name='listar_coisa_id'),

    path('listar', CoisasListView.as_view(), name='listar_coisa'),

]

from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_livro/', views.cadastrar_livro, name='cadastrar_livro'),
    path('pesquisar_livro/', views.pesquisar_livro, name='pesquisar_livro'),
]

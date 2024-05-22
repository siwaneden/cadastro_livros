from django.shortcuts import render
from .models import Livro

def cadastrar_livro(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        isbn = request.POST.get('isbn')
        descricao = request.POST.get('descricao')
        Livro.objects.create(titulo=titulo, autor=autor, isbn=isbn, descricao=descricao)
        return render(request, 'cadastrar_livro.html', {'message': 'Livro cadastrado com sucesso!'})
    return render(request, 'cadastrar_livro.html')

def pesquisar_livro(request):
    isbn = request.GET.get('isbn')
    livro = Livro.objects.filter(isbn=isbn).first()
    return render(request, 'pesquisar_livro.html', {'livro': livro})

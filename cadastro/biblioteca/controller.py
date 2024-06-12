from django.http import JsonResponse
from .models import Livro

def cadastrar_livro(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        isbn = request.POST.get('isbn')
        descricao = request.POST.get('descricao')
        livro = Livro.objects.create(titulo=titulo, autor=autor, isbn=isbn, descricao=descricao)
        return JsonResponse({'message': 'Livro cadastrado com sucesso!'})

def pesquisar_livro(request, isbn):
    livro = Livro.objects.filter(isbn=isbn).first()
    if livro:
        return JsonResponse({'titulo': livro.titulo, 'autor': livro.autor, 'descricao': livro.descricao})
    else:
        return JsonResponse({'message': 'Livro não encontrado'})
    
def listar_livros(request):
    if request.method == 'GET':
        livros = Livro.objects.all().values('titulo', 'autor', 'isbn', 'descricao')
        livros_list = list(livros)
        return JsonResponse(livros_list, safe=False)    


from django.db import models



class LivroManager(models.Manager):
    def buscar_por_titulo(self, titulo):
        return self.get_queryset().filter(titulo__icontains=titulo)
    

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    isbn = models.IntegerField(unique=True)
    descricao = models.TextField()
    objects = LivroManager()

    def __str__(self):
        return self.titulo

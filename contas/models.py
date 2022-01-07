from django.db import models

# Create your models here.

class categoria(models.Model):
    nome=models.CharField(max_length=100)
    dt_criaçao=models.DateTimeField(auto_now_add=True)

class listar(models.Model):
    nome = models.CharField(max_length=100)
    valor= models.CharField(max_length=100)
    unidade=models.CharField(max_length=100)

    def __str__(self):
        return self.nome

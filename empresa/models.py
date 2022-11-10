from django.db import models


# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cidade = models.CharField(max_lengh=30)
    endereco = models.CharField(max_length=30)
    caracteristica_empresa = models.TextField()

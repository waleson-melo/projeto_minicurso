from django.db import models


class Tarefa(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from tarefa.models import Tarefa


class TarefaCadastrar(CreateView):
    template_name = 'tarefa.html'
    model = Tarefa
    fields = ['titulo', 'descricao', 'status']
    success_url = reverse_lazy('listar')


class TarefaListar(ListView):
    template_name = 'listar_tarefa.html'
    model = Tarefa


class TarefaEditar(UpdateView):
    template_name = 'tarefa.html'
    model = Tarefa
    fields = ['titulo', 'descricao', 'status']
    success_url = reverse_lazy('listar')


class TarefaDeletar(DeleteView):
    template_name = 'delete.html'
    model = Tarefa
    success_url = reverse_lazy('listar')

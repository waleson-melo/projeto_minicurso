from django.urls import path

from tarefa.views import TarefaCadastrar, TarefaListar, TarefaEditar, TarefaDeletar


urlpatterns = [
    path('', TarefaListar.as_view(), name='listar'),
    path('cadastrar/', TarefaCadastrar.as_view(), name='cadastrar'),
    path('editar/<int:pk>', TarefaEditar.as_view(), name='editar'),
    path('excluir/<int:pk>', TarefaDeletar.as_view(), name='excluir')
]

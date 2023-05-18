from rest_framework import generics
from .serializers import TaskSerializers
from .models import Tasks
from rest_framework import filters


class ListAllTasks(generics.ListAPIView):

    """
        View para listar todos os itens no banco de dados.
    """


    queryset = Tasks.objects.all()
    serializer_class = TaskSerializers
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['Updated']
    search_fields = ['Task_name']


class DetailsTask(generics.RetrieveAPIView):

    """
        View responsável para leitura via id de item no banco de dados.
    """

    queryset = Tasks.objects.all()
    serializer_class = TaskSerializers


class CreateTasks(generics.CreateAPIView):

    """
        View responsavel para criacao de Tasks no banco de dados.
    """

    queryset = Tasks.objects.all()
    serializer_class = TaskSerializers


class DeleteTasks(generics.DestroyAPIView):
    """
        View responsavel para deletar dados atraves do id,
    """

    queryset = Tasks.objects.all()
    serializer_class = TaskSerializers


class UpdateTasks(generics.UpdateAPIView):

    """
        View responsavel para Atualizar os dados atraves do id.

    """

    queryset = Tasks.objects.all()
    serializer_class = TaskSerializers


class DoneTasks(generics.ListAPIView):

    """
        View para filtrar as tasks já finalizadas.

    """

    queryset = Tasks.objects.filter(Done=True)
    serializer_class = TaskSerializers

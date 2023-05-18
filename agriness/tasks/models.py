from django.db import models


class Tasks(models.Model):

    """
        Classe responsavel pela criacao das Tasks.

        : Parameters :

        Task_name -> Model único para nao deixar escrever mesmos conteúdos em models.

    """
    DATE_INPUT_FORMATS = ['%d-%m-%Y']
    Task_name = models.CharField(max_length=120, unique=True, blank=False)
    Descriptions = models.TextField(max_length=520, blank=False)
    Done = models.BooleanField(blank=False, default=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)



    def __str__(self):

        return f"{self.Task_name}"


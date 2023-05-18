from rest_framework import serializers
from .models import Tasks


class TaskSerializers(serializers.ModelSerializer):
    """
        Serializer responsavel pela chamada da API que será encaminhada ao model de tratamento.
    """

    class Meta:
        model = Tasks
        fields = "__all__"

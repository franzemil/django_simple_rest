from rest_framework import serializers

from todos.models import Tarea


class TareaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nombre = serializers.CharField()
    terminado = serializers.BooleanField()

    def create(self, validated_data):
        instance = Tarea.objects.create(**validated_data)
        return instance




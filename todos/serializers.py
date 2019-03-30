from rest_framework import serializers

from todos.models import Tarea


class TareaSerializer(serializers.Serializer):
    id = serializers.IntegerField(allow_null=True, required=False)
    nombre = serializers.CharField()
    terminado = serializers.BooleanField(default=False, required=False)

    def create(self, validated_data):
        instance = Tarea.objects.create(**validated_data)
        return instance




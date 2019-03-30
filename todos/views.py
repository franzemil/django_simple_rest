from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from todos.serializers import TareaSerializer
from .models import Tarea


@api_view(['POST', 'GET'])
def crear_tarea(request):
    if request.method == 'GET':
        lista_tareas = Tarea.objects.all()
        serializer = TareaSerializer(lista_tareas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = TareaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TareaViewSet(ViewSet):
    def list(self, request):
        lista_tareas = Tarea.objects.all()
        serializer = TareaSerializer(lista_tareas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = TareaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

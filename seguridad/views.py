from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from seguridad.serializers import UserSerializer


@api_view(['GET'])
def me(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


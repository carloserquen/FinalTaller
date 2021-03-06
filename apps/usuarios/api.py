import logging

from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Usuario
from apps.tareas.models import Tarea

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


@api_view(['GET', ])
def usuarios_get(request):
    data = {}
    try:
        usuarios = Usuario.objects.filter(rol="TeamMember")
        arr_list = []
        for usuario in usuarios:
            arr_list.append({
                'nombre': usuario.user.username,
                'id': usuario.id
                })

        data.update({
            'results': arr_list,
            'success': True
        })

        return Response(data)

    except Exception, e:
        logging.error(e)
        content = {'Error': 'Not login as enterprise'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
def tareas_update(request, pk):
    data = {}
    print request.data.get("status")
    try:
        tarea = Tarea.objects.get(id=pk)
        tarea.estado = request.data.get("status")
        tarea.save()
        return Response(data)

    except Exception, e:
        logging.error(e)
        content = {'Error': 'Not login as enterprise'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

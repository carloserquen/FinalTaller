import logging

from .models import Usuario

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

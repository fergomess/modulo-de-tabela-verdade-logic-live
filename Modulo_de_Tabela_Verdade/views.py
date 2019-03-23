from django.shortcuts import render
from Modulo_de_Tabela_Verdade.models import *
from .serializers import *
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import requests
import json


'''def index(request):
    queryset = Modulo.objects.all()
    return render(request, 'Modulo_de_Tabela_Verdade/inicio.html', {'modulos': queryset})'''

# ViewSets define the view behavior.
class UserViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ModuloViewSet(generics.ListAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer

class NivelViewSet(generics.ListAPIView):
    serializer_class = NivelSerializer

    def get_queryset(self):
        nivel_id = self.kwargs['id']
        return Nivel.objects.filter(id=nivel_id)

class ExercicioViewSet(generics.ListAPIView):
    serializer_class = ExercicioSerializer

    def get_queryset(self):
        exercicio_id = self.kwargs['id']
        return Exercicio.objects.filter(id=exercicio_id)

class RecompensaViewSet(generics.ListAPIView):
    serializer_class = RecompensaSerializer

    def get_queryset(self):
        recompensa_id = self.kwargs['id']
        return Recompensa.objects.filter(id=recompensa_id)

@permission_classes((AllowAny,))
class ModuloList(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request,):
        r = requests.get('http://localhost:8000/api/modulos/')
        json = r.json()
        return Response({'modulos': json}, template_name='Modulo_de_Tabela_Verdade/inicio.html')

@permission_classes((AllowAny,))
class ExercicioAprendizagemList(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request,nivel, id, *args, **kwargs):
        r = requests.get('http://localhost:8000/api/exercicio/'+ id)
        dados = r.json()
        if (nivel == '1' or nivel == '2'):
            return Response({'dados': dados}, template_name='Modulo_de_Tabela_Verdade/tela_padrao_conteudos.html')
        else:
            for formula in dados:
                for tabela in formula['Formula_fk_exercicio']:
                    form = json.loads(tabela['formula'])
                    tab = json.loads(tabela['tabela_verdade'])
            return Response({'dados': dados, 'tabela':tab, 'formula':form}, template_name='Modulo_de_Tabela_Verdade/tela_padrao_exercicios.html')
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, generics
from Modulo_de_Tabela_Verdade.models import *


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

#Serializers define the API representation to PERGUNTA_FORMULA
class Pergunta_FormulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pergunta_Formula
        fields = ('id','formula', 'pergunta')

#Serializers define the API representation to FORMULA
class FormulaSerializer(serializers.ModelSerializer):
    Pergunta_Formula_fk_Formula = Pergunta_FormulaSerializer(many=True)
    class Meta:
        model = Formula
        fields = ('formula', 'tabela_verdade', 'quantidade_proposicoes', 'quantidade_linhas', 'Pergunta_Formula_fk_Formula')

#Serializers define the API representation to EXERCICIO
class ExercicioSerializer(serializers.ModelSerializer):
    Formula_fk_exercicio = FormulaSerializer(many=True)
    class Meta:
        model = Exercicio
        fields = ('id', 'nome', 'descricao', 'situacao', 'recompensa', 'nivel','Formula_fk_exercicio')

#Serializers define the API representation to NIVEL
class NivelSerializer(serializers.ModelSerializer):
    Exercicio_fk_Nivel = ExercicioSerializer(many=True)
    class Meta:
        model = Nivel
        fields = ('nome', 'descricao', 'situacao', 'tempo_de_execucao', 'recompensa', 'modulo', 'Exercicio_fk_Nivel')

class ExercicioNivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = ('id', 'nome', 'descricao', 'situacao', 'recompensa', 'nivel')

class NivelModuloSerializer(serializers.ModelSerializer):
    Exercicio_fk_Nivel = ExercicioNivelSerializer(many=True)
    class Meta:
        model = Nivel
        fields = ('id','nome', 'descricao', 'situacao', 'tempo_de_execucao', 'recompensa', 'modulo', 'Exercicio_fk_Nivel')

#Serializers define the API representation to MODULO
class ModuloSerializer(serializers.ModelSerializer):
    Nivel_fk_Modulo = NivelModuloSerializer(many=True)
    class Meta:
        model = Modulo
        fields = ('nome', 'descricao', 'situacao', 'personagem', 'Nivel_fk_Modulo')

#Serializers define the API representation to RECOMPENSA
class RecompensaSerializer(serializers.ModelSerializer):
    Exercicio_fk_recompensa = ExercicioSerializer(many=True)
    class Meta:
        model = Recompensa
        fields = ('nome', 'imagem', 'valor_da_pontuacao', 'Exercicio_fk_recompensa')

#Serializers define the API representation to PERSONAGEM
class PersonagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personagem
        fields = ('nome', 'imagem')

#Serializers define the API representation to RESPOSTA
class RespostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resposta
        fields = ('nivel', 'exercicio', 'academico', 'situacao')
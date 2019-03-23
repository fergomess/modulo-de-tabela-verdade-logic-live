from django.contrib import admin
from .models import *

@admin.register(Academico)
class AcademicoAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'email',)
    list_per_page = 20
    list_display = ('nome', 'email', 'data_de_nascimento')
    list_display_links = list_display
    ordering = ('nome',)

@admin.register(Personagem)
class PersonagemAdmin(admin.ModelAdmin):
    search_fields = ('nome',)
    list_per_page = 20
    list_display = ('nome',)
    list_display_links = list_display
    ordering = ('nome',)

@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    search_fields = ('nome','descricao',)
    list_per_page = 20
    list_display = ('nome', 'descricao', 'situacao')
    list_display_links = list_display
    ordering = ('nome',)

@admin.register(Recompensa)
class RecompensaAdmin(admin.ModelAdmin):
    search_fields = ('nome',)
    list_per_page = 20
    list_display = ('nome', 'valor_da_pontuacao',)
    list_display_links = list_display
    ordering = ('nome',)

@admin.register(Nivel)
class NivelAdmin(admin.ModelAdmin):
    search_fields = ('nome',)
    list_per_page = 20
    list_display = ('nome', 'descricao', 'situacao', 'modulo')
    list_display_links = list_display
    ordering = ('nome',)

@admin.register(Exercicio)
class ExercicioAdmin(admin.ModelAdmin):
    search_fields = ('nome',)
    list_per_page = 20
    list_display = ('nome', 'descricao', 'nivel')
    list_display_links = list_display
    list_filter = ('nivel',)
    ordering = ('nome',)

@admin.register(Formula)
class FormulaAdmin(admin.ModelAdmin):
    #change_list_template = 'admin/Modulo_de_Tabela_Verdade/formula_change_list.html'
    search_fields = ('formula',)
    list_per_page = 20
    list_display = ('formula', 'exercicio', 'quantidade_proposicoes', 'quantidade_linhas')
    list_display_links = list_display
    list_filter = ('exercicio__nivel', 'quantidade_proposicoes')
    ordering = ('exercicio',)



@admin.register(Pergunta_Formula)
class Pergunta_FormulaAdmin(admin.ModelAdmin):
    search_fields = ('formula',)
    list_per_page = 20
    list_display = ('formula', 'pergunta',)
    list_display_links = list_display
    ordering = ('formula',)

@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    search_fields = ('academico',)
    list_per_page = 20
    list_display = ('academico', 'exercicio',)
    list_display_links = list_display
    ordering = ('academico',)
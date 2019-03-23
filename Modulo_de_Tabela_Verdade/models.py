from django.db import models
from .constants import *
from django.utils.timezone import localtime
from ckeditor.fields import RichTextField

class Academico(models.Model):
    nome = models.CharField(verbose_name='Usuário', max_length=255)
    data_de_nascimento = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True, verbose_name='E-mail')
    usuario = models.ForeignKey('auth.User', verbose_name='Usuário', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nome

class Personagem(models.Model):
    nome = models.CharField(verbose_name='Personagem', max_length=128)
    imagem = models.ImageField(upload_to='Modulo_de_Tabela_Verdade_images/',null=True, blank=True, verbose_name='Imagem')
    data_de_cadastro = models.DateTimeField(auto_now=True, editable=False, blank=True)

    class Meta:
        verbose_name_plural = 'Personagens'

    def __str__(self):
        return self.nome

class Modulo(models.Model):
    nome = models.CharField(verbose_name='Módulo', max_length=128)
    descricao = models.TextField(null=True, blank=True, verbose_name='Descrição do Módulo')
    situacao = models.IntegerField(default=0, verbose_name='Situação do Módulo', choices=TIPO_DE_SITUACAO_MODULO.choices(), null=True, blank=True)
    data_de_cadastro = models.DateTimeField(auto_now=True, editable=False, blank=True)
    personagem = models.ForeignKey(Personagem, related_name='Modulo_fk_Personagem', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Módulo'
        verbose_name_plural = 'Módulos'

    def __str__(self):
        return self.nome


class Recompensa(models.Model):
    nome = models.CharField(verbose_name='Recompensa', max_length=128)
    imagem = models.ImageField(upload_to='Modulo_de_Tabela_Verdade_images/',null=True, blank=True, verbose_name='Imagem')
    valor_da_pontuacao = models.DecimalField(max_digits=8, decimal_places=2)
    data_de_cadastro = models.DateTimeField(auto_now=True, editable=False, blank=True)

    class Meta:
        verbose_name_plural = 'Recompensas'

    def __str__(self):
        return self.nome


class Nivel(models.Model):
    nome = models.CharField(verbose_name='Nível', max_length=128)
    descricao = models.TextField(null=True, blank=True, verbose_name='Descrição do Nível')
    situacao = models.IntegerField(default=0, verbose_name='Situação do Nível', choices=TIPO_DE_SITUACAO_NIVEL.choices(), null=True, blank=True)
    tempo_de_execucao = models.PositiveIntegerField(verbose_name='Tempo de Execução', null=True, blank=True)
    recompensa = models.ForeignKey(Recompensa, related_name='Nivel_fk_recompensa', on_delete=models.SET_NULL, null=True, verbose_name='Recompensa')
    data_de_cadastro = models.DateTimeField(auto_now=True, editable=False, blank=True)
    modulo = models.ForeignKey(Modulo, related_name='Nivel_fk_Modulo', on_delete=models.SET_NULL, null=True, verbose_name='Módulo')

    class Meta:
        verbose_name = 'Nível'
        verbose_name_plural = 'Níveis'

    def __str__(self):
        return self.nome

class Exercicio(models.Model):
    nome = models.CharField(verbose_name='Exercício', max_length=128)
    descricao = models.TextField(null=True, blank=True, verbose_name='Descrição do Exercício')
    recompensa = models.ForeignKey(Recompensa, related_name='Exercicio_fk_recompensa', on_delete=models.SET_NULL, null=True)
    data_de_cadastro = models.DateTimeField(auto_now=True, editable=False, blank=True)
    nivel = models.ForeignKey(Nivel, related_name='Exercicio_fk_Nivel', on_delete=models.SET_NULL, null=True, verbose_name='Nível')
    situacao = models.IntegerField(default=0, verbose_name='Situação do Exercício', choices=TIPO_DE_SITUACAO_EXERCICIO.choices(), null=True, blank=True)

    class Meta:
        verbose_name = 'Exercício'
        verbose_name_plural = 'Exercícios'

    def __str__(self):
        return self.nome

class Formula(models.Model):
    formula = models.CharField(verbose_name='Fórmula', max_length=255)
    tabela_verdade = models.TextField(null=True, blank=True, verbose_name='Tabela Verdade')
    data_de_cadastro = models.DateTimeField(auto_now=True, editable=False, blank=True)
    exercicio = models.ForeignKey(Exercicio, related_name='Formula_fk_exercicio', on_delete=models.SET_NULL, null=True, verbose_name='Exercício')
    quantidade_proposicoes = models.IntegerField(default=0, verbose_name='Quantidade de Proposições', null=True, blank=True)
    quantidade_linhas = models.IntegerField(default=0, verbose_name='Quantidade de Linhas', null=True, blank=True)

    class Meta:
        verbose_name = 'Fórmula'
        verbose_name_plural = 'Fórmulas'

    def __str__(self):
        return '{} - {}'.format(self.exercicio, self.formula)

class Pergunta_Formula(models.Model):
    formula = models.ForeignKey(Formula, related_name='Pergunta_Formula_fk_Formula', on_delete=models.SET_NULL, null=True, verbose_name='Fórmula')
    pergunta = models.CharField(verbose_name='Pergunta', max_length=255)
    data_de_cadastro = models.DateTimeField(auto_now=True, editable=False, blank=True)

    class Meta:
        verbose_name = 'Pergunta e Fórmula'
        verbose_name_plural = 'Perguntas e Fórmulas'

    def __str__(self):
        return self.pergunta

class Resposta(models.Model):
    nivel = models.ForeignKey(Nivel, related_name='Resposta_fk_Nivel', on_delete=models.SET_NULL, null=True, verbose_name='Nível')
    exercicio = models.ForeignKey(Exercicio, related_name='Resposta_fk_Exercicio', on_delete=models.SET_NULL, null=True, verbose_name='Exercício')
    academico = models.ForeignKey(Academico, related_name='Resposta_fk_Academico', on_delete=models.SET_NULL, null=True, verbose_name='Acadêmico')
    formula = models.ForeignKey(Formula, related_name='Resposta_fk_Formula', on_delete=models.SET_NULL, null=True, verbose_name='Fórmula')
    resposta_tabela = models.TextField(null=True, blank=True, verbose_name='Tabela Verdade')
    situacao = models.IntegerField(default=0, verbose_name='Situação da Resposta', choices=TIPO_DE_SITUACAO_RESPOSTA.choices(), null=True, blank=True)
    data_da_resposta = models.DateTimeField(auto_now=True, editable=False, blank=True)

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'

    def __str__(self):
        return '{:%d/%m/%Y} - {}'.format(localtime(self.data_da_resposta), self.academico)
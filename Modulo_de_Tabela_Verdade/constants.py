from .utils import ChoicesEnum

class TIPO_DE_SITUACAO_MODULO(ChoicesEnum):
    NAO_INICIADO = (1, 'Não Iniciado')
    INICIADO = (2, 'Iniciado')
    EM_ANDAMENTO= (3, 'Em Andamento')
    FINALIZADO = (4, 'Finalizado')

class TIPO_DE_SITUACAO_EXERCICIO(ChoicesEnum):
    NAO_INICIADO = (1, 'Não Iniciado')
    EM_ANDAMENTO= (2, 'Em Andamento')
    FINALIZADO = (4, 'Finalizado')

class TIPO_DE_SITUACAO_NIVEL(ChoicesEnum):
    NAO_INICIADO = (1, 'Não Iniciado')
    EM_ANDAMENTO= (2, 'Em Andamento')
    FINALIZADO = (4, 'Finalizado')

class TIPO_DE_SITUACAO_RESPOSTA(ChoicesEnum):
    CORRETA = (1, 'Correta')
    INCORRETA= (2, 'Incorreta')
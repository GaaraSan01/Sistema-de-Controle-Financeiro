from ..repository.transacao_repository import TransacaoRepository
from ..entity.trasacao_entity import Transacao

class AddTransacao:
    def __init__(self):
        self.transacao = TransacaoRepository()
        
    def handle(self, valor:int |float, data: str, tipo: str, descricao: str):
        obj_transacao = Transacao(valor, data, tipo, descricao)
        self.transacao.add(obj_transacao)
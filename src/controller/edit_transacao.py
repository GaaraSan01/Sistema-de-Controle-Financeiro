from ..entity.trasacao_entity import Transacao
from ..repository.transacao_repository import TransacaoRepository

class EditTransacao():
    def __init__(self):
        self.transacao_repository = TransacaoRepository()
        
    def handle(self, id: int):
        pass
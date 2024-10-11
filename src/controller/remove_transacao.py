from ..repository.transacao_repository import TransacaoRepository

class RemoveTransacao:
    
    def __init__(self):
        self.transacao_repository = TransacaoRepository()
        
    def handle(self, id: int):
        self.transacao_repository.delete(id)
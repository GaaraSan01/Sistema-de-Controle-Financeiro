from ..repository.transacao_repository import TransacaoRepository

class AllTransacao:
    
    def __init__(self):
        self.transacao = TransacaoRepository()
        
    def handle(self):
        return self.transacao.all()
        
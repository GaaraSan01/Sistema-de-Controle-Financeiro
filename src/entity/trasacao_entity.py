class Transacao:
    
    def __init__(
        self,
        valor: int|float,
        tipo: str,
        descricao: str
        ):
         self._valor = self.__set_valor(float(valor))
         self._tipo = self.__set_tipo(tipo)
         self._descricao = descricao
    
    def get_valor(self):
        return f"R${self._valor: .2f}"
         
    def __set_valor(self, valor: float|int):
        if(type(valor) != float):
            raise ValueError('Valor inválido!')
        
        return valor
    
    def get_tipo(self):
        return self._tipo
    
    def __set_tipo(self, tipo: str):
        tipos_aceitos = ('Receita', 'Despesa')
        
        if(not tipo in tipos_aceitos):
            raise ValueError("Erro ao adicionar tipo!")
        
        return tipo
    
    def get_descricao(self):
        return self._descricao
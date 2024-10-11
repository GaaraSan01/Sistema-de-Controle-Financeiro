from datetime import datetime

class Transacao:
    
    def __init__(
        self,
        valor: int|float,
        data: str,
        tipo: str,
        descricao: str
        ):
         self._valor = self.__set_valor(float(valor))
         self._data = self.__set_data(data)
         self._tipo = self.__set_tipo(tipo)
         self._descricao = descricao
         self._id
         
    def get_id(self):
        return self._id
    
    def set_id(self, id: int):
        self._id = id
    
    def get_valor(self):
        return f"R${self._valor: .2f}"
         
    def __set_valor(self, valor: float|int):
        if(type(valor) != float):
            raise ValueError('Valor inválido!')
        
        return valor
    
    def get_data(self):
        return self._data
    
    def __set_data(self, data: str):
        data_transform = datetime.strptime(data, '%d/%m/%Y')
        data_formatada = datetime.strftime(data_transform, '%d/%m/%Y')
        return data_formatada
    
    def get_tipo(self):
        return self._tipo
    
    def __set_tipo(self, tipo: str):
        tipos_aceitos = ('Receita', 'Despesa')
        
        if(not tipo in tipos_aceitos):
            raise ValueError("Erro ao adicionar tipo!")
        
        return tipo
    
    def get_descricao(self):
        return self._descricao
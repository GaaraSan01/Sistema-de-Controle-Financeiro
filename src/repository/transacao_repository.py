import sqlite3
import os
from ..entity.trasacao_entity import Transacao

class TransacaoRepository:
    
    def __init__(self):
        # Obtém o diretório do arquivo atual
        arquivo_atual = os.path.dirname(os.path.abspath(__file__))
        
        # Constrói o caminho completo para o banco de dados
        db_path = os.path.join(f"{arquivo_atual}","..","..","finance.db")
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()
        
    def add(self, transacao: Transacao):
        sql = "INSERT INTO transacoes(valor, tipo, descricao) VALUES (?, ?, ?)"
        self.cur.execute(sql, (
                transacao.get_valor(),
                transacao.get_tipo(),
                transacao.get_descricao()
            )
        )
        self.con.commit()
        
        return self.cur.lastrowid
    
    def all(self):
        sql = "SELECT * FROM transacoes"
        res = self.cur.execute(sql)
        return res.fetchall()
    
    def delete(self, id: int):
        sql = "DELETE FROM transacoes WHERE id = ?"
        res = self.cur.execute(sql, (id,))
        
        return res
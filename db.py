import sqlite3

con = sqlite3.connect("finance.db")
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS transacoes(
        id INTEGER PRIMARY KEY,
        valor TEXT,
        tipo Text,
        descricao TEXT
    );
''')

# res = cur.execute('''   
# INSERT INTO transacoes(valor, tipo, descricao) VALUES (?, ?, ?)
# ''', (100, 'Receita', 'Teste de banco de dados'))


res = cur.execute('''   
DELETE FROM transacoes WHERE id = ?
''', (2,))

con.commit()

res.execute("SELECT * FROM transacoes")

# res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchall())

con.close()
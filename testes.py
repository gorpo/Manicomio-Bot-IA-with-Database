"""a = 1
b = a
print(id(a),id(b))
"""

import sqlite3

conexao_sqlite = sqlite3.connect('bot_database.db')
conexao_sqlite.row_factory = sqlite3.Row
cursor_sqlite = conexao_sqlite.cursor()
cursor_sqlite.execute("""SELECT * FROM mensagens; """)
mensagens_sqlite = cursor_sqlite.fetchall()
for mensagem in mensagens_sqlite:
    #print(mensagem['tipo'])
    if mensagem['tipo'] == 'imagem':
        print(mensagem['mensagem'])
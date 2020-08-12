from datetime import timedelta, date
import pymysql.cursors

# faz a conexao com o banco de dados
conexao = pymysql.connect(host='localhost', user='root', password='', db='users_tcxs', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
cursor = conexao.cursor()
cursor.execute("select * from usuarios")
cadastro = cursor.fetchall()
hoje = date.today().strftime('%d-%m-%Y')

for dados in cadastro:
    validade = dados['data_cadastro']  + timedelta(days=31)
    usuario = dados['usuario']
    #print(usuario, hoje, validade.strftime('%d-%m-%Y %H:%M:%S'))
    if validade.strftime('%d-%m-%Y') == hoje:
        print(usuario, hoje, validade.strftime('%d-%m-%Y'))

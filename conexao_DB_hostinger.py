from datetime import timedelta, date
import pymysql.cursors

# faz a conexao com o banco de dados
conexao = pymysql.connect(host='92.249.44.1', user='u923273795_users', password='Tcxsproject2020web', db='u923273795_users', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
cursor = conexao.cursor()
cursor.execute("select * from usuarios")
cadastro = cursor.fetchall()
hoje = date.today().strftime('%d-%m-%Y')
#verifica a data local, no banco de dados e faz o calculo do aviso
for dados in cadastro:
    usuario = dados['usuario']
    data_validade = dados['data_cadastro']  + timedelta(days=31)
    aviso_vencimento = dados['data_cadastro'] + timedelta(days=39)
    data_final = dados['data_cadastro']
    if aviso_vencimento.strftime('%d-%m-%Y') == hoje:
        print('aviso dias:  ' + usuario, hoje, aviso_vencimento.strftime('%d-%m-%Y'),data_final.strftime('%d-%m-%Y'))


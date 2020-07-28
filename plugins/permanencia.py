# -*- coding: utf-8 -*-
#███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
#████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
#██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
#██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
#██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
#╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#     [+] @GorpoOrko 2020 - Telegram Bot and Personal Assistant [+]
#     |   TCXS Project Hacker Team - https://tcxsproject.com.br   |
#     |   Telegram: @GorpoOrko Mail:gorpoorko@protonmail.com      |
#     [+]        Github Gorpo Dev: https://github.com/gorpo     [+]



from config import bot
import sqlite3
from plugins.admins import is_admin
from datetime import datetime
from dateutil.relativedelta import relativedelta



async def permanencia(msg):
    try:
        id_usuario = msg['from']['id']
        adm = await is_admin(msg['chat']['id'], msg['from']['id'], id_usuario)
    except Exception as e:
        pass
    conexao_sqlite = sqlite3.connect('bot_database.db')
    conexao_sqlite.row_factory = sqlite3.Row
    cursor_sqlite = conexao_sqlite.cursor()
    try:
        if msg['chat']['type'] == 'supergroup':
            try:
                grupo = f"https://t.me/{msg['chat']['username']}"
            except:
                grupo = f"Secreto: {msg['chat']['title']}"
                pass
            try:
                admin = msg['from']['username']
            except:
                admin = f"@{msg['from']['id']}({msg['from']['first_name']})"
                pass
            try:
                chat_id = msg['chat']['id']
            except:
                pass
            data = datetime.now().strftime('%d/%m/%Y %H:%M')
            chat_type = msg['chat']['type']
            id_grupo = msg['chat']['id']
            id_admin = msg['from']['id']
            #ATIVAR OU DESATIVAR O SISTEMA DE BANIMENTO NO GRUPO------------------------------------------------------------>
            try:#ativar cadastramento automatico para banimento
                if msg['text'].split()[0] == 'ativar_banimento' and adm['user'] == True:
                    valor = 1
                    chat_id = msg['chat']['id']
                    cursor_sqlite.execute(f"""DELETE FROM banimento WHERE id_grupo='{msg['chat']['id']}' """)
                    cursor_sqlite.execute(f"""INSERT INTO banimento (int_id, grupo, tipo_grupo, id_grupo, admin, id_admin, data, valor)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{admin}','{id_admin}','{data}','{valor}')""")
                    conexao_sqlite.commit()
                    await bot.sendMessage(chat_id,f"@{msg['from']['username']} `Sistema de Cadastramento Automático para Banimento:`***ATIVO***\nAgora todos usuários que entrarem no grupo receberão uma data limite de permanencia, caso queira remover restriçao do usuário ou inserir mais dias de permanência consulte /help",'markdown')
            except Exception as e:
                pass
            try:#desativar cadastramento automatico para banimento
                if msg['text'].split()[0] == 'desativar_banimento' and adm['user'] == True:
                    valor = 0
                    cursor_sqlite.execute(f"""DELETE FROM banimento WHERE id_grupo='{msg['chat']['id']}' """)
                    cursor_sqlite.execute(f"""INSERT INTO banimento (int_id, grupo, tipo_grupo, id_grupo, admin, id_admin, data, valor)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{admin}','{id_admin}','{data}','{valor}')""")
                    conexao_sqlite.commit()
                    await bot.sendMessage(chat_id,f"@{msg['from']['username']} `Sistema de Cadastramento Automático para Banimento:`***DESATIVADO***\nAgora todos usuários que entrarem no grupo não receberão uma data limite de permanencia automática, porém estes dados ainda podem ser inseridos manualmente para restringir a permanência do usuário no grupo, para mais informações consulte os menus /help",'markdown')
            except Exception as e:
                pass

            #consulta a frequencia que o doador ainda pode ficar no grupo---------------------------->
            try:
                if  'consulta' in  msg['text'].split()[0]:
                    cursor_sqlite.execute("""SELECT * FROM permanencia; """)
                    resultados = cursor_sqlite.fetchall()
                    for resutado in resultados:
                        data_inicial = resutado['data_inicial']
                        data_ban = resutado['data_final']
                        id_doador = resutado['id_doador']
                        doador = resutado['doador']
                        dias = resutado['dias']
                        data_aviso = resutado['data_aviso']
                        if msg['text'].split()[1] == doador:
                            await bot.sendMessage(chat_id,f"🤖 {doador} ***Sua permanência do grupo.***\n`Usuário:` {doador}\n`Id_Usuário:` {id_doador}\n`Início:` {data_inicial}\n`Termino:` {data_ban}\n`Aviso Vencimento:` {data_aviso}\n`Permanência:` {dias}",'markdown')
            except Exception as e:
                pass

            #sistema cadastro de restriçao de doadores no grupo--------------------------------------------->
            try:
                if 'restringir' in msg['text'].split()[0]:
                    if adm['user'] == True:
                        try:
                            admin = msg['from']['username']
                            doador = f"{msg['text'].split()[1]}"
                            id_doador = msg['text'].split()[2]
                            dias = msg['text'].split()[3]
                            hoje = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                            data_inicial = hoje
                            dias_restantes = datetime.now() + relativedelta(days=int(dias))#--------------------------------
                            data_final = dias_restantes.strftime('%d/%m/%Y %H:%M:%S')
                            data_avisar = dias_restantes - relativedelta(days=int(7))#-------------------------------------
                            data_aviso = data_avisar.strftime('%d/%m/%Y %H:%M:%S')
                            #verifica se existe cadastro:
                            cursor_sqlite.execute("""SELECT * FROM permanencia; """)
                            resultados = cursor_sqlite.fetchall()
                            existe_cadastro = 0  # contador para verificar se o comando ja existe
                            for res in resultados:  # loop em todos resultados da Database
                                if res['id_doador'] == str(id_doador):
                                    existe_cadastro = 1  # troca o valor de existe_cadastro para 1
                            if existe_cadastro == 1:
                                await bot.sendMessage(chat_id, "🤖 `Usuário ja cadastrado, apague ele manualmente e insira os dados novamente`", 'markdown')
                            else:
                                cursor_sqlite.execute(f"""INSERT INTO permanencia(int_id,grupo,id_grupo, admin, doador, id_doador, dias, data_inicial, data_final,data_aviso)VALUES(null,'{msg['chat']['title']}','{msg['chat']['id']}','{admin}','{doador}','{id_doador}','{dias}','{data_inicial}','{data_final}','{data_aviso}')""")
                                conexao_sqlite.commit()
                                await bot.sendMessage(chat_id,f"🤖 ***Dados inseridos com exito no cadastro de permanência do grupo.***\n`Admin:` {admin}\n`Usuário:` {doador}\n`Id_Usuário:` {id_doador}\n`Início:` {data_inicial}\n`Termino:` {data_final}\n`Aviso Vencimento:` {data_aviso}\n`Permanência:` {dias}",'markdown')
                        except:
                            await bot.sendMessage(chat_id,f"🤖 `Ocorreu um erro ao inserir os dados na Database,este comando funciona somente para administradores, tente novamente e verifique se usou o comando da forma correta, qualquer espaço ou dados invalidos podem dar erro ao cadastrar, evitando assim dados invalidos na Database.Envie novamente o comando  exemplo:` ```restringir @doador id_doador dias``` ***Exemplo:*** restringir @xbadcoffee 1367451130 30 ",'markdown')
            except Exception as e:
                pass


            #SISTEMA PARA LIMPAR OS DOADORES CADASTRADOS NA DATABASE DE PERMANENCIA NO GRUPO DE DOADORES---------------------->
            try:
                if 'descadastrar' in msg['text'].split()[0]:
                    if adm['user'] == True:
                        try:
                            doador = msg['text'].split()[1]
                            cursor_sqlite.execute(f"""DELETE FROM permanencia WHERE doador='{doador}'""")
                            conexao_sqlite.commit()
                            await bot.sendMessage(chat_id, f'🤖 `Usuário {doador} apagado do sistema de permanência no grupo.`', 'markdown',reply_to_message_id=msg['message_id'])
                        except Exception as e:
                            await bot.sendMessage(chat_id,f"🤖 `Ocorreu um erro ao deletar os dados na Database,este comando funciona somente para administradores, tente novamente e verifique se usou o comando da forma correta, qualquer espaço ou dados invalidos podem dar erro ao cadastrar, evitando assim dados invalidos na Database.Envie novamente o comando  exemplo:` ```restringir @doador id_doador dias``` ***Exemplo:*** restringir @xbadcoffee 1367451130 30 ",'markdown')
                    #se o doador nao for um admin ele avisa:
                    if adm['user'] == False:
                        await bot.sendMessage(chat_id, f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
            except:
                pass
            ## SISTEMA DE BANIMENTO--------------------------------------------------------------->
            # sistema de verificaçao automatica para banimento no grupo
            try:
                conexao_sqlite = sqlite3.connect('bot_database.db')
                conexao_sqlite.row_factory = sqlite3.Row
                cursor_sqlite = conexao_sqlite.cursor()
                hoje = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                cursor_sqlite.execute("""SELECT * FROM permanencia; """)
                resultados = cursor_sqlite.fetchall()
                for resutado in resultados:
                    data_inicial = resutado['data_inicial']
                    data_ban = resutado['data_final']
                    id_doador = resutado['id_doador']
                    doador = resutado['doador']
                    dias = resutado['dias']
                    aviso = resutado['data_aviso']
                    id_grupo = resutado['id_grupo']
                    # ALERTA DE AVISO PARA O DOADOR----:
                    try:
                        if hoje[0:2] == aviso[0:2]:
                            await bot.sendMessage(id_grupo,f"🤖 {doador} ***Falta uma semana para você grupo, caso ainda tenha interesse em continuar usando a loja faça uma doação, envie o comprovante aqui no grupo que um de nossos administradores irá colocar mas dias em sua permanencia.***\n`Usuário:` {doador}\n`Id_Usuário:` {id_doador}\n`Início:` {data_inicial}\n`Termino:` {data_ban}\n`Permanência:` {dias}",'markdown')
                        # BANE O USUARIO CASO A DATA TENHA SIDO IGUAL A DO DIA HOJE
                        if hoje[3:5] == data_ban[3:5]:
                            await bot.kickChatMember(str(id_grupo), id_doador)
                            cursor_sqlite.execute(f"""DELETE FROM permanencia WHERE doador='{doador}'""")
                            conexao_sqlite.commit()
                            await bot.sendMessage(str(id_grupo),f"🤖 ***Removido do grupo pois deu a sua permanência do grupo.***\n`Usuário:` {doador}\n`Id_Usuário:` {id_doador}\n`Início:` {data_inicial}\n`Termino:` {data_ban}\n`Permanência:` {dias}",'markdown')
                            await bot.unbanChatMember(str(id_grupo), id_doador)
                    except:
                        pass
            except Exception as e:
                print(e)


    except Exception as e:
        pass




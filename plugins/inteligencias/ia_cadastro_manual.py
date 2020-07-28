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



import sqlite3
from config import bot
from datetime import datetime
from plugins.admins import is_admin



async def ia_cadastro_manual(msg):
    try:
        conexao_sqlite = sqlite3.connect('bot_database.db')
        conexao_sqlite.row_factory = sqlite3.Row
        cursor_sqlite = conexao_sqlite.cursor()
        chat_id = msg['chat']['id']
        data = datetime.now().strftime('%d/%m/%Y %H:%M')
        if msg['chat']['type'] == 'supergroup':
            try:
                grupo = f"https://t.me/{msg['chat']['username']}"
            except:
                grupo = f"Secreto: {msg['chat']['title']}"
                pass
            try:
                usuario = msg['from']['username']
            except:
                usuario = f"@{msg['from']['id']}({msg['from']['first_name']})"
                pass
            try:
                adm = await is_admin(msg['chat']['id'], msg['from']['id'],msg['from']['id'])
            except:
                pass
            if msg.get('text'):
                texto = msg['text']
                try:
                    cursor_sqlite.execute("""SELECT * FROM comandos; """)
                    resultados = cursor_sqlite.fetchall()
                    for resultado in resultados:
                        comando = resultado['comando']
                        resposta = resultado['resposta']
                        tipo = resultado['tipo']
                        if tipo == 'texto' and comando == texto.lower():
                            await bot.sendMessage(chat_id, f"{resposta}", reply_to_message_id=msg['message_id'])
                        if tipo == 'imagem' and comando == texto.lower():
                            await bot.sendPhoto(chat_id, photo=resposta, reply_to_message_id=msg['message_id'])
                        if tipo == 'voz' and comando == texto.lower():
                            await bot.sendVoice(chat_id, voice=resposta, reply_to_message_id=msg['message_id'])
                        if tipo == 'audio' and comando == texto.lower():
                            await bot.sendAudio(chat_id, audio=resposta, reply_to_message_id=msg['message_id'])
                        if tipo == 'documento' and comando == texto.lower():
                            await bot.sendDocument(chat_id, document=resposta, reply_to_message_id=msg['message_id'])
                        if tipo == 'video' and comando == texto.lower():
                            await bot.sendVideo(chat_id, video=resposta, reply_to_message_id=msg['message_id'])
                except Exception as e:
                    print(f'Erro no sistema de respostas CDRUD: {e}')
                    pass


                #SISTEMA DE CADASTRO MANUAL FEITO PELOS ADMS OU USUARIOS CASO DEFINIDO, UTILIZANDO O #
                #SISTEMA CADASTRA, RECADASTRA E DELETA CADASTROS USANDO OS COMANDOS # | $ | %
                try:  # SISTEMA DE CADASTRO DE COMANDOS DOS USUARIOS USANDO SOMENTE O # ------------------>
                    if texto.startswith('#') and not msg.get('reply_to_message'):
                        if adm['user'] == True:
                            texto_cadastro = texto[1:].split(' ')
                            comando = str(texto_cadastro[0]).lower()  # gera o texto do comando
                            separador = ' '
                            resposta = separador.join(map(str, texto_cadastro[1:]))
                            cursor_sqlite.execute("""SELECT * FROM comandos; """)
                            resultados = cursor_sqlite.fetchall()
                            existe_cadastro = 0  # contador para verificar se o comando ja existe
                            for res in resultados:  # loop em todos resultados da Database
                                if res['comando'] == comando:
                                    existe_cadastro = 1  # troca o valor de existe_cadastro para 1
                            if existe_cadastro == 1:  # se o valor existe_cadastro esta como 1 ele avisa que ja existe cadastro
                                await bot.sendMessage(chat_id, "Comando já cadastrado, tente outro", reply_to_message_id=msg['message_id'])
                            else:
                                cursor_sqlite.execute(f"""INSERT INTO comandos (tipo,comando,resposta,usuario,grupo,data) VALUES ('texto','{comando}','{resposta}','{usuario}','{grupo}','{data}')""")
                                conexao_sqlite.commit()
                                await bot.sendMessage(chat_id,f"🤖 Dados inseridos com exito.\nComando: {comando}\nResposta: {resposta}",reply_to_message_id=msg['message_id'])
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    pass

                try:  # RECADASTRAMENTO DE RESPOSTAS USANDO O $--------------------------------------------------------------------------------------------------->
                    if texto.startswith('$'):
                        if adm['user'] == True:
                            texto_cadastro = texto[1:].split(' ')
                            comando = str(texto_cadastro[0]).lower()  # gera o texto do comando
                            separador = ' '
                            resposta = separador.join(map(str, texto_cadastro[1:]))  # pega todo resto da lista e poe no separador retornando toda lista em uma linha
                            cursor_sqlite.execute(f"""DELETE FROM comandos WHERE comando='{comando}'""")
                            conexao_sqlite.commit()
                            await bot.sendMessage(chat_id, f'Comando: {comando} apagado do sistema.',reply_to_message_id=msg['message_id'])
                            cursor_sqlite.execute(f"""INSERT INTO comandos(tipo,comando,resposta,usuario,grupo,data)VALUES('texto','{comando}','{resposta}','{usuario}','{grupo}','{data}')""")
                            conexao_sqlite.commit()
                            await bot.sendMessage(chat_id, f"🤖 Dados inseridos com exito.`Comando:` {comando}`Resposta:` {resposta}", 'markdown',reply_to_message_id=msg['message_id'])
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except Exception as e:
                    print(f'Erro ao deletar comando cadastrado: {e}')
                    pass

                try:  # DELETAR COMANDOS CADASTRADOS USANDO O %------------>
                    if texto.startswith('%'):
                        if adm['user'] == True:
                            comando = texto[1:].lower()  # tira do texto o  comando 'cadastrar'
                            cursor_sqlite.execute(f"""DELETE FROM comandos WHERE comando='{comando}'""")
                            conexao_sqlite.commit()
                            await bot.sendMessage(chat_id, f'🤖 `Comando {comando} apagado do sistema.`', 'markdown',reply_to_message_id=msg['message_id'])
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    await bot.sendMessage(chat_id, f'🤖 `Comando {comando} inexistente ou ocorreu um erro.`', 'markdown',reply_to_message_id=msg['message_id'])

                try:  # LISTAR COMANDOS CADASTRADOS PELOS USUARIOS NA DATABASE------------>
                    if texto.lower() == 'comandos' or texto == '/comandos':
                        cursor_sqlite.execute("""SELECT * FROM comandos; """)
                        resultados = cursor_sqlite.fetchall()
                        todos_comandos = []
                        separador = ' \n'
                        for result in resultados:
                            todos_comandos.append(result['comando'])
                        await bot.sendMessage(chat_id,f'`Comandos cadastrados:`\n ***{separador.join(map(str, todos_comandos))}***','markdown', reply_to_message_id=msg['message_id'])
                except Exception as e:
                    print(f'Erro ao listar comandos: {e}')
                    pass



                ##SISTEMA DE CADASTRO USANDO REPLY------------------------------------------------>
                try:  # IMAGENS na Database-------------------------------------------------------------->
                    if 'photo' in msg.get('reply_to_message') and texto.startswith('#'):
                        if adm['user'] == True:
                            comando = texto[1:]
                            id_foto = msg.get('reply_to_message')['photo'][0]['file_id']
                            cursor_sqlite.execute("""SELECT * FROM comandos; """)
                            resultados = cursor_sqlite.fetchall()
                            existe_cadastro_imagem = 0  # contador para verificar se o comando ja existe
                            for res in resultados:  # loop em todos resultados da Database
                                if res['comando'] == comando and 'photo' in msg.get('reply_to_message'):
                                    existe_cadastro_imagem = 1  # troca o valor de existe_cadastro para 1
                            if existe_cadastro_imagem == 1:
                                await bot.sendMessage(chat_id, "🤖 `Comando já cadastrado, tente outro`", 'markdown')
                            else:
                                cursor_sqlite.execute(f"""INSERT INTO comandos (tipo,comando,resposta,usuario,grupo,data) VALUES ('imagem','{comando}','{id_foto}','{usuario}','{grupo}','{data}')""")
                                conexao_sqlite.commit()
                                await bot.sendMessage(chat_id,f"🤖 Dados inseridos com exito.\n`Comando:` {comando}\n`File_id:` {id_foto}",'markdown')
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    pass

                try:  # VIDEOS na Database----------------------------------------------------------------->
                    if 'video' in msg.get('reply_to_message') and texto.startswith('#'):
                        if adm['user'] == True:
                            comando = texto[1:]
                            id_video = msg.get('reply_to_message')['video']['file_id']
                            cursor_sqlite.execute("""SELECT * FROM comandos; """)
                            resultados = cursor_sqlite.fetchall()
                            existe_cadastro_video = 0  # contador para verificar se o comando ja existe
                            for res in resultados:  # loop em todos resultados da Database
                                if res['comando'] == comando:
                                    existe_cadastro_video = 1  # troca o valor de existe_cadastro para 1
                            if existe_cadastro_video == 1:  # se o valor existe_cadastro esta como 1 ele avisa que ja existe cadastro
                                await bot.sendMessage(chat_id, "🤖 `Comando já cadastrado, tente outro`", 'markdown')
                            else:
                                cursor_sqlite.execute(f"""INSERT INTO comandos (tipo,comando,resposta,usuario,grupo,data) VALUES ('video','{comando}','{id_video}','{usuario}','{grupo}','{data}')""")
                                conexao_sqlite.commit()
                                await bot.sendMessage(chat_id,f"🤖 Dados inseridos com exito.\n`Comando:` {comando}\n`File_id:` {id_video}",'markdown')
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    pass

                try:  # DOCUMENTOS na Database------------------------------------------------------------->
                    if 'document' in msg.get('reply_to_message') and texto.startswith('#'):
                        if adm['user'] == True:
                            comando = texto[1:]
                            id_documento = msg.get('reply_to_message')['document']['file_id']
                            cursor_sqlite.execute("""SELECT * FROM comandos; """)
                            resultados = cursor_sqlite.fetchall()
                            existe_cadastro_document = 0  # contador para verificar se o comando ja existe
                            for res in resultados:  # loop em todos resultados da Database
                                if res['comando'] == comando:
                                    existe_cadastro_document = 1  # troca o valor de existe_cadastro para 1
                            if existe_cadastro_document == 1:  # se o valor existe_cadastro esta como 1 ele avisa que ja existe cadastro
                                await bot.sendMessage(chat_id, "🤖 `Comando já cadastrado, tente outro`", 'markdown')
                            else:
                                cursor_sqlite.execute(f"""INSERT INTO comandos (tipo,comando,resposta,usuario,grupo,data) VALUES ('documento','{comando}','{id_documento}','{usuario}','{grupo}','{data}')""")
                                conexao_sqlite.commit()
                                await bot.sendMessage(chat_id,f"🤖 Dados inseridos com exito.\n`Comando:` {comando}\n`File_id:` {id_documento}",'markdown')
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    pass

                try:  # AUDIOS VOZ na Database------------------------------------------------------------>
                    if 'voice' in msg.get('reply_to_message') and texto.startswith('#'):
                        if adm['user'] == True:
                            comando = texto[1:]
                            id_voz = msg.get('reply_to_message')['voice']['file_id']
                            cursor_sqlite.execute("""SELECT * FROM comandos; """)
                            resultados = cursor_sqlite.fetchall()
                            existe_cadastro_voz = 0  # contador para verificar se o comando ja existe
                            for res in resultados:  # loop em todos resultados da Database
                                # se o comando ja existir o valor existe_cadastro passa ser 1
                                if res['comando'] == comando:
                                    existe_cadastro_voz = 1  # troca o valor de existe_cadastro para 1
                            if existe_cadastro_voz == 1:  # se o valor existe_cadastro esta como 1 ele avisa que ja existe cadastro
                                await bot.sendMessage(chat_id, "🤖 `Comando já cadastrado, tente outro`", 'markdown')
                            else:
                                cursor_sqlite.execute(f"""INSERT INTO comandos (tipo,comando,resposta,usuario,grupo,data) VALUES ('voz','{comando}','{id_voz}','{usuario}','{grupo}','{data}')""")
                                conexao_sqlite.commit()
                                await bot.sendMessage(chat_id,f"🤖 Dados inseridos com exito.\n`Comando:` {comando}\n`File_id:` {id_voz}",'markdown')
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    pass

                try:  # AUDIOS MUSICA na Database--------------------------------------------------------->
                    if 'audio' in msg.get('reply_to_message') and texto.startswith('#'):
                        if adm['user'] == True:
                            comando = texto[1:]
                            id_audio = msg.get('reply_to_message')['audio']['file_id']
                            cursor_sqlite.execute("""SELECT * FROM comandos """)
                            resultados = cursor_sqlite.fetchall()
                            existe_cadastro_audio = 0  # contador para verificar se o comando ja existe
                            for res in resultados:  # loop em todos resultados da Database
                                if res['comando'] == comando:
                                    existe_cadastro_audio = 1  # troca o valor de existe_cadastro para 1
                            if existe_cadastro_audio == 1:  # se o valor existe_cadastro esta como 1 ele avisa que ja existe cadastro
                                await bot.sendMessage(chat_id, "🤖 `Comando já cadastrado, tente outro`", 'markdown')
                            else:
                                cursor_sqlite.execute(f"""INSERT INTO comandos (tipo,comando,resposta,usuario,grupo,data) VALUES ('audio','{comando}','{id_audio}','{usuario}','{grupo}','{data}')""")
                                conexao_sqlite.commit()
                                await bot.sendMessage(chat_id,f"🤖 Dados inseridos com exito.\n`Comando:` {comando}\n`File_id:` {id_audio}",'markdown')
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    pass

                try:  # MENSAGENS de texto na Database---------------------------------------------------------------->
                    if 'text' in msg.get('reply_to_message') and texto.startswith('#'):
                        if adm['user'] == True:
                            comando = texto[1:]
                            id_text = msg.get('reply_to_message')['text']
                            cursor_sqlite.execute("""SELECT * FROM comandos; """)
                            resultados = cursor_sqlite.fetchall()
                            existe_cadastro_text = 0  # contador para verificar se o comando ja existe
                            for res in resultados:  # loop em todos resultados da Database
                                if res['comando'] == comando:
                                    existe_cadastro_text = 1  # troca o valor de existe_cadastro para 1
                            if existe_cadastro_text == 1:  # se o valor existe_cadastro esta como 1 ele avisa que ja existe cadastro
                                await bot.sendMessage(chat_id, "🤖 `Comando já cadastrado, tente outro`", 'markdown')
                            elif existe_cadastro_text == 0:  # se o valor de existe_cadastro nao foi alterado ele cadastra novo comando
                                cursor_sqlite.execute(f"""INSERT INTO comandos(tipo,comando,resposta,usuario,grupo,data)VALUES('texto','{comando}','{id_text}','{usuario}','{grupo}','{data}')""")
                                conexao_sqlite.commit()
                                await bot.sendMessage(chat_id,f"`🤖 Dados inseridos com exito.\nComando:` {comando}\n`File_id:` {id_text}",'markdown')
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    pass
#excessao final para tratar do codigo todo--->
    except:
        pass
        return True

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



import time
import speech_recognition as sr
from pydub import AudioSegment
import os
import sqlite3
from config import bot,bot_username,logs
from datetime import datetime
from plugins.admins import is_admin
from plugins.inteligencias.ia_global import ia_global
from plugins.inteligencias.ia_local import ia_local



async def inteligencia(msg):
    try:#verifica se o usuario é um admin de grupo ou canal
        id_usuario = msg['from']['id']
        adm = await is_admin(msg['chat']['id'], msg['from']['id'], id_usuario)
    except Exception as e:
        pass
    try:
        if msg['chat']['type'] == 'supergroup':
            try:
                grupo = f"https://t.me/{msg['chat']['username']}"
            except:
                grupo = f"Secreto: {msg['chat']['title']}"
                pass
            try:
                usuario = f"@{msg['from']['username']}"
            except:
                usuario = f"@{msg['from']['id']}({msg['from']['first_name']})"
                pass
        # database geral---->
        conexao_sqlite = sqlite3.connect('bot_database.db')
        conexao_sqlite.row_factory = sqlite3.Row
        cursor_sqlite = conexao_sqlite.cursor()
        # database logs ---->
        conexao_logs = sqlite3.connect('bot_database_logs.db')
        conexao_logs.row_factory = sqlite3.Row
        cursor_logs = conexao_logs.cursor()
        data = datetime.now().strftime('%d/%m/%Y %H:%M')
        chat_type = msg['chat']['type']
        id_grupo = msg['chat']['id']
        chat_id = msg['chat']['id']
        #inicio da inteligencia artificial---------------------------------------->
        if chat_type == 'supergroup':  # se o chat for supergrupo ele manda mensagem
            if msg.get('text'):
                #inicia o banco de dados geral para captar o tipo de inteligencia------->
                cursor_sqlite.execute("""SELECT * FROM inteligencia; """)
                inteligencias = cursor_sqlite.fetchall()
                for inteligencia in inteligencias:  # loop em todos resultados da Database
                    idgrupo = str(msg['chat']['id'])
                    if inteligencia['inteligencia'] == 'global':
                        pass
                        if inteligencia['id_grupo'] == idgrupo:
                            #print(f'Inteligencia Global setada no grupo {grupo}')
                            inteligencia_global = await ia_global(msg)
                    if inteligencia['inteligencia'] == 'local':
                        pass
                        if inteligencia['id_grupo'] == idgrupo:
                            #print(f'Inteligencia Local setada no grupo {grupo}')
                            inteligencia_local = await ia_local(msg)


                # ATIVA A INTELIGENCIA BASEADO NA IA GLOBAL/LOCAL
                #COMANDO PARA MUDAR ENTRE A INTELIGENCIA GLOBAL/LOCAL--------------------->>
                #sistema de mudança da ia entre global ou local | comando inteligencia ou ia
                if msg.get('text').split()[0] == 'inteligencia':
                    if adm['user'] == True:
                        if len(msg['text'].split()) > 1 and msg['text'].split()[1] == 'global' or len(msg['text'].split()) > 1 and msg['text'].split()[1] == 'local':
                            inteligencia = msg['text'].split()[1]
                            try:
                                tipo = msg['text'].split()[2]
                            except:
                                tipo = 'IA'
                                pass
                            try:
                                linguagem = msg['from']['language_code']
                            except:
                                linguagem = 'none'
                                pass
                            try:
                                cursor_sqlite.execute(f"""DELETE FROM inteligencia WHERE id_grupo='{msg['chat']['id']}' """)
                                cursor_sqlite.execute(f"""INSERT INTO inteligencia (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,inteligencia)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','{tipo}','{data}','{inteligencia}')""")
                                conexao_sqlite.commit()
                                await bot.sendMessage(chat_id,f"@{msg['from']['username']} `Inteligencia Artificial:`***{inteligencia}***\nAgora vocês irão receber coisas que aprendi nesta categoria.",'markdown')
                            except Exception as e:
                                print(f'banco de dados inteligencia erro: {e}')

                if msg.get('text') == 'inteligencia':
                    await bot.sendMessage(chat_id,f"`Inteligencia Artificial:`***Tenho um sistema de IA que aprendo tudo em todos os lugares que estou, para selecionar oque devo falar use os comandos como exemplo:***\n`comando:`inteligencia global\n```---- Com o comando inteligencia global irei falar oque aprendi em todos os lugares que estive.```\n`comando:`inteligencia local\n```Com o comando inteligencia local irei falar oque aprendi aqui.```\n***Para selecionar a frequência de minha interação no grupo use o comando frêquencia***", 'markdown')
                if msg.get('text').split()[0] == 'inteligencia' and adm['user'] == False:
                    await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')

                #sistema que o bot le todas mensagens aprendidas para os usuarios
                if msg.get('text').split()[0] == 'mensagens':
                    if adm['user'] == True:
                        cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                        mensagens = cursor_sqlite.fetchall()
                        a = await bot.sendMessage(chat_id,f"🤖 {msg['from']['first_name']} tenho {str(len(mensagens))} mensagens, vou exibir elas em ordem...",reply_to_message_id=msg['message_id'])
                        time.sleep(2)
                        for mensagem in mensagens:
                            try:
                                mensagem = mensagem['mensagem']
                                await bot.editMessageText((msg['chat']['id'], a['message_id']), f"```{mensagem}```","markdown")
                                time.sleep(1)
                            except:
                                pass

        #CADASTRO AUTOMATICO INTELIGENCIA DATABASE
        #CADASTRA AUTOMATICAMENTE TUDO QUE POSTAREM NA DATABASE, MANTENDO ASSIM CONHECIMENTO PARA IA
        # sistema de cadastro automatico dos posts dos grupos na Database------------------------------------------------------------
        if chat_type == 'supergroup' or chat_type == 'private' or chat_type == 'channel':
            try:
                try:
                    linguagem = msg['from']['language_code']
                except:
                    linguagem = 'none'
                    pass
                if msg.get('sticker'):
                    id_sticker = msg['sticker']['file_id']
                    id_mensagem = msg['sticker']['thumb']['file_unique_id']
                    await bot.sendSticker(msg['from']['id'], sticker=id_sticker)
                    #banco de dados geral mensagens------->>
                    cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                    mensagens = cursor_sqlite.fetchall()
                    #banco de dados logs mensagens ------->>
                    cursor_logs.execute("""SELECT * FROM mensagens; """)
                    cursor_logs.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','sticker','{data}','{id_mensagem}','{id_sticker}')""")
                    conexao_logs.commit()
                    existe_cadastro = 0  # contador para verificar se o comando ja existe
                    for mensagem in mensagens:  # loop em todos resultados da Database
                        if mensagem['id_mensagem'] == id_mensagem:
                            existe_cadastro = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro == 1:
                        pass
                    else:
                        cursor_sqlite.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','sticker','{data}','{id_mensagem}','{id_sticker}')""")
                        conexao_sqlite.commit()

                if msg.get('photo'):
                    id_foto = msg['photo'][0]['file_id']
                    id_mensagem = msg['photo'][0]['file_unique_id']
                    # banco de dados geral mensagens------->>
                    cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                    mensagens = cursor_sqlite.fetchall()
                    # banco de dados logs mensagens ------->>
                    cursor_logs.execute("""SELECT * FROM mensagens; """)
                    cursor_logs.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','imagem','{data}','{id_mensagem}','{id_foto}')""")
                    conexao_logs.commit()
                    existe_cadastro = 0  # contador para verificar se o comando ja existe
                    for mensagem in mensagens:  # loop em todos resultados da Database
                        if mensagem['id_mensagem'] == id_mensagem:
                            existe_cadastro = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro == 1:
                        pass
                    else:
                        cursor_sqlite.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','imagem','{data}','{id_mensagem}','{id_foto}')""")
                        conexao_sqlite.commit()
                    try:
                        await bot.sendPhoto(logs, id_foto)  #canal para marcinho = -1001402280935
                    except:
                        pass
                    try:
                        await bot.sendPhoto(msg['from']['id'], photo=id_foto, caption='Você mandou esta foto no grupo.')
                    except:
                        pass

                if msg.get('document'):#grava os dados pelo nome pois a unique id nao fica mesma se mesmo arquivo
                    id_documento = msg['document']['file_id']
                    try:
                        id_mensagem = msg['document']['file_name']
                    except:
                        id_mensagem = msg['document']['file_unique_id']
                        pass
                    # banco de dados geral mensagens------->>
                    cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                    mensagens = cursor_sqlite.fetchall()
                    # banco de dados logs mensagens ------->>
                    cursor_logs.execute("""SELECT * FROM mensagens; """)
                    cursor_logs.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','documento','{data}','{id_mensagem}','{id_documento}')""")
                    conexao_logs.commit()
                    existe_cadastro = 0  # contador para verificar se o comando ja existe
                    for mensagem in mensagens:  # loop em todos resultados da Database
                        if mensagem['id_mensagem'] == id_mensagem:
                            existe_cadastro = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro == 1:
                        pass
                    else:
                        await  bot.sendDocument(msg['from']['id'], id_documento)
                        cursor_sqlite.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','documento','{data}','{id_mensagem}','{id_documento}')""")
                        conexao_sqlite.commit()
                    try:
                        captado = msg['caption']
                    except:
                        captado = f'Vem de PV q o Pai ta ON: @{bot_username} '
                    await bot.sendDocument(logs, id_documento, captado)  #para marcinho -1001166426209
                if msg.get('audio'):
                    id_audio = msg['audio']['file_id']
                    id_mensagem = msg['audio']['file_unique_id']
                    # banco de dados geral mensagens------->>
                    cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                    mensagens = cursor_sqlite.fetchall()
                    # banco de dados logs mensagens ------->>
                    cursor_logs.execute("""SELECT * FROM mensagens; """)
                    cursor_logs.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','audio','{data}','{id_mensagem}','{id_audio}')""")
                    conexao_logs.commit()
                    existe_cadastro = 0  # contador para verificar se o comando ja existe
                    for mensagem in mensagens:  # loop em todos resultados da Database
                        if mensagem['id_mensagem'] == id_mensagem:
                            existe_cadastro = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro == 1:
                        pass
                    else:
                        cursor_sqlite.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','audio','{data}','{id_mensagem}','{id_audio}')""")
                        conexao_sqlite.commit()

                if msg.get('video'):
                    id_video = msg['video']['file_id']
                    id_mensagem = msg['video']['file_unique_id']
                    # banco de dados geral mensagens------->>
                    cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                    mensagens = cursor_sqlite.fetchall()
                    # banco de dados logs mensagens ------->>
                    cursor_logs.execute("""SELECT * FROM mensagens; """)
                    cursor_logs.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','video','{data}','{id_mensagem}','{id_video}')""")
                    conexao_logs.commit()
                    existe_cadastro = 0  # contador para verificar se o comando ja existe
                    for mensagem in mensagens:  # loop em todos resultados da Database
                        if mensagem['id_mensagem'] == id_mensagem:
                            existe_cadastro = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro == 1:
                        pass
                    else:
                        cursor_sqlite.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','video','{data}','{id_mensagem}','{id_video}')""")
                        conexao_sqlite.commit()
                    try:
                        await bot.sendVideo(logs, id_video)  #marcinho -1001402280935
                    except:
                        pass
                    try:
                        await bot.sendVideo(msg['from']['id'], id_video, caption=f'@{usuario} Você mandou este video no {grupo}.')
                    except:
                        pass


                if msg.get('voice'):#MELHOR NAO APLICAR AQUI A REGRA SE JA EXISTE SENAO NAO VAI CADASTRAR
                    id_voz = msg['voice']['file_id']
                    #id_mensagem = msg['voice']['file_unique_id']
                    await bot.download_file(msg['voice']['file_id'], 'arquivos/audio_usuario_db.ogg')
                    sound = AudioSegment.from_file("arquivos/audio_usuario_db.ogg")
                    sound.export("arquivos/audio_usuario_db.wav", format="wav", bitrate="128k")
                    r = sr.Recognizer()
                    with sr.WavFile('arquivos/audio_usuario_db.wav') as source:
                        audio = r.record(source)
                    texto = r.recognize_google(audio, language='pt-BR')
                    await bot.sendMessage(chat_id, f"`{msg['from']['first_name']} disse:`\n```----  {texto}```", 'markdown', reply_to_message_id=msg['message_id'])
                    os.remove("arquivos/audio_usuario_db.ogg")
                    os.remove("arquivos/audio_usuario_db.wav")
                    # banco de dados geral mensagens------->>
                    cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                    mensagens = cursor_sqlite.fetchall()
                    # banco de dados logs mensagens ------->>
                    cursor_logs.execute("""SELECT * FROM mensagens; """)
                    cursor_logs.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','voz decodificada','{data}','{id_mensagem}','{texto}')""")
                    conexao_logs.commit()
                    existe_cadastro = 0  # contador para verificar se o comando ja existe
                    id_mensagem = texto
                    print(f"🤖 {msg['from']['first_name']} enviou um audio: {id_mensagem}")
                    for mensagem in mensagens:  # loop em todos resultados da Database
                        if mensagem['id_mensagem'] == id_mensagem:
                            existe_cadastro = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro == 1:
                        pass
                    else:
                        cursor_sqlite.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','voz decodificada','{data}','{id_mensagem}','{texto}')""")
                        conexao_sqlite.commit()

                if msg.get('text'):
                    texto = msg['text']#aqui tenho que comparar o texto com texto para nao gravar textos iguais
                    id_mensagem = texto
                    # banco de dados geral mensagens------->>
                    cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                    mensagens = cursor_sqlite.fetchall()
                    # banco de dados logs mensagens ------->>
                    cursor_logs.execute("""SELECT * FROM mensagens; """)
                    cursor_logs.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','texto','{data}','{id_mensagem}','{texto}')""")
                    conexao_logs.commit()
                    existe_cadastro = 0  # contador para verificar se o comando ja existe
                    for mensagem in mensagens:  # loop em todos resultados da Database
                        if mensagem['id_mensagem'] == id_mensagem:
                            existe_cadastro = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro == 1:
                        pass
                    else:
                        cursor_sqlite.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','texto','{data}','{id_mensagem}','{texto}')""")
                        conexao_sqlite.commit()
            except Exception as e:
                #print(f'Sistema de cadastro automatico IA, erro: {e}')
                pass


            # COMANDO PARA MUDAR A FREQUENCIA COM QUE A IA FALA | CADA GRUPO TEM SUA FREQUENCIA PRÓPRIA--------------------->>
            #seta a frequencia da IA | comando frequencia + 0  a 10 onde 0 muta o bot e 10 fala muito
            texto = msg['text']
            if texto.lower().startswith('frequencia') and  texto.split()[1].isdigit():
                try:
                    valor = texto[11:]
                    cursor_sqlite.execute("""SELECT * FROM frequencia; """)
                    frequencias = cursor_sqlite.fetchall()
                    comparar_vazio = []
                    freq = list(frequencias)
                    if freq == comparar_vazio:
                        cursor_sqlite.execute(f"""INSERT INTO frequencia(id_grupo, grupo, valor)VALUES('{id_grupo}','{grupo}','{valor}')""")
                        conexao_sqlite.commit()
                    else:
                        for frequencia in frequencias:  # loop em todos resultados da Database
                            if frequencia['id_grupo'] == msg['chat']['id']:
                                cursor_sqlite.execute(f"""DELETE FROM frequencia WHERE id_grupo='{msg['chat']['id']}'""")
                                conexao_sqlite.commit()
                                cursor_sqlite.execute(f"""INSERT INTO frequencia(id_grupo, grupo, valor)VALUES('{id_grupo}','{grupo}','{valor}')""")
                                conexao_sqlite.commit()
                            if frequencia['id_grupo'] != msg['chat']['id']:
                                cursor_sqlite.execute(f"""INSERT INTO frequencia(id_grupo, grupo, valor)VALUES('{id_grupo}','{grupo}','{valor}')""")
                                conexao_sqlite.commit()
                    if int(valor) == 0:
                        await bot.sendMessage(chat_id, f'🤖 `Frequencia alterada para {valor}, estou mutado so irei reponder comandos cadastrados`','markdown')
                    if int(valor) == 1:
                        await bot.sendMessage(chat_id, f'🤖 `Frequencia alterada para {valor}, vou tentar falar pouco`','markdown')
                    if int(valor) >= 2:
                        await bot.sendMessage(chat_id, f'🤖 `Frequencia alterada para {valor}, vou falar bastante`\nCaso queira que eu pare de falar defina a frequencia: 0\n Para eu falar menos defina frequencia: 1','markdown')
                except Exception as e:
                    pass
        conexao_sqlite.close()
        conexao_logs.close()
    except Exception as e:
        pass
















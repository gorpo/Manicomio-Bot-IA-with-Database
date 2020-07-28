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

import random
import sqlite3
from config import bot

async def ia_local(msg):
    try:
        conexao_sqlite = sqlite3.connect('bot_database.db')
        conexao_sqlite.row_factory = sqlite3.Row
        cursor_sqlite = conexao_sqlite.cursor()
        chat_id = msg['chat']['id']
        chat_type = msg['chat']['type']
        if chat_type == 'supergroup':
            if msg.get('text'):
                cursor_sqlite.execute("""SELECT * FROM frequencia; """)
                frequencia_sqlite = cursor_sqlite.fetchall()
                lista = list(frequencia_sqlite) #pega todas as linhas cadastradas em frequencia em uma lista  | ASSIM SE LE UMA LINHA DA DATABASE: # print(lista)
                for i, id_grupo in enumerate(lista): #faz um loop em todas linhas colocadas em uma lista | # print(i, id_grupo)
                    if id_grupo[0] == msg['chat']['id']:      #se a id da db for igual a id que é o chat ele passa o nome do chat e a frequencia para o bot mandar mensagens
                        frequencia_db = id_grupo[2] #tras a frequencia do grupo do banco de dados
                        contador = int(random.randint(0, frequencia_db * 2))  - 1  #sorteia um numero entre 0 e o valor da frequencia, multiplica a frequencia e tira um para gerar um bom sistema de resposta
                        if contador < frequencia_db:  # se o contador for menor que a frequencia o bot entrara na conversa
                            pass
                        else:
                            cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                            mensagens_sqlite = cursor_sqlite.fetchall()
                            quantidade_mensagens = len(mensagens_sqlite)
                            randomico = random.randint(0,  quantidade_mensagens - 1)  # fornece um numero randomico para pegarmos as mensagens na db
                            mensagem_bot = mensagens_sqlite[randomico][10]
                            tipo_mensagem = mensagens_sqlite[randomico][7]
                            id_grupo_mensagem = int(mensagens_sqlite[randomico][3])
                            mb = mensagem_bot.split()[0]
                            if mb.startswith('fale') or mb.startswith('luppy') or mb.startswith('frequencia') or mb.startswith('comando') or mb.startswith('proibidas') or mb.startswith('🤖') or mb.startswith('#') or mb.startswith('$') or mb.startswith('%') :
                                    print(f'🤖 [*ia_local][proibido] Bot tentou enviar <{tipo_mensagem}> no grupo {msg["chat"]["title"]} com a id {mensagem_bot}')
                            else:
                                if tipo_mensagem == 'imagem' and id_grupo_mensagem == msg['chat']['id']:
                                    await bot.sendPhoto(chat_id, photo=mensagem_bot)
                                    print(f'🤖 [*ia_local] Bot enviou uma imagem no grupo {msg["chat"]["title"]} com a id {mensagem_bot}')
                                if tipo_mensagem == 'documento' and id_grupo_mensagem == msg['chat']['id']:
                                    #await bot.sendDocument(chat_id, document=mensagem_bot)
                                    print(f'🤖 [*ia_local] Bot tentou enviar um documento no grupo {msg["chat"]["title"]} com a id {mensagem_bot}')
                                if tipo_mensagem == 'audio' and id_grupo_mensagem == msg['chat']['id']:
                                    #await bot.sendAudio(chat_id, audio=mensagem_bot)
                                    print(f'🤖 [*ia_local] Bot tentou enviar um audio no grupo {msg["chat"]["title"]} com a id {mensagem_bot}')
                                if tipo_mensagem == 'video' and id_grupo_mensagem == msg['chat']['id']:
                                    await bot.sendVideo(chat_id, video=mensagem_bot)
                                    print(f'🤖 [*ia_local] Bot enviou um video no grupo {msg["chat"]["title"]} com a id {mensagem_bot}')
                                if tipo_mensagem == 'texto' and id_grupo_mensagem == msg['chat']['id']:
                                    await bot.sendMessage(chat_id, mensagem_bot)
                                    print(f'🤖 [*ia_local] Bot enviou no grupo {msg["chat"]["title"]}: {mensagem_bot}')
                                if tipo_mensagem == 'sticker' and id_grupo_mensagem == msg['chat']['id']:
                                    await bot.sendSticker(chat_id, sticker=mensagem_bot)
                                    print(f'🤖 [*ia_local] Bot enviou sticker no grupo {msg["chat"]["title"]} com a id {mensagem_bot}')
# excessao final para tratar do codigo todo--->
    except:
        pass
        return True

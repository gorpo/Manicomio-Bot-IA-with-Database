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
from config import bot, administradores
from plugins.admins import is_admin
import time

async def ia_cadastro_perguntas(msg):
    try:
        conexao_sqlite = sqlite3.connect('bot_database.db')
        conexao_sqlite.row_factory = sqlite3.Row
        cursor_sqlite = conexao_sqlite.cursor()
        chat_id = msg['chat']['id']
        chat_type = msg['chat']['type']
        adm = await is_admin(msg['chat']['id'], msg['from']['id'], msg['from']['id'])
        if chat_type == 'supergroup':  # or chat_type == 'private'
            if msg.get('text'):
                texto = msg['text']

                try:  # CADASTRO PERGUNTAS DOS USUARIOS---------------------------------------------------------->
                    if '??' in texto:
                        usuario = f"@{msg['from']['username']}"
                        cursor_sqlite.execute(f"""INSERT INTO perguntas VALUES (null,'{usuario}','{texto}')""")
                        conexao_sqlite.commit()
                        await bot.sendMessage(chat_id, f"🤖 {msg['from']['first_name']} `sua pergunta foi cadastrada.`",'markdown')
                except Exception as e:
                    pass

                try:  # VERIFICAR PERGUNTAS DOS USUARIOS----------------------------------------------------------->
                    if texto.lower() == 'perguntas':
                        cursor_sqlite.execute("""SELECT * FROM perguntas""")
                        resultados = cursor_sqlite.fetchall()
                        if resultados == []:
                            await bot.sendMessage(chat_id,f"🤖 {msg['from']['first_name']} `não tenho perguntas cadastradas, tente outra hora ou cadastre algumas perguntas.`",'markdown')
                        else:
                            a = await bot.sendMessage(chat_id, f"`Estas são as perguntas que tenho cadastradas:`", 'markdown')
                            time.sleep(2)
                            for resultado in resultados:
                                usuario = resultado['usuario']
                                pergunta = resultado['pergunta']
                                await bot.editMessageText((msg['chat']['id'], a['message_id']),f"`Usuário:`{usuario}\n`Pergunta:` ***{pergunta}***", 'markdown')
                                time.sleep(1)
                            await bot.editMessageText((msg['chat']['id'], a['message_id']),f"`Total de {len(resultados)} perguntas cadastradas`", 'markdown')
                except Exception as e:
                    pass

                try:  # LIMPAR PERGUNTAS DOS USUARIOS------------------------------------------------------------->
                    if texto.lower() == 'apagar perguntas' and msg['from']['id'] in administradores:#admin manual setado no confis.py
                        if adm['user'] == True:
                            cursor_sqlite.execute("""DELETE FROM perguntas""")
                            conexao_sqlite.commit()
                            await bot.sendMessage(chat_id, f"🤖 {msg['from']['first_name']}\n ***Todas perguntas foram apagadas!***",'markdown')
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    pass
#excessao final para tratar do codigo todo--->
    except:
        pass
        return True

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



import subprocess
import os
import sqlite3
from config import bot, sudoers, logs, bot_username,keys
from datetime import datetime
from plugins.admins import is_admin


async def ia_deepnude(msg):
    try:
        # se a mensagem e no privado do bot-------------->
        if msg['chat']['type'] == 'private':
            grupo = f'Privado: @{bot_username}'
            try:
                usuario = msg['from']['username']
            except:
                usuario = f"@{msg['from']['id']}({msg['from']['first_name']})"
                pass
            try:
                texto = msg['text']
            except:
                pass

        # se for um supergrupo ou grupo secreto ele trata o nome do grupo e o usuario se ele tem ou nao um username
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
                texto = msg['text']
            except:
                pass
            try:
                linguagem = msg['from']['language_code']
            except:
                linguagem = 'none'
                pass
        data = datetime.now().strftime('%d/%m/%Y %H:%M')
        chat_type = msg['chat']['type']
        texto = msg['text']
        id_grupo = msg['chat']['id']
        chat_id = msg['chat']['id']
        id_usuario = msg['from']['id']
        if chat_type == 'supergroup' or chat_type == 'private':
                try:
                    if 'photo' in msg.get('reply_to_message') and texto.startswith('deepnude'):
                        id_foto = msg.get('reply_to_message')['photo'][0]['file_id']
                        await bot.download_file(id_foto,'arquivos/file.jpg')
                        await bot.sendMessage(chat_id,f"@{msg['from']['username']} `baixei sua imagem vou iniciar o processo Deep Nude, caso eu não retorne a imagem em até 5 minutos tente novamente.`",'markdown', reply_to_message_id=msg['message_id'])
                        subprocess.call('python plugins/deep_nude/deepnude.py')
                        await bot.sendPhoto(msg['chat']['id'],photo=open('arquivos/renderizada.jpg','rb'),caption='Aqui esta seu DeepNude.', reply_to_message_id=msg['message_id'])
                        #await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                        os.remove('arquivos/file.jpg')
                        os.remove('arquivos/renderizada.jpg')
                        print(f"🤖 [deepnude] Bot enviou o deepnude com sucesso para {msg['chat']['title']}.")
                except:
                    pass
#excessao final para tratar do codigo todo--->
    except:
        pass
        return True

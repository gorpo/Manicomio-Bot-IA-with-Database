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
from telegraph import Telegraph
import pyimgur


async def ia_deepnude(msg):
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
            data = datetime.now().strftime('%d/%m/%Y %H:%M')
            chat_type = msg['chat']['type']
            chat_id = msg['chat']['id']
            texto = msg['text']
            data = datetime.now().strftime('%d/%m/%Y %H:%M')
            chat_type = msg['chat']['type']
            texto = msg['text']
            id_grupo = msg['chat']['id']
            chat_id = msg['chat']['id']
            id_usuario = msg['from']['id']
            conexao_sqlite = sqlite3.connect('bot_database.db')
            conexao_sqlite.row_factory = sqlite3.Row
            cursor_sqlite = conexao_sqlite.cursor()
            token_imgur = keys['token_imgur']
            if chat_type == 'supergroup' or chat_type == 'private':
                    try:
                        if 'photo' in msg.get('reply_to_message') and texto.startswith('deepnude'):
                            id_foto = msg.get('reply_to_message')['photo'][0]['file_id']
                            await bot.download_file(id_foto,'arquivos/file.jpg')
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `baixei sua imagem vou iniciar o processo Deep Nude, caso eu não retorne a imagem em até 5 minutos tente novamente.`",'markdown', reply_to_message_id=msg['message_id'])
                            try:
                                subprocess.call('python plugins/deep_nude/deepnude.py')
                            except:
                                pass
                            im = pyimgur.Imgur(token_imgur)
                            imagem_original = im.upload_image('arquivos/file.jpg', title='Manicomio | Deep Nude | Original')
                            link_imagem_original = imagem_original.link
                            imagem_deepnude = im.upload_image('arquivos/renderizada.jpg', title='Manicomio | Deep Nude | Renderizada')
                            link_imagem_deepnude = imagem_deepnude.link
                            conteudo_html = f'<p>Deep Nude criado com Inteligência Artificial, Machine Learning e Deep Learning.</p><img src="{link_imagem_deepnude}"><img src="{link_imagem_original}"><br><br><br><br><a href="https://t.me/{bot_username}?start=start">Telegram: @{bot_username}</a>'
                            telegraph = Telegraph()
                            a = telegraph.create_account(short_name='manicomio')
                            response = telegraph.create_page('Manicomio | Deep Nude', html_content=conteudo_html)
                            link_final = 'https://telegra.ph/{}'.format(response['path'])
                            print(f"Deep Nude Telegra.ph: {link_final}")
                            await bot.sendMessage(chat_id,f"🤖 {msg['from']['first_name']}:\n{link_final}", reply_to_message_id=msg['message_id'])
                            #await bot.sendPhoto(msg['chat']['id'],photo=open('arquivos/renderizada.jpg','rb'),caption='Aqui esta seu DeepNude.', reply_to_message_id=msg['message_id'])

                            cursor_sqlite.execute(f"""INSERT INTO deepnude_sites (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, data, imagem_original ,imagem_deepnude ,link_telegraph )VALUES(null,'{grupo}','{chat_type}','{chat_id}','{usuario}','{msg['from']['id']}','{data}','{link_imagem_original}','{link_imagem_deepnude}','{link_final}')""")
                            conexao_sqlite.commit()
                            conexao_sqlite.close()
                            os.remove('arquivos/file.jpg')
                            os.remove('arquivos/renderizada.jpg')
                    except:
                        pass
#excessao final para tratar do codigo todo--->
    except:
        pass
        #return True

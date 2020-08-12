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
import os
import sqlite3
import pyimgur
from config import bot, bot_username,keys
from datetime import datetime
from telegraph import Telegraph


async def cria_site_telegraph(msg):
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
                usuario = f"@{msg['from']['username']}"
            except:
                usuario = f"@{msg['from']['id']}({msg['from']['first_name']})"
                pass
            data = datetime.now().strftime('%d/%m/%Y %H:%M')
            chat_type = msg['chat']['type']
            chat_id = msg['chat']['id']
            texto = msg['text']
            if texto == 'links':
                cursor_sqlite.execute("""SELECT * FROM telegraph_sites""")
                resultados = cursor_sqlite.fetchall()
                a = await bot.sendMessage(chat_id, f"🤖 {msg['from']['first_name']} tenho {str(len(resultados))} páginas criadas, vou exibir elas em ordem com uma pausa de 3 segundos...",reply_to_message_id=msg['message_id'])
                for resultado in resultados:
                    link = resultado['link']
                    await bot.editMessageText((msg['chat']['id'], a['message_id']),link)
                    time.sleep(3)

            if 'photo' in msg.get('reply_to_message') and 'web' in texto.split()[0]:
                print('aqui')
                titulo = texto.split()[1]
                separador = ' \n'
                conte = texto.split()[2:]
                conteudo = separador.join(map(str, conte))
                id_foto = msg.get('reply_to_message')['photo'][0]['file_id']
                await bot.download_file(id_foto, 'arquivos/criar_site.jpg')
                token_imgur = keys['token_imgur']
                im = pyimgur.Imgur(token_imgur)
                uploaded_image = im.upload_image('arquivos/criar_site.jpg', title=titulo)
                link_imagem = uploaded_image.link
                conteudo_html = f'<img src="{link_imagem}"><p>{conteudo}</p><br><br><br><br><a href="https://t.me/{bot_username}?start=start">Telegram: @{bot_username}</a>'
                telegraph = Telegraph()
                a = telegraph.create_account(short_name='manicomio')
                response = telegraph.create_page(titulo, html_content=conteudo_html)
                link_final = 'https://telegra.ph/{}'.format(response['path'])
                print(f"Usuário criou um site no telegra.ph: {link_final}")
                await bot.sendMessage(chat_id,f"🤖 {msg['from']['first_name']} acabei seu site:{link_final}", reply_to_message_id=msg['message_id'])
                os.remove('arquivos/criar_site.jpg')
                # tabela do armazenamento dos sites telegraph
                cursor_sqlite.execute(f"""INSERT INTO telegraph_sites (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, data,titulo,texto,imagem,link)VALUES(null,'{grupo}','{chat_type}','{chat_id}','{usuario}','{msg['from']['id']}','{data}','{titulo}','{conteudo}','{link_imagem}','{link_final}')""")
                conexao_sqlite.commit()
                conexao_sqlite.close()
    except Exception as e:
        pass
    try:
        if msg['text'].split()[0] ==  '/notepad':
                conteudo_html = msg['text'][8:]
                telegraph = Telegraph()
                a = telegraph.create_account(short_name='manicomio')
                response = telegraph.create_page('Manicomio', html_content=conteudo_html)
                link_final = 'https://telegra.ph/{}'.format(response['path'])
                print(f"Usuário criou um site no telegra.ph: {link_final}")
                await bot.sendMessage(msg['chat']['id'],f"🤖 {msg['from']['first_name']} acabei seu site:{link_final}", reply_to_message_id=msg['message_id'])
    except Exception as e:
        pass















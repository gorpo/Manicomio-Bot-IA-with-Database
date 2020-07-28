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



import os
import dropbox
import re
from config import bot,token_dropbox,administradores
from datetime import datetime

async def dropbox_upload(msg):
    if msg.get('text') and msg['chat']['type'] != 'channel':
        if msg['from']['id']  in administradores:
            chat_id = msg['chat']['id']
            texto = msg['text']
            try:
                if 'document' in msg.get('reply_to_message') and texto.lower().startswith('dropbox'):
                    id_arquivo = msg.get('reply_to_message')['document']['file_id']
                    nome_arquivo = msg.get('reply_to_message')['document']['file_name']
                    tamanho = msg.get('reply_to_message')['document']['file_size']
                    if tamanho > 10000000:
                        await bot.sendMessage(chat_id, '🤖 `Tamanho maximo para envio de 10mb`', 'markdown',reply_to_message_id=msg['message_id'])
                    if tamanho < 10000000:
                        await bot.download_file(id_arquivo, f'arquivos/{nome_arquivo}')
                        await bot.sendMessage(chat_id,f"🤖 `{msg['from']['first_name']} acabei de baixar seu arquivo, vou upar ele para o Dropbox`",'markdown', reply_to_message_id=msg['message_id'])
                        targetfile = f"/GDRIVE_TCXSPROJECT/MARCINHO_BOT/{nome_arquivo}"
                        d = dropbox.Dropbox(token_dropbox)
                        with open(f'arquivos/{nome_arquivo}', "rb") as f:
                            meta = d.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))
                        link = d.sharing_create_shared_link(targetfile)
                        url = link.url
                        dl_url = re.sub(r"\?dl\=0", "?dl=1", url)
                        await bot.sendMessage(chat_id,f"🤖 {msg['from']['first_name']} acabei upar seu arquivo no Dropbox:{dl_url}", reply_to_message_id=msg['message_id'])
                        os.remove(f'arquivos/{nome_arquivo}')
            except:
                pass


            try:
                if 'video' in msg.get('reply_to_message') and texto.lower().startswith('dropbox'):
                    id_arquivo = msg.get('reply_to_message')['video']['file_id']
                    data = datetime.now().strftime('%d_%m_%Y-%H_%M')
                    nome_arquivo = f'video_{data}.mp4'
                    tamanho = msg.get('reply_to_message')['video']['file_size']
                    if tamanho > 10000000:
                        await bot.sendMessage(chat_id, '🤖 `Tamanho maximo para envio de 10mb`', 'markdown',
                                        reply_to_message_id=msg['message_id'])
                    if tamanho < 10000000:
                        await bot.download_file(id_arquivo, f'arquivos/{nome_arquivo}')
                        await bot.sendMessage(chat_id,f"🤖 `{msg['from']['first_name']} acabei de baixar seu arquivo, vou upar ele para o Dropbox`",'markdown', reply_to_message_id=msg['message_id'])
                        targetfile = f"/GDRIVE_TCXSPROJECT/MARCINHO_BOT/{nome_arquivo}"
                        d = dropbox.Dropbox(token_dropbox)
                        with open(f'arquivos/{nome_arquivo}', "rb") as f:
                            meta = d.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))
                        link = d.sharing_create_shared_link(targetfile)
                        url = link.url
                        dl_url = re.sub(r"\?dl\=0", "?dl=1", url)
                        await bot.sendMessage(chat_id,f"🤖 {msg['from']['first_name']} acabei upar seu arquivo no Dropbox:{dl_url}", reply_to_message_id=msg['message_id'])
                        os.remove(f'arquivos/{nome_arquivo}')
            except:
                pass

            try:
                if 'photo' in msg.get('reply_to_message') and texto.lower().startswith('dropbox'):
                    id_arquivo = msg.get('reply_to_message')['photo'][0]['file_id']
                    data = datetime.now().strftime('%d_%m_%Y-%H_%M')
                    nome_arquivo = f'imagem_{data}.jpg'
                    await bot.download_file(id_arquivo, f"arquivos/{nome_arquivo}")
                    await bot.sendMessage(chat_id,f"🤖 `{msg['from']['first_name']} acabei de baixar seu arquivo, vou upar ele para o Dropbox`",'markdown', reply_to_message_id=msg['message_id'])
                    targetfile = f"/GDRIVE_TCXSPROJECT/MARCINHO_BOT/{nome_arquivo}"
                    d = dropbox.Dropbox(token_dropbox)
                    with open(f'arquivos/{nome_arquivo}', "rb") as f:
                        meta = d.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))
                    link = d.sharing_create_shared_link(targetfile)
                    url = link.url
                    dl_url = re.sub(r"\?dl\=0", "?dl=1", url)
                    await bot.sendMessage(chat_id,f"🤖 {msg['from']['first_name']} acabei upar seu arquivo no Dropbox:{dl_url}",reply_to_message_id=msg['message_id'])
                    os.remove(f'arquivos/{nome_arquivo}')
            except:
                pass










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


from config import bot,token
from bitlyshortener import Shortener


async def link_direto(msg):
    try:
        chat_id = msg['chat']['id']
        chat_type = msg['chat']['type']
        texto = msg['text']
        tokens_pool = ["a001cef9d44ed8083ed4d952d475e98079e60577", ]
        shortener = Shortener(tokens=tokens_pool, max_cache_size=8192)
        if chat_type == 'supergroup':
            try:  # DOCUMENTOS
                if 'document' in msg.get('reply_to_message') and texto == '/link' or 'document' in msg.get('reply_to_message') and texto == 'link':
                    #if adm['user'] == True:
                    id_documento = msg.get('reply_to_message')['document']['file_id']
                    nome = msg.get('reply_to_message')['document']['file_name']
                    arquivo = await bot.getFile(id_documento)
                    tamanho = arquivo['file_size']
                    link = f"https://api.telegram.org/file/bot{token}/{arquivo['file_path']}"
                    try:
                        a = shortener.shorten_urls([link])
                        await bot.sendMessage(chat_id,f"🤖 Aqui está seu link direto.\nArquivo:{nome}\nTamanho:{tamanho}\nLink:{a[0]}",reply_to_message_id=msg['message_id'])
                    except:
                        await bot.sendMessage(msg['chat']['id'], '`Não foi possivel encurtar seu link, tente novamente, talves o serviço esteja offline.`', 'Markdown', reply_to_message_id=msg['message_id'])
            except Exception as e:
                pass

            try:  # IMAGENS
                if 'photo' in msg.get('reply_to_message') and texto == '/link' or 'photo' in msg.get('reply_to_message') and texto == 'link':
                    #if adm['user'] == True:
                    id_foto = msg.get('reply_to_message')['photo'][0]['file_id']
                    nome = 'imagem'
                    arquivo = await bot.getFile(id_foto)
                    tamanho = arquivo['file_size']
                    link = f"https://api.telegram.org/file/bot{token}/{arquivo['file_path']}"
                    try:
                        a = shortener.shorten_urls([link])
                        await bot.sendMessage(chat_id,f"🤖 Aqui está seu link direto.\nArquivo:{nome}\nTamanho:{tamanho}\nLink:{a[0]}",reply_to_message_id=msg['message_id'])
                    except:
                        await bot.sendMessage(msg['chat']['id'], '`Não foi possivel encurtar seu link, tente novamente, talves o serviço esteja offline.`', 'Markdown', reply_to_message_id=msg['message_id'])
            except Exception as e:
                pass

            try:  # AUDIOS
                if 'audio' in msg.get('reply_to_message') and texto == '/link' or 'audio' in msg.get('reply_to_message') and texto == 'link':
                    id_documento = msg.get('reply_to_message')['audio']['file_id']
                    nome = msg.get('reply_to_message')['audio']['title']
                    arquivo = await bot.getFile(id_documento)
                    tamanho = arquivo['file_size']
                    link = f"https://api.telegram.org/file/bot{token}/{arquivo['file_path']}"
                    try:
                        a = shortener.shorten_urls([link])
                        await bot.sendMessage(chat_id,f"🤖 Aqui está seu link direto.\nArquivo:{nome}\nTamanho:{tamanho}\nLink:{a[0]}",reply_to_message_id=msg['message_id'])
                    except:
                        await bot.sendMessage(msg['chat']['id'], '`Não foi possivel encurtar seu link, tente novamente, talves o serviço esteja offline.`', 'Markdown', reply_to_message_id=msg['message_id'])
            except Exception as e:
                pass

            try:  # VIDEOS
                if 'video' in msg.get('reply_to_message') and texto == '/link' or 'video' in msg.get('reply_to_message') and texto == 'link':
                    id_documento = msg.get('reply_to_message')['video']['file_id']
                    nome = 'video'
                    arquivo = await bot.getFile(id_documento)
                    tamanho = arquivo['file_size']
                    link = f"https://api.telegram.org/file/bot{token}/{arquivo['file_path']}"
                    try:
                        a = shortener.shorten_urls([link])
                        await bot.sendMessage(chat_id,f"🤖 Aqui está seu link direto.\nArquivo:{nome}\nTamanho:{tamanho}\nLink:{a[0]}",reply_to_message_id=msg['message_id'])
                    except:
                        await bot.sendMessage(msg['chat']['id'], '`Não foi possivel encurtar seu link, tente novamente, talves o serviço esteja offline.`', 'Markdown', reply_to_message_id=msg['message_id'])
            except Exception as e:
                pass

            try:  # VOZ
                if 'voice' in msg.get('reply_to_message') and texto == 'link' or 'voice' in msg.get('reply_to_message') and texto == '/link':
                    id_documento = msg.get('reply_to_message')['voice']['file_id']
                    nome = f"audio do {msg['from']['first_name']}"
                    arquivo = await bot.getFile(id_documento)
                    #tamanho = arquivo['file_size']
                    link = f"https://api.telegram.org/file/bot{token}/{arquivo['file_path']}"
                    try:
                        a = shortener.shorten_urls([link])
                        await bot.sendMessage(chat_id,f"🤖 Aqui está seu link direto.\nArquivo:{nome}\nLink:{a[0]}",reply_to_message_id=msg['message_id'])
                    except:
                        await bot.sendMessage(msg['chat']['id'], '`Não foi possivel encurtar seu link, tente novamente, talves o serviço esteja offline.`', 'Markdown', reply_to_message_id=msg['message_id'])
            except Exception as e:
                pass


    except Exception as e:
        pass
















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

import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username
import os
import youtube_dl
from bs4 import BeautifulSoup
from utils import pretty_size
from youtubesearchpython import SearchVideos
#pip install youtube-search-python

ydl = youtube_dl.YoutubeDL({'outtmpl': 'arquivos/%(title)s.%(ext)s', 'format': '140', 'noplaylist': True})


async def search_yt(query):
    url_base = "https://www.youtube.com/results"
    url_yt = "https://www.youtube.com"
    async with aiohttp.ClientSession() as session:
        r = await session.get(url_base, params=dict(q=query))
        page = await r.text()
    soup = BeautifulSoup(page, "html.parser")
    id_url = None
    list_videos = []
    for link in soup.find_all('a'):
        url = link.get('href')
        title = link.get('title')
        if url.startswith("/watch") and (id_url != url) and (title is not None):
            id_url = url

            dic = {'title': title, 'url': url_yt + url}
            list_videos.append(dic)
        else:
            pass
    return list_videos


async def youtube(msg):
    if msg.get('text'):

        if msg['text'].startswith('/yt '):
            pesquisar = msg['text'][4:]
            search = SearchVideos(pesquisar, offset=1, mode="dict", max_results=10)
            resultado = search.result()
            #titulo = []
            #link = []
            dic_youtube = []
            for resultado in resultado['search_result']:
                titulo_captado = resultado['title']
                link_captado = resultado['link']
                #titulo.append(titulo_captado)
                #link.append(link_captado)
                dic = {'titulo': titulo_captado, 'url': link_captado}
                dic_youtube.append(dic)
            vids = ['[{}] {} {}'.format(num + 1, i['titulo'], i['url']) for num, i in enumerate(dic_youtube)]
            await bot.sendMessage(msg['chat']['id'], '\n'.join(vids) if vids else "Nenhum resultado foi encontrado", 'HTML',
                                      reply_to_message_id=msg['message_id'],
                                      disable_web_page_preview=True)
            #return True


        if msg['text'].startswith('youtube '):
            pesquisar = msg['text'][8:]
            search = SearchVideos(pesquisar, offset=1, mode="dict", max_results=10)
            resultado = search.result()
            # titulo = []
            # link = []
            dic_youtube = []
            for resultado in resultado['search_result']:
                titulo_captado = resultado['title']
                link_captado = resultado['link']
                # titulo.append(titulo_captado)
                # link.append(link_captado)
                dic = {'titulo': titulo_captado, 'url': link_captado}
                dic_youtube.append(dic)
            vids = ['[{}] {} {}'.format(num + 1, i['titulo'], i['url']) for num, i in enumerate(dic_youtube)]
            await bot.sendMessage(msg['chat']['id'], '\n'.join(vids) if vids else "Nenhum resultado foi encontrado",
                                  'HTML',
                                  reply_to_message_id=msg['message_id'],
                                  disable_web_page_preview=True)


#----------------------------------------------------------------------------------------------------------------------------------------------

        elif msg['text'].split()[0] == '/ytdl':   #aqui era /ytdl tirei pra nao pesar o server
            
            text = msg['text'][6:]

            if text:
                sent_id = (await bot.sendMessage(msg['chat']['id'], 'Obtendo informações do vídeo...', 'Markdown',
                                                 reply_to_message_id=msg['message_id']))['message_id']
                try:
                    if re.match(r'^(https?://)?(youtu\.be/|(m\.|www\.)?youtube\.com/watch\?v=).+', text):
                        yt = ydl.extract_info(text, download=False)
                    else:
                        yt = ydl.extract_info('ytsearch:' + text, download=False)['entries'][0]
                    for f in yt['formats']:
                        if f['format_id'] == '140':
                            fsize = f['filesize'] or 0
                    name = yt['title']
                except Exception as e:
                    return await bot.editMessageText((msg['chat']['id'], sent_id), 'Ocorreu um erro.\n\n' + str(e))
                if not fsize > 52428800:
                    if ' - ' in name:
                        performer, title = name.rsplit(' - ', 1)
                    else:
                        performer = yt.get('creator') or yt.get('uploader')
                        title = name
                    await bot.editMessageText((msg['chat']['id'], sent_id),
                                              'Baixando <code>{}</code> do YouTube...\n({})'.format(name,
                                                                                                    pretty_size(fsize)),
                                              'HTML')
                    ydl.download(['https://www.youtube.com/watch?v=' + yt['id']])
                    await bot.editMessageText((msg['chat']['id'], sent_id), 'Enviando áudio...')
                    await bot.sendChatAction(msg['chat']['id'], 'upload_document')
                    await bot.sendAudio(msg['chat']['id'], open(ydl.prepare_filename(yt), 'rb'),
                                        performer=performer,
                                        title=title,
                                        duration=yt['duration'],
                                        reply_to_message_id=msg['message_id'])
                    os.remove(ydl.prepare_filename(yt))
                    await bot.deleteMessage((msg['chat']['id'], sent_id))
                else:
                    await bot.editMessageText((msg['chat']['id'], sent_id),
                                              f'Ow, o arquivo resultante ({pretty_size(fsize)}) ultrapassa o meu limite de 50 MB')

            else:
                await bot.sendMessage(msg['chat']['id'], '*Uso:* /ytdl URL do vídeo ou nome', 'Markdown',
                                      reply_to_message_id=msg['message_id'])

            return True

        elif msg['text'].split()[0] == '': #aqui era ytldl gorpo tirei tb
            text = msg['text'][17:]

            if text:
                sent_id = (await bot.sendMessage(msg['chat']['id'], 'Obtendo informações do vídeo...', 'Markdown',
                                                 reply_to_message_id=msg['message_id']))['message_id']
                try:
                    if re.match(r'^(https?://)?(youtu\.be/|(m\.|www\.)?youtube\.com/watch\?v=).+', text):
                        yt = ydl.extract_info(text, download=False)
                    else:
                        yt = ydl.extract_info('ytsearch:' + text, download=False)['entries'][0]
                    for f in yt['formats']:
                        if f['format_id'] == '140':
                            fsize = f['filesize'] or 0
                    name = yt['title']
                except Exception as e:
                    return await bot.editMessageText((msg['chat']['id'], sent_id), 'Ocorreu um erro.\n\n' + str(e))
                if not fsize > 52428800:
                    if ' - ' in name:
                        performer, title = name.rsplit(' - ', 1)
                    else:
                        performer = yt.get('creator') or yt.get('uploader')
                        title = name
                    await bot.editMessageText((msg['chat']['id'], sent_id),
                                              'Baixando <code>{}</code> do YouTube...\n({})'.format(name,
                                                                                                    pretty_size(fsize)),
                                              'HTML')
                    ydl.download(['https://www.youtube.com/watch?v=' + yt['id']])
                    await bot.editMessageText((msg['chat']['id'], sent_id), 'Enviando áudio...')
                    await bot.sendChatAction(msg['chat']['id'], 'upload_document')
                    await bot.sendAudio(msg['chat']['id'], open(ydl.prepare_filename(yt), 'rb'),
                                        performer=performer,
                                        title=title,
                                        duration=yt['duration'],
                                        reply_to_message_id=msg['message_id'])
                    os.remove(ydl.prepare_filename(yt))
                    await bot.deleteMessage((msg['chat']['id'], sent_id))
                else:
                    await bot.editMessageText((msg['chat']['id'], sent_id),
                                              f'Ow, o arquivo resultante ({pretty_size(fsize)}) ultrapassa o meu limite de 50 MB')

            else:
                await bot.sendMessage(msg['chat']['id'], '*Uso:* /ytdl URL do vídeo ou nome', 'Markdown',
                                      reply_to_message_id=msg['message_id'])

            return True    

        elif msg['text'].startswith('download youtube'):
            text = msg['text'][17:]

            if text:
                sent_id = (await bot.sendMessage(msg['chat']['id'], 'Obtendo informações do vídeo...', 'Markdown',
                                                 reply_to_message_id=msg['message_id']))['message_id']
                try:
                    if re.match(r'^(https?://)?(youtu\.be/|(m\.|www\.)?youtube\.com/watch\?v=).+', text):
                        yt = ydl.extract_info(text, download=False)
                    else:
                        yt = ydl.extract_info('ytsearch:' + text, download=False)['entries'][0]
                    for f in yt['formats']:
                        if f['format_id'] == '140':
                            fsize = f['filesize'] or 0
                    name = yt['title']
                except Exception as e:
                    return await bot.editMessageText((msg['chat']['id'], sent_id), 'Ocorreu um erro.\n\n' + str(e))
                if not fsize > 52428800:
                    if ' - ' in name:
                        performer, title = name.rsplit(' - ', 1)
                    else:
                        performer = yt.get('creator') or yt.get('uploader')
                        title = name
                    await bot.editMessageText((msg['chat']['id'], sent_id),
                                              'Baixando <code>{}</code> do YouTube...\n({})'.format(name,
                                                                                                    pretty_size(fsize)),
                                              'HTML')
                    ydl.download(['https://www.youtube.com/watch?v=' + yt['id']])
                    await bot.editMessageText((msg['chat']['id'], sent_id), 'Enviando áudio...')
                    await bot.sendChatAction(msg['chat']['id'], 'upload_document')
                    await bot.sendAudio(msg['chat']['id'], open(ydl.prepare_filename(yt), 'rb'),
                                        performer=performer,
                                        title=title,
                                        duration=yt['duration'],
                                        reply_to_message_id=msg['message_id'])
                    os.remove(ydl.prepare_filename(yt))
                    await bot.deleteMessage((msg['chat']['id'], sent_id))
                else:
                    await bot.editMessageText((msg['chat']['id'], sent_id),
                                              f'Ow, o arquivo resultante ({pretty_size(fsize)}) ultrapassa o meu limite de 50 MB')

            else:
                await bot.sendMessage(msg['chat']['id'], '*Uso:* /ytdl URL do vídeo ou nome', 'Markdown',
                                      reply_to_message_id=msg['message_id'])

            return True        

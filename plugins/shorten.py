# Copyright (C) 2018-2019 Amano Team <contact@amanoteam.ml>
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



from config import bot
from bitlyshortener import Shortener



async def shorten(msg):
    if msg.get('text'):
        if msg['text'].startswith('/shorten'):
            text = msg['text'][9:]
            if not text:
                await bot.sendMessage(msg['chat']['id'],'*Uso:* `/shorten https://google.com` - _Encurta uma URL. ','Markdown',  reply_to_message_id=msg['message_id'])
            else:
                if not text.startswith('http://') or not text.startswith('https://'):
                    texto = 'https://' + text
                    try:
                        #sistema do pipy acima
                        tokens_pool = ["a001cef9d44ed8083ed4d952d475e98079e60577", ]
                        shortener = Shortener(tokens=tokens_pool, max_cache_size=8192)
                        urls = [texto]
                        a = shortener.shorten_urls(urls)
                        await bot.sendMessage(msg['chat']['id'], '*Link Encurtado:* {}'.format(a[0]), 'Markdown', reply_to_message_id=msg['message_id'])
                    except:
                        await bot.sendMessage(msg['chat']['id'], '`Não foi possivel encurtar seu link, tente enviando com http ou https, talves o serviço esteja offline.`', 'Markdown', reply_to_message_id=msg['message_id'])
            return True


from config import bot


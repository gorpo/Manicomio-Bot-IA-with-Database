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
import aiohttp
from config import bot

async def coub(msg):
    if msg.get('text'):
        if msg['text'].startswith('/coub') or msg['text'].startswith('coub'):
            text = msg['text'][4:]
            try:
                async with aiohttp.ClientSession() as session:
                    r = await session.get(f'https://coub.com/api/v2/search/coubs?q={text}')
                    rjson = await r.json()
                content = random.choice(rjson['coubs'])
                links = content['permalink']
                title = content['title']
                await bot.sendMessage(msg['chat']['id'], f'*{title}*[\u00AD](https://coub.com/v/{links})',
                                      reply_to_message_id=msg['message_id'], parse_mode="Markdown")
            except IndexError:
                await bot.sendMessage(msg['chat']['id'], 'Not Found!', reply_to_message_id=msg['message_id'])
            return True

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


import aiohttp
from config import bot

async def ip(msg):
    if msg.get('text'):
        if msg['text'].split()[0] == '/ip' or msg['text'].split()[0] == '!ip':
            text = msg['text'][4:].split('://')[-1]
            
            if text == '':
                await bot.sendMessage(msg['chat']['id'], '*Uso:* `/ip IP/endereço`',
                                      parse_mode='Markdown',
                                      reply_to_message_id=msg['message_id'])
            else:
                async with aiohttp.ClientSession() as session:
                    r = await session.get('http://ip-api.com/json/' + text)
                    req = await r.json()
                x = ''
                for i in req:
                    x += "*{}*: `{}`\n".format(i.title(), req[i])
                await bot.sendMessage(msg['chat']['id'], x, 'Markdown',
                                      reply_to_message_id=msg['message_id'])
       
            














































            return True

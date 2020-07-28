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


async def git(msg):
    if msg.get('text'):
        if msg['text'].startswith('/git ') or msg['text'].startswith('!git') or msg['text'].startswith('git'):
            text = msg['text'][5:]
            
            async with aiohttp.ClientSession() as session:
                req = await session.get('https://api.github.com/users/' + text)
                res = await req.json()
            if not res.get('login'):
                return await bot.sendMessage(msg['chat']['id'], 'Usuário "{}" não encontrado.'.format(text),
                                             reply_to_message_id=msg['message_id'])
            else:
                await bot.sendMessage(msg['chat']['id'], f'''*Nome:* `{res["name"]}`
*Login:* `{res["login"]}`
*Localização:* `{res["location"]}`
*Tipo:* `{res["type"]}`
*Bio:* `{res["bio"]}`''', 'Markdown',
                                      reply_to_message_id=msg['message_id'])
            return True

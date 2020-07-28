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
from config import bot, keys

giphy_key = keys['giphy']


async def gif(msg):
    if msg.get('text'):
        if msg['text'].startswith('/gif') or msg['text'].startswith('gif'):
            text = msg['text'][5:]
            
            async with aiohttp.ClientSession() as session:
                r = await session.get("http://api.giphy.com/v1/gifs/search",
                                      params=dict(q=text, api_key=giphy_key, limit=7))
                rjson = await r.json()
            if rjson["data"]:
                res = random.choice(rjson["data"])
                result = res["images"]["original_mp4"]["mp4"]
                await bot.sendVideo(msg['chat']['id'], result,
                                    reply_to_message_id=msg['message_id'])
            else:
                await bot.sendMessage(msg['chat']['id'], "Sem resultados",
                                      reply_to_message_id=msg['message_id'])
            return True



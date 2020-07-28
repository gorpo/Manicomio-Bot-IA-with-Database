# -*- coding: utf-8 -*-
# ███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
# ████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
# ██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
# ██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
# ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
# ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
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
from utils import send_to_dogbin, send_to_hastebin

import ctypes
from multiprocessing import Process, Manager



def replace(res, pattern, replace_with, text, count, rflags):
    res.value = re.sub(pattern, replace_with, text, count=count, flags=rflags)


async def sed(msg):
    if msg.get('text'):
        if re.match(r's/(.+)?/(.+)?(/.+)?', msg['text']) and msg.get('reply_to_message'):
            exp = re.split(r'(?<![^\\]\\)/', msg['text'])
            pattern = exp[1]
            replace_with = exp[2]
            flags = exp[3] if len(exp) > 3 else ''

            count = 1
            rflags = 0

            if 'g' in flags:
                count = 0
            if 'i' in flags and 's' in flags:
                rflags = re.I | re.S
            elif 'i' in flags:
                rflags = re.I
            elif 's' in flags:
                rflags = re.S

            if msg['reply_to_message'].get('text'):
                text = msg['reply_to_message']['text']
            elif msg['reply_to_message'].get('caption'):
                text = msg['reply_to_message']['caption']
            else:
                return

            manager = Manager()
            res = manager.Value(ctypes.c_char_p, None)

            p = Process(target=replace, args=(res, pattern, replace_with, text, count, rflags))
            p.start()
            p.join(0.2)
            p.terminate()

            if res.value is None:
                await bot.sendMessage(msg['chat']['id'], 'Ocorreu um erro com o seu padrão regex.',
                                      reply_to_message_id=msg['message_id'])
            else:
                await bot.sendMessage(msg['chat']['id'], f'<pre>{html.escape(res.value)}</pre>', 'html',
                                      reply_to_message_id=msg['reply_to_message']['message_id'])

            return True

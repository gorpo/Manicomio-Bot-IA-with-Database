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
from config import bot, bot_username
import pyqrcode


async def qrcode(msg):
    if msg.get('text'):
        try:
            if msg['text'].startswith('/qrcode'):
                a = await bot.sendMessage(msg['chat']['id'], f"🤖 {msg['from']['first_name']} ***vou gerar seu QrCode***",'markdown',reply_to_message_id=msg['message_id'])
                codigo = msg['text'][8:]
                qrcode = pyqrcode.create(codigo)
                qrcode.png('arquivos/qrcode.png', scale=10)
                await bot.editMessageText((msg['chat']['id'], a['message_id']), f"🤖 {msg['from']['first_name']} ***aqui esta seu QrCode***",'markdown')
                await bot.sendPhoto(msg['chat']['id'],photo=open('arquivos/qrcode.png','rb'), reply_to_message_id=msg['message_id'])
                os.remove('arquivos/qrcode.png')
        except Exception as e:
            pass
















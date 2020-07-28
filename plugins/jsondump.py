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
from config import bot,bot_username
import json
from io import BytesIO



async def jsondump(msg):
    if msg.get('text'):
        if msg['text'].startswith('/jsondump') or msg['text'].startswith('!jsondump') or msg['text'] == '/jsondump@' + bot_username or msg['text'].startswith('jsondump'):
            msgjson = json.dumps(msg, indent=2, sort_keys=False)
            
            if '-f' not in msg['text'] and len(msgjson) < 4080:
                await bot.sendMessage(msg['chat']['id'], '<pre>' + html.escape(msgjson) + '</pre>',
                                      'html', reply_to_message_id=msg['message_id'])
            else:
                await bot.sendChatAction(msg['chat']['id'], 'upload_document')
                file = BytesIO(msgjson.encode())
                file.name = "dump.json"
                await bot.sendDocument(msg['chat']['id'], file,
                                       reply_to_message_id=msg['message_id'])
            return True

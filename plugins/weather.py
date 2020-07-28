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

import re
import json
import aiohttp
import requests
from config import bot, keys
from utils import get_flag

async def weather(msg):
    if msg.get('text'):
        if msg['text'].startswith('/clima'):
            if msg['text'][7:] == '':
                res = '*Uso:* `/clima <cidade>` - _Obtem informações meteorológicas da cidade._'
            else:
                cidade = msg['text'][7:]
                try:
                    url = 'https://api.hgbrasil.com/weather'
                    key = '0418e7f0'
                    fields = "only_results,temp,city_name,forecast,max,min,date"
                    data = {'key': key, 'fields': fields, 'city_name': cidade}
                    req = requests.get(url, data=data, timeout=3000)
                    json = req.json()
                    await bot.sendMessage(msg['chat']['id'], f"`Cidade:`{json['city_name']}\n`Temperatura:`{json['temp']}°C\n`Min:`{json['forecast'][0]['min']}°C\n`Max:`{json['forecast'][0]['max']}°C",'markdown',reply_to_message_id=msg['message_id'])
                except Exception as e:
                    #print(e)
                    await bot.sendMessage(msg['chat']['id'], "`Não foi possivel obter a previsão do tempo ou deu um erro, tente mais tarde`",'markdown', reply_to_message_id=msg['message_id'])
                    pass
        if msg['text'].lower().startswith('clima'):
            if msg['text'][:6] == '':
                res = '*Uso:* `/clima <cidade>` - _Obtem informações meteorológicas da cidade._'
            else:
                cidade = msg['text'][6:]
                try:
                    url = 'https://api.hgbrasil.com/weather'
                    key = '0418e7f0'
                    fields = "only_results,temp,city_name,forecast,max,min,date"
                    data = {'key': key, 'fields': fields, 'city_name': cidade}
                    req = requests.get(url, data=data, timeout=3000)
                    json = req.json()
                    await bot.sendMessage(msg['chat']['id'],
                                          f"`Cidade:`{json['city_name']}\n`Temperatura:`{json['temp']}°C\n`Min:`{json['forecast'][0]['min']}°C\n`Max:`{json['forecast'][0]['max']}°C",
                                          'markdown', reply_to_message_id=msg['message_id'])
                except Exception as e:
                    #print(e)
                    await bot.sendMessage(msg['chat']['id'],
                                          "`Não foi possivel obter a previsão do tempo ou deu um erro, tente mais tarde`",
                                          'markdown', reply_to_message_id=msg['message_id'])
                    pass
            return True









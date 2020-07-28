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
from config import bot, sudoers, logs, bot_username, keys
from utils import send_to_dogbin, send_to_hastebin

traducao = keys['yandex']

idiomas = [
    'az', 'ml', 'sq', 'mt', 'am', 'mk', 'en', 'mi', 'ar', 'mr', 'hy', 'mhr', 'af', 'mn', 'eu', 'de', 'ba', 'ne', 'be',
    'no', 'bn', 'pa', 'my', 'pap', 'bg', 'fa', 'bs', 'pl', 'cy', 'pt', 'hu', 'ro', 'vi', 'ru', 'ht', 'ceb', 'gl', 'sr',
    'nl', 'si', 'mrj', 'sk', 'el', 'sl', 'ka', 'sw', 'gu', 'su', 'da', 'tg', 'he', 'th', 'yi', 'tl', 'id', 'ta', 'ga',
    'tt', 'it', 'te', 'is', 'tr', 'es', 'udm', 'kk', 'uz', 'kn', 'uk', 'ca', 'ur', 'ky', 'fi', 'zh', 'fr', 'ko', 'hi',
    'xh', 'hr', 'km', 'cs', 'lo', 'sv', 'la', 'gd', 'lv', 'et', 'lt', 'eo', 'lb', 'jv', 'mg', 'ja', 'ms'
]


def get_lang(text):
    if len(text.split()) > 0:
        lang = text.split()[0]
        if lang.split('-')[0] not in idiomas:
            lang = 'pt'
        if len(lang.split('-')) > 1:
            if lang.split('-')[1] not in idiomas:
                lang = 'pt'
    else:
        lang = 'pt'
    return lang


async def translate(msg):
    if msg.get('text'):
        if msg['text'].startswith('/tr ') or msg['text'] == '/trad' or msg['text'] == 'traduz' or msg['text'] == 'tradutor' or msg['text'] == 'traduzir' or msg['text'] == 'tradução' or msg['text'] == 'traduçao' or msg['text'] == 'traducao':
            text = msg['text'][4:]
            
            lang = get_lang(text)
            if msg.get('reply_to_message'):
                if msg['reply_to_message'].get('text'):
                    text = msg['reply_to_message']['text']
                if msg['reply_to_message'].get('caption'):
                    text = msg['reply_to_message']['caption']
            else:
                text = text.replace(lang, '', 1).strip() if text.startswith(lang) else text

            if len(text) > 0:
                sent = await bot.sendMessage(msg['chat']['id'], '`Aguarde enquanto eu traduzo isto para você...`','markdown',
                                             reply_to_message_id=msg['message_id'])
                async with aiohttp.ClientSession() as session:
                    r = await session.post("https://translate.yandex.net/api/v1.5/tr.json/translate",
                                           data=dict(key=traducao, lang=lang, text=text))
                    req = await r.json()

                await bot.editMessageText((msg['chat']['id'], sent['message_id']),
                                          '''<b>Idioma:</b> {}
<b>Tradução:</b> <code>{}</code>'''.format(req['lang'], html.escape(req['text'][0])),
                                          parse_mode='HTML')

            else:
                await bot.sendMessage(msg['chat']['id'],
                                      'Uso: /tr `<idioma> texto para traduzir` ***(pode ser usado em resposta a uma mensagem)***','markdown',
                                      reply_to_message_id=msg['message_id'])
            return True

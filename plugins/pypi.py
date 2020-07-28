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
from config import bot, sudoers, logs, bot_username, version
from utils import send_to_dogbin, send_to_hastebin
import html
import re

from amanobot.namedtuple import InlineKeyboardMarkup


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def escape_definition(definition):
    for key, value in definition.items():
        if isinstance(value, str):
            definition[key] = html.escape(cleanhtml(value))
    return definition

async def pypi(msg):
    if msg.get('text'):
        if msg['text'].startswith('/pypi '):
            text = msg['text'][5:]
            
            async with aiohttp.ClientSession() as session:
                r = await session.get(f"https://pypi.python.org/pypi/{text}/json",
                                      headers={"User-Agent": "Eduu/" + version})
                json = await r.json()
            if r.status == 200:
                
                message = "<b>%s</b> by <i>%s</i> (%s)\n" \
                          "Platform: <b>%s</b>\n" \
                          "Version: <b>%s</b>\n" \
                          "License: <b>%s</b>\n" \
                          "Summary: <b>%s</b>\n" % (
                              pypi["name"], pypi["author"], pypi["author_email"], pypi["platform"],
                              pypi["version"], pypi["platform"], pypi["summary"])
                return await bot.sendMessage(msg['chat']['id'], message, reply_to_message_id=msg['message_id'],
                                             parse_mode="HTML", disable_web_page_preview=True,
                                             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                                 [dict(text='Package home page', url=pypi['home_page'])]]))
            else:
                return await bot.sendMessage(msg['chat']['id'], f"Cant find *{text}* in pypi",
                                             reply_to_message_id=msg['message_id'], parse_mode="Markdown",
                                             disable_web_page_preview=True)
        if msg['text'].startswith('lib '):
            text = msg['text'][4:]
            
            async with aiohttp.ClientSession() as session:

                r = await session.get(f"https://pypi.python.org/pypi/{text}/json",
                                      headers={"User-Agent": "Eduu/" + version})
                json = await r.json()
            if r.status == 200:
                
                pypi = escape_definition(json["info"])
                message = "<b>%s</b> by <i>%s</i> (%s)\n" \
                          "Platform: <b>%s</b>\n" \
                          "Version: <b>%s</b>\n" \
                          "License: <b>%s</b>\n" \
                          "Summary: <b>%s</b>\n" % (
                              pypi["name"], pypi["author"], pypi["author_email"], pypi["platform"],
                              pypi["version"], pypi["platform"], pypi["summary"])

                return await bot.sendMessage(msg['chat']['id'], message, reply_to_message_id=msg['message_id'],
                                             parse_mode="HTML", disable_web_page_preview=True,
                                             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                                 [dict(text='Package home page', url=pypi['home_page'])]]))
            else:
                return await bot.sendMessage(msg['chat']['id'], f"Cant find *{text}* in pypi",
                                             reply_to_message_id=msg['message_id'], parse_mode="Markdown",
                                             disable_web_page_preview=True)   
        if msg['text'].startswith('pip '):
            
            text = msg['text'][4:]
            async with aiohttp.ClientSession() as session:
                r = await session.get(f"https://pypi.python.org/pypi/{text}/json",
                                      headers={"User-Agent": "Eduu/" + version})
                json = await r.json()
            if r.status == 200:
                pypi = escape_definition(json["info"])
                message = "<b>%s</b> by <i>%s</i> (%s)\n" \
                          "Platform: <b>%s</b>\n" \
                          "Version: <b>%s</b>\n" \
                          "License: <b>%s</b>\n" \
                          "Summary: <b>%s</b>\n" % (
                              pypi["name"], pypi["author"], pypi["author_email"], pypi["platform"],
                              pypi["version"], pypi["platform"], pypi["summary"])
                return await bot.sendMessage(msg['chat']['id'], message, reply_to_message_id=msg['message_id'],
                                             parse_mode="HTML", disable_web_page_preview=True,
                                             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                                 [dict(text='Package home page', url=pypi['home_page'])]]))
            else:
                return await bot.sendMessage(msg['chat']['id'], f"Cant find *{text}* in pypi",
                                             reply_to_message_id=msg['message_id'], parse_mode="Markdown",
                                             disable_web_page_preview=True)      

        if msg['text'].startswith(f'/pypi@{bot_username}'):
            text = msg['text'][16:]
            

            async with aiohttp.ClientSession() as session:
                r = await session.get(f"https://pypi.python.org/pypi/{text}/json",
                                      headers={"User-Agent": "Eduu/" + version})
                json = await r.json()
            if r.status == 200:
                pypi = escape_definition(json["info"])
                message = "<b>%s</b> by <i>%s</i> (%s)\n" \
                          "Platform: <b>%s</b>\n" \
                          "Version: <b>%s</b>\n" \
                          "License: <b>%s</b>\n" \
                          "Summary: <b>%s</b>\n" % (
                              pypi["name"], pypi["author"], pypi["author_email"], pypi["platform"],
                              pypi["version"], pypi["platform"], pypi["summary"])
                return await bot.sendMessage(msg['chat']['id'], message, reply_to_message_id=msg['message_id'],
                                             parse_mode="HTML", disable_web_page_preview=True,
                                             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                                 [dict(text='Package home page', url=pypi['home_page'])]]))
            else:
                return await bot.sendMessage(msg['chat']['id'], f"Cant find *{text}* in pypi",
                                             reply_to_message_id=msg['message_id'], parse_mode="Markdown",
                                             disable_web_page_preview=True)      
            return True

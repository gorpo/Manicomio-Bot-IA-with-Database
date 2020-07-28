# Copyright (C) 2018-2019 Amano Team <contact@amanoteam.ml>
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

import os
import html
import aiohttp
import time
import zipfile
from aiohttp.client_exceptions import ContentTypeError
from datetime import datetime
from sys import platform

async def send_to_dogbin(text):
    if not isinstance(text, bytes):
        text = text.encode()
    async with aiohttp.ClientSession() as session:
        post = await session.post("https://del.dog/documents", data=text)
        try:
            json = await post.json()
            return "https://del.dog/" + json["key"]
        except ContentTypeError:
            text = await post.text()
            return html.escape(text)

async def send_to_hastebin(text):
    if not isinstance(text, bytes):
        text = text.encode()
    async with aiohttp.ClientSession() as session:
        post = await session.post("https://haste.thevillage.chat/documents", data=text)
        try:
            json = await post.json()
            return "https://haste.thevillage.chat/" + json["key"]
        except ContentTypeError:
            text = await post.text()
            return html.escape(text)


def pretty_size(size):
    units = ['B', 'KB', 'MB', 'GB']
    unit = 0
    while size >= 1024:
        size /= 1024
        unit += 1
    return '%0.2f %s' % (size, units[unit])


def get_flag(code):
    offset = 127462 - ord('A')
    return chr(ord(code[0]) + offset) + chr(ord(code[1]) + offset)


def escape_markdown(text):
    text = text.replace('[', '\[')
    text = text.replace('_', '\_')
    text = text.replace('*', '\*')
    text = text.replace('`', '\`')

    return text



def backup_sources(nome,output_file=None):
    ctime = int(time.time())
    cstrftime = datetime.now().strftime('%d-%m-%Y_%H-%M')
    if isinstance(output_file, str) and not output_file.lower().endswith('.zip'):
        output_file += '.zip'
    t = time.localtime()
    fname = output_file or f'{nome}{cstrftime}.zip'
    with zipfile.ZipFile(fname, 'w', zipfile.ZIP_DEFLATED) as backup:
        for folder, _, files in os.walk('.'):
            for file in files:
                if platform == 'linux' or platform == 'linux2':#foi adicionado para nao incluir as pastas no linux
                    if file != fname and not file.endswith('.pyc') and '.heroku' not in folder.split('/'):  #and 'dls' not in folder.split('/')
                            backup.write(os.path.join(folder, file))
                if platform == 'win32':#adicionado para nao pegar a pasta .git no backup
                    if file != fname and not file.endswith('.pyc') and '.heroku' not in folder.split('/'): #and 'dls' not in folder.split('/')
                        if '.\.git' in folder:#deletar isto em caso de uso linux
                            pass
                        else:
                            backup.write(os.path.join(folder, file))

    return fname
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
from config import bot, sudoers, logs, bot_username
from utils import send_to_dogbin, send_to_hastebin
import subprocess
import time
import speech_recognition as sr
from pydub import AudioSegment
import os
import dropbox
import re
import wikipedia
import sqlite3
from config import bot, sudoers, logs, bot_username,token_dropbox
from datetime import datetime
from plugins.admins import is_admin

async def ia_privado_bot(msg):
    chat_id = msg['chat']['id']
    chat_type = msg['chat']['type']
    if chat_type == 'private':
        try:
            if msg.get('voice'):
                await bot.download_file(msg['voice']['file_id'], 'arquivos/audio_usuario_db.ogg')
                sound = AudioSegment.from_file("arquivos/audio_usuario_db.ogg")
                sound.export("arquivos/audio_usuario_db.wav", format="wav", bitrate="128k")
                r = sr.Recognizer()
                with sr.WavFile('arquivos/audio_usuario_db.wav') as source:
                    audio = r.record(source)
                texto = r.recognize_google(audio, language='pt-BR')
                await bot.sendMessage(chat_id, f"`{msg['from']['first_name']} disse:`\n```----  {texto}```", 'markdown',reply_to_message_id=msg['message_id'])
            if msg.get('text'):
                if msg.get('text') == 'att':
                    await bot.sendMessage(chat_id, f"@{msg['from']['first_name']} você esta tentando roubar a TCXS Store, cara vou pegar seu ip e te hackear agora mesmo!!! ", 'markdown',reply_to_message_id=msg['message_id'])
                conexao_sqlite = sqlite3.connect('bot_database.db')
                conexao_sqlite.row_factory = sqlite3.Row
                cursor_sqlite = conexao_sqlite.cursor()
                cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                mensagens_sqlite = cursor_sqlite.fetchall()
                quantidade_mensagens = len(mensagens_sqlite)
                randomico = random.randint(0,  quantidade_mensagens - 1)  # fornece um numero randomico para pegarmos as mensagens na db
                mensagem_bot = mensagens_sqlite[randomico][10]
                tipo_mensagem = mensagens_sqlite[randomico][7]
                if tipo_mensagem == 'imagem':
                    await bot.sendPhoto(chat_id, photo=mensagem_bot)
                    print(f'🤖 [private_bot] Bot enviou uma imagem: {msg["chat"]["title"]} com a id {mensagem_bot}')
                if tipo_mensagem == 'documento':
                    #await bot.sendDocument(chat_id, document=mensagem_bot)
                    print(f'🤖 [private_bot] Bot tentou enviar um documento: {msg["chat"]["title"]} com a id {mensagem_bot}')
                if tipo_mensagem == 'audio':
                    #await bot.sendAudio(chat_id, audio=mensagem_bot)
                    print(f'🤖 [private_bot] Bot tentou enviar um audio: {msg["chat"]["title"]} com a id {mensagem_bot}')
                if tipo_mensagem == 'video':
                    await bot.sendVideo(chat_id, video=mensagem_bot)
                    print(f'🤖 [private_bot] Bot enviou um video: {msg["chat"]["title"]} com a id {mensagem_bot}')
                if tipo_mensagem == 'texto':
                    await bot.sendMessage(chat_id, mensagem_bot)
                    print(f'🤖 [private_bot] Bot enviou: {msg["chat"]["title"]}: {mensagem_bot}')
                if tipo_mensagem == 'sticker':
                    await bot.sendSticker(chat_id, sticker=mensagem_bot)
                    print(f'🤖 [private_bot] Bot enviou sticker: {msg["chat"]["title"]} com a id {mensagem_bot}')
        except Exception as e:
            pass

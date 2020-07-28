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

from PIL import Image, ImageDraw, ImageFont
from config import bot


async def prints(msg):
    if msg.get('text'):

        if msg['text'].lower() == 'print' and msg.get('reply_to_message'):
            texto_repetido = msg['reply_to_message']['text']
            text = msg['reply_to_message']['text']
            try:
                await bot.sendMessage(msg['chat']['id'], '`Tirando print...`','markdown', reply_to_message_id=msg['message_id'])
                img = Image.new('RGBA', (1000, 1000), (255, 255, 255))  #ele cria esta imagem para nada mas é necessario ela sera substituida, queremos pegar o tamanho do texto
                draw = ImageDraw.Draw(img)
                text_size = draw.textsize(text, ImageFont.truetype("arial.ttf", 30))
                # print(text_size)
                img2 = Image.new('RGBA', text_size, (255, 255, 255))
                draw2 = ImageDraw.Draw(img2)
                draw2.text((1, 1), text[0:45], (0, 0, 0), ImageFont.truetype("arial.ttf", 30))
                img2.save('arquivos/pil_text.png')
                await bot.sendPhoto(msg['chat']['id'],photo=open('arquivos/pil_text.png','rb'), reply_to_message_id=msg['message_id'])
                os.remove('arquivos/pil_text.png')
            except Exception as e:
                await bot.sendMessage(msg['chat']['id'], '`diminua seu texto, tente novamente`', 'markdown',
                                      reply_to_message_id=msg['message_id'])
                pass

        if msg['text'].startswith('/print') or msg['text'].startswith('!print'):
            text = msg['text'][6:]
            try:
                await bot.sendMessage(msg['chat']['id'], '`Tirando print...`','markdown', reply_to_message_id=msg['message_id'])
                img = Image.new('RGBA', (1000, 1000), (255, 255, 255))  #ele cria esta imagem para nada mas é necessario ela sera substituida, queremos pegar o tamanho do texto
                draw = ImageDraw.Draw(img)
                text_size = draw.textsize(text, ImageFont.truetype("arial.ttf", 30))
                # print(text_size)
                img2 = Image.new('RGBA', text_size, (255, 255, 255))
                draw2 = ImageDraw.Draw(img2)
                draw2.text((1, 1), text[0:45], (0, 0, 0), ImageFont.truetype("arial.ttf", 30))
                img2.save('arquivos/pil_text.png')
                await bot.sendPhoto(msg['chat']['id'],photo=open('arquivos/pil_text.png','rb'), reply_to_message_id=msg['message_id'])
                os.remove('arquivos/pil_text.png')
            except Exception as e:
                await bot.sendMessage(msg['chat']['id'], '`diminua seu texto, tente novamente`', 'markdown',
                                      reply_to_message_id=msg['message_id'])
                pass


        if msg['text'].startswith('print') and not msg.get('reply_to_message'):
            text = msg['text'][5:]
            try:
                await bot.sendMessage(msg['chat']['id'], '`Tirando print...`','markdown', reply_to_message_id=msg['message_id'])
                img = Image.new('RGBA', (1000, 1000), (255, 255, 255))  #ele cria esta imagem para nada mas é necessario ela sera substituida, queremos pegar o tamanho do texto
                draw = ImageDraw.Draw(img)
                text_size = draw.textsize(text, ImageFont.truetype("arial.ttf", 30))
                # print(text_size)
                img2 = Image.new('RGBA', text_size, (255, 255, 255))
                draw2 = ImageDraw.Draw(img2)
                draw2.text((2, 1), text[0:45], (0, 0, 0), ImageFont.truetype("arial.ttf", 25))
                img2.save('arquivos/pil_text.png')
                await bot.sendPhoto(msg['chat']['id'],photo=open('arquivos/pil_text.png','rb'), reply_to_message_id=msg['message_id'])
                os.remove('arquivos/pil_text.png')
            except Exception as e:
                await bot.sendMessage(msg['chat']['id'], '`diminua seu texto, tente novamente`', 'markdown', reply_to_message_id=msg['message_id'])
                pass


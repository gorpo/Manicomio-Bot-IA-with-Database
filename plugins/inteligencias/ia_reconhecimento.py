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
from config import bot
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2


async def ia_reconhecimento(msg):
    try:
        chat_id = msg['chat']['id']
        chat_type = msg['chat']['type']
        texto = msg['text']
        if chat_type == 'supergroup':
            if 'photo' in msg.get('reply_to_message') and texto.startswith('recog'):
                id_foto = msg.get('reply_to_message')['photo'][0]['file_id']
                await bot.download_file(id_foto,'arquivos/recognition.jpg')
                image = cv2.imread('arquivos/recognition.jpg')
                bbox, label, conf = cv.detect_common_objects(image)
                out = draw_bbox(image, bbox, label, conf)
                cv2.imwrite("arquivos/recognition_out.jpg", out)
                await bot.sendPhoto(chat_id,photo=open('arquivos/recognition_out.jpg','rb'), reply_to_message_id=msg['message_id'])
                os.remove('arquivos/recognition.jpg')
                os.remove('arquivos/recognition_out.jpg')
    except:
        pass

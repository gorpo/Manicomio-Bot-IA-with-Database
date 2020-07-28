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
from config import bot

async def hora_data(msg):
    if msg.get('text'):
        #hora e data  --- obrigado ao guanabara pelo curso gratis kkjj
        if  'que dia é hoje' in msg['text'].lower() or msg['text'].lower() == 'Que dia é hoje' or msg['text'].lower() == 'que dia é hoje' or msg['text'].lower() == 'data' or msg['text'].lower() == 'dia':
            t = time.localtime()
            await bot.sendMessage(msg['chat']['id'],'Hoje é  {}/{}/{} e faltam poucos dias para começar a guerra!'.format(t[2],t[1],t[0]),reply_to_message_id=msg['message_id'])
        if msg['text'].lower() == 'que hora é agora' or msg['text'].lower() == 'que horas são agora' or msg['text'].lower() == 'que hora é agora' or msg['text'].lower() == 'que horas são agora' or msg['text'].lower() == 'que hora é agora' or msg['text'].lower() == 'que hora é agora?' or  msg['text'].lower() == 'que horas são agora' or msg['text'].lower() == 'que horas são agora?' or msg['text'] == 'Que horas são?' or msg['text'] == 'Que horas são ' or msg['text'] == 'que horas são ' or msg['text'] == 'que horas sao' or msg['text'].lower() == 'hora' or msg['text'] == 'que hora e agora':
            t = time.localtime()
            await bot.sendMessage(msg['chat']['id'],'Agora são {}:{}:{} e você pode morrer a qualquer momento!'.format(t[3],t[4],t[5]),reply_to_message_id=msg['message_id'])



        






























            return True

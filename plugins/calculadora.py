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


from config import bot

async def calculadora(msg):
    if msg.get('text'):
        try:
            if '+' in msg['text']:
                n1 = int(msg['text'].split('+')[0])
                n2 = int(msg['text'].split('+')[1])
                calc = n1 + n2
                await bot.sendMessage(msg['chat']['id'],'`Sua soma  {} + {} = {} `'.format(n1,n2,calc), 'markdown',
                                          reply_to_message_id=msg['message_id'])
                return True

            if '-' in msg['text']:
                n1 = int(msg['text'].split('-')[0])
                n2 = int(msg['text'].split('-')[1])
                calc = n1 - n2
                await bot.sendMessage(msg['chat']['id'],'`Sua subtração  {} - {} = {} `'.format(n1,n2,calc), 'markdown',
                                          reply_to_message_id=msg['message_id'])
                return True

            if '*' in msg['text']:
                n1 = int(msg['text'].split('*')[0])
                n2 = int(msg['text'].split('*')[1])
                calc = n1 * n2

                await bot.sendMessage(msg['chat']['id'],'`Sua multiplicação {} * {} = {} `'.format(n1,n2,calc), 'markdown',
                                          reply_to_message_id=msg['message_id'])
                return True

            if '/' in msg['text']:
                try:
                    n1 = int(msg['text'].split('/')[0])
                    n2 = int(msg['text'].split('/')[1])
                    calc = n1 / n2
                    await bot.sendMessage(msg['chat']['id'],'`Sua divisão {} / {} = {} `'.format(n1,n2,calc), 'markdown',
                                              reply_to_message_id=msg['message_id'])
                except:
                    pass
        except:
            pass
            return True
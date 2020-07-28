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
from telegraph import Telegraph


async def notepad_telegraph(msg):
    try:
        if msg['chat']['type'] == 'supergroup' and msg['text'].split()[0] ==  'notepad':
                conteudo_html = msg['text'][8:]
                telegraph = Telegraph()
                a = telegraph.create_account(short_name='manicomio')
                response = telegraph.create_page('Manicomio', html_content=conteudo_html)
                link_final = 'https://telegra.ph/{}'.format(response['path'])
                print(f"Usuário criou um site no telegra.ph: {link_final}")
                await bot.sendMessage(msg['chat']['id'],f"🤖 {msg['from']['first_name']} acabei seu site:{link_final}", reply_to_message_id=msg['message_id'])
    except Exception as e:
        pass
















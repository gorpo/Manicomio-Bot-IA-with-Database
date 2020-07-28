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



import wikipedia
from config import bot


async def ia_wikipedia(msg):
        if msg['chat']['type'] == 'supergroup' and msg.get('text'):
            try:
                if 'fale sobre' in msg['text'].lower():
                    termo = msg['text'][10:]
                    wikipedia.set_lang("pt")
                    pesquisa = wikipedia.summary(termo)
                    await bot.sendMessage(msg['chat']['id'], f"```{pesquisa}```",'markdown', reply_to_message_id=msg['message_id'])
            except:
                await bot.sendMessage(msg['chat']['id'], '`Desconheço este assunto...`\n```---- Caso queira que eu aprenda fale sobre o assunto converse comigo sobre ele até que eu aprenda ou use o comando # informando o tema e após ele a explicação que devo aprender conforme exemplo:``` #tema ***informações que devo aprender***','markdown', reply_to_message_id=msg['message_id'])
                pass



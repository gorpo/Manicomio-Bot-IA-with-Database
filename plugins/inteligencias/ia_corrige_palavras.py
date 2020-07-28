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
from spellchecker import SpellChecker

async def ia_corrige_palavras(msg):
    try:
        chat_id = msg['chat']['id']
        chat_type = msg['chat']['type']
        if chat_type == 'supergroup' and msg.get('text'):
            texto = msg['text']
            if 'text' in msg.get('reply_to_message') and texto.startswith('corrigir'):
                spell = SpellChecker(language='pt')
                mensagem = msg['reply_to_message']['text']
                misspelled = spell.unknown(msg['reply_to_message']['text'].split())
                palavra_errada = list(misspelled)[0]  # retorna a palavra que estava errada na frase
                for palavra_final in misspelled:
                    corrigir = spell.correction(palavra_final)
                    candidatos = spell.candidates(palavra_final)
                    mensagem_corrigida = mensagem.replace(palavra_errada,corrigir)  # nova frase com replace na palavra errada pela mais provavel.
                    a = await bot.sendMessage(chat_id,f"@{msg['from']['username']} `aqui esta a frase corrigida, em 2 segundos irei mostrar outras alternativas caso existam:`\n***{mensagem_corrigida}***",'markdown')
                    time.sleep(2)
                    for candidato in list(candidatos):  # outras alternativas de correção
                        alternativas_corrigidas = mensagem.replace(palavra_errada, candidato)  # novas frases com replace na palavra errada pelas outras mais provaveis
                        await bot.editMessageText((msg['chat']['id'], a['message_id']), f"`Algumas alternativas:`\n***{alternativas_corrigidas}***",'markdown')
                        time.sleep(2)
                    await bot.editMessageText((msg['chat']['id'], a['message_id']),f"`Correção:`\n***{mensagem_corrigida}***", 'markdown')
    except:
        pass
        return True

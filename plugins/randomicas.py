# -*- coding: utf-8 -*-
# ███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
# ████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
# ██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
# ██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
# ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
# ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#     [+] @GorpoOrko 2020 - Telegram Bot and Personal Assistant [+]
#     |   TCXS Project Hacker Team - https://tcxsproject.com.br   |
#     |   Telegram: @GorpoOrko Mail:gorpoorko@protonmail.com      |
#     [+]        Github Gorpo Dev: https://github.com/gorpo     [+]



import random
from config import bot
async def randomicas(msg):
    if msg.get('text'):

        # exemplo de animação--->
        if 'aham' in msg['text']:
            await bot.sendAnimation(msg['chat']['id'], animation='CgADBAADsgEAAmPDvFLYWdDUh36QARYE',   reply_to_message_id=msg['message_id'])

        # Exemplo de uma mensagem randomica do bot.....
        if 'seu cu' in msg['text']:
            print('Usuario {} solicitou seu cu random'.format(msg['from']['first_name']))
            cu1 = str('`Pau no seu cu filho da puta!`')
            cu2 = str('`Seu cu o caralho para de fala merda mano!`')
            cu3 = str('`É mais arregaçado que o da minha mãe quela vaca vadia galinha piranha!`')
            cu4 = str('`O da sua namorada quela puta rampeira!`')
            cu5 = str('`Ah legal, chegou o mano que só fala bosta no grupo!`')
            cu6 = str('`Seu cu, meu cu, teu cu o cu de todo mundo, foda-se!`')
            cu7 = str('`Eu lambo!`')
            cu8 = str('`Empurro a bosta com o pau!`')
            cu9 = str('`Ta arregaçado!`')
            cu10 = str('`Não tem mais nenhuma prega!`')
            cu11 = str('`Estourei ele!`')
            cu12 = str('`O meu ta suave!`')
            cu13 = str('`Eu o @Gorpo Orko @usergutto @mahayana66 fizemos um estrago!`')
            lista = [cu1, cu2, cu3, cu4, cu5, cu6, cu7, cu8, cu9, cu10, cu11, cu12, cu13]
            escolhido = random.choice(lista)
            await bot.sendMessage(msg['chat']['id'], escolhido, 'markdown', reply_to_message_id=msg['message_id'])
            


        if 'sherry' in msg['text']:
            print('Usuario {} solicitou seu sherry random'.format(msg['from']['first_name']))
            sherry1 = str('https://i.imgur.com/i8PURpP.jpg')
            sherry2 = str('https://i.imgur.com/lO5r9xj.jpg')
            sherry3 = str('https://i.imgur.com/eoSUKOq.jpg')
            sherry4 = str('https://i.imgur.com/cSimPV4.jpg')
            sherry5 = str('https://i.imgur.com/Sf0FKPD.jpg')
            sherry6 = str('https://i.imgur.com/E9FuuiZ.jpg')
            sherry7 = str('https://i.imgur.com/DKQudSD.jpg')
            sherry8 = str('https://i.imgur.com/SrqbEWJ.jpg')
            sherry9 = str('https://i.imgur.com/zawDBEu.jpg')
            sherry10 = str('https://i.imgur.com/sc3xwaz.jpg')
            sherry11 = str('https://i.imgur.com/xakVPza.jpg')
            sherry12 = str('https://i.imgur.com/6JKY8zl.jpg')
            sherry13 = str('https://i.imgur.com/XN1VAIp.jpg')
            sherry14 = str('https://i.imgur.com/g1Xo6wM.jpg')
            sherry15 = str('https://i.imgur.com/5lVbxmP.jpg')
            lista = [sherry1, sherry2, sherry3, sherry4, sherry5, sherry6, sherry7, sherry8, sherry9, sherry10, sherry11, sherry12, sherry13,sherry14,sherry15]
            escolhido = random.choice(lista)
            await bot.sendMessage(msg['chat']['id'], escolhido, reply_to_message_id=msg['message_id'])
                
        




            return True

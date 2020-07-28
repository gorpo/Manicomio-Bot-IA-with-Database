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



from amanobot.namedtuple import InlineKeyboardMarkup
from config import bot, version, bot_username, git_repo
import keyboard

async def start(msg):
    if msg.get('text'):
        if msg['text'] == 'lista jogos' or msg['text'] == 'lista de jogos' or msg['text'] == 'Lista jogos' or msg[
            'text'] == 'Lista jogos' or msg['text'] == 'Lista de jogos' or msg['text'] == 'PSN' or msg[
            'text'] == 'PSN Stuff' or msg['text'] == 'PSN stuff' or msg['text'] == 'psn' or msg['text'] == 'psn stuff':
            if msg['chat']['type'] == 'private':
                kb = InlineKeyboardMarkup(inline_keyboard=[])
            else:
                kb = InlineKeyboardMarkup(inline_keyboard=[
                    [dict(text='🎮 Jogos de A a B', callback_data='AaB')] +
                    [dict(text='🎮 Jogos de B a D', callback_data='BaD')] ,
                    [dict(text='🎮 Jogos de E a G', callback_data='EaG')]+
                    [dict(text='🎮 Jogos de G a K', callback_data='GaK')] ,
                    [dict(text='🎮 Jogos de K a M', callback_data='KaM')] +
                    [dict(text='🎮 Jogos de M a P', callback_data='MaP')],
                    [dict(text='🎮 Jogos de R a S', callback_data='RaS')] +
                    [dict(text='🎮 Jogos de S a T', callback_data='SaT')] ,
                    [dict(text='🎮 Jogos de T a Z', callback_data='TaZ')]+
                    [dict(text='« Voltar', callback_data='inicio_menu')]
                    ])
            smsg = '''🎮 Temos jogos para download com link direto 🎮
Basta clicar no botão que te trarei a lista com link direto para download, pedimos sua contribuição para que este projeto se mantenha vivo, Obrigado a todos da TCXS!'''
            await bot.sendMessage(msg['chat']['id'], smsg, reply_to_message_id=msg['message_id'], reply_markup=kb)



        if msg['text'] == '/start' or msg['text'] == '!start' or msg['text'].split()[0] == '/start@' + bot_username or msg['text'] == 'start':
            if msg['chat']['type'] == 'private':
                kb = InlineKeyboardMarkup(inline_keyboard=[
                    [dict(text='📚 Comandos', callback_data='all_cmds')] +
                    [dict(text='ℹ️ Informações', callback_data='infos')],
                    [dict(text='➕ Add em um grupo', url='https://t.me/{}?startgroup=new'.format(bot_username))]
                ])
            else:
                kb = InlineKeyboardMarkup(inline_keyboard=[
                    [dict(text='🤖 Iniciar uma conversa', url='https://t.me/{}?start=start'.format(bot_username))]
                ])
            await bot.sendMessage(msg['chat']['id'], 'Olá! Eu sou o Manicomio Bot, confira meus comandos e tudo sobre minha Inteligencia Artificial nos menus /help ou inicie uma conversa privada para ver demais configurações.',
                                  reply_to_message_id=msg['message_id'], reply_markup=kb)
            return True


    elif msg.get('data') and msg.get('message'):
        cmds_back = InlineKeyboardMarkup(inline_keyboard=[
            [dict(text='« Voltar', callback_data='all_cmds')]
        ])
        start_back = InlineKeyboardMarkup(inline_keyboard=[
            [dict(text='« Voltar', callback_data='start_back')]
        ])
        if msg['data'] == 'tools_cmds':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      text='''*Ferramentas:*
/tr      -traduz um texto
/yt      -pesquisa videos no YouTube
/r       -pesquisa um termo no redit
/clima   -exibe informacoes de clima
/coub    -pesquisa de pequenas animações
/dados   -jogo de dados
/gif     -gif do giphy
/git     -usuario do github
/id      -id do usuario
/ip      -informa dados de um ip
/jsondump -retorna dados formatados
/stickerid -pega id de um sticker
/getsticker -baixa um sticker
/pypi -pesquisa libs python
/rextester -interpretador de varias linguagens de programação
/mark -repete o texto informado usando Markdown
/html -repete o texto informado usando HTML
/request -faz uma requisicao a um site
/rt -repete concordando com o usuario na reposta  
/fala -Repete o texto que voce pedir para ele falar
/print -gera um print doque falou
/dogbin - envia seu material em texto para o dogbin
/hastebin - envia seu material em texto para o hastebin
/echo - Repete o texto informado.    
/shorten - Encurta uma URL.
/recog - reconhecimento com IA (nem sempre disponivel)
/notepad - cria um site com o texto enviado
/crawler - pega todos links dentro de um site
/corrigir - corrige palavras erradas
/token - Exibe informaces de um token de um outro bot.''',
                                      parse_mode='Markdown',
                                      reply_markup=cmds_back)
            return True


        elif msg['data'] == 'admin_cmds':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      '''*Comandos administrativos:*
/welcome -boas vindas
/ban -bane usuario
/unban -desbane usuario
/kick -kicka usuario
/mute -muta usuario
/unmute -desmuta usuario
/unwarn -remove advertencias
/warn -adverte usuario
/pin -fixa posts
/unpin -desfixa posts
/title -muda titulo grupo
/defregras -define regras
/regras -ler regras
/config -privado
/admdebug -debug admin
/id -id usuario
/ip -dados ip
/jsondump -retorna dados 
/stickerid -id sticker
/getsticker -baixa sticker
/criar_sticker -cria pacote stickers
/kibar -copia sticker para o pacote de stickers
/mark -repete o texto markdown
/html -repete o texto HTML
/request -requisição site
/recog - reconhecimento com IA (nem sempre disponivel)
/notepad - cria um site com o texto enviado
/crawler - pega todos links dentro de um site
/corrigir - corrige palavras erradas
/link - pega link de um arquivo use como resposta
Outros comandos ver nos menus da Inteligencia Artificial.
''',
                                      parse_mode='Markdown',
                                      reply_markup=cmds_back)
            return True


        elif msg['data'] == 'user_cmds':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      '''*Comandos para usuários:*
/start   -inicia o bot
/regras  -leia nossas regras
/admin   -admins do grupo
/freepkg -loja gratuita PS3 
/fix -fix han
/tutorial -como instalar a loja
/rap -licenças dos jogos  
/desbloqueio -desbloquear PS3
/segundoplano -download 
/codigoerro  -codigos PSN/PS3
/listajogos -download direto
/doadores -instruções
/mercadopago -doar/loja 
/tcxs -informações sobre 
/tcxspyject -criar lojas
/ps1 -cria xml para loja
/ps2 -cria xml para loja 
/psp -cria xml para loja
/ps3 -cria xml para loja
/proxy -velocidade no PS3
/tr      -traduz um texto
/yt      -pesquisa videos no YouTube
/r       -pesquisa um termo no redit
/clima   -exibe informacoes de clima
/coub    -pesquisa de pequenas anima??es
/dados   -jogo de dados
/gif     -gif do giphy
/git     -usuario do github
/id      -id do usuario
/ip      -informa dados de um ip
/jsondump -retorna dados formatados
/stickerid -pega id de um sticker
/getsticker -baixa um sticker
/pypi -pesquisa libs python
/rextester -interpretador de varias linguagens de programação
/mark -repete o texto informado usando Markdown
/html -repete o texto informado usando HTML
/request -faz uma requisicao a um site
/rt -repete concordando com o usuario na reposta  
/fala -Repete o texto que voce pedir para ele falar
/print -gera um print doque falou
/dogbin - envia seu material em texto para o dogbin
/hastebin - envia seu material em texto para o hastebin
/echo - Repete o texto informado.    
/shorten - Encurta uma URL.
/recog - reconhecimento com IA (nem sempre disponivel)
/notepad - cria um site com o texto enviado
/crawler - pega todos links dentro de um site
/corrigir - corrige palavras erradas
/token - Exibe informaces de um token de bot.''',
                                      parse_mode='Markdown',
                                      reply_markup=cmds_back)
            return True


        elif msg['data'] == 'start_back':
            kb = InlineKeyboardMarkup(inline_keyboard=[
                [dict(text='📚 Comandos', callback_data='all_cmds')] +
                [dict(text='ℹ️ Informações', callback_data='infos')],
                [dict(text='➕ Add em um grupo', url='https://t.me/{}?startgroup=new'.format(bot_username))]
            ])
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      'Olá! Eu sou o Manicomio Bot, confira meus comandos e tudo sobre minha Inteligencia Artificial nos menus /help ou inicie uma conversa privada para ver demais configurações.',
                                      reply_markup=kb)
            return True

        elif msg['data'] == 'all_cmds':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      'Selecione uma categoria de comando para visualizar.\n\nCaso precise de ajuda com o bot ou tem alguma sugestão entre no bot e digite /bug seguido de seu texto e tudo será reportado para o criador do bot.',reply_markup=keyboard.all_cmds)
            return True


        elif msg['data'] == 'infos':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      '''• Manicomio Bot

Version: {version}
Nosso site: <a href="https://tcxsproject.com.br">Manicomio TCXS Project</a>
Developers: <a href="https://github.com/gorpo">GorpoOrko</>


Partnerships:
 » <a href="https://t.me/tcxsproject2">telegram</>

©2020 - <a href="https://t.me/tcxsproject2">TCXS Project™</>


'''.format(version=version, sourcelink=git_repo[0]),
                                      parse_mode='html',
                                      reply_markup=start_back,
                                      disable_web_page_preview=True)
            return True


        elif msg['data'] == 'BaD':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),'''• Manicomio Bot
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30464_00/KTzJCzFUSOTbVwkJLAYUkhpHcUyuZOIDVsDLjCpwHHTsQQJelxDLOsaBZbwhPNKFtELsTMdaDtHvbnlEnQKPgVzMGgbAChKDFVDpO.pkg"> Burnout CRASH - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30040_00/a3qO9Yexagwp6uI8L3PMYX43LbtaCkI4MiFutdsrFIPeQPPi4oeDFLbxvKLpRBULt8nOyRDctUsT490U6NRcTccQu4raKJrmb7fjf.pkg"> Burnout Paradise - The Ultimate Box</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA80483_00/aNCDPUJQPrMwcqvLvrolYCWCQSHOqESMLiNlmcjZBNfDAXmKzncevtDPfdkHAjvjAlqpFtGMUWMMHwCdigDSuprSIfWWKmDggBbnT.pkg"> BUZZ Quiz Player - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0002/NPUB30065_00/tBt4wBP69DBCq2kFA7HvKJwnrd7iti4VVrEMVEfy54SWI5ovlpxO5hOMxW8DF71P4UcnHy6qeQgmtyF4Q8PrfEtT1BuyE4UoNTraI.pkg"> Call of Duty Classic</a>
<a href="http://zeus.dl.playstation.net/cdn/EP0002/NPEB00113_00/SNhRkR6CwU5mHbsD6eeliocSFWu971vOE5MAMEtl59UKYDh6TQlPTgymBjkD1SK5JMEtdVWKm9AfxbUKNdHyeWovrXa9n48cKsv7r.pkg"> Call of Duty Classic French Version</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80088_00/EAFieenx1iE3lKd0i5YqOIyjpUeVOjN2vSnQMSq2JJRU0yQaa4RIF577OUPmARnFNcb27iScjcePbfQTx9EuyXVYTgWJ5rCOixQod.pkg"> Calling All Cars</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80696_00/eiVaYJGDYWsojvSxNzRBBWCXVTveUcoocEPbWzHVHPYtavPeSDnTFIQQAtmtsHXlcXnGEWtzBzkgfJFfAwFjoQehgEINmVXsjzjRS.pkg"> Carnival Island</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0017/NPUB30001_00/x8W9aUGR5F4h2RaenQheUDaHbV8XERc0KnMvXFeKY6s1BUAOoOQsuthDMDcyF2Mg9TS51sEOmy8fIRQAaoGeEpBh7UuN5xM4hp4TI.pkg"> Cash Guns Chaos</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2015/NPUB30181_00/0ynfk37IHJ5nXuLpGEOAp3GDgQJ2ay4hr4LvHHSuydLud8FgXbNjyoAgf1dUQGuab1KP0cIwtsdP8GppwWbUQB7b7hKacXAV48Gjj.pkg"> Castle Crashers - RAP not Required</a>
<a href="http://ares.dl.playstation.net/cdn/UP0001/NPUB30042_00/m2FMGc7kE5ajDIAWCVQK83O5DApMFOk1gHU5Qcg5rpfcQD633hubxDDlg2HJb4nOEY2SBlSqyvYqjmf2BeU60qmh39eiJ5d0IyH2n.pkg"> Cellfactor Psychokinetic Wars - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2007/NPUB30372_00/bLWhuwwobALmSDeNHCjMvFsiehiSWEHbavzrKoxLzlGmDrgOqyUtqkmHEylHjKJQkfEZovVEKIRgUqArfJWocrwlrVSsgdDmhWFCF.pkg"> Chime Super Deluxe - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2009/NPUB30061_00/BMroVO5po3u4amPutwCuxMxYtstBtTvhj9a6HivqX4AHPYFhsc2dgR1ThmifCtb9IPhkRvHEx3kMCpRwu3diFX1pNwBcg4lkABbN4.pkg"> Comet Crash</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0177/NPUB30460_00/mPRatcKfAcfnfpnknAQXZMYCztADSuSlpkRlhUtrMuamMhZxgXfUNiqzscDXKnwxfGfPfSKbQQGLZUWQDRivMgbQKxeYPGkndyAtt.pkg"> Comix Zone</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1005/NPUB30267_00/qYK6MhhUFmCiFEnvhY4g4G7MnVvrGbnHjj2758pSGoKsblg1wBjTd45aERQ8wFK0Eg4rgkRQ0FPDaXwQUUpcSSpdusvbhB9rRBvtG.pkg"> Costume Quest - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80870_00/FNzpwImuRmYdLTtDCVHOzMfBIslvytHaSiTprTZVihwyCDnaTVXgyoIXONbmjTMXuJQIOzNknJTPhxsgWpsLpHYgqXQIsckxnlelG.pkg"> CounterSpy</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80216_00/80gYmOUKQGWsB8fqXji3Ltom5T5Y1hHrlWK4x79rovj0IoqE9GXhcadUeKWTLef2Pc6OyIA8Iruq4u6qXTCXoqs4cHPHymwNe9Jl6.pkg"> Crash Commando</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4165/NPUB30433_00/uhBDIWikRZpZBTIlEIXmsFREGHOBXzWPtyrBcZYmdWqxXIucTzSknCyEFTSflhdTPrmNAXDfJmnMpmKwTDusjTDmtHffAikULvFxk.pkg"> Crazy Machines Elements - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0177/NPUB30242_00/o1cDhCVlKcHALxLh5SIb03qBIFUF8y2DwKCePWHOebiVIautrjtjhN4Sfw1LLiGYv6x1y1RgH2fI3xgqSnyxHU6Euksl8tN2El20v.pkg"> Crazy Taxi</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0017/NPUA30032_00/vWuDGDrpxNXJG1mV59WIm3AJFbRJKhPha0IfJ3nMnDUQRcmXG09D4uiSaeGCXMdKoB2itAFOltmBABFOo4dEJELLjJ6s4eQWtHPFH.pkg"> Crescent Pale Mist</a>
<a href="http://ares.dl.playstation.net/cdn/UP2003/NPUB30059_00/glUD1uN0AAt77u8gq5IPyl6Ynn3NUl1WJM27D4DkbX56feYv40P0qAEqrpKFcA4aSoAPiMGFICLHVbaCxPELJtMAhFy2oQ8s1gHYI.pkg"> Critter Crunch - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30302_00/CpTiAdnBRurENGgGEqdeTInHGLjyEINxNFNHUVCUndFvzTUfgLDBBKtsIseDdyqATKeYppZPhpgGVTQiokMDinfUCxuKxPSZsUQpA.pkg"> Crysis HD</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0082/NPUB30092_00/SswAAGCMthMc6PMdpp3GVR6TMhQTKr8t10oHmNt2JaRYfWvh4m417VVI6tN4CvidjnLB0rhcJiTAVEfcga3pU6FbxR6eysJwgTbfX.pkg"> Crystal Defenders</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4132/NPUB30350_00/tbDFNbArxwFLnaPMkcNDYpPboCcfcBQtcPIcsEWEudQKjVlrzBhUeGTlIshwgNILBBJiAocEXmWaAzfwXCyAPrTkngUXjKqPsDUVF.pkg"> Cubixx HD - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2004/NPUB30054_00/dWuNytEYFP4b5Iq0OtLoMjHyEkoN1x4isglD1lqtsvuUAgLYgt3wLjRoWonSvrxmlf9HBJojVp8supoVfRvBU8YenFy2Cc8yiybIy.pkg"> Cuboid</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80694_00/PkkDrVrnAiVKnXBIvKHnwHBJaRfxCRpgzyyOGvhIxqYVsDXRdxhDCojpClbfndLEJHqrSqkFJTpzQcGmZMhUYiVgmIcLFmhEVyfGF.pkg"> Datura</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0017/NPUB30462_00/bNwVIDbvNqgCSRoOCdYQCAQaknSPbxAszGdOcAqbcqHbkHuESMButoKptypCnkIWKNYrhnbcnWUsccytMXhFMAYUoteTFmiTyUxGa.pkg"> DC Universe Online</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1005/NPUB30466_00/TVbrNEMsktCUDhNDKLLjDwFtxGSZJjajEMQydSDMzXmYeHguHqjbKwuxsMGIOqutEtgBrlFNFWZAKeFXWpEugtgJHHKcXpEgzMwzS.pkg"> De Blob 2</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80358_00/fa4OP6kX1hpjp4y4g7QgpUlb7242nOo3RC387APkqphcksKJCtdLRJ10B0RCwMxfYAD6Do8JV7IDcoNlLKn6I4oE4UD7ccoa3f3II.pkg"> Dead Nation</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30314_00/zZyBxuyRDPGzGCrzuxCqEUFvplMyLZsMphAGCplWTTrSsOWiySmEtIuRkZQoVvfmeRurdkgPsFInAiSQRKdicaGllIJfHqrWEMDAk.pkg"> Dead Space Extraction - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30269_00/WkAR5Lpkun305OBEgqOaOPL3LlJwxtRKl1LaOdBEHNOJCf4VQ2CCvESClYw0r8EiB3r9QmobMkkUWONLW37KdLYOguN8VSpXK6Von.pkg"> Dead Space Ignition - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2041/NPUB30309_00/6mJ1MyyiJ1XQx5pOMvMQiSGiprtRCvihgp8oloaBlqJEAxnG8btTV7ERMnoEE4xelo37Muv5rlG401WjogpGX07L76D10h521UkWF.pkg"> Deadliest Warrior - The Game - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4054/NPUB30145_00/6FhrBe6sDvJdtww3uLtGk2IdmtjJSfbmSTyWlwIdEOBOGotV2pGroBhpeMvYlK0eLX6UDA3U6K8ovYk75JMT5xK3PmsdCBm8CkKdD.pkg"> Death Track: Resurrection</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30165_00/xEx628B8HuNG7GfirYVWk4BP2UGve1cXhjbseDDiIwuidbYTrHWqJiNuySyGs650AbefnNXrD4oTyQa5TKqBoTuvSqUQdJV720fUE.pkg"> Deathspank</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30292_00/IrJPnkEhRIuBhAsVFuwchlw5Nfp5WEP31mq0i4gTnaFM1HX5M7fxI0Oc0d2rgAh8kDmRpDP0plHIhFBpQTU957puuxRRQWyR4KCMc.pkg"> DeathSpank - Thongs of Virtue - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80008_00/E3NjWOmPJjdQGYAc58xKJueh0lEeXUV0iyRsXXLkAUOjXicsXhFu06IJSaRu6U2TVPxeS06Bomi9dnwGh5dAYm17J6fHjwRRxd6JP.pkg"> Detuned</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4073/NPUB30089_00/651xSrmW6a7oQrxbulq38nyb46taQbJfHp2VskK7K6DLr15QhQajRNldbcepNMEOM4FwvkbcEQN3HYbn1ngfj4fTo4Ffed8tgeN0F.pkg"> Digger HD</a>
<a href="http://ares.dl.playstation.net/cdn/UP0555/NPUB30066_00/glpgdVX0rqUCUpFucxblcfvGh0VlFefsa4n7QjEaVyYTvWSLW56FLomCsNq52O4VN8JpyduQ1NSJTX0Oss7KLYTuY0BGlY948ORIY.pkg"> Diner Dash - RAP not Required</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA81052_00/xryPRtbzyZHUNmOVsIUazyfPDONXpDHkneFeqJDgvBuuJwktfEMSOAFFAkmboFrS.pkg"> Doki Doki Universe - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30476_00/DEtafACTVGlxKf"> Dragon Age 2</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30475_00/kUwUwzIlPuNedlPLEXQhYdXvliXfKfhNtvEDNUyYvAFBzSDnhThPMMeoWcIHZjTgxLXePqXLVcOhRmBPxdUPPivLdjcWhsUBUiIxT.pkg"> Dragon Age Origins</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2043/NPUB30217_00/redvO2Wyi5qL124BpKNxQvDj20HqiarUtiOSqBfQvf1u6nVExh3kDPC1QidiTxuID4JtRfIkFwoGL6qi0NVA7J3GP7VNq4SrTg5PT.pkg"> Dragons Lair</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2043/NPUB30390_00/OfGOAbvKPULWwcPXmfMnaKDSWTYtfUsQrujFBMeOYSbpDYjyLgFUdGGnHfFyhAcvpNtPxCkLVbckpVeHzjLjIueNooSImxYPdsCBz.pkg"> Dragons Lair 2 - Time Warp</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0555/NPUB30192_00/mfDivdReYhnV3OE3WjNptedT1DFDgFeWp59Sk0ga0RntjTBc5TvH0lMxtSnkVR5omiscrgbthiOV8lfumcNdx2jD4CrSFUAExpjV6.pkg"> Dream Chronicles - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0005/NPUB30057_00/YmVXI2N3mwaIfHdBQx4vnPIbNfykQUgmyLUlypipD3n3eDQ3rigpx31XCdLGrFaV81VjdmNlId0LboBM8S383q7cuuFqA3ClfTtUu.pkg"> Droplitz</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2050/NPUB30251_00/XdEMETKwheVWwGWrZIFtatMWoiYmERtZcuIFwqKAyIEZvafXEkhjXzQKSmYbVKMXPipSvKXqgANXuVzogMffkMpdVVDnwiIVSFaEp.pkg"> Dungeon Defenders - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2006/NPUB30227_00/HXOwAIzgEYmUnoPrZTVnWXSAsKVwCgNbObKWrrEwzIyYAAhXtrnkmCQwZNDNapnvfbIMWbbswmJCSKKHyzkCqkbIypVOXBJIBjUCs.pkg"> Dungeon Hunter Alliance - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4181/NPUB30340_00/pRibNYLjbfoTmstwXNedKFymiHCfjIGOrMtyoMDXRGulgtSbXseZXuDfgEjkqAoVShbJrTQhneMTCCoHlwdooZigarQBuGXUrrbTD.pkg"> Dungeon Twister - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0182/NPUB30318_00/bKoNYkLIrAhzQobxNMMsZfRWlBGRarhRCcMBVlPJemuCrUwPAcZfwFxAtrddMVzJJewrqeroHHcyatbZQFbHtdshegNXzSjKiFdEZ.pkg"> Dungeons and Dragons - Daggerdale - RAP not Required</a>
 
''', parse_mode='html',disable_web_page_preview=True,reply_markup=keyboard.lista_jogos)
            return True


        elif msg['data'] == 'EaG':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),'''• Manicomio Bot
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30026_00/LXctHVuHjfmFMX4JXAmN74WdK2IMelGmWv3aeO2ebkp6ilhgOwtMs8fFF3GBw5yDNuaTkaMeU60mCn6Ek6PSV2ba9FCHxWY7epI8D.pkg"> EA SPORTS Fantasy Football Live Draft Tracker - Missing RAP?</a>
<a href="http://ares.dl.playstation.net/cdn/UP2006/NPUB30120_00/KjAh9vgT1VmOJAK4ju02lrEE1iHR5XBfebtM2LuTUSRPWCBmYRbvm0SUlxS9QnDpLkPSBtmN5nIEeAaSp23bLgGV2UT63yS5OeN6j.pkg"> Earthworm Jim HD - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80488_00/GFBmNOsBQtSoCnfPeWRtuiiAmFFjXyMOZFmGAorxDqqKVGJAPBIIyGtMkoDSGvLGhtXIcnCqXEfTQupxaQbnxUuaWihLAdGVZcEtz.pkg"> Eat Them</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80134_00/4UHG7b6oru9hsYDRc2smh2fKbVbTqCePEilGaSBxCrECwdG08QskRV1R331XxAKn7qDwYRbnW0LW4B8uvBSEqLRk5snXdFf0RVoFM.pkg"> Echochrome</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80473_00/eIEJRCpQFVcMfxhGgXFLitoourZGgMfivbVNKRPpatikxTEfoigjgOMnLzTTxDCYVsmyFsWXXgncWQyQWpnrUxXmLZXFwQUjVLUQX.pkg"> echochrome II</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80157_00/yL3vTaB6Xcg0xlT6y5cQ19vL9b4QUQQg9YQAEHm7vSwjpMdRHyrSx3TjrMLwuvH1nAoXkDm4gFjqc4GnQgIUuHYS0hdjH7CWvvQ52.pkg"> Elefunk</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0555/NPUB30248_00/QkaFJvcusWTpMnUVfZydpBNdCucELYWrvxUYiRMBOnCwCRYFpzVEGeMHEoieHuYMwqQfDzfcJxXkvpFHaGJqNYVOaitacqweuChQn.pkg"> Elemental Monster Online Card Game</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0082/NPUB30428_00/SoHQNcgCFUXIUwfeDYjEuWgJfrOQLtcdjpwywYgIPEcoguLIlhrNbnzbKuBaXJjFlduLAfcTzMKbnamZqITsUJWkoUeEdbTbkusql.pkg"> ELEVATOR ACTION DELUXE</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA81051_00/HAFdjfEyJIOoPOMmUIfUacIkcKemIEXFUxjeGqKkiwCighibBBDgNJaHXkdgoXgd.pkg"> Entwined</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2052/NPUB30453_00/LWDtEsvXgmvtIzvGuOCQkxxyNSTKcTueljOEOaaYMlzkXAMrkQIZOQqGXjfrIrwxevPMTfTpdVRTcBueVbEIPlPoEpbIxwkJVmWgX.pkg"> Eufloria</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA80853_00/KgODlSsOxutjCzfsHfkqlvBFJWxPprQaJENFNTUxTNznktRLumUKUUsCuBBAJDBKPgvxNjWIFTLwtWKOndtOLXXeJlVlueyrTchTf.pkg"> Everybody Dance Digital - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80098_00/3dfvqya0LoxSHkF4rVChiM8qQOAjtirlnlT6hr0QojkMeGmAGKrlFGSCgYGsje0JijwJ091fwP4S763Fa4TcqPEKL5wWCep04rO3K.pkg"> Everyday Shooter</a>
<a href="http://ares.dl.playstation.net/cdn/UP4185/NPUB30272_00/MXVEBhztZIyNVBmRxXMtDpSgmBkDCdpvGmsEBBtqcUNnWPfbXbihNioSwpimtAgAyKCdYHGRcixKGPjxiuPUYYCJvVmRplCrKNxJR.pkg"> Explodemon! - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4133/NPUB30250_00/SVQHFmdAznWmtsDwCPAZtbAaOHqCkHAZOhIJMvqSjsenKmceanPICfDGbUUZDRYmoXzZRiRBFKMeZluolLWbOaHEIWXEOdvAEeAKY.pkg"> Faery Legends of Avalon - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2019/NPUB30188_00/iLYvrjTLduTCjFsSWDtD9jrtWyW00FHaimDAv57raE7xn5j9CdAGD0L3SLtu26HErmBB1yN3a0winhJhyUvm6SsW5Op3ExFtuTcU9.pkg"> Family Feud</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30343_00/FagQqXWWvdUzgccGkRzjgpzIuZQLpNqgpIbRqWfpzxhShUChYkridZHoRrdqWJZUTeYgSpHGIkUXxVCsKsWEynxbrMGWWkeoUBQEZ.pkg"> Fancy Pants Adventures - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80139_00/j9ly445oJ3oc1s0k0skP5MJxQHCLo9fRByLWqW4I2ksEQt53q71eYRbEY2kTkQViVU1umjMBycOhx8Pt1Bn8dpkgTtqXYchYrh8CK.pkg"> Fat Princess</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0106/NPUB30023_00/igWgoslLtYUjK4opqvmSifFeJ9HKf3QvOxJcO0w5QCgcPckuyFT3wKTK5eOyLfd300RCYEVqgyh7le9NNA07yIqcD9jcqrYK2eCQg.pkg"> Fatal Inertia EX</a>
<a href="http://ares.dl.playstation.net/cdn/UP0017/NPUA30006_00/bvlXEi5JR1VWGth0W6muNSsnVDefNBwYV6qvYslgCXStPjV4eXXm8vFc2RWRr2tgEfnMxeMQudai7hSqSQeC7omWDJUKnwDaYka7H.pkg"> Feeding Frenzy 2 - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0102/NPUB30087_00/BJ933rswYKNipj7Na60SnaIUsWXLcEqWQleW70O2Mcb9X1murmt4b4NrQYCpYoqLy1HRf7vhUUkVLYSJ5bryi6aKjifKMYQbkIbP2.pkg"> Final Fight - Double Impact</a>
<a href="http://ares.dl.playstation.net/cdn/UP0102/NPUB30052_00/4saIlPN1ut8dK8ivfhqEH15GblK2XbVFxD0NN7I5Dra0Sm0IIxiygcjHObjgUtEIDhypJIl4uW1oqkR0hYFtkwhvt8stHoMvBPWK9.pkg"> Flock - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80001_00/iBDQhUOAmiA8nHE0HEqe6T2aC6Fk1uIGcIS3KB0uTsq2TgjnA62bm9NTTgSOtbJs2fLX8K0DL7npGNtESvHrFrRcRl9HcBJtioaqA.pkg"> flOw</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80001_00/JXm8CKOhtxIv8X4LkvlmRwfTXMDV4OqpOsiiPwYQdNqvsshAshIDFGeSc8i1khI8KsHc3Fe5TlG1jPJuWla10re4KOMAiWmCr1lfQ.pkg"> flOw Promotion</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80083_00/MPPevp2xcECLo9l0GCFR64QaY5HL18EtceFPDA1mXmlXUincH9p8RSxb61ws5inEwpGTnnnk9VUDAcjgKPPkQHQdksxAU0h84GlK6.pkg"> Flower</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0325/NPUB30147_00/TNp3GonGw2jVpEeQ4MT4ThYfs3cl6nY6daOLY44S6TP18pgwCUn8UNvBJMtVt2XFKmPvYfs3ep2PqGgUGVKim8x95cb4bTuQEV8PI.pkg"> Fret Nice - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0101/NPUB30118_00/1WNstUIpHI9k7aebAv5JPbWnngihcM04boYQNGIOX0Pj0WtpJ4HywD7ltQ9biE1CCsBalspCbsdAws2om9fbIgbUYtiO7ofcoPsTA.pkg"> Frogger Returns</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0001/NPUB30418_00/FbfcGFBhFHFgVUZGLTmBdUahytyXdwhQdJxlZpZXUnyUQDhUJiWTgFqSnRAiUwpnDFRNiqIFkSbRruWETrKhNpkcJDSGkKxcAhuxM.pkg"> From DUST - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4181/NPUB30339_00/yaKVwGvQcLKwIlqULrXUKnnPezOaVrARxHgKFENlBBOKcgWkiNehgflALsfaGBUZCZhMtVeDCcWtdTKBBjUERjnnYOiglvoLonrrL.pkg"> Funky Lab Rat - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/JP0571/NPJJ00277_00/8KWsoeW9X64xk8ThcL82PAYJ8axMGDsTHytC6rS99nS5jDJivjwdFoYAECw0vYjS34ho5d4PSc4d2y2D7nUo5qlfAMaJlB8GrJlTM.pkg"> GaiaSeed: Project Seed Trap (PSX)</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0700/NPUB30321_00/IyPuZUETGHvDwvVlpPlQwFejwWlsPzrMtuRUdOpMLPneyMvIyzBPaFWkwRixJbKUJFHaZPEbhzQDIrzwqjSTeMesVcVZIHdkGMwZp.pkg"> Galaga Legions DX - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30454_00/MqgxAJITUzXABVSiySpMOHffSEDHcaZdwwqhLVAEzAJaTvgJkqigdWlTqbxYFswtsfYwYFhkYEdpyHmxsreurZTHorGKsXqeYkeAY.pkg"> Gatling Gears - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0017/NPUB30006_00/hRi0AFiBeSRjAJwS1rBfUjMdqIOF0TD248qUsqL6rxWOA4dqU6BP0WXXgwNWPIdNxjcwNJRALvJhkmOgH6VwLo63qlBnmilFFGvjI.pkg"> Gauntlet 2</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0182/NPUB30365_00/JebpUZTUEDjARxVYGZDetOKhaHmfffHsNzQxoJYXGndFNCbvLEKmyqPWsKShMNYnWRrbFKKAMWHLGrmxPBcerdRiEtGPTHHeelHjW.pkg"> Ghost Busters Sanctum Of Slime - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80022_00/5C0g8SqTenwnm52GhU7nFfWQl1OfIaj9QWvRuF1e0P0896bodjNFfNJT26jjXgIDdOCghHDV0B8Qry8Bja1sFQoSctaBWAwbIKQBh.pkg"> Go Puzzle - Unlock/License by DLC</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80092_00/rRX2FnMCTbMgcKYy3r4Oe3Ur5qxvRdHwhUjxnUF0eLcS3j22U0KH5AThKjtIy1nHnkDgj3twwfWF6W2OeiriXR97EA4atOEgHk94c.pkg"> Go Sports - Skydiving</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80070_00/em8fa51dqnJ5wSOgv0kwO9w23InqXN3XNEU5jSBDscDrBhlTW4o2Adnbbkhq3e1H054boFnBPdXA2En2Mly8I0HajIG9VeLe5b7Po.pkg"> Go Sports Ski</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA80011_00/Cm5KFmL8DL9nbY5CBIJ40nx4L8opreET9wWAx41eewo0a0rk4UlwVawT8ABpdfegAWigmxGRwuY5E9aDaP7g3XkcRoDgd9oD857e7.pkg"> Go Sudoku - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80637_00/FZyUrfXnxKZMRYfSsCiyIhkHOQDgFCMhXAlQIZbKqUYgxPImgwKNuuKlQbhvkoNAbffalVMfKaEJCTbqFmnKBSjwPxAeKkDEQjAve.pkg"> God of War - Chains of Olympus</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80636_00/jAmmbyVGchttYyfaMPRCyjmjirocbegklMcKsjKDNgGExiXZkXBhsMOzRFTwZTpWjNBWXBjPbdgpJqQtjIsWSxkmBJPMByarFIjUz.pkg"> God of War - Ghost of Sparta</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80491_00/8N8Bfnr6KkJK1AEE4ScNR5PK4PAS6IddadTdGb4nKy9Og3oNlPT1MlN8Vf9cDIrBoMlH7r2T7eQC1jBfLMX1IhxKeIKXIl39LO5Ov.pkg"> God of War 2 HD</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80918_00/CeOvzDdDsBlXxMLySmhFiqvweBfKTKFUrKsZUjHNojmbkNKpjHetAQykAclglBSM.pkg"> God of War Ascension</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80490_00/Q4aHEarfYLMYVaICOq1wi6StDeytGiQqpS7OYr743UDSktKcKQEkesEOYQbM9mfnU77TNdDOWurCqO3u9hXrQvX0xFtbi0WsUQIWH.pkg"> God of War HD</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1018/NPUB30252_00/tsPWNSIrJBZKICvStLKSxGmRRseIHRViGSjaQoQbPRBCMSjnWBKSIhjWtYSNhdhWUTzZGkYjVBICnxqsZAodlNxRyfwFgqRRANQaB.pkg"> Gotham City Imposters - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80075_00/JvlRY2aTWbYYacobdJMWmuu4lYAWnV9e8KiWV9gLIG8fBiSd8LWqNRL1mGRD83qnOPOmhiSg05IdWNhYJorG7dJLi5R1kyE7jwW2R.pkg"> Gran Turismo 5 Prologue</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA81049_00/hqQqSraIcVRhAwhijZmNzJJHKWSLoXThclDUdyEKDWnCIJimEFcNSvxsfJdtkqDT.pkg"> Gran Turismo 6</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA80019_00/6eswGLr8L7re4iye4yd8ycdqodyPtY7jj8dVjYaXvrb5Mqr1Srx87uLIYtqnuAWpx2mxOFWYrDjUj42FXw1SWnCjHqMKvAoevm0Ky.pkg"> Gran Turismo HD Concept v1.2 - RAP not Required</a>

''', parse_mode='html',disable_web_page_preview=True,reply_markup=keyboard.lista_jogos)
            return True


        elif msg['data'] == 'GaK':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),'''• Manicomio Bot
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA80292_00/u18VSJaNLeV3c2c1ijIa9VUAP3L8smSleLmc4A37MoeTFYC1MeMVAiiOd7N3c6xYP9HbWWV7hWbE2do6DTiY8Gi7uRe1uvE91ct8h.pkg"> Gravity Crash - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4104/NPUB30130_00/kwE7yj7JRMvYeE52CaSlxD4mJ09fk8NmkOkojOgNnMkf2Wvlb8W5E2rJFtuJ6J0k2W7QOhsD0Nrcuc7iu0Y0SMPDOXFNyRD1PckkG.pkg"> Greed Corp</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1012/NPUB30334_00/bZrcCxiCPBayVYAFeXwoEQXNqreSPiQebIrLtKjOoXOSHBXMnXTAuXizIublZAuFPjmwjxazExSedZHkRiJdweJbdyMyvWDYWNCeK.pkg"> Greg Hastings Paintball 2</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0017/NPUB30002_00/iNVxg3h5KVGbdm63XAQ8vaH1ACxwaP5jaeLRYaXG2Ro64SoTIe2UEILV926MBbTiQPLRlyocRgsbqMQaqVAlHFbjWHIm0t60l0YFS.pkg"> GripShift</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0017/NPUA30014_00/iSOgSAnUJA5PEjhff1DdN1cUGg8kReh21PlW2BwS4QrY77GBFNxoGkAuwkeyeGfYQUm8Mfekb41j7xeAygKeohwIvPUMTBwgLDa0s.pkg"> Groovin Blocks</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0017/NPUA30031_00/2aarmS5WqeQAKssd9jco19DRRB0LXBktl1x1teTW49cTv2gd8m6IgoKiqXqiHfPk81BOSmwUCeqidvxGNP1fxwKyWaVpm0jiKiGE4.pkg"> GundeadliGne</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0017/NPUA30029_00/qitGLvLDArHM3sHKbmVHIiIQRmlGdQteqOKBWAmwTntHEbkEWNuuKum1CyaQVGdvOnXbXDJBM9Nmt9iNRXuvaxuRtuXnIoVI5cPdA.pkg"> Gundemonium Recollection</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0177/NPUB30078_00/GYOy1P6keVjxL4Fp5oirvq3MtTUTTdtfKiR3q7O5AGuenWyb2ASXkUdEP72vOpcpKX7q40cUtj4GxY3B6EFWyT2om1Dspaiv8rqiC.pkg"> Gunstar Heroes</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4122/NPUB30458_00/rVPKhsmzNHkjAIbccjBjEARZoLfGxWytAmcaWDyqGfQNemAEVpOoNKgBARPjJWeGxrwrJWNCqKiCZPAzZPZkWjXbZiOkOQTPMKtUn.pkg"> Hamiltons Great Adventure</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2016/NPUB30101_00/Qx8KA3bYslAMWPJYFHwogjRbg8WTfSLSR08gAPuRmfplRVkHG6IV87334TNByNVTNwTDGdPnksnJ3HFkKJOxLinJLF53EH3ogGB1E.pkg"> Hamster Ball</a>
<a href="http://ares.dl.playstation.net/cdn/UP0101/NPUB30096_00/wWvCPVqgTcfMwsWMAHnqTlwfAeoXKWsDBCdLBLdwWqJXaxuNCFXEUxhTdjCFbknFXftihcaIOipaKzgJciYWOjsUfKMycjDATPafB.pkg"> Hard Corps Uprising - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30093_00/0wSVU8bBixku0J7NTg4jHFpfd5NMJHadVaCx6pJ2hfhh24EduVUHfvJV9Lm6E4w1cpICcBpet3AgYlibhqDf2FDdavgTNwLFypB59.pkg"> HASBRO Family Game Night</a>
<a href="http://ares.dl.playstation.net/cdn/UP0017/NPUA30004_00/eQ7YSLGmnAtPjIK2dwegwljRQmluoDNe24dahUBfyilXFs3DH18JShMVgLf6571SP456vbObEyn5UwT2no3bhX2kT4JJ57VL711Rl.pkg"> Heavy Weapon - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80930_00/JKTDbIaLnjDRcBUdMQhnBwfZoZYnLjMbxLbgEzuZyXoYHGFatjDDRGuHAZskQbWD.pkg"> HELLDIVERS</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0017/NPUB30016_00/4BMkdQ8NCnNpcC0PUBNLQnWQeopvol9mP4bTuBfkWLO2NcDsi8dxtNQpPMh2sp3hMUK5uHgggenRH1XbTesqF17pReS9MpsYyqqRY.pkg"> High Stakes - Vegas Strip Poker Edition</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80044_00/qOoHEAcCo7DyqssUqcEgx1yB0T7ctC0TItCWQfqHrONcVWe80YCnvIeETf524bwf1GE9KLcerxhxlRSvC6SSUfA4t6Ujbxpm6IPwV.pkg"> High Velocity Bowling</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0017/NPUA30030_00/cinLiLleaffFQGbQrbJK9OO8t4p8yfO5afSYVs4b3VU5EluMPbVFe9BVOEBbOr3vKGDNr8QDn97r14xedvEqcJjBngvm9DSLqEBRx.pkg"> Hitogata Happa</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2046/NPUB30422_00/lpBjcpEUaQALNyWKehjZfgInDDEixjVTtFLkGlLjnasGmlvtqOAbxMrYCqJoEAMLAYOLCvEiOnFwygqxjLONkhkjLxypngPQITowU.pkg"> Hoard - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80783_00/IwLopfrSpQbCQdQovEEclMknhPMNeTTTVbeEZNgtjtYUwcTalRzGpPEErHegnXWnPfjmtxWmxUxdznttOFVNKCDrMoupLkKpZnUUV.pkg"> Hohokum</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80765_00/ixTqQGSJxCvVBOHEvlciKlrpLqioWoqBohuWlFlSbuGUXalZaXKkNcrVpAfAmHQrwJCFZYpqPhxgZalrLOXKMcaowKrKpJNJeWvUQ.pkg"> Hot Shots Golf - Out of Bounds Complete Collection</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80864_00/xWpDMWJncCozrjMGoggjRZPUtGIYrBSgsBYImpcRWhVOYMRSFnWScmVEvCOTnYxRGESNxTihPNAvgMOvwGJkrqDjkkjmobOndCLYU.pkg"> Hot Shots Golf - World Invitational</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80291_00/I54LXhYdcmySPytNRqwso7dwvfFxMP0gi7wPH3aF8x6yGu1QGHo2TyFKLmScEVO99ejPR3Uepb6eNbRrkVbImsTv6AwqCC9pg8P4W.pkg"> Hustle Kings</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4068/NPUB30233_00/yLGLyYYGBWRNxjEsxCItNqUkaBqmhqiAhwjgDDZmyoyVDZzOAfwpIpWaAddmTnwyOWBKBQCylHGqZNUVjKnfFRxsuDsRxCbQLAOFk.pkg"> Hydrophobia Prophecy</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4118/NPUB30189_00/iC0NjUQPiR3XttA6KD7KuyUocTYcTsnNpPN2q7oYmAqTYEbUPGbgI18uVrHlgNHhIBBNvPeVgI3mBAshD2CdkNu4MNcQDNFGFUToH.pkg"> Hyperballoid HD</a>
<a href="http://ares.dl.playstation.net/cdn/UP0001/NPUB30383_00/HGoqGKULratGDQChoNvPZmIoPwzStFjzJKVeSzYsUObqycipFFhsktYtFJXjJyMdYUvalvcmZiJpJXqkFwWVlMYoQMwyXzvhBJprw.pkg"> I AM ALIVE - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80676_00/slEgkSMAsXKKUSskgfAPiJEmZdGrdWjsdgfJoGlJQhFlOYhZfQcFooQolyZgGrKdyEhgXCyAYXbmnVBSrwMzQZoSEECejaVAkmCrU.pkg"> Ico HD</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80480_00/EWuNWyWqVaIsykUkMPQhqIRSbyrKvjzagKzwdJgqBcKtJcFyXzGtreFyhGprTlKhYvWSBHUmFBRLfmCfDsZwoxdbtqOuvQkugpvlD.pkg"> inFAMOUS</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80480_00/Jr34rAPhDK1ay2CsuU3pjwGJrbMir0jG6EV7ABPmkNqjDHSqL7CDoS7dm9pqI4KB8OauJc5HHy2KG3vqgpJR9e4alGnFSHhcB5L1M.pkg"> inFAMOUS 1 - Collection</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80638_00/gMxSOPbAdDfSFZAaZTjNIfBmsudlfqPBmumpwEqnbHYExdlkeXPxHxsAzSZwEqVuKiSLQemfittEXmXaIqRwPQWtjjLwmawBtehUW.pkg"> inFAMOUS 2</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA70046_00/9XTKhOvnJXw3iVUaRtoVh2GIxtsEnvphgTyOWCoPHJj7iU0I2GtvppIpsVWRcUbauQm2cSPHLePMaDCFq6lKoQhYWwXgodIhxtkQP.pkg"> Infamous demo - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80657_00/LrZeqyhydeLqcofuMAewBWiYLmtmuzbhNLqwTaUZZbhqXlIRIEWMWStDlRxbPiBOiJwHEAnmRCEiMBRAuLVdHUfyACHDkoCysfhKk.pkg"> inFAMOUS Festival of Blood</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4068/NPUB30104_00/YLC7Vlh1Pne6LlI5Mb4yyc9i4JvaTRBmaeVh9MvDWts0vwOGVAXmV4tVPcVAOsyOoMVBkfYuGtRYPyR7Iv7Nnid1GgVVwg7ylFp8u.pkg"> Inferno Pool</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2004/NPUB30100_00/PHft7WFIjLySTpQRkKim9dlfXwlRhNv1NchAiXJaPTqTdKWNDaVUk0jnGa8Uu8kaDo1xBScexNoNo2sqdPIvYhM0TWMf0Ra6ukgp3.pkg"> Interpol: The Trail of Dr. Chaos</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0700/NPUB30073_00/yftHMLuyjThIDxU8uKdTmkTBIApEbVl4v3hG46Ka1bpffTV9jConWYfrndPcbEqAL1uCkO6T2rPSq1T5YTkHQgHqLX5NISyiUtMfK.pkg"> Invincible Tiger</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA80983_00/TIVxZAsniSMdUriWkaSMepLEktNUMRJkXKxJqGVjtBOQoSjMmmvRJzqFuhSgvuDd.pkg"> Invizimals: The Lost Kingdom - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80707_00/XooArfZGVNGKVPnDaDWCnmOvXmXGLXDYcbbhqHNBYDhWqeXEYGPHkjXzxHSlehQDfBkGPSaxzDQfKBUjPGDKiOaFRNuCzyfXSEvgQ.pkg"> Jak 2</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80708_00/vzYhVzqTsUQAcLDKYpKvdTDpVKIAoZnVlOAftkSugMVHVACFMIEXgHwAuxOBMggCjAXYjlbPliXjgFOdzLBHUTXgEWfzdwcVYmyDU.pkg"> Jak 3</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80706_00/JEmDDUpxfKrhvwUFVCTXGvLPlGwXOnUxCiwUQxbVstHOBJXqPmmYxIWTELVPtLAHbrtsSnvBGRlmrOPdxsnuZXIwPwQFbiwMaVoAh.pkg"> Jak And Daxter - The Precursor Legacy HD</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0017/NPUA80227_00/WSN6qokYNcvIDhd42hVqsLrIrGVGUT24d7PukPRDhhp5mKagrCn6btvbaacUWyL6sr7nXwt6dmgG60L9ggKYoht6dEs4M9CwC7HMH.pkg"> Jeopardy</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2049/NPUB30368_00/UtkqoestrSObnjQJlVelKyQsJMrQlsAErYzuhAstARtrBHishLpjLHOQAQlwjKbhivZhlICArHlXwOYVQRYbJnxLAuefmJiDQdZyv.pkg"> Jeremy McGraths Offroad</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2034/NPUB30315_00/fNrrnvfNn0hY9BMHf6ad7slks1lGUKIGPMTL3lO0cyoBXTJI6kmlCOp3fypmlkNw2tAJrkOPNO6OX7Qb9qdXOMCjP1oEOU0DPuGjh.pkg"> Joe Danger - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80275_00/bsHsRCfuVmnDPfigiuykTWXdtjUwJjeTdOlevIIJhfAmzKQYTjJSzLUcBdVHAavZzHwIDnLtmjmaatshErgvtlLmHUuKUpyXaRhHA.pkg"> Journey</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA80275_00/aCKxNJrjSCjNjgJflSDFKSMpmOmDumfMrcnfKDXvPsrperfouTCvTgHGtejhRClfCZBWSgvsJgxvTSbLqBdKpTPTCJoVnFLGjpDLo.pkg"> Journey - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2031/NPUB30231_00/2GQr1IK4eFMr8DBCuxUXaSTSs5YsDsuR6XC7v9yEXeGwDIRjiWKNmuoao7m0rlq1FxJKnXQLLNfGvvRoa94Nr8pAxjIKeaOO6uws9.pkg"> Kick-Ass</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4042/NPUB30183_00/mouEgMuNIQZIJrhAKhlLnPxqqsQAuujqAKunkSAGGoQYIdJXABmKJUWEgdqRJhLK.pkg"> KickBeat - RAP not Required</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA70167_00/bGcKVBsyiAotSuhxdUmXjitiglHrHkHmpNUdohMINHTOvqXlMEfEMNBTRDsfpMRAzlsGnQTpgWocBnqutIKXVuwhbbivqjNgodYjs.pkg"> Killzone 3 Multiplayer - RAP not Required</a>

''', parse_mode='html',disable_web_page_preview=True,reply_markup=keyboard.lista_jogos)
            return True


        elif msg['data'] == 'KaM':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),'''• Manicomio Bot
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80856_00/ZGwPtXvUtvHabPiHjkWmZOIQYbQvCLdIRKseMMPCEzVlwDXhcdFwhiJISMRBwZrZKiQBMlZuloGliIRkezyNZXFwvJWppPKcAMSPf.pkg"> Killzone HD</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4073/NPUB30235_00/OIwBlVDdkkXYIeIbHybOMOrLMdSbIkEipTfvjMpmiZYtWftaCEAVQDAAXKvGgLvx.pkg"> Labyrinth Legends</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0082/NPUB30225_00/uJaVMxNprEydSbonXRukWuUFiPLwxxaadxRatcgrYxwkzELFgsBzGnHOAGYUByaQOCCqYClfVNWBwciwycgUelyqlrllJapqxCees.pkg"> Lara Croft and the Guardian of Light</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4139/NPUB30228_00/cJlMEt3Fh5IODcX1hYbt8cOHnwa8L6ns3i4xt2BX3EDs9SCjU8d5wy1l8QiqQldvlQWI8bBlUKOqvJChXM6V1lrRvokKKGcAmAqI0.pkg"> Lead And Gold Gangs Of The Wild West</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4295/NPUB30461_00/UXbViDNauzObYbIpFFyxxQALhnYkhuMBtRJxFVdNoBDadLrLODlzbNsHUQDxgGQhoiGWvxXabWaxLOCoQLpbmHsUIDEIVAYGKdJDK.pkg"> Learning with the PooYoos - Episode 1</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80012_00/rmcIOlwEncBASn4ARx8ukk3wqQ451E2QNR0j2MVyuHoAV25uA22GMde5iJsE9TWvEIFl37XjT9FO1UfeE98fyOfH9VuIth8ECj1GH.pkg"> Lemmings</a>
<a href="http://ares.dl.playstation.net/cdn/UP4096/NPUB30435_00/nOSAerrUMEqJEMpLEJbRnGCYQwHXhLFAJPxeKUNBkUGFHoOJGdfjmDOkhBnLexheVRNKeJkhgzhHcrQvLThXcLgzScDuqmzVgVaND.pkg"> LIGHTS  CAMERA  PARTY! - Missing RAP?</a>
<a href="http://ares.dl.playstation.net/cdn/UP2054/NPUB30373_00/GiUrIooWcueOdoRXJVdKUGHvGSGStHinlGUqDYZdoAukvrWOwfhukwTehThOlLnKHMyAOLPtdOkvIOIheQdfFQcgglVJnmSsTBeWy.pkg"> Limbo - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80009_00/p5iRLNPPrOLmwhDs2pJ1UIdEV63c64qfFtB9J51AsqhNb0gmFAD8IjgeTJJsFPAsoE0BF8COvlNCPcIsafOlM2onuAsnpmvfwQ8Gb.pkg"> Linger In Shadows</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80662_00/UcYyGmZcjkVVOIGyhPmNxHcnKgwkGLsuhdMaqIXARhhFFnpFDuosvdPyMkLWZZXiWGkJlKExtlvMeqpXNAzCIBsJFAgJFHJUyXXdl.pkg"> Little Big Planet 2</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80848_00/INTvKaLuhpnWvBIaXeOhxVFYaAgElelJgPorzDuOPZemFDYfRlayiEwJNUVByZQcXviOHuwNhzocwGatOFrbnPjjhCDapaOeMQbnI.pkg"> Little Big Planet Karting</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80472_00/qFcxgxEXqEWYODYHhjub4YI3Km5QY1iayRkkO6QXk6bFsTiwn7QW3l1r9rviiaqtGce9VRgWLrNpmYmDr1kC1VjBEsgocCb5HSRh5.pkg"> LittleBigPlanet</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA81116_00/aKFlQguFjIQtodJibSefHesXqMsbnyNxJDxiaScFMbGpcvVUrkBOlAymJJNOQMpphWBlyrwyVzMzdnjZDqfMvbqcTsYRuzuDpYAaK.pkg"> LittleBigPlanet 3</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80069_00/TnHpdqAYvirgDGR8hwC3KgAQ5qPtYu5yLqT9bni9gxI2Da7mKRDilISHfi3MB9E2dKa7VhNK7jgaRcRtfTDOaU2BIrkHeODDe0YG3.pkg"> LocoRoco Cocoreccho</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4055/NPUB30048_00/ymvBhU0kEQqmn60lll5enMYvNvH8THkVtDxJ860PRbbbFuDwYfLORcqEsw1rtOMGuDTB5Ixqdvap2PbvpM4Fpt39FMw4n2bstMI2b.pkg"> LUMINES Supernova</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30134_00/hEH94fwFWItOSIvtE3IsaUQi9GOOnB7jqoxMyS3XpC3mMJEw3IS9iYHNoY27Iclgsjr3lkAOMJap9PIov3uvxoSkxecTbprpwWGK5.pkg"> Madden NFL Arcade</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA70126_00/ffMzBBXDedxaPJJXeHVGyqzoAzeEuJMYHACcAZrhSEBHJTjJiWYwbIMmIMZEmHexcULizPuvVaMMoQZbCNhINAECmlcBMeWxacuvH.pkg"> MAG - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2004/NPUB30047_00/dyxF64c1McFv6ofNC1IIuVFIraMvf2OXF2R2L4fhk7qXL4avvU2Wu3U7CHPAN5mjX6HrwI0GN29IgRV3nMFYUOqebl7EmY247huwb.pkg"> Magic Orbz</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2037/NPUB30408_00/uWlZOUcOHXKTgCVSoBsmXCtQWNvaSxCIMIPJjpMDdpPwMaoVIamEXRYLKUcYIRHIBAtQBrFmUpxfanVZFFqSzZWbsnptuRIdotHTC.pkg"> Magic The Gathering - Duels of the Planewalkers - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2037/NPUB30330_00/2G3sVXvE9bPX2DNMIehwsa3MJVXGNiXtcDBBh5hDu48Km3W6x45emGjyOvg0L5eEV0MlCK36LFaFjjrUul5gghHTOErTL2YILHsJ8.pkg"> Magic The Gathering - Duels of the Planewalkers - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2004/NPUB30045_00/mEA9vEMVnKXVmNhny4kF1tewxb2qitGr7TQ75nKH88hPO27ijWV3mynHWwx2vun0NXVp7LPadxhhWtNjnSHYFkxERcBcqq9BWlMxV.pkg"> Mahjong Tales Ancient Wisdom</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80797_00/TkqTvCSqkbMSjihdaPNieqFTjqivSrOllUMaCUDWeJZiUNsVLmbFDLJCkCyEEoxqiTDKAqLHSRDkvoeyajaYLvoQIwfthLuxThtQF.pkg"> Malicious</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4042/NPUB30182_00/qxDJSgGcDkodYcwgXqKPgHbRWuFCphRGCrjjfycJROWipheIbEwDeXGzVebzddWOPkawHNDMIDjLZofqmxtDNcdLBpizHXoOWFKIn.pkg"> Marvel Pinball</a>
<a href="http://ares.dl.playstation.net/cdn/UP0102/NPUB30068_00/djJRVWbroKa4GOr5f7D5dDYEOFG5QiMnDcVw69i0fAp5r07PpjMrjonymaLLUjGCmdmE9wPyWwXroeMRgT9METvxL2OIXxPSgdlf9.pkg"> Marvel Vs Capcom 2 - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30447_00/BKvgBHanxyIhKFzVaDZkWHnrEmwzxJygzOQbkKmjmrMiNZFHxIptBkJwzfSvrjjTQqdBTiqWZFAHKvUGqZebVhCEGjoEifrhtOSun.pkg"> Mass Effect 2</a>
<a href="http://ares.dl.playstation.net/cdn/UP0367/NPUB30102_00/MBN2nkv9nbm9t61UaBwyJo8O5GF4YL5FIG49NKogE6CGbxhy0SxolqCv8fcvhIswL1Uq4585VLF2A5EsYhutaLvyv8RDFODb6UtdL.pkg"> Matt Hazard - Blood Bath and Beyond - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30288_00/VWAbctBuxuuPYAYOffoEAGxNbjRsLEplnFcVXREzQkqCCnHrScMcpitSMmsPipxMpLWsblLswLbQpwiAqTGTAglawQQcmauczrkoC.pkg"> Medal of Honor Frontline</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0102/NPUB30114_00/BPOxkiNI2ajfRD9hYNxmMQOXHLln4wRqcjKUnvrypKIW9eekPXxUkMcy9QxiaVh4YRLc71LbjNc3YdhDyLTMb9dVQxhjCfKjHPNar.pkg"> Mega Man 10</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0102/NPUB30036_00/Gs9jIyRV2fiAC8RjPILQ4w36NY04SaDfeFEPspj2qSdEPivGlp8tHw69epBMeP1Fe5gnbOoDdgtA3HBQY3wknolgsTsnTKiHNFfvK.pkg"> Mega Man 9</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4002/NPUB30419_00/yYBsgtpUnzghzYDmgcEgwtrBLYyVSHlGrYbtAdOFEXzLZJDLNAZQyVzWkRuLWikUQTIwEjXkQGfafvEDTDYmcsJekbNBRKRndmjQF.pkg"> Mercury HG - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80132_00/HLXx22H1WRXVTOidMGpmNilC3ONLi0X7FtLDkCE6DlBP9Egk0XoCGEx229khhhxcmJO0cShdQyP7OfQJg00t9we8oXGUPkLXmbPR8.pkg"> Mesmerize</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80132_00/SKwVrerwrGp7DqDGgHLgP7sGJaRSihFxJV6y7TSWRMJpQSaCAgrykmywMV1pEQwi8pshnY1BbPjGmp4irtK2aObMy5lMSvrQCmFls.pkg"> Mesmerize: Trace</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30333_00/lySuCSkjcZJjmOjPJJiZgesUAmGlMVZtgOyAzTmDdgZcwUwkPddQsMljotNsDFyHezxeSTRNOJkDqYtZEzXLARvHrBWvoiVUCrFJF.pkg"> MicroBot - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1004/NPUB30471_00/UohqJcPecEqnvdVnDCjxalIETeCDSVtIcuMPiayMpwmbbSkPZVJOeksIqOTJQOKrzCSykyxTJKmPouXxfoZMwQbhdazwJmJqwPHuT.pkg"> Midnight Club LA Complete Edition</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0001/NPUB30174_00/DQKAiNvYLzQgbWWbMgrUEZiehEqOcAbAToVaELudIYrZugtqlRhkBSENeRycxyugzqSLPdtUbcxhckuduKWBqtLbGNqjKnabeqiHS.pkg"> Might and Magic - Clash of Heroes - RAP not Required</a>
<a href="http://ares.dl.playstation.net/cdn/UP0555/NPUB30067_00/lYpwcghm0u7wvInQrITUihOR0GwQdQ5setRIv9IYAfG3Ea13jNkqMbBktfk3Yng1BXl98p6HOGTg02tmnj9cpK0ACEBAu1Gcn1kAm.pkg"> Military Madness Nectaris - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80982_00/mHEZesKDPfEWkLrybOhSABPviMcStktOSSpChoaeKQezfmNHhepHQJlBOzjgZedLCaOfQDYJXXJCmlNgaFbaRjZuGHlTCWbPxUcxt.pkg"> MLB 13 The Show - Home Run Derby Edition</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80912_00/wcXtOOSqhVPVearxlYLPwGLChqCjuJFEXWjdXfIouQVVhIMztHSkKhigKIIdQqZrswCuOmDFLUMVbhloTcwBzrXctuekgIwMTkNPp.pkg"> MLB 13 The Show - Part 1</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80912_00/NuidXfAGdKCzAPNHKltKoMgHaWFdQRYzkrKEGBWqKzRFGNWnzMQgANzhvjgEZyceADSvXxhBMmaLQmqTfJGjwHHXoNpyWlwmKyVYJ.pkg"> MLB 13 The Show - Part 2</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80969_00/ysbVAlscyCDTZBzEWgPdEoXZRQEOvOWSrJvpaEBEGGCXmjPRtudiwSfNyGfkuPQP.pkg"> MLB 14 THE SHOW</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA81353_00/UP9000-NPUA81353_00-MLB16THESHOWHDDM_bg_1_2ee045c927f48b3b0bb30e604bceaec892b7b253.pkg"> MLB The Show 16 - Missing RAP?</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2006/NPUB30268_00/WRdSoFVCRqbKTSeVjhtkKSmTCHyXwwtxwyxvvvDRLDYqCFtYUtkfLQyUQAXKUTjWbTVwnPKsIhTsWxCwiAcOjoBNfweoNWhnBwqsm.pkg"> Modern Combat Domination - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80535_00/PIZyAOqZbjEULQdqPxkgqfRyqLYnTrVpThzsaRLhAqBQLBjfknaqvgwprgeXQXFWcVYRZqICZmKhyUbciYdTVpWkGsBBhmcpghBMf.pkg"> ModNation Racers</a>
<a href="http://zeus.dl.playstation.net/cdn/JP0035/NPJJ00137_00/PEDAwjqmIiarRsPYMveeDeFAayGxTauBVPHjvmjLJxyhlYzuQHdOpTrJnrZghYGSPDKCtXRNJAwFaKLAgAusuLcuALWRbPbBRzyQy.pkg"> Money Idol Exchanger (PSX)</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1010/NPUB30196_00/49kVch1Hn6jj7BUvNCe7FWVi5EqN8aQp3xkQrDSqTKacmV08TYxXxrB6UQadyXHCOaK0qiR8GF1jtScGELcGVEEtgfnJQxCCldSKF.pkg"> Monkey Island 2 Special Edition LeChucks Revenge - RAP not Required</a>

''', parse_mode='html',disable_web_page_preview=True,reply_markup=keyboard.lista_jogos)
            return True

        elif msg['data'] == 'MaP':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),'''• Manicomio Bot
<a href="http://zeus.dl.playstation.net/cdn/UP0177/NPUB30324_00/BAnRHYsElgKYJGtOlLtivmYMPbJbdzOHnXNYJzZUOTqbHTqkNyGZPoWgEQIeLruqnmedYDVdBuNxhxvrPInibiIaKXwMXskqmeUav.pkg"> Monster World 4</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0082/NPUB30345_00/XMVAvDgtwRduRGdWoKhPbqVsLnWkiVHqOWftLGQpEFYMIzarSqZXpCJsyedxuqwGyyhZHgXtGDsjofovELEJKzNjefqVgXeGDHiHr.pkg"> Moon Diver</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0017/NPUB30004_00/p2ouH2OhdRKdbnPN7TvppnPRsGq5WE97uaVu2BDCSNPoR4NOMuM1awyfYbLdWeXPleqUjCh5grgGDFlXTFLQjIItBlcAPTRoU3E95.pkg"> Mortal Kombat 2</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1018/NPUB30468_00/xchlzPIZKdZXOEpzkmKXoWIUfHXSOnqdYXrqPyzDQKrrvqpiyzUFCdNeMMPeOUqnnbeeJQERnZxdaadgLBjaxepTtTLZqWstPtitc.pkg"> Mortal Kombat Arcade Kollection</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0017/NPUB30004_00/cxrKu6N7EHiUhOuErGj7BaGuQv1t63eobWMMIHBOriOOntemw0bC4qftsC7eK954Q8X6lUQh62fwykFtvjaC8AgHhC9X7usU34AiK.pkg"> MORTAL KOMBAT II</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80499_00/buIy65dm2VBvJGWLobBVs6eCKXMqpjGmNuhMCrEnBuCsNY9RIQfwAiXdOECYtDnor3k4KBurtwqEJjcwWIvXRsJwDEcWNlfJaoSFa.pkg"> Motorstorm 3D Rift</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80661_00/siwasQNpJbHPiWNapHIqabLGZgOHNbAldTCKMirtuiqsTwAlfihmOOUZoiMwJzcCDGIkpRLeRNcMaIQhljerLfbsApjFYyjHkybAk.pkg"> Motorstorm Apocalypse</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80678_00/SUCXBQjCucjSNjwlmVGpitBrlzUnvVERqcitqvJXjvtpCBkPAcTPGSuUxOgwfGVWSujccgFDySpKEiXrhwomASrNQFaEkUOXVmZQk.pkg"> MotorStorm RC - Unlock/License by DLC</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4073/NPUB30099_00/OnVUUYjjVwd04EVONlWFacqV9OoggOsVxpe4uPwbFp4A8DhHb4GRwc3q0oLVsj2EkH9V8BHDo2O0seRkHMnJP2TY2jAsaIV5HBN0b.pkg"> Mushroom Wars</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0555/NPUB30255_00/ySvU6Lui7Oq2wdOBeBonihi3ELX3XxUe8SFJe52jp8YhR6lfih45Aq6IjuFgkDXsoFabnI6YwCQRpgdCHIEltuWs4A5kVkmKn1yKs.pkg"> My Aquarium</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0700/NPUB30086_00/jb3MLAjiE5fB0ajuT58X54fmhwXhyJqVQT8g0PfeY9w2RoqMksfYi596GRvc66AGXHaUxplhXg3RxsuMkVQiU6OQSB2HxbQrlOhfE.pkg"> Namco Museum Essentials</a>
<a href="http://ares.dl.playstation.net/cdn/UP8801/NPUB30129_00/PLLGR8H9t273lJJaA4sXhs8HIfRmY9UW1yhxTKQb9T18LX6tNwiIF8ycA1esrx23ryUVgKBVd8KLSkkebchjf3yXFIc9fAX2Kw1lb.pkg"> NBA 2k10 Drift Combine - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0325/NPUB30146_00/ACj3kUuAbGYeYBsrV7mKlpFFusIToG3rB0urByQVXURxdh13DAIRX5OnDH4nA0YtqRvNw9F4w5FRMkvCeUsy2HQNWg7kXthJXl34k.pkg"> NBA Unrivaled</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0576/NPUB30263_00/QICUvXvLXENjreqGPqDcArOOWUoTUSfYvLjRWRpEyknpzdpZypaWgcxVGSfWZQEBYneHYWyaUEbdgarDmOqDPWYyZWNxaiiVQkIEP.pkg"> NEOGEO Station - Alpha Mission 2</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0576/NPUB30261_00/XwBJZSjuYmFHxNnAMzFMKPiyFpZmkxZtleysjSORhvnAltfuZqqDTEGHavSHBoZFVsYgRbbaOCCMdZIkbNRFcKmgLYGLadxWJxPiz.pkg"> NEOGEO Station - Art of Fighting</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0576/NPUB30262_00/jOieEhuWwLGOdSFfObsoWzlRtiuMKtKLqztybBsLCUXjrhZgVsxMlhAvupRzDqKIDnlAQUYhetXRoHzmdtvkCYaWCvCBPsbqWUVRr.pkg"> NEOGEO Station - Baseball Stars Professional</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0576/NPUB30260_00/fECjlcyOUpsRbTiYTkqWzmjpDFKfKwgCBFCFPkvrbgReDMHYriwbgieRrUpFCNXOOaithDGWEfyIKwYahHKkpIpGYoOZrblSqKlmk.pkg"> NEOGEO Station - Fatal Fury</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0576/NPUB30266_00/GzskiMCDhdAMQtEkaXkDDBhxgSBjPoZncjeVUcFzBBzBoqUOHwLjTVLtxsWCoLztSrUCTmartyOTsBSdMUdmylcCwKaDVwaLZkoKf.pkg"> NEOGEO Station - King of Fighters 94</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0576/NPUB30257_00/RFVAhRSAxjUKXpXJecrxOgyfyNBCxshfuOrGnYdBxemUTicAXROMPTDLzEnjaLEkiLhAopLNDWPeYoOGpzHhqMrKarDWxtBOfcELn.pkg"> NEOGEO Station - League Bowling</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0576/NPUB30264_00/oDgpTBgIqNYHvsEyvdrzmstMxnqRISvncjJBmDntccjwCRyoXWauMiAgsSniifenQDjlZkqUHZHmQwInqOoXhphgGNwtTpIZNemKP.pkg"> NEOGEO Station - Magician Lord</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0576/NPUB30258_00/adKsVqlFkDDJebgVhaGCEKfuSTdeRgRWsRinKDXImDhrvkZcGeGkEKInrQhfKOGiqvKjbOpXsQdAhlpAyQvINVbqGdPBvkRiGelWR.pkg"> NEOGEO Station - Metal Slug</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0576/NPUB30265_00/mdvcuniPqScKPrelFgRozRJZuIekUlAWkusARUCbLxnvKPSLFHlenscjiXoHpQHWdSYmSuceJOkakXhQtlaRRZsvTogCoKKJUPNid.pkg"> NEOGEO Station - Samurai Showdown</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0576/NPUB30259_00/mTJvtXqCwwycTztEwqSBWjLoFKylOuhEMHuyDVzibMqhaGkNcYYoEejciGywxOaaaUcziZMGNhWjSOKYvzeqNRaZyWZHGEbQbenkf.pkg"> NEOGEO Station - Super Sidekicks</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0700/NPUB30032_00/tmcLc3eKrgnD3qX5Y8yjBSrnaYHWnFqtLa5N2YedfA42gPid5RTnvfGejiReea19I8XVCoOXdrhaE6Y9FVWAg6QOr75mt23W7XD2G.pkg"> Noby Noby Boy</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2001/NPUB30025_00/li0spWryQBDMkmtlP6ljQlsdaynodHtoqx1kcxfD3yNgXS5FJQ3b8eXNcutmE0L0M1EAIibdaLD6g61j19TmFcmUXqA5yQND3c7jB.pkg"> NovaStrike</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA80064_00/LLjHrv5xVed2xwuwTU6OrYplknFPn70EtKPG8yTnCTGXnH7BN093rA8LGXXljCHM1PNkPoqQJQbjeRscJsXtltVdvltHuPFes7GCA.pkg"> Nucleus - Unlock/License by DLC</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80319_00/bXfT0nnuC6KTRPpuAhWnlMvKHWPwlBeUhvM564AwmfF0hRflMIdoB4TUknhAMRCYHicsSTONX81aPiOqwcO4VTsEgOLLXmSH6xt8Y.pkg"> Numblast</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80129_00/j8862AbbYqGuntyRrEFNwKGiedmns2yE0xbea5pMmRnF3FitdIPKcA4uTojAH3RCLwT1VmSURIF3QKOG33UTyKgayL5ij52MFBOKN.pkg"> Operation Creature Feature</a>
<a href="http://ares.dl.playstation.net/cdn/UP0001/NPUB30163_00/GkIXuJAhsnFyHfAnWqoiJeFkSfyQDdPTBnRizLqachrTobsNUUHKrIdWCxUdCdKQtKiTUeqyVUpjjfLIdGaGpqYNYPovkFASxsFvz.pkg"> OUTLAND - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0700/NPUB30304_00/kr3NoQWKw28DeUOBPdFPc2hs3h90s6JP7OaJDWaA2RIVYwiBWLEDmFthv9OE2BALg6PK7D2kkpVqxJqeiW3fegsoMkFLM3fAL6GpA.pkg"> PAC-MAN Championship Edition DX - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80073_00/Kr8hlAE3HL5vMuiNAYxFhJxUkR7M5PrdRWMGVpFH8VxPA9RgcOn7TEV1qbkqG1s3dcgJLHHhqILm33XukGLLVwjcjohaX9pBwxgPq.pkg"> Pain</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0017/NPUA30073_00/jMTnWLxDIzVoYQbIlNztdLvCnBNhyYlMTJImZanyKyyJgdACzkOCpZmtCxufdwhhoFSQEdRVdXBKYqtuucMYNgNpsFKSkNNMOopks.pkg"> Payday - The Heist - Unlock/License by DLC</a>
<a href="http://ares.dl.playstation.net/cdn/UP0017/NPUA30005_00/NH9yQ2O2tBxGWmvArip9Cc8TEHdulfrSo5VMOnbdb3lWNVM29uC8pmfkVjjyaI51NOPhdHLAk2ysque8sJd9DeCa0gPdQxqoAhQgB.pkg"> Peggle - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4049/NPUB30043_00/lin1SdSPPIdEBCMQ0TtItDjPnge9bQYqslv5CIQNp9bGWLNirb4tAlf6VEGHMe5oehTUn9tjSIS3mUkvxLD9v8k4oBGORDPlP5GbD.pkg"> Penny Arcade Adventures On The Rain Slick Precipice of Darkness Episode One</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4049/NPUB30056_00/VEvL30nVFA40nJ3S777csR6v9KuRbRx9FwSGrHdO2qJw1tc4idg8lUrnxOn0Bua5enaVMNc1nGFGYjEnYXTcsFEmr2akFDDWgcSdd.pkg"> Penny Arcade Adventures On The Rain Slick Precipice of Darkness Episode Two</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4073/NPUB30110_00/AfChJJcLHQqooVikzYrPOEVVkdigKXlJuyCarsjPZjqFwreYRezqQXYDSCyQktVKpeLdAVAwdsKKxTnIjJVJiTRgZVQvGBkOLmaCQ.pkg"> Pinballistik</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80100_00/uVJWMEnycbBjMj7ggfIgDmnslGhmQA201QxDp2a9a7Vu8HmWXmmwdEnok0kHj2c68e89UyLtffw6mPQdT17cQ4WuP4pX1xLIXrERX.pkg"> PIXEL JUNK RACERS (DEMO) - RAP not Required</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA80538_00/QRFaWLZARrDIeeiLKAsMPNmGsBXjWacBTVRfpPRxBwqNMUjMALPDzcWHyXnWVlMWmuAWhDWlKLtkDvGootuEDveHpbeeAFhWmMdjP.pkg"> PixelJunk 4AM - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80160_00/iYXh0cPk234s4erUkTL0Y9yojvdxhC4yKx0bBF0Q5cn7DrMlC53ma9jVHidVHE4rkVAKReO4TBkk4KAW5Jyp7aKTMpAFPXOPvCcer.pkg"> PixelJunk Eden</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80108_00/n6w5uS0drx7V2vKMmJx9RfOIS91qs0FMtjDmjBJBX7PSio7aE7JdNwW8Gi7GFiHYnJwjB7GuxWahBbCX6gHTu5uO7DJN5JBKKlSX8.pkg"> PixelJunk Monsters</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80395_00/MJMfna9pYmVshfwCS8X6oe0BfLnHkBlFcOpBScIaLotA4jDAmxTRubk13xCugrYisjuNfYjqobEXnByRSMjQ7MkbTyufLqepOLgyv.pkg"> PixelJunk Racers 2nd Lap</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80253_00/efcETApKOgtBO2FVO9bV4s3r1LP6ipUXBUIQl3vsiG1NwGH4Y8ViWF2EbQnHsBIONuqoAvjweSHM90XQjoBRO40EPxQRSVCxTSRSy.pkg"> PixelJunk Shooter</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80396_00/sVxYNeUsqjgIBNnkMxHfETubtskwVURTbztlMwIhmTYveseWCiHVekCDOirbtmoFMDKErLYWFtcfdGrzsJMIjPZSxDQzcSRBRUyMe.pkg"> PixelJunk Shooter 2</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80091_00/PwxXciOrtMRfqOWJMeKR1Vi50hgQ43xWnEIKIXd98PMlpojW5k6TAqrgLQsRnF46OP23nUJU9WBiEhKQjRUDt1huWJ4ewY7E3xVv6.pkg"> Piyotama</a>
 
''', parse_mode='html',disable_web_page_preview=True,reply_markup=keyboard.lista_jogos)
            return True


        elif msg['data'] == 'PaR':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),'''• Manicomio Bot
<a href="http://zeus.dl.playstation.net/cdn/UP4042/NPUB30122_00/6NSFcbGflHAMCkBVps16fDw5XubuVExDVHOGbNXYy6RAwv8ALIvtSEIQyk361n38dmROax3qihUoOI0KK3XxNpeK6V2RDRv8INYQM.pkg"> Planet Minigolf</a>
<a href="http://ares.dl.playstation.net/cdn/UP0017/NPUA30059_00/iKsdyDdBEejDuZrONoLZlLskLksEFthWjGRYMGunzVEyOPKsXrGRZbWyHAAmLoHANOvnUfqeaOttBvsJEjPVyPSjuRMkbkcGLxEPm.pkg"> Plants VS Zombies - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80316_00/KExUTHpUOOnTCCRHhNkzDAhVrcQwXpAhFfDZTZCBcaGdwAzkpTcZDvKIOdsXRjPBkuyVWjeOvnsTTVIYShvMmnSZZCMDrCcsEWwWU.pkg"> PlayStation All-Stars Battle Royale</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80619_00/OVcMGknPyMmfOkVqpHfxGxJInxeBsjYFcsvvnVAjnNFHbrNFFxFnCoCniKZpQkPmPlbbLsuUAgTsCszdGYEEVosnHXLpPJwZsQFNv.pkg"> Playstation Move Heroes</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA80823_00/YTySjLzKgJYIXtdemeJCCzVCOdmIHMxBJxGuGvqowedGEEEBePuCSQmXtffVWOrKeTYOzfBBrvFLzVtDCWcaDRTPikCMYrNbZDJUq.pkg"> PlayStationMove Fitness - Unlock/License by DLC</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1021/NPUB30113_00/38jI7wrF3HoMgxMp5UhvOIBlcaAxDvfwUsgmKbIkVihNMIu8LE833RFnEeKK7cn5JgfQ9tFfFYuVMcrOT1AqhTbS92JY7el5NpHyK.pkg"> Polar Panic</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2019/NPUB30187_00/AhmFRS6J1MpAv1FakYOgWXgHTdUowfjKsV6gBbn20fPf6t4Tpf7aD0aGDIa07E7lP1W7hriAsyS5Ck3k9DM4aurBb1oOA7dhsuP8r.pkg"> Press Your Luck</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0001/NPUB30424_00/ZFBLFnNXGsKlFxYPOTdXYWhIZMsISkUeKaapCzZMraeYJRzzKCpoZdTUdlrjInrioRSMBMeSyxLqjLljfvbxkYykpWDfiXgERpZTS.pkg"> Prince of Persia</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0001/NPUB30303_00/4AnptOLokoT2jRCQbE17ajoX7l6JjAeFPXLcwB4h94qEWIJufVeoFYh09dEHbQ4ljRKSpOlL7HkBhW6rdWcYeq748OmlQxAAJLx65.pkg"> Prince of Persia - The Sands of Time</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0001/NPUB30387_00/aoPLwYrtYtsrXeCVDEaXfOOiYRwkUwhvRiyEbfgmgeiOgrphjXqUoMzvQzRegIloOjMCLoQCwqXPwHljZnEicqfSdSDVbRZXYeuRS.pkg"> Prince of Persia - The Two Thrones</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0001/NPUB30031_00/b6KmDC2rqImxGQnMG6j2EQWA6Mu6QUoMCf8MmSpPpC6hYB9jNo5vaOxLVjgcNl2JC7pJfkiJ6WCGcp0xTXQkoXRNRQkVscnPf6ep8.pkg"> Prince of Persia Classic</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0001/NPUB30388_00/YeYIeSpoJKqPMMrikAUvYuKHRWgOKBavrUbxAhNFTLCdPaPLdIGhTpZqWfFMAudbUjWdejRPvyvyEoKGqLEYVNgtERLctvMtpysPb.pkg"> Prince Of Persia Warrior Within</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0002/NPUB30389_00/XUhpTjaWsjYJbdzKgQUGzFQEhBwsybFhugsyBhnEUlDtxXSgCaZNhMEssZokuGuvIygmNjnfdimLOIpnvZBlcFdLEDnxRSRvXOfsF.pkg"> Prototype</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0101/NPUB30439_00/CTMkGMlNouUWeYQnNRBRvnibNbdvcUMysrprFTAFEWPMWbzFetuTIrGkGSugHaRkAKpCeICLYJGjtRAYVnRVZYROzfGsvwAYmCwEj.pkg"> Puddle - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80959_00/vuXlSLDRmywNwZZUpCJCqLjMOWqibqcpXyLZcynyjaNtodBKVhcXykBlIOtmafbe.pkg"> Pupeteer</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1082/NPUB30449_00/UAoaGpuZsnRgwWViwqJPOlSsWRRtFceUqGhUKASjXaaOFRFtDbelDoYkesnUBgWVWwxqUsZuhHYDiqTBPqNCfGGbDzJiocJomkOUG.pkg"> Pure</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30448_00/OOctahQvopsyTnQihTMzTHljpGibkvvqggUkBayTVUFSBGxeIblppTZNjCwHHjIkDiEcuTBYnyRoamAgoDvyXVTntPGmvaUAIYpiw.pkg"> Puzzle Agent</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0101/NPUB30076_00/3NFO5jiIEhUEVaX0rDE2li7plMqpfHKFgPIDwP2lwldjELxUb5eNYejCtsVWSSdROjhndSw5xOfO9ncAfkBKqBY7UPmyuBt05QGjQ.pkg"> Puzzle Chronicles</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0367/NPUB30041_00/XgRaOr969dGmiB6VNdBJ7WoWJ0fh4YOaHjxNINuVu6nNLhmDf7FdHQvfw0dDedm663W6TXO7CFwgQwKmHTSQabuGIyDEUjS3KYoPB.pkg"> Puzzle Quest - Challenge of the Warlords</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0367/NPUB30072_00/rF7tVeXs7jeiCPP2cRLiY0lIybOwoPcCyuuB1xBV5Xi6IuGdluFYkGOxSyE0vuUWKKiKE8jLY3bq4XCNjpAunLD6dEENli6teUmtX.pkg"> Puzzle Quest Galactrix</a>
<a href="http://ares.dl.playstation.net/cdn/UP0325/NPUB30125_00/9TP6KA070LhUbswsFl1QeBXrKQ82AMCrN91quhYRMdgBw8XspyKsLDbhSsJGIojrGIPcYId4L1fqtn2m63prDSgdQ5su9qfDbd5k4.pkg"> Puzzlegeddon - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0017/NPUB30010_00/AODHjt6YAjUySclreB3f22HvdynShRmDNQUL8bB2l3c6JbMkohngQ9Jeg8TYfE2vh7VP1aaspMMyfRt8pVlp4shslaonsSRrqgW7Q.pkg"> Q Bert</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80217_00/5PMpnykoLYafbA9fW4SJiUbugdQWuJ6AieEpKD6dJyj85ntjLPK7U5b9p4Oxa8cgmqe1u2tUriKKkJkqsXJnUhrJWdUISwEwXXXKr.pkg"> Rag Doll Kung Fu: Fists of Plastic</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80719_00/ngzXLjtxHoYtNDLuvdJNHkrIxAJZhnrYGXCnCmFmTiCKLcxlwMwccWozyUMItggZ.pkg"> Rain</a>
<a href="http://ares.dl.playstation.net/cdn/UP2005/NPUB30434_00/EcrJIGQMFoYXSAwWyvzMptiroLVGaApcDBvmejZxrCoqJuRCgXrzTuvgEqowucxWaHXQdFwZXhSHgLljjuJqDNyYtrRBDJADUwvIo.pkg"> Rainbow Moon - Unlock/License by DLC</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0017/NPUB30003_00/JnAaAksWBk9Lryk2yldr1kXFlTSE3o4rBOgKX93bE3C4icEcNfWX5Ok0S9xXleMHFDbYJJyH8SkbJ2JUvg5G9Buk5d7GiTUx3v7NB.pkg"> Rampage World Tour</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80145_00/W6YdyqW4xIHnlcXYt8EE6HDtt0TB97BGCV3jkMy79vUw2OorUup4AL1HagbRavt78tGp6mK3YknM7FjSWm8NHMjASSwaSF9DpG8rA.pkg"> Ratchet &amp; Clank Future - Quest For Booty</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80966_00/phbiyMKQbUdwqUUzKfUmmvDirvcfuQhXDBXBgJGAKMDKILXFUskIWtMKMzsBAfhXtopGIKPbWCulXfYfRXFeCwdXQHyXmexCJsfZy.pkg"> Ratchet &amp; Clank: A Crack in Time</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA80642_00/jAYYfKWKOYkRMayLgrPAtrElcCckCXhiAsfzDfESMJdNgNyNqRALKdavdBBqGjJECJqGEVjgIbJgDORrQruMMgvOhUAFRESoRmJxC.pkg"> Ratchet and Clank - Full Frontal Assault - Unlock/License by DLC</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80908_00/TaQKuXxmZckUeWtowWPzjNzaEhmhpDshbquRUpnUlyQXQNXUbDXjYRIoxnhIRBEd.pkg"> Ratchet and Clank - Into the Nexus</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80644_00/fdniuoKvVCZYXXieqDAZHRjSyuHybeczfdifbMYtUGvzADHhqNMWAEoGhhRhXeHaEinXsvEuVSPVqPqWYeBpfnPuplaQBPNilArwe.pkg"> Ratchet and Clank 2: Going Commando HD</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80645_00/MwePLXokUtnogOibwwaIspMTxNWNilGlvfKanXpIlUrlMyAtLGFwRTLhsWtYcSKqjxxddLoeFmldCURmXynOvHaabEqoQieVJkNYB.pkg"> Ratchet and Clank 3: Up Your Arsenal HD</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80695_00/aEsftNftMEGiFhSmskznHzIiRiivXhNwkxqRYmLnfuLvzgYxBdHoeriUXGPrlMlsNSVokwdnOcDxWKKATrdTekwFFjNaKZiFAHsZy.pkg"> Ratchet And Clank All 4 One</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80643_00/duHcFKPmDHwaYLWVsqtKmaEAnEwBatEIWXiPmuwuLOtkxcIHDlMarJRHQZbgSlQsBxGXHPNQeOWEoSMPmrKpddpIwBMRCLDWiVqxg.pkg"> Ratchet and Clank HD</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80646_00/OxtXcotLtxhmgvLlJWevAkkMXGCWkXFrNUOckbtpNoxRqEnmmCoPnNNlwNhYEsOtStEemydQDAmXAZcKlXLtJOSawMoOyeOvptSfa.pkg"> Ratchet Deadlocked HD</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1024/NPUB30142_00/AJa0NJhN9oNj6F0b4cc1E7qniK5rLywlhi64cRGn8ilQQaSIKsQFnVvLANvdquEn8f6Joioh7fhn3Fbg9HAjhiUjAqql9OHt5GiEH.pkg"> Record of Agarest War</a>
<a href="http://ares.dl.playstation.net/cdn/UP1002/NPUB30030_00/OTponHyEj6xuBoAetRgwIaUQPITtaUjh2J5IixTtn0eiYqeuS8Vwl1f8r5Y0Ji5nqnvh4t8bFk2eovtVUM7FamraPiQ0YXp7VOxtL.pkg"> Red Baron - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1005/NPUB30296_00/DwrovatfHopBtzKtxZzKagNLwTIDLAjvzTDpqjplAKiPrUugDrquRJbHyzXkSNheqxKXzxrvPbTVUwQeXryqhbgdacQcdpWwZIDmE.pkg"> Red Faction Battlegrounds</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1005/NPUB30295_00/0WT2nTTRTLbDdvO6KHSIfkRUXrMMVFvjKJWPUAphA4ySN3NW08XFvhx9bDrcUdtwcdWWLXXFtjgrxtQMqWqgf8dwQPeJ7dQSm0OBu.pkg"> Red Faction Guerilla</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4295/NPUB30426_00/kwjLoOZAReWudlchwIvTAlMnieZNerTnYlXjxztETKoYlMuMQUHbSPjhfPAzOrzplIGebAdbShwmwEVgLwGfRTXrXBQqDzOzDngUO.pkg"> Red Johnsons Chronicles</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0177/NPUB30406_00/wxRdJcnCESbfqVOGWXCyzyeLBWWWHafawHJlXCWtHbaKvZzdMlGXKvziMLTWDGfCVPXFPoPShehPMQIOIzJDiyPQIZBRTrWxnHvsV.pkg"> Renegade Ops - Unlock/License by DLC</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0102/NPUB30312_00/CSIkFNzjvhaZJlMYvXUkmAiNmAwVYNBPAGRYZeoMdRtCQdRLRmrKtgbalIWXBHvLMZXrsZmYbfMZvwBRUfopkgyPhyatgRrjYmWjk.pkg"> Resident Evil 4 HD</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0102/NPUB30467_00/KvrkPgurTEFxKzLWQAZVdwRwaFWDIGHcChOEfXhrJcBKmPmROiyHtlKcCDYzuKkfFsCZeHWJNUKIJlARgNgKvYvqyOEQVyIaGDIbs.pkg"> Resident Evil Code - Veronica X</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80900_00/NOHUiVRJnqKnwQAMEkKoWHUJlZigHDoCiCkJhUOmgLnnKtKEIVFvvVLbWEcpiAer.pkg"> RESOGUN</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2036/NPUB30280_00/bWtHYpEXNoVtISmjLEkNxMFVVEuNrlWIeLYSwlronLZhlLfNTUnaNhieehASiyZyzMGmbEsXZDFJfeBHSLzCfKgHNlNzQIszIbmQc.pkg"> Retro Grade - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0017/NPUA30016_00/MIBXvTAVObJyihbQEMCEQfg0j33ha2mlFOhQ7s10iYPAKfbvAtlRq2FdMqgNa4AN2CwFyHUngykprfRLI20Ww5SvcUj2Ok6cfHYae.pkg"> Revenge of the Wounded Dragons</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2016/NPUB30172_00/SquJhxiRTdxJRyRZlpuawLSDcHKOmJPFvfJNFtEPvPHbkEFKQgJxcLBZskLhtDVaPxDiAccOPDVKqvTaILMctQfATEBkLhKOEHsGf.pkg"> Ricochet HD - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0700/NPUB30457_00/HMNgUwAnjFJPNEPcYdNkMUgGIQOSyvnrARNKmqQrUdJIOUjEuxjRBFEJRLJqaWlDElEjdJVDvuSyWwBSvUHtIPzScTykCoRIGAqOE.pkg"> Ridge Racer 7 3D</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30391_00/SODmSgIcudTthTDfvZacbtAeofkxeGsWChuSCSVuWbOAXrCjROKRjalNMBduqzVCjBFIsrbZznokpLOvIqyyifFswXnAGeRISwxmo.pkg"> Risk Factions - RAP not Required</a>

''', parse_mode='html',disable_web_page_preview=True,reply_markup=keyboard.lista_jogos)
            return True

        elif msg['data'] == 'RaS':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),'''• Manicomio Bot
<a href="http://ares.dl.playstation.net/cdn/UP0017/NPUA30061_00/hkiNXzOQvXbKnEQiWrHImTLNZwAwxCwizmhvjhwcMtXfCbKPHgSzHeVLUoDdNtrsgsVjRHnjrqSgpQUeXeKjbNvDaDRdqIeJQGlbe.pkg"> Rochard - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0005/NPUB30332_00/VrJQZijMYmwSfhkuqNjFBosEVyTrRBgYzcDkimWEQzrLfhgvSEDZBKsfXkuyJjdVHcIniiRUjvBJvfnVnTjZtzHUwXUXXxsxrfDmD.pkg"> Rock of Ages - RAP not Required</a>
<a href="http://ares.dl.playstation.net/cdn/UP0101/NPUB30123_00/S4No0pFa8NHETU2TD8lsBVMMDKbr1AKmSONTe59l7W1UcxWHOvJaWURpJdUl5Rc3r2CyYMiRLjiKA2jq61QdpMMc11kkbQoKxxVug.pkg"> Rocket Knight - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0102/NPUB30018_00/BI2u5bFr52WWRo7DfF3avtSMvuglb52xmdwukYBkFqyf36jglBT3yLidoHYJEWnoWnOw8yIKXjv7tvorAj6fVsFLPvmPbXGhFkdoH.pkg"> Rocketmen: Axis Of Evil</a>
<a href="http://ares.dl.playstation.net/cdn/UP0101/NPUB30112_00/ggfvBOZDpPBgduWoZIwcikkHvWZavrlByJlsWYPqxgnmMylBQlPLsESSyhLgqyfkbiLWWgSyDvPeZPJAHdFfhdUvswMeMjIzEXVBP.pkg"> Rush N Attack - Ex-Patriot - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80479_00/WKHAroznqHIwLdlRJmkvsBCCXBwxENCqgVprAPphQKeaNSlGxEcbZpFIHnuKwLWYlTSixWpYwhWAevgcIqCkXzwgbUYpEymsVCboi.pkg"> Sackboys Prehistoric Moves</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30185_00/2KsftQkXQmGfA6qMSJ2uiEb8t7uaPyL1gQC72lhot1HA5GRdaQEuWOamC2jynGSH1iJjcab8FmvwCq3hSmgVl8WbUWsHwyEEdTBf7.pkg"> Sam and Max - The Devils Playhouse - Episode 1 - Unlock/License by DLC</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30219_00/UbpQc9DjMwfWCOlAIchh4N7Gy2BCGUy31HU35QaxkICAmCkD6EpCKlqA2qhutjpGaRQMPK5AG5E3K6TNNUH9y4v1YgGu4lKDrl8Fr.pkg"> Sam and Max - The Devils Playhouse - Episode 2</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30220_00/QWfXBKbMvsf4trV32AptcXsJDS0LoTV8YnhPaw5oJBOasFNhuKPgFvF4qC74cqIhswvSj38fIIK72vBpcCH2w6So4OccEvNIK9Sea.pkg"> Sam and Max - The Devils Playhouse - Episode 3</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30221_00/E12B88K1mTIq4r7f1ie9mg7wfBWnuwrVBinDsSCjYHa41iRkAylW4RkJ1HphnBRmfYlJWbeaFUikpvVdwv9cFhNyMs8iJfTt6vgRa.pkg"> Sam and Max - The Devils Playhouse - Episode 4</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30222_00/XD9eoEL1qqA6cXbcn5DVOWAS8OlpMQFccPnAuyaMhU32yhAgR7IgTbMqf2WepVgSBhcE9FwHf0Roh3H3KTBrsPuh5kiX1PtuxTmem.pkg"> Sam and Max - The Devils Playhouse - Episode 5</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80228_00/PhEpsMBgKUmdguyoSwT1hX8YIK4HJaG6x3oKSb9N9pnifGWMiOWxsGfSei3sXHd3WPPkL9GLF0SVlr8Vv3qnkS4nOArNKbve1g3UL.pkg"> Savage Moon</a>
<a href="http://ares.dl.playstation.net/cdn/UP0001/NPUB30162_00/244L2uq6x6VmR9KMgGbAW8Ecc6xeTUo5W2fM7LmW7N7NA7wf58VX9HYU08U7SE9FxTAPH3MRxu7xFpXC8OlodCMj7EMsrGUwY2mQ0.pkg"> Scott Pilgrim vs The World - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2024/NPUB30161_00/bj6T95A3ubt7b7GxuIAPyq6mwV928Kqc2nFxw8l27m1qjICmN8Tx8IUULrLNy8I7GDxW3XevcByIBeNULj5Vh9tt1ThTfvgPBEWb5.pkg"> Section 8 - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2024/NPUB30381_00/KahdEcQwXTZIfkreDkfjDCMFHZQSjTDMNywffjwdbGYcmBniamXurAQzRRsFBRDDnZkywujYHLDAWAgurzXWGXxInuYTplrYUvSsm.pkg"> Section 8 Prejudice - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0177/NPUB30459_00/CMeIqdYELRDydwRBUySjipGTNObdOPsxhuHlTUeCRzbljcJHCUogoWtatlsuxuTfvZekbtGXYpaBLjmNtSfLWLotnWVPfKUInLgfo.pkg"> SEGA Classics - Altered Beast</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0177/NPUB30441_00/nKZtdzxZtJniwEyKrdJVgUJjgTcBQBXPrSquXESmnxYkuMEgjmedjiDDqBKpDpfguPjjVpnEZoOnKEVkjGxlGthFBsARSiSjsYAhl.pkg"> SEGA Classics - Golden Axe I</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0177/NPUB30375_00/PAQaJNooPjMWrqCFWzpmyrZDOGxFjktBRQTdIPuEcXNifRIFDNuiXXcXECBhKFUYnvnVmOmJiNrPMLYbZgVbWlMRlvhYYuuaNpOmB.pkg"> Sega Rally Online Arcade</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80677_00/pYiXbhrFscKsTrYsXNFdOyRVitlcPeqlQRNyrLcLbhkKPfLNyrpvbcTBmNpYJvwdRZRuhXneEIOsaqBtNRwZeWsYKmYgZmkZmWDOj.pkg"> Shadow of the Collossus HD</a>
<a href="http://ares.dl.playstation.net/cdn/UP0006/NPUB30232_00/yjhybkSNkhVP9C2YgfEp2AcfT2fHm9sG5wu49Q0gCOsXBcWJnyiqDUsUcTon0r8a6mbYKXKStXNRf5SpjgSRh3iLEfDhf4twYxfv3.pkg"> Shank - Missing RAP?</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4051/NPUB30091_00/I9MADsQHjro5mdWKHhsNrgHmFBGcwi6CWpWdnoHheCcXYq5lPfsWbfhe2S7lCbafFMUAQGQLiFjg1TWssBtvLGukcMSJse674PNdO.pkg"> Shatter</a>
<a href="http://ares.dl.playstation.net/cdn/UP0017/NPUA30066_00/ipuYHvINIzpoVwGwjZyCBEaFDFMgAQBGOuxLKGtgDcomNnJTgTteuwbJYKYUiVZRPExdYCkytwSTAZdyGASgTZWAofuSOEZxpkkAG.pkg"> Sideway New York - RAP not Required</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA80756_00/UP9000-NPUA80756_00-SINGSTARPS3V0100_bg_1_05c45a2cd6538f30086d6690d4d4f6b424150ed7.pkg"> SingStar - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80136_00/KV6dkccdIuIc0JxuqhYlXTr1mUf4hTw1bhYDxS4QpLGPgrPwYk4p27dcXOSDAaTBvUKufFgxACi8rFFuukfiQf3UCXeWI82RY1Fbi.pkg"> Siren - Blood Curse Episode 1</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2004/NPUB30144_00/H3OCARPw28JlAAJhso3GP96lJP7csDnUyXsyhFWmjffE58sd3oibIFFFx6GK9BSu2OA50vfyDVgulSbIS5wM9eQg1bFF1XRQwcISh.pkg"> Sky Fighter - Unlock/License by DLC</a>
<a href="http://ares.dl.playstation.net/cdn/UP0017/NPUA30060_00/qsMrCCrPcjxntuDHHFUXukZiEEyAJaWmoRwjVhZGgprIvAIlLzxxXhzAOrvkZhJCVlkTxEVVLIRISzqgDIPrjdSwZKVeEMDKVyjFm.pkg"> Slam Bolt Scrappers - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80664_00/dOKcnXSYrKyEedLNcgxQUiEAoHnveWinOXbBpTTVRqVwjUwGJYfSRhmJBnuJuKxLvyEbNiiGlnlACzqeNIAAJYYxWmdXSQLJmHpvR.pkg"> Sly 2: Band of Thieves</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80665_00/BoBVoeuCjPDsFrZUzHjGtAxyFtqkOcOJLBaDvCYXFfqJhBnlPFQkNdnqzjYzkWLUBCnEaBFIRyiNjwTuUWRGTbqmjfkqRKzQKTGAc.pkg"> Sly 3:Honor Among Thieves</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80875_00/CdOmSDsObJsJAjzTsePkRhKOiRiQlScNktnOeOGdDrmIVXKDXNfKrVPAVVkvWAOqtEbFkfmkxyqaevbmkCFddTVyNCaNfzXVyjepZ.pkg"> Sly Cooper - Thieves in Time</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80663_00/zXgKXJZqpwpnBEbZWPzMjaeTWhwlhFiQxDURvGbiNdRtSZvOcUdimlBPgZahjSeWWEFfEjvjjNTAxkMIwNmVLoTswXUVdvkvylVyG.pkg"> Sly Cooper and the Thievius Raccoounus</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2004/NPUB30097_00/Exf8DRDqvhVSwJNCGduvxl6qSDioWwRPJVY1IuhkN876CIItFYsQLTTvDPEltIDmwoG1biJc70eOYsiIPXS98MQ7UL5kWjIQvMAv1.pkg"> Smash Cars</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA80072_00/Q49C5GaOLp2dES3L0jJk9NmeAF9t3jmlsysIeTmVsC5JxLCO8RM82j1QdTns5gRYOt24fnyB7qPSl8j5VoYIG2irHNlqjQTsRqKln.pkg"> Snakeball - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2005/NPUB30039_00/csN6b3D04pR5KeQEowUQ7dMvHsDFbt0cvCSdcqGvCNj9BD4uLs073naCRwOBEK1MDqcEkgeE97cgsok0WRXpfhMOFGHHpJL3r169f.pkg"> Soldner-X Himmelssturmer</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2005/NPUB30105_00/luYMuIdBW4kgpdAyAthexBy2s6hYfI6NHqahUXA3xPjPnCCxcKuX11VKlK0D1sGTTdo3Qn8CNd1FkvtvW3R6uUbLJdHfdRafJdRd2.pkg"> Soldner-X2 Final Prototype</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0177/NPUB30442_00/yesLlobfRUYrPgotrXdDSJkwAGjiQxMdkWCueZENjxBqMahNGzgKulTeLHJRvmBcvFhdkKsdTciVlfjGDBsWUYDWLyEeORaOIFbQC.pkg"> Sonic - The Hedgehog</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0177/NPUB30443_00/HtyNVjpKrPKNEtwhvpvwZqEEIWSetnXIOnnZAFiyTNpGQIVphWROtpDkqvVymZChrDYhsoPNuGRhbLxsgMveXJGKYsmWMSiSJRvGR.pkg"> Sonic - The Hedgehog 2</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0177/NPUB30249_00/3iv1aHbMFk8X3Yba1NYwlmQi7yaROrPVeKq5bP3bnHMyO6Ot2dcDKaxDvvEtO4i72LtMvQCJNEyWXBpBsp10NAO7gHYxQn2FMAqre.pkg"> Sonic Adventure</a>
<a href="http://ares.dl.playstation.net/cdn/UP0177/NPUB30127_00/AFf5lLpuAPl8WkUyVG0SjLjT8CLngvememrkNiWLQpB1sMmhYAnp3sNVF06QOSEvjWKlg0hCrq1PbcKoJ2O41nCF07x5Bf7Swap2e.pkg"> Sonic The Hedgehog 4 Episode 1 - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80796_00/DyVkpSqESDlZJtvwAViuiYjYhNquljFluXNaotNPLfdDNTOhYZHqnPeKuuhClTiYyjuDWcWwUBsQgjGXGhiMdclMVzKnQDVoCrEtt.pkg"> Sorcery</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80543_00/gnEKgBzFbFwdHaouJuihVyJVDGXbvScDfNvkBCwiwReBFqYsteMrFsaHUfWHweXOfBsrNkYwpYMDluFqMwKhRdUhJLQNjgMkypdHG.pkg"> Sound Shapes</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2043/NPUB30386_00/REVEVjrUxOeWQuzkAcTTiaSwVNywTzDaOYWKNcEerGWCYuCeoHuxENqCjpIZmGMeWSbyEtUFSpCsyiHoqTnKOqouJazZivboiCguG.pkg"> Space Ace</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0177/NPUB30353_00/dosfXnxEhdVLYFZJdZGkxXIeGIPOdRBWEERkpbsMLOZBwhXWShGgfAgLLxoPQZsoLDRzAcejZgKLKTOwtynItIZZcXCIXJAfekXau.pkg"> Space Channel 5 Part 2</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0082/NPUB30305_00/DCPKEkfW4Pq4dllOWujYd5A3NxSU4hwYLJrFsCckDtBgAj4DOcvNbG8AEKdT821fYwA8dvxB2lrlMNRP0aoTlIm4TmM18MNhgOBrt.pkg"> Space Invaders Infinity Gene</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30310_00/sgUtLLPVxugOQhnFlkxaSWLoLktUZzypoIeacqWLfIWvkpVQyOnNUdDpyngOmjDrbCVMZaVLynJCXvMEFTgBYtaETKgUgtjmpsghf.pkg"> Spare Parts - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2038/NPUB30152_00/3qBFPANM0xO78mPaCRQ99vFiEJFYocVmdtTtKK4onptlQtdA7wXvYcBdmotYHThn4LMCl5SWbyrw11sNbObtyVFVYkiSiaaTbNWCb.pkg"> Spelunker HD</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1082/NPUB30450_00/fUgAFMvAQxxDiHoYcktsTvtvOOEADZxSohrCvgFjqVMRSANnFQmuTxYPNltkuRDzMfeBqSWlOwHqYCgepOrAmMJpBCuWRuYSnEJfa.pkg"> Split Second</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80670_00/CPTSHmRHWFKYvkvPfryCtnoUcmctILHXklOmVXxjrdNutPzUXcCuCgKsJceqpvOberjhjWWZwCJEbbUQKOuLSXpSkxPNYOgvKoFZv.pkg"> Sports Champions</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80802_00/iykriDccWEkXeGpkcBFMHJKBYSJQgUROcboGVHRHsgdavYspcrXhXqxemIKACaLscajRasJqCgEkintyGQNXfVbhvYmsxgjCKlKFd.pkg"> Sports Champions 2</a>
<a href="http://ares.dl.playstation.net/cdn/UP1005/NPUB30290_00/IwgMqfuhkTFTYFcfHlpnGHHxPUbzGycwxqIhNstnFbzPZTTRixGLPSIIBtmqfFibdcrqYVqeUeYgoaRnXjyoYsuHgcukVrWhlZNaC.pkg"> Stacking - RAP not Required</a>
                
''', parse_mode='html',disable_web_page_preview=True,reply_markup=keyboard.lista_jogos)
            return True






        elif msg['data'] == 'SaT':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),'''• Manicomio Bot
<a href="http://zeus.dl.playstation.net/cdn/UP0182/NPUB30420_00/WCEVDRzDygeQfzXWNOmRuqJElUyFIGLdIwITHNkTqImOVpkVgfkTxQDAvbVYUooOfoBVtZoHGRnfkffRpRjOnNJQzxogFsvbqGdfR.pkg"> Star Raiders - RAP not Required</a>
<a href="http://ares.dl.playstation.net/cdn/UP2017/NPUB30084_00/Fx8GYkV8RfedXaUVY2YedRTcVw1P0qvBLleUXKH7yb1LRGvVw9DLJctFjPBQEAi51CFPheaPEh0Iggbq7UPcQWDAi5rfoy850Ahvq.pkg"> Star Trek - D A C - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4101/NPUB30403_00/rtvFtnGRUuSJynGYwjKzMJgznTgHQdBJcvapBUUmmkgQrCMJjpGvuyeyyWCzyCCuYrFexzTCAUXsTGCXupjEUmwNowudGogMovvqy.pkg"> Stardrone</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80812_00/akkzQsccHTcuAFkiPkCIKYScNnZAyqBtbethLfMCsThYDpCUtsWqNmlvzAkOuxBMGIwqAuZasmMVOIESRYCyFVKDkKmSDbhuwdVaX.pkg"> Starhawk Solo Campaign</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1026/NPUB30210_00/NcyThYBuAIcjSTRmyPTVtdSoxWlHAtwMINwmcbSMrZEVAtpoyvbfLvAGfRsxoZhG.pkg"> Storm - RAP not Required</a>
<a href="http://ares.dl.playstation.net/cdn/UP0102/NPUB30301_00/FCAqiVNFQOTDYkcxiIbgHEWQEDcjTxxOiWoREQKbEVdcORPPNVBhBdKVuywydjYPfSRshCRrvpCzCZjRHALSFPAjInCHDqsXMaHPT.pkg"> Street Fighter III: Third Strike Online Edition - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0177/NPUB30444_00/NxGQgTEvzVwmvdaodTAuekKOyKHGtkQKThPcSJooCuWmSfqefCOmehHFRAVRjhEQUmdHIiouLWtiAiSZIBuTftTydVPCLlfiXUalt.pkg"> Streets of Rage 2</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30395_00/QkonyFYTYaTdpnZLCEnIzsFPwfYQWiSIGnqTQXmhnhlEHNYaGlTgtGLfvcxHfegRuvOQHmynjacvwsMTvtTDOmodhXwDumGJuoNEw.pkg"> StrongBad's Cool Game For Attractive People - Episode 1: Homestar Ruiner</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30396_00/jgnGFBgYkxfqVmqeilClASxIOIdAkFxerLQFYSKTIzKDBGpdcamDyZzMqehqwNvNWPgOmmAjZpkYwgqPxHewfHnmqPlgHotLLEfQT.pkg"> StrongBad's Cool Game For Attractive People - Episode 2: StrongBadia The Free</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30397_00/WHKPNqKxVCxxpUauhDDRdrZElkpJqPDzyWBQECCcyeJiDZaeFlnFeZEfzdJtuXuBzeONqLbSYagFuwQEhekEvYbHmIhcDPNrNQAvc.pkg"> StrongBad's Cool Game For Attractive People - Episode 3: Baddest of the Bands</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30193_00/uhEuhfTalhhXlMkOkJBxamoxBIenWfHWMIBFKeeGqCOaBfSDRLPEvNwrBkbxsqjyFCJljDLPgDAPsGdvNYUHWMqrmMYVNKczlTfIr.pkg"> StrongBad's Cool Game For Attractive People - Episode 4: Dangeresque 3</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30398_00/JFmKpJHvJRpxDHJMDtpaggYJcNwcaDchlMnJOPZHrPJelzBRUbvMVytfnsxzyAUwRkdKJgsCwSxXfvUpCeBKsWkLdxeCChjjgIEME.pkg"> StrongBad's Cool Game For Attractive People - Episode 5: 8 Bit Is Enough</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0177/NPUB30326_00/YyUOhRUGIOOkdOIkRfTJgCRMEtrCgxLslOZuJcGnWsCncomtzLVdpyyKsVpqMOBTVcMdMjpkIvWiBPtQqTsrWqLcTZxDnQoljXFWt.pkg"> Super Hang-On</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0102/NPUB30017_00/xEL2OJAIegkrPdSbcac3snaGwBJiPeP3iPqSaUb2vaVTuMJICtFEgpVhCRP8A1qtLbYO6biuJAylGM8cUqWhAYE8SRio7b8K4r9vO.pkg"> Super Puzzle Fighter 2 TURBO HD REMIX</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80063_00/SpsXb5K15r6vv5uGgv5CO2a1gYGTrDjICkU5gCrH1qb4jBKbnJntrWv9slD6eTIcaggqtdGutFgOWDkBw5WMUjyoOq8pUmFg2X3Mp.pkg"> Super Rub A Dub</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2028/NPUB30148_00/j7Ak1vBT7uvIQ5bsCe7MSPhcpsPnP7OyFdXjH8baP2JL4mDQjx7faPBJ3LsRYPJ8lAumPy9D6OOs19NqkIHn6XWEPtSn8eSJEcVwe.pkg"> Super Stacker Party</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80068_00/iu4IyrmdR1cO0eSO49kOlB6LkHhJon8ED8k5uHyk1Kt3bIcN8338rCfXKM4Fc3Qq0fsNmYnSX0OUc91yq9tqFIgj7XVNuWvySFSU2.pkg"> SUPER STARDUST HD</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4003/NPUB30338_00/2i7VSSXcrTN5mEAAW6jKTuHgjFlU7L9Os3nfMBD3wfaWbLsGocqiGuD4TE3yfpUH4katI52Y7VefcjOJqLx8F873D79W25Y9hN3K8.pkg"> Super Stars V8 Racing</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0102/NPUB30034_00/CiQskOTvlMKp5wjwlNexv4NJCRvO7wSD2msPM4XIIbcnCpvebsvTbI7X9keNBPOxjGCSmmg5XSVPDM54K62wfvgEpC6CnV0u8ky6R.pkg"> Super Street Fighter II HD Remix</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2002/NPUB30035_00/8332ldcBhpH1thTO0VKeQSBMSTrv28YSHkj2Rp9Mms9Mqlbtt4UA2aruxjxMpUE2GQe1FpWu3hkVRirYFLHtUXU8HOM27jh1rDIMk.pkg"> Supersonic Acrobatic Rocket - Powered Battle Cars</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4002/NPUB30346_00/iRQdlZNOoRwOnrwKmKPUZOjegAnGVfKrZbYRitWVDFhYVbhAZnAsbxXHzcnRGAwhqqdewVbzDZsJPADWyCEHpcwvpuTQFXIEQhbLy.pkg"> Swarm - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0017/NPUA30013_00/jb3vKOF8tw3wfUIePyVQvmhswRRjH8fKMFbDfh7DAS53QlpVCoa9tuLYscxGBBPgpr435MsRM6laTT9Ri2GQaaMRMOCKgBNi26aw7.pkg"> Switchball</a>
<a href="http://ares.dl.playstation.net/cdn/UP0017/NPUA30035_00/PAdTIUBaOMC3f8gjWBhWjMQ8RU53N436sMrkVxwNCw7fOkS5DERthvcNqYYfdC5x9MtB0C6m62jc4Tpktsd4ma4JjEahWPPKanNRH.pkg"> Swords and Soldiers - RAP not Required</a>
<a href="http://ares.dl.playstation.net/cdn/UP2045/NPUB30311_00/CJnDjZIcIPWbxfalwceSRIEYMDjhpNjUnFCCpYqTdvUDbvkokxCiLSNTRDrHcnNCaAQuPtkfScqrVPpUPuDJQNuhUgqUkOGCYttaQ.pkg"> Tales From Space - About a Blob - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30283_00/7mBId0rdK37rcFIceAljHUukpWl0hl5CcruPbjBmKEo7hargXO6fkq5aLTxTKuISRqor7qaQpgcfsd8eHgF4ach5J3CJWwT57ys1D.pkg"> Tales of Monkey Island - Chapter 1 - Unlock/License by DLC</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30284_00/k1rdUJ8MGObLvvKgdbY7SbQKE6JwngNSvU7rK6kXvF7HV0XVOp0J396d1rAKjhBrwYYTHtHW3GioCpeNkCjU2rmCrEFcLMeG4NR1r.pkg"> Tales of Monkey Island - Chapter 2</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30285_00/w163BbcInNyWxmgxWxNvQFap836hSUdaUgEi9JaUvfLfRlAtwvmMjlxvJpeDqoqosPQDfRbvKUoVtU7LAvX8r712SWAbpJXk5sI8R.pkg"> Tales of Monkey Island - Chapter 3</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30286_00/i9Ff1tSI19EuRi02jwfhrP1nmABrRxobqViPSQ2kknYOSKiCSUmuE2eaLwkjpgihrfam92x9FOxHULfuFfCxk5tfaHDyFUkV70cKl.pkg"> Tales of Monkey Island - Chapter 4</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30287_00/UcSJ0tRCy1HbH9vrKhtAdSy9XSgWxiKKQfsvN9DCchJYrdYpyUI7NSE36wuD87J2jBfVrNQT6GSe3pO51LcHMrLGcT93KcbjnYsr4.pkg"> Tales of Monkey Island - Chapter 5</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2006/NPUB30154_00/NxIt3byadTla6rxS4yjbMFD8S3sjn8sXFsYVtcMpiAbokL7YF4woutM0rD8fQUPY6nCcFV67JcHNnvJBYKS4L2YrXi7Ml66vix3Uq.pkg"> Tank Battles - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4108/NPUB30243_00/wyUVHN6CGWDYoa5f83SAAroSTrbCrvL3cQowgJOQlO6SnJoKLvG9FHlvr43DQFbNsty146ktv9BdHqbUWvHjdWfnlbiLEPs4jmyHj.pkg"> TECMO Bowl Throwback</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0700/NPUB30009_00/1q0GyHsd1I8cTKIhT5Iu6uwogl2xmTN6kp965kSrT5KSxXG3fHgQ1msU3QVQjHnmPg8qBrmLFOEpjNskhEbUhtVWT5qOie7MMFGFK.pkg"> Tekken 5 - Dark Resurrection</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0700/NPUB30009_00/A2UkupkbpLRyld6wYv0DKU1DjVm16t9K9h7AFcGlUaQR9tRycf8q0wit04EbU5blwHkg1H1XfGxsqskPKxOnDKNekyHleXRU7hmHD.pkg"> Tekken 5 - Dark Resurrection Online</a>
<a href="http://ares.dl.playstation.net/cdn/UP0017/NPUA30037_00/nISo0IOm6bmEybBGJvpS3g40tjYdq3oQkjRUFpjqFDXKAuDU0EWVxGiCCAlsTQO05FYeW3a30FjdLisj1M4IgNA2kxKi44RCcDvFh.pkg"> TerRover - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4073/NPUB30223_00/EZEbuITWrwEoXsNNXzHWhuYgHRJEipjnjXSqvntECCZyPrHYBuyIFOaiFbIBcwBVKnOoLkuPVrlKxGOrFWhuCRyDTcrLzGBtolvzB.pkg"> Test Yourself</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0006/NPUB30226_00/KjCVZJIqSIHLwAKzGozwCxqUgbxrUwIfouDQMYAVhAemQrpBtrxBEIenJBZJvRtOVByJokKTUvnwyobrBbhhKtkZPOVRTiScLnhdo.pkg"> Tetris</a>
<a href="http://ares.dl.playstation.net/cdn/UP0006/NPUB30417_00/EqGNWTTBGiGKCZpwMSFpFphPVwPxvGUHDikKiymHoSkrUXlpmlAeyqyxcinNlmeAXxFRWrHVheApfvSlXUAxupUXlexQLVpuFtjaR.pkg"> Tetris - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0367/NPUB30064_00/xSFm71tbKcq8961nP2rs3a0O8ATU6B43vAHONn7LhcYXHYr1LTKef1uyqFn1YYSYaqNI7IdRdHpepRkO3j9PiJxkoNUF4S4A6EOGY.pkg"> Texas Cheat'em</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80154_00/9MkkSHQnVouO6GFM0eG6Wr84jFV2TcSE9SPrAeTd4Tdbul0ly2PosgT97OwxiJnFL6fr3jcjIYVwV4LSCi96lwflGce6IqfBJpeS5.pkg"> The Last Guy</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80960_00/kXLfyOhGFLCBFKeHDopmqkCrYKbIQIAVEBkdtiNpzIyBRebMQCkGigjAGbdyAzNCHjKITHlMLKjOZHLzNebUYyOkJkQMhFMttvVuO.pkg"> The Last of Us (Downloader  needs 27GB of free space)</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA81175_00/UP9000-NPUA81175_00-THELASTOFUSDIG01_bg_1_a747d441df8483e991d3a9af79df68e68e963f07.pkg"> The Last of Us: Left Behind Stand Alone</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2019/NPUB30167_00/TgxEf4xM6CNx4Gj0uiw4oYCikSsdrVlyj5Adb0vhBYPNACX8k7ieUmyjgokSfBpMUtUrRNUwaAypCw0mjId5rYnpA57cHhONMVIRL.pkg"> The Price is Right</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4042/NPUB30070_00/b1LLVlFlsG5rWRQHefSa8lx2IB9gWD35bXOTSr8NB1HsXCGXgTQq8Ho1eLUU1r2vP3QVFMNAcUMSn9vsPtMjaHPHBwJCrDMvLfgyK.pkg"> The Punisher No Mercy</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0177/NPUB30325_00/aGHoRpwvLXlEurZbIFqeGoNmnpibFKIQudrdqYJdKpiPfnUCbLAeHMlbPcqnaXapvUreRxKEyBJmJEUfwrZojDmpYZLFUISacGwfJ.pkg"> The Revenge of Shinobi</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1010/NPUB30197_00/T8Ftab3fbyrATFUMGRnND8H2629CV4vtSub1RUp09iVDTiCaeNB9KynNJC97Shgcw2DRDKdN3DNRaN4CWpuTIX26JtQN9uNYA0EHL.pkg"> The Secret of Monkey Island Special Edition</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80128_00/mfEwYnDujn163lQQQLXgSooRM5bAE2sRubPfUvfiAshwGsG9YWhnM5MfVXUDO5MWOfsv31WiFmQUNERgcNJPd89GTYHiTSJ8794e0.pkg"> The Trials of Topoq</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0182/NPUB30297_00/rfaaupHRkosXQuEETBbTdQHuJGZdpqCiHZSClFoQGzGdpDhBOBOtiCjDXoPQalpNFzVuLZdNwGitIWzlkGEFJXGXmHnmFYAlWRxrk.pkg"> The Undergarden - RAP not Required</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA98202_00/iaPLFengBZyacBoNXSigaPQBPSuyKdxouknQOjxxFxnDAOhhZhDwvkPxkUMrFoasshmihtYLBJjgFySPRNYktXTjWJNBDXkGljDqA.pkg"> The Unfinished Swan - RAP not Required</a>
 
''', parse_mode='html',disable_web_page_preview=True,reply_markup=keyboard.lista_jogos)
            return True

        elif msg['data'] == 'TaZ':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),'''• Manicomio Bot
<a href="http://zeus.dl.playstation.net/cdn/UP0082/NPUB30157_00/TecnT02RxgqFd2vqbbGA0eS1EBUo7n1HjSgDDl7IG0OlBM7jOIn5VkxttfwUdfN8tvM6PnWUCSspA3smThUEPskQBfFV5bA4A0I96.pkg"> THEXDER NEO</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4048/NPUB30474_00/lQOHGxyTMmBmfJlmDKIJhsgIpdmofekyQJVfJqWjUbXiEnaooOrBgZxoFZfstsAoSjXHmQqyJoSewklKHPxWnKgZRnFcbENxfNWgr.pkg"> Time Machine Rogue Pilot - RAP not Required</a>
<a href="http://ares.dl.playstation.net/cdn/UP0001/NPUB30107_00/VhwITo7VEgLiGaK0mMXQ1viQjrA9ppTM00LUeJ2xA33eHbp14fxK4UcXp6BDh9T46WAyHerNRqilu1GTSegXoIdfSEVKIX7hL699J.pkg"> TMNT: Turtles in Time Re-Shelled - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4165/NPUB30278_00/kSWTzRdzxehTwljkPIbEeEOSNALdXGJAXBRMUQaAiBYNokZCdSiDghqcDIzLNPbFadCJYcupaNRkyqrnficEifgoPkiSykbsOwqCt.pkg"> TNT Racers - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80523_00/cCntAJLxMgMrDVioTNjfSYmizsrwbjSBnoTfHSVicdKlzbmghtxsdQnmyWAAVGsmSdXQXkwFxrpyPSHiPqJditPRoEleENUdEJyGZ.pkg"> Tokyo Jungle</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0082/NPUB30370_00/X6PYSecTt1Er9E2vNBQJrUsy7guDS7s80bCSCWjeFw8hO4C7DVa4FY2v6fc2b692sEv8YlMrDNGrHHq97DufLQh6l7bbJQWow9X2D.pkg"> Tomb Raider Underworld</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4009/NPUB30063_00/DCAIHIiPTHOpSHcaIp8YvuA9HjIAyp7wKXN3D5G86gxTSMK3uoH4Nb7VBuG4LHNIHutfcjtiYjb99TfPPym4CbBvTs6WtoqDGLBjP.pkg"> Topatoi</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4009/NPUB30316_00/mJNdFFlMDk8iO5wISqN58wLRrwB11qy1B3Km2gEyCQIg2WqPpRUqAqEjWt9vPAj0RCY870wTX1sBbYgpEQqvv5fKUOlByy0ireOLu.pkg"> Topatoi - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80133_00/j7hBLr1AoAGuKe7GC0VUnDrAt1jebkNvfWEdHlNDIE74ew7pxXU9y7Ju9IQ8c9T3B0oyKx0HTFLXDLNBpcjPF2UaxkTA5VbLW4CdD.pkg"> Tori Emaki</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80104_00/1jIgiiqyT6icmqDGPKFJCEvvI8RxK1Pb7mBrxfP9jJF261eCrABCgh1prjvx3UJ0R4UqyJ1WMix6IwAhJ3V7kYDjrDF22uHHNucjv.pkg"> Toy Home</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80247_00/0i5vr44aJdo5SVpCyNcEjFRRmTbCg4PIdLO0bYvqDRRftyXq2vfNQBQ5YUCy2rf2vDwycBFfy1hm1BH9iBWPx7mxCREyLt1EsXHIL.pkg"> Trash Panic</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4029/NPUB30109_00/QgxkDu2qCrju8FUgR5eRJE4lSVbA7qdGJkwwqWGai1vTgMabOCqPKnrCnjmxlXj6Df6UkfB0tJuDmqUqiLNR7cq9CSBV6xlEpGEwL.pkg"> Trine</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0005/NPUB30331_00/magzqMTMFFSfXAAOZHabvxTTyyVYTTafIVFBQBLDFUMvmgvGJqoRENJOlbCUEzRJFGYasWJytyFSHWHCRmaEElXhINoAINCPzPumn.pkg"> Trine 2 - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2006/NPUB30155_00/TxGte2l3yiAOoqAkExEllR8RT9ctcakjeMLBMplN9mmVH3N369HkRr58Aa8kqTksKdQok5YUwvWnghtYmyPYfuC3bkkDIEBdxeMad.pkg"> TV Show King - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80079_00/GtTZfhzMYZNVXjMBineZrIXtxYUeVBBRALXsNTPgukIfnCGrQQaXpZYPxhXHZMkYFdqoPTHOJZSahnbfFEynrMvHxURefGiAKpwQP.pkg"> Twisted Metal</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80697_00/VKXNEcVcJVciABhzEgxkrzMNYIjhoCXRmlkZwJSKmlrStcTohdkjtHKiFDHUhvfIegnJHrmmfbTNkdQLwHSSYOwokcHoHBiVUaSoU.pkg"> Uncharted - Drakes Fortune</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80698_00/ftZMEmWLrGqjEHKXIBnGMKwRkyjImyQwgNPVfMZYIJluNTMNcpWdxjOGJaMInMxcXylNjdBBslPvQhbHyCdxAYfphddDuAZJBAaye.pkg"> Uncharted 2 - Among Thieves - GotY</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80234_00/mkuJUoBuYxvMqWbpvQSgESx6XNlCvlG8XA0AVuh6sUpfKNDCvvpUu9iJW439bkcrN64TF8FH1H8ewRO8ANcflychxYVSehSg7j8CA.pkg"> UNCHARTED 2: Among Thieves - Eye of Indra 1-4 Bundle</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA80858_00/gtENzwoZitJdOLoXYYepUxliypTkjxHujRIzBjdWPNVkoTWEMhUOynchChKuryQcyKFLLVnqLOsiuQbOvAzgAMGakFDxBIfeQupez.pkg"> Uncharted 3 - Multiplayer - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2006/NPUB30082_00/Rx3iEgJTp8LDueyRLS7O594qQDxAepbSBSfgnxyMSP7GhwibIWFGP8AbCMDiEvsJXNfOIbjTQUP07RYC3ObxaRup7Rpv2eIoxGlFd.pkg"> Uno</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2006/NPUB30160_00/P41YHHW1xsCYTkH4qTNdXXeOg3AV1xLMmO0HkRMJxItLmtdO5HX8BnumWSXA67sKA1sf2NGfHfe4h9aYxeikm9c0rkPmFXDHm2sai.pkg"> UNO - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0101/NPUB30075_00/DVqGitFC88wdJVrwRfCvEAC3s2STfpc4pLVVSbb4RVrhTGwfJcv85sPgIjwJEWlp6gs1q2BSJMkiDWmo0A7d76nn4WdSK0L3bWiud.pkg"> Vandal Hearts: Flames of Judgment</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0001/NPUB30186_00/pCrvJf9a774BgeIMTcD3y7hasKAqeYcxUNuRMWCEsdtuliWeNwo3OyrTmk4AjgcAEfEQkGjFgHO04eohqDJdLbOoURjeOVb9OG387.pkg"> VooDoo Dice - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2004/NPUB30098_00/dMHhfYB3SfDffJce8jud40JS5yxcQCxBFgW1ckR3IL7vWLNwwUMtck0qRc0Talp3PEVfuwUAcYh5IfYBvmUrXH3ifcdOJJP0VfYFE.pkg"> Wakeboarding HD</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1026/NPUB30446_00/rJCzZCfjNIKMeDaNijvVNBJPMenvOLMfgOWNJHgxfYvmvMINrSZmRdmPyeYSTDnYNcUFVJlSXuQVtAYUJshnsimzXooCxUXEkdziN.pkg"> Wanted CORP - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1005/NPUB30473_00/UthalCimxdxToGAMowqJsuQcyPxscgraVHSwpAhVTEllUioUqRqoDHYIUuzdlDPJEKXdiIeKuRdspDEADkOjyULuFNDwGWIvcZxGT.pkg"> Warhammer 40000 - Kill Team - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80077_00/mKtvmaSVBHFB3T8b7HUsrjpuORXSXinq6S4WLvjbwnOx8K8ELa6lPDwRJrIUxALvJcpD9EegEwVP7XWe708WsLcjSsnA8EwaeihLd.pkg"> Warhawk</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0182/NPUB30431_00/lxcTcPVZWNtmcFdnzxAeTPsczSTTwVLwxDCrgjwzGCbxaxZzOsRjjedGCpOgtida.pkg"> Warlords - RAP not Required</a>
<a href="http://ares.dl.playstation.net/cdn/UP1018/NPUB30050_00/coBLkAw5ccsCbUMM0hUF44kdj928EWpqDv8U6SilfhyXPedayVCNkS7l56LyCp0cYJvlrFm9wRD40VmWWP3T9GR5NTyhxXCPg6UFL.pkg"> Watchmen - The End is nigh EP1 - RAP not Required</a>
<a href="http://ares.dl.playstation.net/cdn/UP1018/NPUB30071_00/fkuArhfTYWNnYmJLOulTICxgGHiBkaq3SObyKx4TKAvjGVqDhjXKBRGmsia74kl3W7mUlYA51lc9LGMFRmH7Vjp6c1DKGAdIhCC6t.pkg"> Watchmen - The End is nigh EP2 - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0017/NPUA80137_00/A8g8wTrTCslEOvg4oYhyrSHpvYcUOtaFvsbmK1xfMB3w7dp1vAOB3N6Q5tXwOYQNMioBD5iE20qtnDtQhvwJ5Grjs1hP8TjJnVjCx.pkg"> Wheel of Fortune</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA80754_00/CyjRYiwjOOoRhajlAhyUkXIYlgRMGvxADowjNVpjFuXprhQaPhDydZSwBDAVTgaANpEalwqQghcioTOCApdqTHsSIxJDWauXGTfSL.pkg"> When Vikings Attack - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2019/NPUB30427_00/CyWgHtCLitCJiTWzDcXVRASLkzovFodZoPkUgtWDRORygkJmPRXeoLwrGVbOattgetPYoBmMlHsYVFphfpCtLCnKjPtbpaJroNzrQ.pkg"> Who Wants To Be A Millionaire</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80105_00/rg8UH2OcLmrXYSkNGEaPIyWHMu0QxiU9xmEop8aTymvvUaby066N8iN6idmGNgFNWlFr7ImXsnSFnK8wDKduYTDgMe10btD0cPRXi.pkg"> Wipeout HD - Unlock/License by DLC</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1023/NPUB30452_00/uIxiwswNgqcNLkAnmmDjpobqUTGMTYPxpLhZaKldAVLwRZnOrEiRFhvmijpWZvheebCpdJGRNrndZSWTyYwnCUxTRrPbxekyPvTMw.pkg"> Wizardry Labyrinth of Lost Souls - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0102/NPUB30021_00/6rSiVgNJCb8kb9NTPU92NgtCTqEeaGwdnvKhlgt0jK3pGIwe0NOgj2r7wWuo0uSm1uCuqjByHmyEWNh4r0d9gutRK2VCIBWDT0OU9.pkg"> Wolf of The Battlefield Commando 3</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0002/NPUB30074_00/xO84EAKjFbluLvMParJSf9bkPxHGyVLQJxW3yHY9Ct3TIXUjy8PsSTFlyKb8XqUCOgcfGuHWfAgiAQ8pqYTV0EC2klUkK6AyNnPWb.pkg"> Wolfenstein 3D</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0177/NPUB30327_00/ALNDUbSlkjzfuCaqaqQGaDykpicdyISgnlzAltvsLliUfWvPgzSjmJTujxolyfoRbPwuHbRjGskctwILwuAnDxaJaUuHPbrBChWGu.pkg"> Wonder Boy in Monster World</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4064/NPUB30060_00/UlUITncH2LrRTc7iBfOxjWU2ox8DlGjPOofGkEhqw2ClgTMyFDg3W69Lh3Njq2YUisJfMfshwTeyNhLWwk1U0jYNRganNidLx7T9w.pkg"> Worms</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4064/NPUB30230_00/uRoFfognVaOEaBF0kwFOtaYV9ruyLP2KQDsC9kV0wWOiKo6DBeBhNaB7XvPpDr1L4VQ0ygJCrU45j5FnIyOpODurj0cNUpYsP1g37.pkg"> Worms 2 Armageddon - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4064/NPUB30385_00/VwuFAhEGqNRxTCHUKPaLfCoOkRTqrEKngaQTFnQvgapQBgdjCUUBDwVFAqEIlMFaKmVfTSYLIwJchIvTtAiIKViPIRbvMwbTEfafz.pkg"> Worms Crazy Golf</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0101/NPUB30320_00/CrXzeuWafGLEeyOLLMMrFgGtrqiUPtJnPNEAhPoineLvCyputfuuLHSdkaDaxoBaackUIAmLuxPeyVwjkdHpybMxATOMzkVOUdGEE.pkg"> X-Men - The Arcade Game</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4042/NPUB30055_00/iOJkMtCvchfvdWvGNu5U2Y5oq6RcYYrJaIfI3xPK4uJNrCDym6WH7U5QkgQP3p6WOgXxg4TR25IT0dHIM5nqlUIO4C6RxnsJ7kxkU.pkg"> Zen Pinball</a>
<a href="http://ares.dl.playstation.net/cdn/UP0101/NPUB30069_00/onk4mbHNwd99tIrjHNvFwi8R3MTBpFodI54wt8hQydLFhsC45aAaO5heJh0kDRSyak6ALiUY6hlkmORdT3oA8urKey8Xc27R9BVFi.pkg"> Zombie Apocalypse - RAP not Required</a>
<a href="http://ares.dl.playstation.net/cdn/UP0017/NPUA30003_00/ioK4HQEme7gxPUvRL2GdkKcQ22m8NSbH18wyykhfRciOKfcS3wRbg8wDi5mV55RqLthom20FQkQoMj2bdmlYMABmssDfnsbDMVP9s.pkg"> Zuma - RAP not Required</a>
 
''', parse_mode='html',disable_web_page_preview=True,reply_markup=keyboard.lista_jogos)
            return True

        elif msg['data'] == 'AaB':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      '''• Manicomio Bot PSN Stuff By Gorpo Orko TCXS Project!
<a href="http://zeus.dl.playstation.net/cdn/UP0102/NPUB30024_00/M5owiRSUtMTCwCy7BgpFRQFkb9VBJKjytrBfEfuvylNCSIqvdXBQyDIrO893SlB3Ndnbm9MaQ12u2grVWTs5dxxOGO9BTOHJmsK8x.pkg"> 1942: Joint Strike</a>
<a href="http://ares.dl.playstation.net/cdn/UP0006/NPUB30058_00/kljSpLyFOKIfbG9diNkpsHsG0LAk6PFfWcbVNHhokb8LXwktcGdh6puQ6pAmDLonXcxk158FjLGUbvlBQrUislRlKyr9jrp7adhpV.pkg"> 3 on 3 NHL Arcade - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4009/NPUB30347_00/OcAagtcdqQGFTaNMTXYMzfXcXYpvGVxoSuUCuOOOXUvJszZEQXQeSWNAWnVqslWFNsNlsbEEPzuucPqoKkyCRKNoWyCOVgXdYYulA.pkg"> 4 Elements HD</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2056/NPUB30275_00/wUhrgIzXdFLRfORYpPUeDIWzhDfpEwuuRuiSSaAakAxeFlpRBkTLqflJfRymhsAR.pkg"> Absolute Supercars</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0177/NPUB30151_00/7cNlEN8tUcxG5DD8vk35xVq9j3p1BCFk5UCLy3NDXaRmfJRIWycE5Okurx5FC5cLr3KKXUHUyKblvskbICvbIQfWeGAn4HTcEPREx.pkg"> After Burner Climax</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0102/NPUB30033_00/8EJJULqG54jm9LT6JuFY6rkq9Rxf4CC1XybLp4qv468DY7eX1jA34qJkbHF9ttIhGSuEhWqSy5ye1eqTxmIAqTJo7hXLI1SIrl5Sh.pkg"> Age of Booty - Unlock/License by DLC</a>
<a href="http://ares.dl.playstation.net/cdn/UP0017/NPUA30036_00/nHaGXrCcmqeWPNDCMyKrbneUPoiTdkZretFMbOOxFkhMScXmLCiqhCxdetdVDrzAbOhKlnlxgWjHOfseQkkfFYHrCDwHGBYaMdeXC.pkg"> Akimi Village - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0177/NPUB30323_00/ekTDeLUiXbgafBqYuVrSYAWFTKMVKqgjsXTlIvOLkYWxogtOHIgCCwPWBhaIczztyyKctKedqQyXcqYWADifvubOKjfEEOAgXUFUU.pkg"> Alex Kidd in Miracle World</a>
<a href="http://ares.dl.playstation.net/cdn/UP4064/NPUB30335_00/roSboKbypjrjappfWZyUEhAldhVWAMqCOPblMAIVhlsFWDupCagAMkNizZLtrBcJsYwMeovCXHdJSIozvjGnAeAZQlrDnmqEIHjVX.pkg"> Alien Breed 2: Assault - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4064/NPUB30336_00/emNRmxydfOvXKNWphaqyzLnxbISFZuCqwVeZAIxHQbSIjTnDWtnZqRUMPCzeTAqfcwoNgHKcfIpVOJBJXoaoKcOhPpVkYJWiUadDN.pkg"> Alien Breed 3: Descent - RAP not Required</a>
<a href="http://ares.dl.playstation.net/cdn/UP4064/NPUB30141_00/cShiO9kKmsj63ONTCYRa4LTuaKXlDXhdOFv6dMtvi3OWu8S2pwOLtUFrik8ttdHluFAC8IAaVy0eHClpduYjPRtk1HI1lMulouADd.pkg"> Alien Breed: Impact - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2007/NPUB30308_00/KQfiZSzAbmRlMPuGpMhbkvobuuzpLpYEWjYgExcWTdUxEtKvjqacpcTnonSSeIjBtpvFdgmNjKEJjFyCvmVqIVZyCudCBrolMqMQl.pkg"> All Zombies must die</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4054/NPUB30106_00/C2crrnrb9hp38pGar3fQOwpbK70MRC1I4tW7a9E44kkbcKLDHmhWgqfP48VXbAhrJ0hn9tcSl2x1Ke1smeMoo4hwmpUbsRjQtfYVI.pkg"> Anarchy: Rush Hour</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1005/NPUB30463_00/uBWacHthVujQoycolkdxlADjVfBHrururLZJwfrQDBCURZeUvzERXOjawVUxzVyxwVfOkGCaXvZVDgxJykdmTzGOjbIPHNbushKMB.pkg"> Apples to Apples - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4129/NPUB30203_00/mfOLhlF6DHkaomqw406YtM9NWAmN2CW0wTfnCWHG8YLE4y7Ia3S9K9bsFRE4dakA1ISMSDKBEOm5gNcv4KCJxT82qW4tYKHXHbfNo.pkg"> Aqua Panic! - Missing RAP?</a>
<a href="http://zeus.dl.playstation.net/cdn/UP9000/NPUA80127_00/lL6g6LehkeKpMXc4PbdscUclnxEgd1jjRt6FVtV0sRpsVABl2rJcEQqktwSAAsgvkRMADEUH6E12fic41kuXNEv9lhgWR8S52LUq2.pkg"> Aquatopia</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1024/NPUB30425_00/LTCgdWvbtWlfJFLkXJJodIOcIxcTjdRvuCLEieQQKZIdIdbspqjqXeGXqddMoCOwFIPTGxkxWeThrhpOerbikUripNOlwJQRdTmQm.pkg"> Arcana Heart 3</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0001/NPUB30451_00/EWJIuyxHFBPRNSSdMCJOsCbxvsQCeHlHsKZTPqaeBmJRCqANKvyxiucWsKSOznxQyxaFoWHyFmtzUKnqwlIHIqnJsbZCdQaQYpLxH.pkg"> Assassin's Creed</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0001/NPUB30423_00/mQkeEoyLPzzPKLlOOOlJZzqxgYWNVFgZaVWTESOkkRmNeilinfVWNgbXIquAMyFDsevqZvQZFEzxhEhCSQWkanyJICfSohzURtxAi.pkg"> Assassin's Creed 2 - Deluxe Edition</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0101/NPUB30028_00/FTVixwwaMBjYvfxrNaqanBRmYQPRkgHBADOoOOuI6wtsopbCt8PaXWVLbG6PCIN6cM0Oo8FrFS04ddfB2AvAufVe66o1n6oY47ysH.pkg"> Assault Heroes</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4052/NPUB30062_00/m8YwDdS8upbqJ43JJ9i3dTrHRaMIssKYWUf64iRYFaWNERwpsWyVWjvvyHIQnQkAb4Iy8Lj7WGL8erJoHMvTvhVDwtjg47j9raelF.pkg"> Astro Tripper</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1026/NPUB30245_00/KwLI9kg7GG2ybe93cMip9JVNvD2g8Ti7q2hR3PR5gblcd0HcFxtpNAcxu4IUhvU6M6GImCKEFVEUfWCARMNo6U9sDGs44t2qwGoN5.pkg"> Auditorium HD</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30401_00/TIRQoHXRBUHVcSaMcVrfVuZnqfoVTiqkvsdDTGfqTtvQHFZdBAIRdwQpjglCKISqFrIxArkMdpuLUfwNEmYjKgEQdyoutvhjhTSHY.pkg"> Back to the Future Episode 1 - Unlock/License by DLC</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30409_00/RxnbrHOhbjUGAyLYXCbklkSFHLhqeBekjpBrtmyXEhWaeiVYdixIGKzEbMSgPuetaOqpNNkCPpGWdeoleLDEPjjXJkEVoITyIFRFO.pkg"> Back to the Future Episode 2</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30410_00/EZUojBqyFNpzVBzEuHoUGWOQEfCaDLmMgblEdgKfWONqkRaVQVdcaWbBWWFxqhlvcDVnrKuZuObitfJONKXhdYUMBBiHMViZwbhdF.pkg"> Back to the Future Episode 3</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30411_00/yQxogrMMQrmPbIqmokyMAwLWYMiELUlRtGibTEXPkpEMuQDfWijJUkmiIdCVQTfxDVGXpZlBPdXsstprfrpmkyAMPxNSIPwatXeZq.pkg"> Back to the Future Episode 4</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2026/NPUB30412_00/GaNCjzsugYOShccqXLiBlfxzbAPUtujVpDLUmvqgDdsKHEQvjBGlWgNfThkkHsjpGaioCERyFteJsYHfIsvHGNoqYftisAQsMJpAQ.pkg"> Back to the Future Episode 5</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1024/NPUB30126_00/97ri6539HhyLw3QCsLsmfrqDf0DTdm55rrDAVVbSK9wPGnaTFTTLMJepi8pAm2iNV8c8mhtKI8B84FisiMyjovaKBYpEx206nFEX6.pkg"> Battle Fantasia</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0101/NPUB30470_00/kcaJbDPKOCCopmjZLQavGjQBYRACHDSCbDswAWIKkKcqJYcCrdtoSBDXybjgYWJTkEPbTXjcsDIdUZqyBzjHizMaBjolmdExqKUuq.pkg"> Battle Los Angeles</a>
<a href="http://ares.dl.playstation.net/cdn/UP0006/NPUB30077_00/ymidd0pl3nu1W22UbpvOytnXa5GrrpaFSx88JdfW3BTq0PkB9FPpysy3YCJTkqkLYJkRG8Ry6RqPcSYPw9iRjxCvswWEXA2sWNsM0.pkg"> Battlefield 1943 - RAP not Required</a>
<a href="http://ares.dl.playstation.net/cdn/UP0017/NPUA30002_00/Jtjh2BLj2lxls0no6QHRYAObnFH1O0fx3fMopA51KWAxNvCgyId4ca9TICIJYOcud74Tj35aevkqpfpSn6Hbxjl1YcTgkgD9G80oh.pkg"> Bejeweled 2 - RAP not Required</a>
<a href="http://ares.dl.playstation.net/cdn/UP9000/NPUA80882_00/MthHhXIAXWswyXDmnvjpXuquWuVpZbmeYMcaUkfZudJWPZihBHuZvnltCsypSZjiFZgadSjMBgHRhGDJjzMIExCrvqRppEMSBaETU.pkg"> Bentleys Hackpack - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0001/NPUB30394_00/joEXlWTjPppHpRTcBKLTaJRuWblWLrKKvVWYVDyFYYXEnQVhHwqZGigWzdxVvzzxmPAZVCPTZODdWKRAAkZHPgXgfvnECamxSFrGo.pkg"> Beyond Good and Evil HD - Unlock/License by DLC</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0102/NPUB30022_00/70GiocFvym3Rc5FD3gLTT6YXAALLBo555NlnwKLJwxea0BFOndPNGgG2fksFDxx8h6Lugcb7ftV5RXt0dn1rjHF6vNw7XcvELvdSB.pkg"> Bionic Commando Rearmed</a>
<a href="http://zeus.dl.playstation.net/cdn/UP0102/NPUB30131_00/KEbgOFuMSwdBobzrZoLQHFbjzTumnEXiwEnzGDoYfvKvzhoWESMWqLMfrsrfGTEyRcjACpYfRbBmaWTCrRepnsfRhnRvaFVsCraDi.pkg"> Bionic Commando Rearmed 2</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1001/NPUB30393_00/HgmqqIwonUqfaDJwQGBtRpjzRkJGLAjfyEEuWBhmxDidAOTmsCCOuKyoGKoyQSiuHCQvAjWaXqvitNQkTbOPeNHBDTgxKpoOpSuQe.pkg"> BioShock</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1001/NPUB30392_00/aOeKEnJHzdWDnDUFCPEipskjjfOaNQxpAEhmAlKeyXVuKfEpxsDiUWYFWwbwZcWEewaIkNWlwUWaMYupruQwtVMrCEkEfDlbUVEEu.pkg"> BioShock 2</a>
<a href="http://ares.dl.playstation.net/cdn/UP4002/NPUB30224_00/DT8tRJ6S3o4PLGAeHCrIXijnh4YfG0PCaRjWqBhYVXAuMT0Q6LH66uluWvjwOWpBKiKmpeoBVDEwdl2OkMsd3fNEjO1R2yoCTt8O6.pkg"> Blacklight Tango Down - RAP not Required</a>
<a href="http://ares.dl.playstation.net/cdn/UP0182/NPUB30253_00/YMMHJYouqJjmWI8EPxrGvjdspAE3cKaNocTXPLDRgOCXotUr1wr6sTdFPxFdlHYsRTHx6ol3iGAMuOe8VelnG8jVFN3DL4kNgQlTy.pkg"> Blade Kitten - Unlock/License by DLC</a>
<a href="http://ares.dl.playstation.net/cdn/EP9000/NPUA80002_00/laYELyMBfjCyqd6KVjGHcrYDi0C7o8OV1fGGfaeIXlnjXY2QhKQ9nBgVtdwlww9DowAp0VU0unn1sKGwiysP75Ktn6cVEPlUJECJe.pkg"> Blast Factor - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2006/NPUB30367_00/JPmqZWRLHZHzeTzSgvaQnauRVEEvpFOYHNoTUGxnLLMwCaIljwKYFFZUfCBSCjrHNkehdVgPklAoorQGgwpyMKOlopNHxVeNfKFkm.pkg"> Blokus - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1012/NPUB30377_00/yAKtEiPPllrSYmXHXuuTMdQOQsrPJqaTDjtuQpqQqoNCNbMRQbSkwxxjeFzmcqVCnohBBVVERiarxmeusTsbYiDMZSEXzJRVzxRkX.pkg"> Bloodrayne - Betrayal - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4075/NPUB30159_00/CiA548nIAfx2DWBW3VHIwVT00bnj8Ivg3fRIJMxCxJMnabmbQMojOtK9nO9MmUhyBF0qOOu9SDSyF1jfyo71AKkV8Q8RHPWIqGrjT.pkg"> Blue Toad Murder Files - Episode 1</a>
<a href="http://ares.dl.playstation.net/cdn/UP0555/NPUB30051_00/4GQBIsH0TsJvVWpNpDCPburaOnRDIx2Y90AyB2VVXLXg2g5GFDPN1Db46Kw4DYAUMH4syup0BdOGjjJKxjIAtIjtSj18V9lVj6Ekl.pkg"> Bomberman Ultra - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP1001/NPUB30413_00/gJPHSuCAYZBnhxKUQxfAaWyghzImxYwhiXpFkgMtTqnpWnYeRvuMWShqzGzMPgKDqmlcWqYxzbMOvyaBssduUaKfHOVrbTLBXoFnK.pkg"> Borderlands</a>
<a href="http://zeus.dl.playstation.net/cdn/UP4049/NPUB30133_00/vaMJjYU6mQ1N6kXDWKoKPuqgXJ8UaINGi5N6oYoRp9M9hpwWvKDB9WhkQpaf5HgK7l7HdHQGp8qb2BVY9lMVeaoCIM39cXSe8XUPl.pkg"> Braid</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2006/NPUB30049_00/hKlPMbFUUDJrprNO8enKfmvYT7cOIY3PNVt8iAsPFqjDG80QirDnpe9UnD76MMBGgR52RLloXM8aePohnbBsMsu6xdysosRyMjhuJ.pkg"> Brain Challenge</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2006/NPUB30158_00/wMV6TJIdEnYYV9VicQsHrrtIapiR1vgTRbHMCeUXKGJSvPLVuAMlbY84Lj5CuiOdeNIh7GeWtqWNbNAxAcC2Fn5c4R10dJfFL46J3.pkg"> Brain Challenge - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2039/NPUB30384_00/UWVgRifebvLrsNRIpeacllvxLnQUCuHPcTWAFOXOVpHSiRhbkvGMqMPUPpQFWlxcPDvzQPuasuJwoiXeazrQYMobegJYLMjuHedyG.pkg"> Burgertime World Tour - RAP not Required</a>
<a href="http://zeus.dl.playstation.net/cdn/UP2007/NPUB30046_00/Q8tEqCfgRPiOb4RB7b5tgHmdfdChfi89rAslQqKCK7VHKof2VKj4tQojXe16P75r2DqjUBLv6mRgaj7lrrV62NyMvfghtFJbAtOtb.pkg"> Burn Zombie Burn</a>

''', parse_mode='html',disable_web_page_preview=True,reply_markup=keyboard.lista_jogos)
            return True



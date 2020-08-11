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


import random
from config import bot,  bot_username, keys
import aiohttp
import wikipedia
from datetime import datetime
import png
import sqlite3
import os
import pyqrcode
import time
import requests
from spellchecker import SpellChecker
from PIL import Image, ImageDraw, ImageFont
#para o sistema de reconhecimento /recog
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2
#para o jsondump
import html
import json
from io import BytesIO

async def extras(msg):

    #exibe todas imagens cadastradas
    if msg.get('text'):

        #envia todas imagens cadastradas na db
        if msg.get('text') == 'todas imagens':
                conexao_sqlite = sqlite3.connect('bot_database.db')
                conexao_sqlite.row_factory = sqlite3.Row
                cursor_sqlite = conexao_sqlite.cursor()
                cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                mensagens_sqlite = cursor_sqlite.fetchall()
                for mensagem in mensagens_sqlite:
                    try:
                        if mensagem['tipo'] == 'imagem':
                            await bot.sendPhoto(msg['chat']['id'], photo=f"{mensagem['mensagem']}")
                    except:
                        pass
        #clima
        if msg['text'].startswith('/clima'):
            if msg['text'][7:] == '':
                res = '*Uso:* `/clima <cidade>` - _Obtem informações meteorológicas da cidade._'
            else:
                cidade = msg['text'][7:]
                try:
                    key = keys['token_weather']
                    url = 'https://api.hgbrasil.com/weather'
                    fields = "only_results,temp,city_name,forecast,max,min,date"
                    data = {'key': key, 'fields': fields, 'city_name': cidade}
                    req = requests.get(url, data=data, timeout=3000)
                    json = req.json()
                    await bot.sendMessage(msg['chat']['id'], f"`Cidade:`{json['city_name']}\n`Temperatura:`{json['temp']}°C\n`Min:`{json['forecast'][0]['min']}°C\n`Max:`{json['forecast'][0]['max']}°C",'markdown',reply_to_message_id=msg['message_id'])
                except Exception as e:
                    #print(e)
                    await bot.sendMessage(msg['chat']['id'], "`Não foi possivel obter a previsão do tempo ou deu um erro, tente mais tarde`",'markdown', reply_to_message_id=msg['message_id'])
                    pass
        if msg['text'].lower().startswith('clima'):
            if msg['text'][:6] == '':
                res = '*Uso:* `/clima <cidade>` - _Obtem informações meteorológicas da cidade._'
            else:
                cidade = msg['text'][6:]
                try:
                    url = 'https://api.hgbrasil.com/weather'
                    key = '0418e7f0'
                    fields = "only_results,temp,city_name,forecast,max,min,date"
                    data = {'key': key, 'fields': fields, 'city_name': cidade}
                    req = requests.get(url, data=data, timeout=3000)
                    json = req.json()
                    await bot.sendMessage(msg['chat']['id'],
                                          f"`Cidade:`{json['city_name']}\n`Temperatura:`{json['temp']}°C\n`Min:`{json['forecast'][0]['min']}°C\n`Max:`{json['forecast'][0]['max']}°C",
                                          'markdown', reply_to_message_id=msg['message_id'])
                except Exception as e:
                    #print(e)
                    await bot.sendMessage(msg['chat']['id'],
                                          "`Não foi possivel obter a previsão do tempo ou deu um erro, tente mais tarde`",
                                          'markdown', reply_to_message_id=msg['message_id'])
                    pass


        #jsondump
        if msg['text'].startswith('/jsondump') or msg['text'].startswith('!jsondump') or msg['text'] == '/jsondump@' + bot_username or msg['text'].startswith('jsondump'):
            msgjson = json.dumps(msg, indent=2, sort_keys=False)
            if '-f' not in msg['text'] and len(msgjson) < 4080:
                await bot.sendMessage(msg['chat']['id'], '<pre>' + html.escape(msgjson) + '</pre>','html', reply_to_message_id=msg['message_id'])
            else:
                await bot.sendChatAction(msg['chat']['id'], 'upload_document')
                file = BytesIO(msgjson.encode())
                file.name = "dump.json"
                await bot.sendDocument(msg['chat']['id'], file,reply_to_message_id=msg['message_id'])

        #ip
        if msg['text'].split()[0] == '/ip' or msg['text'].split()[0] == '!ip':
            text = msg['text'][4:].split('://')[-1]
            if text == '':
                await bot.sendMessage(msg['chat']['id'], '*Uso:* `/ip IP/endereço`',parse_mode='Markdown',reply_to_message_id=msg['message_id'])
            else:
                async with aiohttp.ClientSession() as session:
                    r = await session.get('http://ip-api.com/json/' + text)
                    req = await r.json()
                x = ''
                for i in req:
                    x += "*{}*: `{}`\n".format(i.title(), req[i])
                await bot.sendMessage(msg['chat']['id'], x, 'Markdown',reply_to_message_id=msg['message_id'])

        #coub
        if msg['text'].startswith('/coub') or msg['text'].startswith('coub'):
            text = msg['text'][4:]
            try:
                async with aiohttp.ClientSession() as session:
                    r = await session.get(f'https://coub.com/api/v2/search/coubs?q={text}')
                    rjson = await r.json()
                content = random.choice(rjson['coubs'])
                links = content['permalink']
                title = content['title']
                await bot.sendMessage(msg['chat']['id'], f'*{title}*[\u00AD](https://coub.com/v/{links})',
                                      reply_to_message_id=msg['message_id'], parse_mode="Markdown")
            except IndexError:
                await bot.sendMessage(msg['chat']['id'], 'Not Found!', reply_to_message_id=msg['message_id'])

        #data
        if  'que dia é hoje' in msg['text'].lower() or msg['text'].lower() == 'Que dia é hoje' or msg['text'].lower() == 'que dia é hoje' or msg['text'].lower() == 'data' or msg['text'].lower() == 'dia':
            t = time.localtime()
            await bot.sendMessage(msg['chat']['id'],'Hoje é  {}/{}/{} e faltam poucos dias para começar a guerra!'.format(t[2],t[1],t[0]),reply_to_message_id=msg['message_id'])

        #hora
        if msg['text'].lower() == 'que hora é agora' or msg['text'].lower() == 'que horas são agora' or msg['text'].lower() == 'que hora é agora' or msg['text'].lower() == 'que horas são agora' or msg['text'].lower() == 'que hora é agora' or msg['text'].lower() == 'que hora é agora?' or  msg['text'].lower() == 'que horas são agora' or msg['text'].lower() == 'que horas são agora?' or msg['text'] == 'Que horas são?' or msg['text'] == 'Que horas são ' or msg['text'] == 'que horas são ' or msg['text'] == 'que horas sao' or msg['text'].lower() == 'hora' or msg['text'] == 'que hora e agora':
            t = time.localtime()
            await bot.sendMessage(msg['chat']['id'],'Agora são {}:{}:{} e você pode morrer a qualquer momento!'.format(t[3],t[4],t[5]),reply_to_message_id=msg['message_id'])



        #avatar dos usuarios
        if msg.get('text') == 'avatar':
            id_avatar = await bot.getUserProfilePhotos(msg.get('reply_to_message')['from']['id'])
            avatar = id_avatar['photos'][0][0]['file_id']
            await bot.sendPhoto(msg['chat']['id'], avatar, reply_to_message_id=msg['message_id'])

        #github users
        if msg['text'].startswith('/git ') or msg['text'].startswith('!git') or msg['text'].startswith('git'):
            text = msg['text'][5:]

            async with aiohttp.ClientSession() as session:
                req = await session.get('https://api.github.com/users/' + text)
                res = await req.json()
            if not res.get('login'):
                return await bot.sendMessage(msg['chat']['id'], 'Usuário "{}" não encontrado.'.format(text),
                                             reply_to_message_id=msg['message_id'])
            else:
                await bot.sendMessage(msg['chat']['id'], f'''*Nome:* `{res["name"]}`
*Login:* `{res["login"]}`
*Localização:* `{res["location"]}`
*Tipo:* `{res["type"]}`
*Bio:* `{res["bio"]}`''', 'Markdown',reply_to_message_id=msg['message_id'])

        #giphy
        if msg['text'].startswith('/gif') or msg['text'].startswith('gif'):
            giphy_key = keys['token_giphy']
            text = msg['text'][5:]
            async with aiohttp.ClientSession() as session:
                r = await session.get("http://api.giphy.com/v1/gifs/search",
                                      params=dict(q=text, api_key=giphy_key, limit=7))
                rjson = await r.json()
            if rjson["data"]:
                res = random.choice(rjson["data"])
                result = res["images"]["original_mp4"]["mp4"]
                await bot.sendVideo(msg['chat']['id'], result,
                                    reply_to_message_id=msg['message_id'])
            else:
                await bot.sendMessage(msg['chat']['id'], "Sem resultados",
                                      reply_to_message_id=msg['message_id'])

        #qrcode
        if msg['text'].startswith('/qrcode'):
            a = await bot.sendMessage(msg['chat']['id'], f"🤖 {msg['from']['first_name']} ***vou gerar seu QrCode***",
                                      'markdown', reply_to_message_id=msg['message_id'])
            codigo = msg['text'][8:]
            qrcode = pyqrcode.create(codigo)
            qrcode.png('arquivos/qrcode.png', scale=10)
            await bot.editMessageText((msg['chat']['id'], a['message_id']),
                                      f"🤖 {msg['from']['first_name']} ***aqui esta seu QrCode***", 'markdown')
            await bot.sendPhoto(msg['chat']['id'], photo=open('arquivos/qrcode.png', 'rb'),
                                reply_to_message_id=msg['message_id'])
            os.remove('arquivos/qrcode.png')

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

        #fotos da chartubate sherry sheen
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

        #mede seu ping
        if msg['text'] == 'ping' or msg['text'] == '/ping' or msg['text'] == '/ping@' + bot_username:
            first = datetime.now()
            sent = await bot.sendMessage(msg['chat']['id'], '*Pong,kkkjj ai seu ping!*', 'Markdown',
                                         reply_to_message_id=msg['message_id'])
            second = datetime.now()
            await bot.editMessageText((msg['chat']['id'], sent['message_id']),
                                      '*Pong!* `{}`ms'.format((second - first).microseconds / 1000), 'Markdown')
        #rola dados (dice)
        if msg['text'] == '/dados' or msg['text'] == 'dados' or msg['text'] == '/dados@' + bot_username:
            dados = random.randint(1, 6)
            await bot.sendMessage(msg['chat']['id'], '🎲 O dado parou no número: {}'.format(dados),
                                  reply_to_message_id=msg['message_id'])

        #mede quanto shemale vc esta
        if msg['text'] == 'shemale':
            dados = random.randint(1,100)
            await bot.sendMessage(msg['chat']['id'], 'Você esta {}% shemale hoje.'.format(dados),
                                  reply_to_message_id=msg['message_id'])
            await bot.sendDocument(msg['chat']['id'], document='CgACAgQAAx0CViT8vwABA6-3Xl1vBd53xqknuyULa2YPoYB3w24AAmgJAAIz6iBR5pLYRkLVaC4YBA', reply_to_message_id=msg['message_id'])

        try:#sistema de reconhecimento com opencv
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

        try:#corrige palavras SpellChecker
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

        try:#wikipedia
            if 'fale sobre' in msg['text'].lower():
                termo = msg['text'][10:]
                wikipedia.set_lang("pt")
                pesquisa = wikipedia.summary(termo)
                await bot.sendMessage(msg['chat']['id'], f"```{pesquisa}```", 'markdown',
                                      reply_to_message_id=msg['message_id'])
        except:
            await bot.sendMessage(msg['chat']['id'],
                                  '`Desconheço este assunto...`\n```---- Caso queira que eu aprenda fale sobre o '
                                  'assunto converse comigo sobre ele até que eu aprenda ou use o comando # informando '
                                  'o tema e após ele a explicação que devo aprender conforme exemplo:``` #tema '
                                  '***informações que devo aprender***',
                                  'markdown', reply_to_message_id=msg['message_id'])
            pass


        #sistema de prints
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
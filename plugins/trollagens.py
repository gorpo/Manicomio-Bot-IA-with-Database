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

import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username
from utils import send_to_dogbin, send_to_hastebin

async def trollagens(msg):
    if msg.get('text'):
        if msg['text'] == 'chartubate':
            await bot.sendMessage(msg['chat']['id'], 'ai noob ja conferiu o chartubate da nossa musa Sherry -->> https://m.chaturbate.com/sherryshen/'.format(msg['from']['first_name']),reply_to_message_id=msg['message_id'])
        if msg['text'] == 'vanessinha':
            await bot.sendMessage(msg['chat']['id'], '`vanessinha tira o gutto do serio {} `'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
            await bot.sendPhoto(msg['chat']['id'], photo='AgADAQADQ6gxG-BOyER2xRrlf-rZJIfSbgYABAEAAwIAA3gAA8puAAIWBA', reply_to_message_id=msg['message_id'])
            await bot.sendDocument(msg['chat']['id'], document='CQADAQAD_wADqlsJRUl_c63JowABaxYE', reply_to_message_id=msg['message_id']) 
            await bot.sendPhoto(msg['chat']['id'], photo='AgACAgEAAx0CViT8vwABAzm7XjJOmX6bpde3AAFeFwlmMaoRX0RJAAJXqDEbRcuARW6HPRy_x1LI4eprBgAEAQADAgADeAADgkoCAAEYBA', reply_to_message_id=msg['message_id'])
      
        
        if msg['text'] == 'birl' or msg['text'] == 'birll' or msg['text'] == 'bril' or msg['text'] == 'birlll' or msg['text'] == 'birllll' or msg['text'] == 'brill' or msg['text'] == 'bam' or msg['text'] == 'comi pra caralho':
        	await bot.sendVideo(msg['chat']['id'], video='BAACAgEAAx0CViT8vwABAznMXjJQMaQ5gn0oshTJ-aR4hsOxqpQAAmQAA4GqMEULivNNxE7fYhgE', reply_to_message_id=msg['message_id']) 
        
        if msg['text'] == 'amigo' or msg['text'] == 'amigos' or msg['text'] == 'so eu e meu pc' or msg['text'] == 'coddando'  or msg['text'] == 'sem visita' or msg['text'] == 'visita':
        	await bot.sendVideo(msg['chat']['id'], video='BAACAgEAAx0CViT8vwABAznPXjJQ1ZuyAWK6p3j_PB9Sa1LjlIEAAmUAA8xjqUenWqNRGjMDNBgE', reply_to_message_id=msg['message_id']) 
       
        if msg['text'] == 'msgames' or msg['text'] == 'ms games' or msg['text'] == 'Msgames':
        	await bot.sendAudio(msg['chat']['id'], audio='CQACAgEAAx0CViT8vwABAznUXjJRtlW9MtdYUpwNdWPp57PuoqIAAq0AAwNa6UXaOuGG73s6lhgE', reply_to_message_id=msg['message_id']) 
        if msg['text'] == 'beicinho':
            await bot.sendVideo(msg['chat']['id'], video='BAACAgEAAx0CUYaz7wACC7ledmbqFRhLIBHSmsBQbZrt8Ed3kwACmwADHjG5R4Spzmu3Ml7tGAQ', reply_to_message_id=msg['message_id']) 
                   
        #com este comando e a id do grupo geral consigo enviar uma mensagem exclusivamente la             
        #if msg['from']['first_name']:
         #   await bot.sendMessage(-1001306342097, '`{} deu nada não feio. `'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        


         #tcxs pyject store creator
        if msg['text'] == 'tcxs pyject' or msg['text'] == 'pyject' or msg['text'] == 'Tcxs pyject' or msg['text'] == 'TCXS Pyject' or msg['text'] == 'Pyject' or msg['text'] == 'Criador de loja' or msg['text'] == 'criador de loja' or msg['text'] == 'programa que cria loja' or msg['text'] == 'cria loja':
            await bot.sendMessage(msg['chat']['id'], 'Salve {}  O @GorpoOrko criou um programa que cria lojas em PKG e tambem cria a loja diretamente no PlayStation3, o programa é super facil de usar!  Caso tenha alguma duvida o @GorpoOrko irá atender a pedidos,perguntas e respostas somente via comentarios no github, siga o @GorpoOrko no Github e fique por dentro dos maiores hacks e programas mais atuais para seu console!  Você pode baixar a souce neste link: https://github.com/gorpo/TCXS_Pyject_PlayStation3_Store_Creator e o tutorial de uso do programa neste link: https://www.youtube.com/watch?v=EQbymbu5htA'.format(msg['from']['first_name']),reply_to_message_id=msg['message_id'])




        #if msg['text'] == 'qq deu':
        #    await bot.sendMessage(msg['chat']['id'], '`{} deu nada não feio. `'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        elif msg['text'].split()[0] == 'corpo':
            await bot.sendMessage(msg['chat']['id'], '`gorpo = corpo`','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'site tcxs' or msg['text'].split()[0] == '/site':
            await bot.sendMessage(msg['chat']['id'], '`{} Passa la e da um confere nos posts e nos hacks!` http://tcxsproject.com.br'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'facebook' or msg['text'].split()[0] == 'face' or msg['text'].split()[0] == '/facebook' :
            await bot.sendMessage(msg['chat']['id'], '`{} eu sou um bot tão foda q tenho meu proprio facebook, mas dei o nome dele de manicomio, entra la e veja as bizarrice e poste algumas tambem,` http://tcxsproject.com.br/facebook/'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'netflix' or msg['text'].split()[0] == '/netflix':
            await bot.sendMessage(msg['chat']['id'], '`{} Netflix o caralho eu tenho minha propria netflix chamo ela de ManicomioFlix, entra la e confere, cria uma conta é gratis!` http://tcxsproject.com.br/flix/'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'anime' or msg['text'].split()[0] == '/anime':
            await bot.sendMessage(msg['chat']['id'], '`{} Tenho um site de anime, ainda mais com umas bizarrice da um confere la:` http://tcxsproject.com.br/anime'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'pkg' or msg['text'].split()[0] == '/pkg':
            await bot.sendMessage(msg['chat']['id'], '`❤Tenho um site de jogos em PKG para PS3 totalmente gratis, confere meus posts la:` http://tcxsproject.com.br/category/nohan/','markdown',
                                                  reply_to_message_id=msg['message_id'])    

        elif msg['text'].split()[0] == 'biblioteca' or msg['text'].split()[0] == '/biblioteca':
            await bot.sendMessage(msg['chat']['id'], '`Eu tenho uma biblioteca hacker cheinha de livros hacker bem como alguns livros sobre ghoetia, satanismo e anarquia, confere la:` http://tcxsproject.com.br/dev','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == '.':
            await bot.sendMessage(msg['chat']['id'], '@{}`Relaxa que eu to aqui `'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'brick':
            await bot.sendMessage(msg['chat']['id'], 'https://www.youtube.com/watch?v=AaQJ23Hosc8','markdown',
                                                  reply_to_message_id=msg['message_id'])     
        



            return True

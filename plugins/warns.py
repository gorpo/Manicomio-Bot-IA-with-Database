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


from db_handler import cursor, conn
from .admins import is_admin


cursor.execute('''CREATE TABLE IF NOT EXISTS user_warns (
                                                         user_id INTEGER,
                                                         chat_id INTEGER,
                                                         count INTEGER)''')


def get_warns(chat_id, user_id):
    cursor.execute('SELECT count FROM user_warns WHERE chat_id = ? AND user_id = ?', (chat_id, user_id))
    return cursor.fetchone()[0]


def get_warns_limit(chat_id):
    cursor.execute('SELECT warns_limit FROM chats WHERE chat_id = ?', (chat_id,))
    return cursor.fetchone()[0]


def add_warns(chat_id, user_id, number):
    cursor.execute('SELECT * FROM user_warns WHERE chat_id = ? AND user_id = ?', (chat_id, user_id))
    if cursor.fetchone():
        cursor.execute('UPDATE user_warns SET count = count + ? WHERE chat_id = ? AND user_id = ?',
                       (number, chat_id, user_id))
        conn.commit()
    else:
        cursor.execute('INSERT INTO user_warns (user_id, chat_id, count) VALUES (?,?,?)', (user_id, chat_id, number))
        conn.commit()
    return True


def reset_warns(chat_id, user_id):
    cursor.execute('DELETE FROM user_warns WHERE chat_id = ? AND user_id = ?', (chat_id, user_id))
    conn.commit()
    return True


async def warns(msg):
    if msg.get('text'):
        if msg['text'].split()[0] == '/warn' or msg['text'].split()[0] == 'aviso':
            
            if msg['chat']['type'] == 'private':
                await bot.sendMessage(msg['chat']['id'], 'Este comando só funciona em grupos ¯\\_(ツ)_/¯')
            else:
                warns_limit = get_warns_limit(msg['chat']['id']) or 3
                if msg.get('reply_to_message'):
                    reply_id = msg['reply_to_message']['from']['id']
                    reply_name = msg['reply_to_message']['from']['first_name']
                elif len(msg['text'].split()) > 1:
                    u_id = msg['text'].split()[1]
                    try:
                        get = await bot.getChat(u_id)
                        reply_id = get['id']
                        reply_name = get['first_name']
                    except (TelegramError, KeyError):
                        await bot.sendMessage(msg['chat']['id'],
                                              'ID inválida ou desconhecida. use nesse formato: /warn ID do usuário',
                                              reply_to_message_id=msg['message_id'])
                        return
                else:
                    reply_id = None

                adm = await is_admin(msg['chat']['id'], msg['from']['id'], reply_id)

                if adm['user']:
                    try:
                        int(reply_id)
                    except (TypeError, ValueError):
                        return await bot.sendMessage(msg['chat']['id'], 'Responda alguém ou informe sua ID',
                                                     reply_to_message_id=msg['message_id'])
                    if adm['bot']:
                        if adm['reply']:
                            await bot.sendMessage(msg['chat']['id'], 'Esse aí tem admin',
                                                  reply_to_message_id=msg['message_id'])
                        else:
                            add_warns(msg['chat']['id'], reply_id, 1)
                            user_warns = get_warns(msg['chat']['id'], reply_id)
                            if user_warns >= warns_limit:
                                await bot.kickChatMember(msg['chat']['id'], reply_id)
                                await bot.sendMessage(msg['chat']['id'],
                                                      '{} seu filho da puta, vc foi banido(a) pois atingiu o limite de advertências'.format(
                                                          reply_name),
                                                      reply_to_message_id=msg['message_id'])
                            else:
                                await bot.sendMessage(msg['chat']['id'],
                                                      '{} Foi advertido(a) ({}/{})'.format(reply_name, user_warns,
                                                                                           warns_limit),
                                                      reply_to_message_id=msg['message_id'])
                    else:
                        await bot.sendMessage(msg['chat']['id'], 'Ei, eu nao tenho admin aqui, me poe de admin que eu como cu destes pau no cu!',
                                              reply_to_message_id=msg['message_id'])
            return True


        elif msg['text'].split()[0] == '/unwarn' or msg['text'].split()[0] == '!unwarn':
            
            if msg['chat']['type'] == 'private':
                await bot.sendMessage(msg['chat']['id'], 'Este comando só funciona em grupos ¯\\_(ツ)_/¯')
            else:
                if msg.get('reply_to_message'):
                    reply_id = msg['reply_to_message']['from']['id']
                    reply_name = msg['reply_to_message']['from']['first_name']
                elif len(msg['text'].split()) > 1:
                    u_id = msg['text'].split()[1]
                    try:
                        get = await bot.getChat(u_id)
                        reply_id = get['id']
                        reply_name = get['first_name']
                    except (TelegramError, KeyError):
                        await bot.sendMessage(msg['chat']['id'],
                                              'ID inválida ou desconhecida. use nesse formato: /unwarn ID do usuário',
                                              reply_to_message_id=msg['message_id'])
                        return
                else:
                    reply_id = None

                adm = await is_admin(msg['chat']['id'], msg['from']['id'], reply_id)

                if adm['user']:
                    try:
                        int(reply_id)
                    except (TypeError, ValueError):
                        return await bot.sendMessage(msg['chat']['id'], 'Responda alguém ou informe sua ID.',
                                                     reply_to_message_id=msg['message_id'])
                    if adm['reply']:
                        await bot.sendMessage(msg['chat']['id'], 'Esse aí tem admin.',
                                              reply_to_message_id=msg['message_id'])
                    else:
                        reset_warns(msg['chat']['id'], reply_id)
                        await bot.sendMessage(msg['chat']['id'], 'Advertências de {} removidas.'.format(reply_name),
                                              reply_to_message_id=msg['message_id'])
            return True

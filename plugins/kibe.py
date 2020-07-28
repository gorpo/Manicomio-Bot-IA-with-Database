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

import os
from amanobot.namedtuple import InlineKeyboardMarkup
from amanobot.exception import TelegramError
from config import bot, bot_username

async def kibe(msg):
    if msg.get('text'):
        if msg['text'].startswith('/stickerid') or msg['text'].startswith('!stickerid'):
            if msg.get('reply_to_message') and msg['reply_to_message'].get('sticker'):
                await bot.sendMessage(msg['chat']['id'], "Sticker ID:\n```" +
                                      msg['reply_to_message']['sticker']['file_id'] + "```",
                                      parse_mode='markdown', reply_to_message_id=msg['message_id'])
            else:
                await bot.sendMessage(msg['chat']['id'], "Responda um Sticker com este comando para ter sua ID.",
                                      reply_to_message_id=msg['message_id'])
            return True


        elif msg['text'].startswith('/getsticker') or msg['text'].startswith('!getsticker'):
            
            if msg.get('reply_to_message') and msg['reply_to_message'].get('sticker'):
                chat_id = msg['chat']['id']
                file_id = msg['reply_to_message']['sticker']['file_id']
                await bot.download_file(file_id, 'sticker.png')
                await bot.sendDocument(chat_id, document=open('sticker.png', 'rb'))
                os.remove("sticker.png")
            else:
                await bot.sendMessage(msg['chat']['id'], "Responda um sticker com este comando para baixar ele em png.",
                                      reply_to_message_id=msg['message_id'])
            return True


        elif msg['text'].startswith('/kibe') or msg['text'].startswith('!kibe') or msg['text'] == 'kibe':
            
            if msg.get('reply_to_message') and msg['reply_to_message'].get('sticker'):
                user = msg['from']
                file_id = msg['reply_to_message']['sticker']['file_id']
                await bot.download_file(file_id, str(msg['from']['id']) + '_kibe_sticker.png')
                packname = "a" + str(user['id']) + "_by_" + bot_username
                if len(msg['text'][5:]) > 0:
                    sticker_emoji = msg['text'].split()[1]
                else:
                    try:
                        sticker_emoji = msg['reply_to_message']['sticker']['emoji']
                    except KeyError:
                        os.remove(str(msg['from']['id']) + "_kibe_sticker.png")
                        return await bot.sendMessage(msg['chat']['id'],
                                                     'Você precisa definir um emoticon para este sticker.',
                                                     reply_to_message_id=msg['message_id'])
                success = False
                try:
                    await bot.addStickerToSet(user_id=user['id'], name=packname,
                                              png_sticker=open(str(msg['from']['id']) + '_kibe_sticker.png', 'rb'),
                                              emojis=sticker_emoji)
                    success = True
                except TelegramError as e:
                    if e.description == "Bad Request: STICKERSET_INVALID":
                        await bot.sendMessage(msg['chat']['id'], "Use /criar_sticker para criar um pacote de sticker antes.",
                                              reply_to_message_id=msg['message_id'])
                        return
                    elif e.description == "Internal Server Error: sticker set not found":
                        success = True
                    else:
                        await bot.sendMessage(msg['chat']['id'], 'Error: ' + e.description,
                                              reply_to_message_id=msg['message_id'])
                        return
                finally:
                    os.remove(str(msg['from']['id']) + "_kibe_sticker.png")

                if success:
                    await bot.sendMessage(msg['chat']['id'],
                                          "Sticker successfully added to [pack](t.me/addstickers/%s)" % packname,
                                          parse_mode='markdown', reply_to_message_id=msg['message_id'])

            else:
                await bot.sendMessage(msg['chat']['id'], "Responda com /kibe para copiar o sticker para o pacote de stickers.")
            return True


        elif msg['text'].startswith('/criar_sticker') or msg['text'].startswith('!make_kibe'):
            
            user = msg['from']
            name = user['first_name']
            name = name[:50]
            packname = "a" + str(user['id']) + "_by_" + bot_username
            success = False
            try:
                success = await bot.createNewStickerSet(user['id'], packname, name + "'s ManicomiO ",
                                                        png_sticker="https://i.imgur.com/0euQLEU.png",
                                                        emojis='©')
            except TelegramError as e:
                if e.description == "Bad Request: o nome de pacote de stickers ja existe.":
                    await bot.sendMessage(msg['chat']['id'],
                                          "Seu pacote de stickers [here](t.me/addstickers/%s)" % packname,
                                          parse_mode='markdown', reply_to_message_id=msg['message_id'])
                elif e.description == "Bad Request: PEER_ID_INVALID":
                    await bot.sendMessage(msg['chat']['id'], "Contate-me no privado primeiro.",
                                          reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                              [dict(text='Start', url="t.me/{}".format(bot_username))]]),
                                          reply_to_message_id=msg['message_id'])
                else:
                    await bot.sendMessage(msg['chat']['id'],
                                          "Falha ao criar o pacote de Stickers.\n\n" + str(e),
                                          reply_to_message_id=msg['message_id'])

            if success:
                await bot.sendMessage(msg['chat']['id'],
                                      "Pacote de Stickers criado com sucesso, veja ele aqui [here](t.me/addstickers/%s)" % packname,
                                      parse_mode='markdown', reply_to_message_id=msg['message_id'])
            return True

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


from config import bot, bot_username
from db_handler import conn, cursor
from .admins import is_admin


def get_rules(chat_id):
    cursor.execute('SELECT rules FROM chats WHERE chat_id = (?)', (chat_id,))
    try:
        return cursor.fetchone()[0]
    except IndexError:
        return None


def set_rules(chat_id, rules):
    cursor.execute('UPDATE chats SET rules = ? WHERE chat_id = ?', (rules, chat_id))
    conn.commit()


async def rules(msg):
    if msg.get('text'):

        if msg['text'].startswith('/start_rules'):
            chat_id = msg['chat']['id']
            rules = get_rules(int(chat_id)) or 'Sem regras!'
            await bot.sendMessage(msg['chat']['id'], rules, 'Markdown')
            return True


        elif msg['text'] == '/rules' or msg['text'] == '!rules' or msg['text'] == '/regras' or msg['text'] == 'regras' or msg['text'] == '/regras@' + bot_username or msg['text'] == '/rules@' + bot_username:
            
            rules = get_rules(msg['chat']['id']) or 'Sem regras!'

            await bot.sendMessage(msg['chat']['id'], rules, 'Markdown',reply_to_message_id=msg['message_id'])
            return True


        elif msg['text'].split()[0] == '/defrules' or msg['text'].split()[0] == '/defregras' or msg['text'].split()[0] == '/defregras' or msg['text'].split()[0] == '!defregras' or msg['text'].split()[0] == '/defregras@' + bot_username or msg['text'].split()[0] == '/defrules@' + bot_username:
            
            if (await is_admin(msg['chat']['id'], msg['from']['id']))['user']:
                if len(msg['text'].split()) == 1:
                    await bot.sendMessage(msg['chat']['id'], 'Uso: /defregras Regras do grupo (suporta Markdown)',
                                          reply_to_message_id=msg['message_id'])
                elif msg['text'].split()[1] == 'reset':
                    set_rules(msg['chat']['id'], None)
                    await bot.sendMessage(msg['chat']['id'], 'As regras do grupo foram redefinidas com sucesso.',
                                          reply_to_message_id=msg['message_id'])
                else:
                    set_rules(msg['chat']['id'], msg['text'].split(' ', 1)[1])
                    await bot.sendMessage(msg['chat']['id'], 'As regras do grupo foram definidas com sucesso.',
                                          reply_to_message_id=msg['message_id'])
            return True

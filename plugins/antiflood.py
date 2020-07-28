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

from db_handler import conn, cursor
from .admins import is_admin
from config import bot

cursor.execute('CREATE TABLE IF NOT EXISTS antiflood (chat_id, user_id, unix_time)')


async def antiflood(msg):
    if msg.get('chat') and msg['chat']['type'].endswith('group') and msg.get('from'):
        adm = await is_admin(msg['chat']['id'], msg['from']['id'])
        if not adm['user'] and adm['bot']:
            # Delete old rows.
            cursor.execute('DELETE FROM antiflood WHERE chat_id = ? AND unix_time < ?',
                           (msg['chat']['id'], int(time.time()) - 5))
            conn.commit()

            # Insert antiflood row.
            cursor.execute('INSERT INTO antiflood (chat_id, user_id, unix_time) VALUES (?,?,?)',
                           (msg['chat']['id'], msg['from']['id'], int(time.time())))
            conn.commit()

            # Get total rows count.
            cursor.execute('SELECT COUNT(*) FROM antiflood WHERE chat_id = ? AND user_id = ?',
                           (msg['chat']['id'], msg['from']['id']))
            msgs = cursor.fetchone()[0]

            if msgs == 5:
                await bot.sendMessage(msg['chat']['id'], 'Flood!')
                return True

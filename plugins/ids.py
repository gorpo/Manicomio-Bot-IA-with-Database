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


from config import bot, bot_username


async def ids(msg):
    if msg.get('text'):
        if msg['text'] == '/id' or msg['text'] == '!id' or msg['text'] == '/id@' + bot_username or msg['text'] == 'id':

            if msg['chat']['type'] == 'private':
                if 'last_name' in msg['from']:
                    last_name = msg['from']['last_name']
                else:
                    last_name = ''
                if 'username' in msg['from']:
                    username = '@' + msg['from']['username']
                else:
                    username = ''
                await bot.sendMessage(msg['chat']['id'], '''
*Informações:*

*Nome:* `{}`{}{}
*ID:* `{}`
*Idioma:* `{}`
*Tipo de chat:* `{}`'''.format(msg['from']['first_name'],
                               '\n*Sobrenome:* `{}`'.format(last_name) if last_name != '' else '',
                               '\n*Último nome:* `{}`'.format(username) if username != '' else '',
                               msg['from']['id'],
                               msg['from']['language_code'],
                               msg['chat']['type']),
                                      parse_mode='Markdown',
                                      reply_to_message_id=msg['message_id'])
            else:
                sent = await bot.sendMessage(msg['chat']['id'], '⏰ Consultando informações...',
                                             reply_to_message_id=msg['message_id'])
                members = await bot.getChatMembersCount(msg['chat']['id'])
                if 'username' in msg['chat']:
                    chat_username = '@' + msg['chat']['username']
                else:
                    chat_username = ''
                if 'language_code' in msg['from']:
                    lang_code = msg['from']['language_code']
                else:
                    lang_code = '-'
                first_name = msg['from']['first_name']
                if 'last_name' in msg['from']:
                    last_name = msg['from']['last_name']
                else:
                    last_name = ''
                if 'username' in msg['from']:
                    username = '@' + msg['from']['username']
                else:
                    username = ''
                user_id = msg['from']['id']
                if 'reply_to_message' in msg:
                    from_info = msg['reply_to_message']['from']
                    first_name = from_info['first_name']

                    if 'last_name' in from_info:
                        last_name = from_info['last_name']
                    else:
                        last_name = ''

                    user_id = from_info['id']

                    if 'username' in from_info:
                        username = '@' + from_info['username']
                    else:
                        username = ''

                    if 'language_code' in from_info:
                        lang_code = from_info['language_code']
                    else:
                        lang_code = '-'

                await bot.editMessageText(
                    (msg['chat']['id'], sent['message_id']),
                    text='''
*Informações do chat:*

*Nome:* `{}`{}{}
*ID:* `{}`
*Idioma:* `{}`

*Nome do grupo:* `{}`{}
*ID do grupo:* `{}`
*Mensagens:* `{}`
*Tipo de chat:* `{}`
*Membros:* `{}`'''.format(
                        first_name,
                        '\n*Último nome:* `{}`'.format(last_name) if last_name != '' else '',
                        '\n*Username:* `{}`'.format(username) if username != '' else '',
                        user_id,
                        lang_code,
                        msg['chat']['title'],
                        '\n*Username do grupo:* `{}`'.format(chat_username) if chat_username != '' else '',
                        msg['chat']['id'],
                        msg['message_id'],
                        msg['chat']['type'],
                        members
                    ),
                    parse_mode='Markdown'
                )
            return True

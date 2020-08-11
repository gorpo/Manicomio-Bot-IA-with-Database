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


from amanobot.exception import TelegramError
import sqlite3
from config import bot
from plugins.admins import is_admin



async def ia_mensagens_proibidas(msg):
    try:
        adm = await is_admin(msg['chat']['id'], msg['from']['id'], msg['from']['id'])
        conexao_sqlite = sqlite3.connect('bot_database.db')
        conexao_sqlite.row_factory = sqlite3.Row
        cursor_sqlite = conexao_sqlite.cursor()
        chat_id = msg['chat']['id']
        chat_type = msg['chat']['type']
        # SISTEMA QUE DELETA MENSAGENS PROIBIDAS --------------------------------------------------------------------->
        if chat_type == 'supergroup' and msg.get('text'):# verifica se a palavra é proibida, se for deleta a mensagem do usuario e envia um aviso------>
                cursor_sqlite.execute("""SELECT * FROM proibido; """)
                mensagens_proibidas = cursor_sqlite.fetchall()
                texto = msg['text']
                for mensagem in mensagens_proibidas:
                    if mensagem['termo'] in texto and not 'permitir' in texto:
                        try:#em caso de erro inverter este try except pelo de baixo pois da erro entre message_id e reply_to_message
                            await bot.deleteMessage((msg['chat']['id'], msg['message_id']))
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `você usou uma palavra proibida, não fale bosta aqui!`",'markdown')
                        except TelegramError:
                            try:
                                await bot.deleteMessage((msg['chat']['id'], msg['reply_to_message']['message_id']))
                                await bot.sendMessage(chat_id,f"@{msg['from']['username']} `você usou uma palavra proibida, não fale bosta aqui!`",'markdown')
                            except TelegramError:
                                pass

        try:
            if msg.get('text'):
                texto = msg['text']
                if texto.lower().startswith('proibir') and adm['user'] == True:  # proibe as palavras e as cadastra na Database------------------------------->
                    palavra_proibida = texto[8:]
                    if palavra_proibida.lower() == 'proibir' or palavra_proibida.lower() == '' or palavra_proibida.lower() == ' '  or palavra_proibida.lower() == '' or palavra_proibida.lower() == 'comandos' or palavra_proibida.lower() == '/help' or palavra_proibida.lower() == 'fale sobre' or palavra_proibida.lower() == 'frequencia' or palavra_proibida.lower() == 'cmd' or palavra_proibida.startswith('/') or palavra_proibida.startswith('#') or palavra_proibida.startswith('$') or palavra_proibida.startswith('%') or palavra_proibida.startswith('@'):
                        await bot.sendMessage(chat_id,f"@{msg['from']['username']} `não posso proibir esta palavra, talvez ela seja um comando meu.`",'markdown')
                        pass
                    else:
                        cursor_sqlite.execute(f"""INSERT INTO proibido VALUES('{palavra_proibida}')""")
                        conexao_sqlite.commit()
                        await bot.sendMessage(chat_id,f'🤖🚫 `Proibido:`***{palavra_proibida}***\nPara voltar permitir esta palavra use o comando `permitir`, para ver palavras proibidas use `proibidas`','markdown', reply_to_message_id=msg['message_id'])
                if texto.lower().startswith('proibir') and adm['user'] == False:
                    await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                if texto.lower().startswith('permitir') and adm['user'] == True:  # permite novamente as palavras e as descadastra na Database------------------------------->
                    palavra_permitida = texto[9:]
                    cursor_sqlite.execute(f"""DELETE FROM proibido WHERE termo='{palavra_permitida}'""")
                    conexao_sqlite.commit()
                    await bot.sendMessage(chat_id, f'🤖✔️ `Permitido:`***{palavra_permitida}***\nPara voltar proibir esta palavra use o comando `proibir`, para ver palavras proibidas use `proibidas`','markdown', reply_to_message_id=msg['message_id'])
                if texto.lower().startswith('permitir') and adm['user'] == False:
                    await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')

                if texto.lower().startswith('proibidas'):  # lista as palavras proibidas cadastradas  na Database------------------------------->
                    cursor_sqlite.execute("""SELECT * FROM proibido; """)
                    mensagens_proibidas = cursor_sqlite.fetchall()
                    todas_proibidas = []
                    separador = ' \n'
                    for result in mensagens_proibidas:
                        todas_proibidas.append(result['termo'])
                    await bot.sendMessage(chat_id,f'🤖 `Palavras Proibidas:`\n ***{separador.join(map(str, todas_proibidas))}***','markdown', reply_to_message_id=msg['message_id'])
        except Exception as e:
            pass
# excessao final para tratar do codigo todo--->
    except:
        pass
        return True

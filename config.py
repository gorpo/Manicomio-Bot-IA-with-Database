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


import amanobot.aio
import asyncio
import sqlite3

"""
#HEROKU CONFIG - rodar no heroku use as linhas abaixo------->
token = os.environ['TELEGRAM_TOKEN']
logs = os.environ['LOGS']
sudoers = os.environ['SUDOERS']

LOCAL CONFIG rodar em local host use as linhas abaixo--->
token =  "1096480409:AAE6sg6eJZtH5Z_TEIzgq10SQtCvGf4KYSc"
logs = -1001402280935
sudoers = [522510051,]
backups_chat = 522510051  # Put a 0, False or None to disable ou seu id privado ou id privado de um canal ou grupo
keys = dict(
    here = {'app_id': 'key_id_here', 'app_code': 'key_code_here'},  # https://here.com
    yandex = 'trnsl.1.1.20190811T184100Z.f3e1e6d6d3507525.7ea9c786af32b18cedeb125ca46cc2d9ee154e09',
    giphy = '7f6ws7EvslO9BuaAKie9BieyYnD3OkkT',
    token_dropbox = 's4rxVFP2mcAAAAAAAAC2eXinDL33K0tSIhnR1chqOmrtBPy-Dl6Ll0znnRP3Phm5',
    token_imgur = "ebfc2558bda96e5",
    token_bitly = ["a001cef9d44ed8083ed4d952d475e98079e60577", ],  #link?
)
"""

# database dos tokens, inserir tokens na database usando painel ou via CLI
conexao_sqlite = sqlite3.connect('bot_database.db')
conexao_sqlite.row_factory = sqlite3.Row
cursor_sqlite = conexao_sqlite.cursor()
cursor_sqlite.execute("""SELECT * FROM tokens_bot""")
tokens = cursor_sqlite.fetchall()

# token do bot pegar no @botfather
token = tokens[0]['token_bot']
# contem a id do canal que serão enviados arquivos captados e logs
logs = int(tokens[0]['id_canal'])
# id do sudo | quem hospeda o bot para ter permissoes especiais
sudoers = [int(tokens[0]['id_pessoal']), ]
# id do chat que receberá os backups, pode ser um grupo / canal / id pessoal
backups_chat = int(tokens[0]['id_backups'])

keys = dict(
    token_dropbox=tokens[0]['token_dropbox'],  # https://www.dropbox.com/developers/
    token_giphy=f"{tokens[0]['token_giphy']}",  # https://developers.giphy.com
    token_weather=f"{tokens[0]['token_weather']}",  # https://api.hgbrasil.com/weather
    token_imgur=f"{tokens[0]['token_imgur']}",  # https://api.imgur.com/oauth2/addclient
    token_yandex=tokens[0]['token_yandex'],  # https://tech.yandex.com/translate
    token_bitly=[f"{tokens[0]['token_bitly']}", ],  # https://dev.bitly.com/v4/
)

# variaveis do bot essenciais
loop = asyncio.get_event_loop()
bot = amanobot.aio.Bot(token)
na_bot = amanobot.Bot(token)
me = loop.run_until_complete(bot.getMe())
bot_username = me['username']
bot_id = me['id']

# horario de backup e git
backup_hours = ['15:56']
git_repo = ('https://github.com/gorpoorko/Manicomio-Bot-IA', 'master')  # repositorio para upgrade do bot
max_time = 60
version = '7.0'

enabled_plugins = [
    'processmsg',
    'start',
    'rules',
    'admins',
    'criar_sticker',
    'translate',
    'rextester',
    'inlines',
    'welcome',
    'warns',
    'youtube',
    'extras',
    'reddit',
    'sudos',
    'ids',
    'misc',
    'tcxs',
    'trollagens',
    'calculadora',
    'users',
    'antiflood',
    'dropbox_gdrive',
    'link_direto',
    'cria_site_telegraph',
    'inteligencia',
    'ia_privado_bot',
    'ia_mensagens_proibidas',
    'permanencia',
    'ia_cadastro_manual',
    'ia_cadastro_perguntas',
    'ia_crawler_sites',

]
#'ia_deepnude',
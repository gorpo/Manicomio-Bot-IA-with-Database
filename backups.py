# Copyright (C) 2018-2019 Amano Team <contact@amanoteam.ml>
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
import time
import schedule
from datetime import datetime
from utils import backup_sources
from multiprocessing import Process
from config import backups_chat, backup_hours, na_bot,token_dropbox
import dropbox
import time
from config import bot, version, bot_username, git_repo,logs,sudoers
import os
from datetime import datetime
import sqlite3


#função que faz os backups com base em hora
def backup_func():
    cstrftime = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
    file = backup_sources('Backup_automatico_bot')
    targetfile = f"/GDRIVE_TCXSPROJECT/MARCINHO_BOT/{file}"
    d = dropbox.Dropbox(token_dropbox)
    with open(file, "rb") as f:
        meta = d.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))
        link = d.sharing_create_shared_link(targetfile)
        url = link.url
        print(f"Backup automatico concluido: {cstrftime}\nDownload: {url}")
        na_bot.sendMessage(logs,f"Backup automatico concluido: {cstrftime}\nDownload: {url}")
    os.remove(file)
    file1 = backup_sources('Backup_bot')
    na_bot.sendDocument(logs, open(file1, 'rb'), caption="📅 " + cstrftime)
    os.remove(file1)


    #sistema de verificaçao automatica para banimento no grupo
    try:
        conexao_sqlite = sqlite3.connect('bot_database.db')
        conexao_sqlite.row_factory = sqlite3.Row
        cursor_sqlite = conexao_sqlite.cursor()
        hoje = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        cursor_sqlite.execute("""SELECT * FROM permanencia; """)
        resultados = cursor_sqlite.fetchall()
        for resutado in resultados:
            data_inicial = resutado['data_inicial']
            data_ban = resutado['data_final']
            id_doador = resutado['id_doador']
            doador = resutado['doador']
            dias = resutado['dias']
            aviso = resutado['data_aviso']
            id_grupo = resutado['id_grupo']
            #ALERTA DE AVISO PARA O DOADOR----:
            try:
                if hoje[0:2] == aviso[0:2]:
                    na_bot.sendMessage(id_grupo,f"🤖 {doador} ***Falta uma semana para você grupo, caso ainda tenha interesse em continuar usando a loja faça uma doação, envie o comprovante aqui no grupo que um de nossos administradores irá colocar mas dias em sua permanencia.***\n`Usuário:` {doador}\n`Id_Usuário:` {id_doador}\n`Início:` {data_inicial}\n`Termino:` {data_ban}\n`Permanência:` {dias}",'markdown')
                #BANE O USUARIO CASO A DATA TENHA SIDO IGUAL A DO DIA HOJE
                if hoje[3:5] == data_ban[3:5]:
                    na_bot.kickChatMember(str(id_grupo), id_doador)
                    cursor_sqlite.execute(f"""DELETE FROM permanencia WHERE doador='{doador}'""")
                    conexao_sqlite.commit()
                    na_bot.sendMessage(str(id_grupo),f"🤖 ***Removido do grupo pois deu a sua permanência do grupo.***\n`Usuário:` {doador}\n`Id_Usuário:` {id_doador}\n`Início:` {data_inicial}\n`Termino:` {data_ban}\n`Permanência:` {dias}",'markdown')
                    na_bot.unbanChatMember(str(id_grupo), id_doador)
            except:
                pass
    except Exception as e:
        print(e)





def backup_scheduler(target):
    for hour in backup_hours:
        schedule.every().day.at(hour).do(target)
    while True:
        schedule.run_pending()
        time.sleep(5)


def backup_service():
    p = Process(target=backup_scheduler, args=(backup_func,))
    p.start()

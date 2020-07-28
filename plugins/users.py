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
from amanobot.namedtuple import InlineKeyboardMarkup
import keyboard
from datetime import datetime
from config import bot, version, bot_username, git_repo,logs,sudoers
import sqlite3
import os
from plugins.admins import is_admin



async def users(msg):
    # variaveis que iniciam a Database para enviar a att paga pelos BOTOES
    conexao_sqlite = sqlite3.connect('bot_database.db')
    conexao_sqlite.row_factory = sqlite3.Row
    cursor_sqlite = conexao_sqlite.cursor()
    # database logs ---->
    conexao_logs = sqlite3.connect('bot_database_logs.db')
    conexao_logs.row_factory = sqlite3.Row
    cursor_logs = conexao_logs.cursor()
    try:
        id_usuario = msg['from']['id']
        adm = await is_admin(msg['chat']['id'], msg['from']['id'], id_usuario)
    except Exception as e:
        pass
    if msg.get('text') and msg['chat']['type'] == 'supergroup':
        if msg['from']['first_name']:
            pass
            print('->Usuario:{} ->Envio:{} ->Grupo:{} ->Data/Hora:{} '.format(msg['from']['first_name'],msg['text'],msg['chat']['title'],time.ctime()))


## SISTEMA DE GRAVAÇÃO E ENVIO DE LOGS ---------------------------------------------------------------------------------------------------------------->
        if msg['text'].lower() == 'logs':
            if adm['user'] == True:
                cursor_logs.execute("""SELECT * FROM mensagens ; """)
                mensagens_logs = cursor_logs.fetchall()
                arquivo_logs = open('arquivos/logs.txt', 'a',encoding='utf-8')
                arquivo_logs.write('-------[+] REGISTO DE MENSAGENS CAPTADAS PELO BOT NOS GRUPOS E PRIVADO [+]-------\n\n')
                for mensagem in mensagens_logs:
                    grupo = mensagem['grupo']
                    tipo_grupo = mensagem['tipo_grupo']
                    id_grupo = mensagem['id_grupo']
                    usuario = mensagem['usuario']
                    id_usuario = mensagem['id_usuario']
                    linguagem = mensagem['linguagem']
                    tipo = mensagem['tipo']
                    data = mensagem['data']
                    mensagem = mensagem['mensagem']
                    try:
                        texto = f"Usuario: {usuario} |Id Usuario:{id_usuario} | Linguagem: {linguagem} | Grupo: {grupo} | Id Grupo: {id_grupo} | Tipo Grupo: {tipo_grupo} Tipo: {tipo} | Data: {data} ----->\nMensagem: {mensagem}\n"
                    except:
                        texto = ''
                    arquivo_logs.write(texto)
                arquivo_logs.close()
                await bot.sendDocument(msg['chat']['id'], open('arquivos/logs.txt','rb'), reply_to_message_id=msg['message_id'])
                await bot.sendMessage(msg['chat']['id'], '`{} Esta aqui o log de conversas que tenho armazenado, espero que não tenha nada neste log que te incrimine!`'.format(msg['from']['first_name']),'markdown', reply_to_message_id=msg['message_id'])
                os.remove('arquivos/logs.txt')
            else:
                await bot.sendMessage(msg['chat']['id'], f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')


        #LIMPAR OS LOGS
        if msg['text'].lower() == 'limpar logs' or msg['text'].lower() == 'apagar logs' or msg['text'].lower() == 'backup logs':
            if adm['user'] == True:
                cursor_logs.execute("""SELECT * FROM mensagens; """)
                mensagens_logs = cursor_logs.fetchall()
                arquivo_logs = open('arquivos/logs.txt', 'a',encoding='utf-8')
                arquivo_logs.write('-------[+] REGISTO DE MENSAGENS CAPTADAS PELO BOT NOS GRUPOS E PRIVADO [+]-------\n\n')
                for mensagem in mensagens_logs:
                    grupo = mensagem['grupo']
                    tipo_grupo = mensagem['tipo_grupo']
                    id_grupo = mensagem['id_grupo']
                    usuario = mensagem['usuario']
                    id_usuario = mensagem['id_usuario']
                    linguagem = mensagem['linguagem']
                    tipo = mensagem['tipo']
                    data = mensagem['data']
                    mensagem = mensagem['mensagem']
                    try:
                        texto = f"Usuario: {usuario} |Id Usuario:{id_usuario} | Linguagem: {linguagem} | Grupo: {grupo} | Id Grupo: {id_grupo} | Tipo Grupo: {tipo_grupo} Tipo: {tipo} | Data: {data} ----->\nMensagem: {mensagem}\n"
                    except:
                        texto = ''
                    arquivo_logs.write(texto)
                arquivo_logs.close()
                await bot.sendDocument(msg['chat']['id'], open('arquivos/logs.txt', 'rb'),reply_to_message_id=msg['message_id'])
                await bot.sendMessage(msg['chat']['id'],'`{} Esta aqui o Backup de logs de conversas que tenho armazenado, caso preciso guarde este arquivo pois irei limpar a Database`'.format(msg['from']['first_name']), 'markdown', reply_to_message_id=msg['message_id'])
                os.remove('arquivos/logs.txt')
                cursor_logs.execute("""DELETE FROM mensagens""")
                conexao_logs.commit()
                await bot.sendMessage(msg['chat']['id'], f"🤖 {msg['from']['first_name']} Todas os logs de usuários e grupos foram apagados!")
            else:
                await bot.sendMessage(msg['chat']['id'], f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')



#SISTEMA DE BOTOES INICIO ---------------------------------------------------------------->
        if  msg['text'].lower() == 'comando' or msg['text'] == '/help'  or msg['text'] == '/comandos' or msg['text'] == 'comandos' or 'help' in msg['text'].lower() or 'ajuda' in msg['text'].lower():
            kb = InlineKeyboardMarkup(inline_keyboard=[
                [dict(text='📦 Store Free', callback_data='store_free')] +
                [dict(text="📦 Store Doadores", callback_data='store_doadores')],
                [dict(text='🦸 Usuários', callback_data='comandos_usuarios')] +
                [dict(text="🤖‍ Admin's", callback_data='comandos_admins')],
                [dict(text='🧰 Ferramentas', callback_data='ferramentas_gerais')] +
                [dict(text='📣 Info | Extras', callback_data='infos_extras')],])
            await bot.sendMessage(msg['chat']['id'],f"***{msg['from']['first_name']} Aqui está uma lista com todos meus comandos e informações que você precisa saber.***" ,'markdown',  reply_markup=kb)
        #return True


#PEGA OS DADOS DO keyboard.py ----------------------:
    elif msg.get('data') and msg.get('message'):

        if msg['data'] == 'inicio_menu':# precisa de dois menus para voltar para o inicio criando um loop entre os dois----->
            kb = InlineKeyboardMarkup(inline_keyboard=[
                [dict(text='📦 Store Free', callback_data='store_free')] +
                [dict(text="📦 Store Doadores", callback_data='store_doadores')],
                [dict(text='🦸 Usuários', callback_data='comandos_usuarios')] +
                [dict(text="🤖‍ Admin's", callback_data='comandos_admins')],
                [dict(text='🧰 Ferramentas', callback_data='ferramentas_gerais')] +
                [dict(text='📣 Info | Extras', callback_data='infos_extras')], ])
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"***{msg['from']['first_name']} Aqui está uma lista com todos meus comandos e informações que você precisa saber.***", 'markdown',reply_markup=kb)

#TCXS STORE FREE PKG    ------------------------------------------------------------------------------------------------------------------------->
        elif msg['data'] == 'store_free':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"```------  Espero que tenha um pendrive em mãos e saiba usar a\n loja, não daremos suporte para USUARIOS GRATUITOS, agora  copie os arquivos abaixo para a raiz de um pendrive e coloque na USB direita do seu console, caso use HAN instale o FIX, caso use HEN apenas instale a loja!```",'markdown', reply_markup=keyboard.store_free)

        #entrega da loja free:
        elif msg['data'].split()[0] == 'download_store_free':
            cursor_sqlite.execute("""SELECT * FROM loja_free""")
            resultados = cursor_sqlite.fetchall()
            if resultados == []:
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🤖 ***Bot diz:*** `não tenho lojas cadastradas, insira o banco de dados com dados ou cadastre um PKG enviando ela no meu privado com nome inicinando com TCXS, exexmplo:` ***TCXS_Store_3.9.pkg***",'markdown', reply_markup=keyboard.voltar_store_doadores)
            else:
                for resultado in resultados:
                    id_pkg = resultado['pkg']
                    nome_pkg = resultado['versao']
                    data_att = resultado['data']
                    uploader_id = resultado['uploader']
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"📦 `INSTRUÇÕES:` ```------ Abaixo temos a ultima atualização da TCXS Store para PlayStation3, baixe  e insira no pendrive, plugue o pendrive em seu console, ative o Hen e instale ela pelo Package Manager.\nCaso seja usuário de HAN será necessário usar o Fix,baixe ele, depois basta inserir o Fix e a Loja em seu pendrive e através do seu Han instalar ambos arquivos, ambos processos concluidos reinicie seu console!```",'markdown', reply_markup=keyboard.voltar_store_free)
                await bot.sendDocument(msg['message']['chat']['id'], document=id_pkg,caption=f'{nome_pkg} upada em {data_att} por @{uploader_id}')

        #entrega do fix
        elif msg['data'].split()[0] == 'download_fix':
            cursor_sqlite.execute("""SELECT * FROM fix_han""")
            resultados = cursor_sqlite.fetchall()
            if resultados == []:
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🤖 ***Bot diz:*** `não tenho o fix han, insira o banco de dados com dados ou cadastre um PKG enviando ele no meu privado com nome de:` ***FIX_HAN.pkg***",'markdown', reply_markup=keyboard.voltar_store_free)
            else:
                for resultado in resultados:
                    nome_pkg = resultado['versao']
                    data_att = resultado['data']
                    id_pkg = resultado['pkg']
                    uploader_id = resultado['uploader']
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"📦 `INSTRUÇÕES:` ```------ Abaixo temos o Fix da TCXS Store para PlayStation3, baixe  e insira no pendrive, plugue o pendrive em seu console com o Fix e a Loja, através do seu Han instalar ambos arquivos, ambos processos concluidos reinicie seu console!```",'markdown', reply_markup=keyboard.voltar_store_free)
                    await bot.sendDocument(msg['message']['chat']['id'], document=id_pkg,caption='Fix para usuários HAN')


        elif msg['data'].split()[0] == 'tutorial_segundo_plano':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"📦 `TUTORIAL:` ```------ Abaixo temos o Tutorial TCXS Store ensinando como fazer os Downloads em Segundo Plano em seu PlayStation3!```",'markdown', reply_markup=keyboard.voltar_store_free)
            await bot.sendMessage(msg['message']['chat']['id'], 'https://youtu.be/_21a5REKhBc')
            #return True
        elif msg['data'].split()[0] == 'fone_bluetooth':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"📦 `TUTORIAL:` ```------ Sabia que você pode usar seu fone bluetooth para jogos em seu PlayStation3?```",'markdown', reply_markup=keyboard.voltar_store_free)
            await bot.sendMessage(msg['message']['chat']['id'], 'https://www.youtube.com/watch?v=_wYG7iMa5uY')
            #return True
        elif msg['data'].split()[0] == 'proxy_usuarios':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"📦 `TUTORIAL:` ```------ Siga nosso tutorial de proxy para melhorar sua conexão e evitar banimento do seu PlayStation3!```",'markdown', reply_markup=keyboard.voltar_store_free)
            await bot.sendMessage(msg['message']['chat']['id'], 'https://youtu.be/l4o8ySk1Do4')
            #return True





#TCXS STORE PKG DOADORES |  PAYD------------------->
        elif msg['data'] == 'store_doadores':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"```------ Leia atentamente como adquirir acesso a Loja para Doadores, caso discorde basta não doar. Caso queira doar agora ou renovar sua entrada no grupo de doadores clique em Doar Agora, você será redirecionado para o Mercado Pago da TCXS Project. Não prestamos reembolsos e após doar basta enviar um comprovante no privado dos administradores.```\n`Pra ver os administradores digite:` /admin",'markdown', reply_markup=keyboard.store_doadores)
            #return True
        elif msg['data'] == 'como_participar':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"```------ Para participar você precisa fazer uma doação, pagamos mensalmente Dropbox de 5tb para armazenamento dos jogos e o valor é cobrado em dolar, a doação é mensal e doando você não esta comprando um produto, mas sim participando de uma vaquinha, todo dinheiro arrecadado fica retido na conta do Mercado Pago  para pagarmos o servidor, resumindo contribuindo você faz parte de uma vaquinha de doadores que mantem o servidor, nós da TCXS Project não temos lucro e nosso trabalho é voluntário, caso queira ajudar em algo e se juntar a equipe é bem vindo. Leia atentamente esta documentação e caso discorde de algo pedimos que não doe, não prestamos reembolsos.```\n`Pra ver os administradores digite:` /admin",'markdown', reply_markup=keyboard.voltar_store_doadores)
            await bot.sendMessage(msg['message']['chat']['id'], 'http://tcxsproject.com.br/doadores-tcxs-store-regras/')

        elif msg['data'] == 'mercado_pago':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"```------ Vejo que tem interesse em ser doador, usamos o sistema do Mercado Pago somente, favor nao insistir com outras formas.\nO Mercado Pago aceita pagamentos online e com cartão de crédito e boletos, este sistema é o mais seguro para nos da equipe e para vocês doadores, lembre que a doação é mensal e doando você faz parte da vaquina que mantem os servidores de 5tb da Dropbox onde encontram-se nossos jogos. Pedimos que antes de doar leia atentamente as regras como mencionado antes e após fazer sua doação envie o comprovante no privado de um de nossos administradores.```\n`Pra ver os administradores digite:` /admin",'markdown', reply_markup=keyboard.voltar_store_doadores)
            await bot.sendMessage(msg['message']['chat']['id'], 'https://www.mercadopago.com.br/checkout/v1/redirect?pref_id=354396246-315fce8c-d8f9-4aa0-8583-95d678936375')
##  ATUALIZAÇÃO PARA DOADORES ATRAVÉS DO SISTEMA DE BOTÕES------------------------------------------------------------------------------>>
        #LOJA PAGA PARA DOADORES COM DATABASE E BOTOES------------>
        elif msg['data'].split()[0] == 'download_store_doadores':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"📦 `INSTRUÇÕES:` ```------ Bem vindo a TCXS Project ,agora você faz parte dela, entenda que as doações sao mensais e nossa equipe nao ganha nada por este projeto, todo dinheiro arrecadado neste grupo é para pagar os servidores dos quais dispomos jogos. Logo a PSN STUFF IRÁ ACABAR POIS OS SERVIDORES SERÃO DESLIGADOS e assim nao terá mais os jogos gratuitos por ai, restando apenas este acervo que é mantido por voces doadores!     Vamos a Instalação!!!  --> Espero que tenha um pendrive em mãos!  --> copie os arquivos da VERSÃO 3.6 e caso use o fix de acordo com seu Exploit/Desbloqueio, se voce tem han ou CFW use o FIX HAN, caso contrário e seja o Exploit HEN em seu console use o FIX HEN, é necessaria a instalacao deste arquivo para que a loja apareca em seu console! Ative seu HAN/HEN e instale o FIX, após o FIX instalado instale a TCXS Store PKG, recomendamos reiniciar o console após este processo!!```",'markdown', reply_markup=keyboard.voltar_store_doadores)
            if msg['message']['chat']['title'] == 'Doadores TCXS 2020':
                cursor_sqlite.execute("""SELECT * FROM loja_doadores""")
                resultados = cursor_sqlite.fetchall()
                if resultados == []:
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🤖 ***Bot diz:*** `não tenho lojas cadastradas, insira o banco de dados com dados ou cadastre um PKG enviando ela no meu privado com nome inicinando com TCXS, exexmplo:` ***TCXS_Store_3.9.pkg***",'markdown', reply_markup=keyboard.voltar_store_doadores)
                else:
                    for resultado in resultados:
                        id_pkg = resultado['pkg']
                        nome_pkg = resultado['versao']
                        data_att = resultado['data']
                        uploader_id = resultado['uploader']
                    await bot.sendDocument(msg['message']['chat']['id'], document=id_pkg,caption=f'{nome_pkg} upada em {data_att} por @{uploader_id}')
            else:
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🚨 `ATENÇÃO`🚨  ```------ Este comando só funciona no grupo de doadores.```",'markdown', reply_markup=keyboard.voltar_store_doadores)
            #return True

        #FIX HAN PARA DOADORES COM DATABASE E BOTOES------------>
        elif msg['data'].split()[0] == 'download_fix_han_doadores':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"📦 `INSTRUÇÕES:` ```------ Abaixo temos o Fix da TCXS Store para PlayStation3, baixe  e insira no pendrive, plugue o pendrive em seu console com o Fix e a Loja, ambos processos concluidos reinicie seu console!```",'markdown', reply_markup=keyboard.voltar_store_doadores)
            if msg['message']['chat']['title'] == 'Doadores TCXS 2020':
                cursor_sqlite.execute("""SELECT * FROM fix_han""")
                resultados = cursor_sqlite.fetchall()
                if resultados == []:
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🤖 ***Bot diz:*** `não tenho o fix han, insira o banco de dados com dados ou cadastre um PKG enviando ele no meu privado com nome de:` ***FIX_HAN.pkg***",'markdown', reply_markup=keyboard.voltar_store_doadores)
                else:
                    for resultado in resultados:
                        nome_pkg = resultado['versao']
                        data_att = resultado['data']
                        id_pkg = resultado['pkg']
                        uploader_id = resultado['uploader']
                        await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🚨 `ATENÇÃO`🚨  ```------ Veja o tutorial INSTALAÇÃO EXPLOIT HAN E HEN! no menu abaixo ```",'markdown', reply_markup=keyboard.voltar_store_doadores)
                        await bot.sendDocument(msg['message']['chat']['id'], document=id_pkg,caption='Fix para usuários HAN')
            else:
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🚨 `ATENÇÃO`🚨  ```------ Este comando só funciona no grupo de doadores.```",'markdown', reply_markup=keyboard.voltar_store_doadores)
            #return True

        # FIX HEN PARA DOADORES COM DATABASE E BOTOES------------>
        elif msg['data'].split()[0] == 'download_fix_hen_doadores':
            if msg['message']['chat']['title'] == 'Doadores TCXS 2020':
                cursor_sqlite.execute("""SELECT * FROM fix_hen""")
                resultados = cursor_sqlite.fetchall()
                if resultados == []:
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🤖 ***Bot diz:*** `não tenho o fix hen, insira o banco de dados com dados ou cadastre um PKG enviando ele no meu privado com nome de:` ***FIX_HEN.pkg***",'markdown', reply_markup=keyboard.voltar_store_doadores)
                else:
                    for resultado in resultados:
                        id_pkg = resultado['pkg']
                        await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🚨 `ATENÇÃO`🚨  ```------ Veja o tutorial INSTALAÇÃO EXPLOIT HAN E HEN! no menu abaixo ```",'markdown', reply_markup=keyboard.voltar_store_doadores)
                        await bot.sendDocument(msg['message']['chat']['id'], document=id_pkg,caption='Fix para usuários HEN')
            else:
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🚨 `ATENÇÃO`🚨  ```------ Este comando só funciona no grupo de doadores.```",'markdown', reply_markup=keyboard.voltar_store_doadores)
            #return True

        # FIX CFW XML DOADORES COM DATABASE E BOTOES------------>
        elif msg['data'].split()[0] == 'download_fix_cfw_doadores':
            if msg['message']['chat']['title'] == 'Doadores TCXS 2020':
                cursor_sqlite.execute("""SELECT * FROM fix_cfw_xml""")
                resultados = cursor_sqlite.fetchall()
                if resultados == []:
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🤖 ***Bot diz:*** `não tenho o fix cfw xml, insira o banco de dados com dados ou cadastre um PKG enviando ele no meu privado com nome de:` ***category_network_tool2.xml***",'markdown', reply_markup=keyboard.voltar_store_doadores)
                else:
                    for resultado in resultados:
                        id_pkg = resultado['pkg']
                        await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🚨 `ATENÇÃO`🚨  ```------ Veja o tutorial INSTALAÇÃO EM CONSOLES CFW no menu abaixo ```",'markdown', reply_markup=keyboard.voltar_store_doadores)
                        await bot.sendDocument(msg['message']['chat']['id'], document=id_pkg,caption='Fix para usuários CFW')
            else:
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🚨 `ATENÇÃO`🚨  ```------ Este comando só funciona no grupo de doadores.```",'markdown', reply_markup=keyboard.voltar_store_doadores)
            #return True

        # FIX HEN XML PARA DOADORES COM DATABASE E BOTOES------------>
        elif msg['data'].split()[0] == 'download_fix_hen_xml_doadores':
            if msg['message']['chat']['title'] == 'Doadores TCXS 2020':
                cursor_sqlite.execute("""SELECT * FROM fix_hen_xml""")
                resultados = cursor_sqlite.fetchall()
                if resultados == []:
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🤖 ***Bot diz:*** `não tenho o fix hen xml, insira o banco de dados com dados ou cadastre um PKG enviando ele no meu privado com nome de:` ***category_network.xml***",'markdown', reply_markup=keyboard.voltar_store_doadores)
                else:
                    for resultado in resultados:
                        id_pkg = resultado['pkg']
                        await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🚨 `ATENÇÃO`🚨  ```------ Veja o tutorial INSTALAÇÃO EM CONSOLES CFW no menu abaixo ```",'markdown', reply_markup=keyboard.voltar_store_doadores)
                        await bot.sendDocument(msg['message']['chat']['id'], document=id_pkg, caption='Fix XML para usuários HEN avançados')
            else:
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🚨 `ATENÇÃO`🚨  ```------ Este comando só funciona no grupo de doadores.```",'markdown', reply_markup=keyboard.voltar_store_doadores)
            #return True

        #ACIMA DISTO PARTE DA ATT QUE PRECISA DE DB | SEGUE CODIGOS DOS DOADORES E DA ATT PAGA--------------------->
        elif msg['data'].split()[0] == 'tutorial_loja':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"📦 `TUTORIAL:` ```------ Abaixo temos o Tutorial TCXS Store instalar a loja em seu PlayStation3!```",'markdown', reply_markup=keyboard.voltar_store_doadores)
            await bot.sendMessage(msg['message']['chat']['id'],'https://cos.tv/videos/play/1586413688272059934')
            #return True
        elif msg['data'].split()[0] == 'tutorial_cfw':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"📦 `TUTORIAL:` ```------ Abaixo temos o Tutorial TCXS Store ensinando como usar em consoles CFW PlayStation3!```",'markdown', reply_markup=keyboard.voltar_store_doadores)
            await bot.sendMessage(msg['message']['chat']['id'],'https://cos.tv/videos/play/1586411677524278797')
            #return True
        elif msg['data'].split()[0] == 'tutorial_segundo_plano_doadores':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"📦 `TUTORIAL:` ```------ Abaixo temos o Tutorial TCXS Store ensinando como fazer os Downloads em Segundo Plano em seu PlayStation3!```",'markdown', reply_markup=keyboard.voltar_store_doadores)
            await bot.sendMessage(msg['message']['chat']['id'],'https://youtu.be/_21a5REKhBc')
            #return True
        elif msg['data'].split()[0] == 'fone_bluetooth_doadores':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"📦 `TUTORIAL:` ```------ Sabia que você pode usar seu fone bluetooth para jogos em seu PlayStation3?```",'markdown', reply_markup=keyboard.voltar_store_doadores)
            await bot.sendMessage(msg['message']['chat']['id'],'https://www.youtube.com/watch?v=_wYG7iMa5uY')
            #return True
        elif msg['data'].split()[0] == 'proxy_usuarios_doadores':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"📦 `TUTORIAL:` ```------ Siga nosso tutorial de proxy para melhorar sua conexão e evitar banimento do seu PlayStation3!```",'markdown', reply_markup=keyboard.voltar_store_doadores)
            await bot.sendMessage(msg['message']['chat']['id'],'https://youtu.be/l4o8ySk1Do4')
            #return True






# COMANDOS_USUARIOS  ------------------------------------------------->
        elif msg['data'] == 'comandos_usuarios':#esta tabela pela a reply_markup da primeira e le os dados do keyboard.py e oque respondido volta pra ca ou nao, para usar local "palavra" para usar la
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"***Comandos para usuários:***",'markdown', reply_markup=keyboard.comandos_usuarios)
            #return True
        elif msg['data'] == 'comandos_users':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      f"""/start   -inicia o bot
/regras  -leia nossas regras
/admin   -admins do grupo
/freepkg -loja gratuita PS3 
/fix -fix han
/tutorial -como instalar a loja
/rap -licenças dos jogos  
/desbloqueio -desbloquear PS3
/segundoplano -download 
/codigoerro  -codigos PSN/PS3
/listajogos -download direto
/doadores -instruções
/mercadopago -doar/loja 
/tcxs -informações sobre 
/tcxspyject -criar lojas
/ps1 -cria xml para loja
/ps2 -cria xml para loja 
/psp -cria xml para loja
/ps3 -cria xml para loja
/proxy -velocidade no PS3
/tr      -traduz um texto
/yt      -pesquisa videos no YouTube
/r       -pesquisa um termo no redit
/clima   -exibe informacoes de clima
/coub    -pesquisa de pequenas anima??es
/dados   -jogo de dados
/gif     -gif do giphy
/git     -usuario do github
/id      -id do usuario
/ip      -informa dados de um ip
/jsondump -retorna dados formatados
/stickerid -pega id de um sticker
/getsticker -baixa um sticker
/pypi -pesquisa libs python
/rextester -interpretador de varias linguagens de programação
/mark -repete o texto informado usando Markdown
/html -repete o texto informado usando HTML
/request -faz uma requisicao a um site
/rt -repete concordando com o usuario na reposta  
/fala -Repete o texto que voce pedir para ele falar
/print -gera um print doque falou
/dogbin - envia seu material em texto para o dogbin
/hastebin - envia seu material em texto para o hastebin
/echo - Repete o texto informado.    
/shorten - Encurta uma URL.
/recog - reconhecimento com IA (nem sempre disponivel)
/notepad - cria um site com o texto enviado
/crawler - pega todos links dentro de um site
/corrigir - corrige palavras erradas
/token - Exibe informaces de um token de bot.
""",'markdown', reply_markup=keyboard.voltar_comandos_usuarios)
            #return True
        elif msg['data'] == 'sites_users':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),"/torrent -pkg torrent\n/pkg_games -pkg's\n/site -doadores\n/facebook -facebook cadastre-se\n/anime -anime gratis\n/onion -deepweb\n/dev -hacker ", reply_markup=keyboard.voltar_comandos_usuarios)
            #return True
        elif msg['data'] == 'cria_xml_users':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),"""***Temos um programa de computador que cria lojas diretamente no console PlayStation3***
/tcxspyject -criar lojas

***Criar XML PSP Instruções:*** 
`comando:`/psp -cria xml para loja
    ```
    1 - meu comando sempre começa com /xml
    2 - eu não aceito espaços no nome de arquivo, nome de jogo e nem na descrição!
    3 - você pode copiar o caractere especial invisivel dentro das aspas abaixo para usar onde precisar de espaço!``` 
    `Copie de dentro das aspas o caractere invisivel:`"⠀"
    
    **VAMOS AO COMANDO EM SI**
    `Exemplo com caractere invisivel:`
    ``` gow god⠀of⠀war descriçao⠀usando⠀caractere⠀invisivel     www.linkdropbox.com```
    `Exemplo sem caractere visivel:`
    ``` /psp gow god_of_war descrição_sem_caractere_visivel   www.linkdropbox.com```
    **Onde cada campo:**
    `/psp` ```- chama comando```
    `gow` ```- nome do xml```
    `god_of_war` ```- nome do jogo, se quiser tirar os _ usar caractere especial no lugar```
    `descrição_do_jogo` ```- descrição, se quiser tirar os _ usar caractere especial no lugar``` 
    `www.linkdropbox.com` ```- Link do Dropbox```

***Criar XML PS1 Instruções:*** 
`comando:`/ps1 -cria xml para loja
    ```
    1 - meu comando sempre começa com /xml
    2 - eu não aceito espaços no nome de arquivo, nome de jogo e nem na descrição!
    3 - você pode copiar o caractere especial invisivel dentro das aspas abaixo para usar onde precisar de espaço!``` 
    `Copie de dentro das aspas o caractere invisivel:`"⠀"

    **VAMOS AO COMANDO EM SI**
    `Exemplo com caractere invisivel:`
    ``` gow god⠀of⠀war descriçao⠀usando⠀caractere⠀invisivel     www.linkdropbox.com```
    `Exemplo sem caractere visivel:`
    ``` /ps1 gow god_of_war descrição_sem_caractere_visivel   www.linkdropbox.com```
    **Onde cada campo:**
    `/ps1` ```- chama comando```
    `gow` ```- nome do xml```
    `god_of_war` ```- nome do jogo, se quiser tirar os _ usar caractere especial no lugar```
    `descrição_do_jogo` ```- descrição, se quiser tirar os _ usar caractere especial no lugar``` 
    `www.linkdropbox.com` ```- Link do Dropbox```
    
***Criar XML PS2 Instruções:*** 
`comando:`/ps2 -cria xml para loja
    ```
    1 - meu comando sempre começa com /xml
    2 - eu não aceito espaços no nome de arquivo, nome de jogo e nem na descrição!
    3 - você pode copiar o caractere especial invisivel dentro das aspas abaixo para usar onde precisar de espaço!``` 
    `Copie de dentro das aspas o caractere invisivel:`"⠀"
    
    **VAMOS AO COMANDO EM SI**
    `Exemplo com caractere invisivel:`
    ``` gow god⠀of⠀war descriçao⠀usando⠀caractere⠀invisivel     www.linkdropbox.com```
    `Exemplo sem caractere visivel:`
    ``` /ps2 gow god_of_war descrição_sem_caractere_visivel   www.linkdropbox.com```
    **Onde cada campo:**
    `/ps2` ```- chama comando```
    `gow` ```- nome do xml```
    `god_of_war` ```- nome do jogo, se quiser tirar os _ usar caractere especial no lugar```
    `descrição_do_jogo` ```- descrição, se quiser tirar os _ usar caractere especial no lugar``` 
    `www.linkdropbox.com` ```- Link do Dropbox```
  
***Criar XML PS3 Instruções:*** 
`comando:`/ps3 -cria xml para loja
    ```
     1 - meu comando sempre começa com /xml
     2 - eu não aceito espaços no nome de arquivo, nome de jogo e nem na descrição!
     3 - você pode copiar o caractere especial invisivel dentro das aspas abaixo para usar onde precisar de espaço!
     4 - meu sistema para por jogos de PS3 aceitam apenas 3 links preciso deles como exemplos.``` 
     `Copie de dentro das aspas o caractere invisivel:`"⠀"
    
     **VAMOS AO COMANDO EM SI**
     `Exemplo com caractere invisivel:`
     ``` gow god⠀of⠀war descriçao⠀usando⠀caractere⠀invisivel     www.linkdropbox.com  www.linkdropbox.com  www.linkdropbox.com```
     `Exemplo sem caractere visivel:`
     ``` /ps3 gow god_of_war descrição_sem_caractere_visivel   www.linkdropbox.com www.linkdropbox.com www.linkdropbox.com```
     **Onde cada campo:**
     `/ps3` ```- chama comando```
     `gow` ```- nome do xml```
     `god_of_war` ```- nome do jogo, se quiser tirar os _ usar caractere especial no lugar```
     `descrição_do_jogo` ```- descrição, se quiser tirar os _ usar caractere especial no lugar``` 
     `www.linkdropbox.com` ```- Link do Dropbox, preciso de 3 links separados por espaço```
/ps3 -cria xml para loja""",'markdown', reply_markup=keyboard.voltar_comandos_usuarios)
            #return True
        elif msg['data'] == 'lista_jogos_users':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      f"```------ Tenho esta lista de jogos em PKG para PlayStation3 todos com links diretos, estes jogos são originais, portanto precisam de Licenças ou como conhecemos precisam dos Rap's```\n`Basta clicar no botão que te trarei a lista com link direto para download, pedimos sua contribuição para que este projeto se mantenha vivo, Obrigado a todos da TCXS!` ",
                                      'markdown', reply_markup=keyboard.lista_jogos)

        elif msg['data'] == 'info_doacao_users':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      f"""```------ A TCXS Project fornece e desenvolve o aplicativo para PlayStation3 TCXS Store, para poder ter nosso aplicativo em seu console basta fazer uma doação nos botões deste bot ou pelo site, antes de doar leia atentamente a todas as regras, já quero explicar como funciona a doação, todo montante arrecadado fica preso em uma conta do Mercado Pago a qual é usada para pagar o servidor do Dropbox e outros serviços, ao doar você esta participando de uma vaquinha onde a união de todos doadores mantém a vaquinha no mercado pago assim possibilitando pagar os serviços que usamos, nossa loja não é paga e em momento algum você é obrigado a pagar, fornecemos jogos para download direto aqui neste bot bem como temos uma loja free que tem todos jogos das demais lojas free, a loja ficou definida apenas para doadores a pedido deles, pois o download fica muito mais rápido e não temos mais perda de jogos, ressalto que o grupo de doadores esta limitado apenas a 200 pessoas e caso esteja lotado você terá que esperar alguem sair, continuando... Logo após doar você deve ir em nosso grupo de telegram e procurar por @MsT3Dz ou @Odeiobot e mostrar seu comprovante de doação assim você estará dentro do grupo que contém as novidades, jogos e nossa TCXS Store PKG PlayStation3.```
` As doações são feitas pelo mercado pago, onde aceitamos todos os cartões, pagamentos online e boletos.
        Não prestamos reembolsos pois se trata de doações e não uma venda direta para uso dos serviços!
        O material completo é apenas para doadores. Além do projeto para PlayStation3  a TCXS Project conta com inumeros projetos e Sites para seu entreterimento. Após fazer sua doação basta ir no grupo de TELEGRAM e procurar pelo nosso administrador @MsT3Dz  ou @Odeiobot , enviar um print de seu comprovante de pagamento que ele irá fornecer acesso a todo material, exigimos que seja feito o pedido no grupo! Outros administradores não irão te responder no privado, contamos com seu bom senso e cordialidade! NÃO PRESTAMOS REEMBOLSOS!
        Queremos deixar a todos cientes que as doações feitas são exclusivas para pagar os servidores da Dropbox e serviços como hospedagem de site, sendo assim nos adm’s declaramos não receber nenhum valor neste projeto sendo assim nosso trabalho voluntário e todo e qualquer que queira entrar na equipe para ajudar a contribuir de forma expontanêa é bem vindo. Nossa equipe desenvolve sem cobrar nada pela sua mão de obra os sites acima citados bem como o desenvolvimento da TCXS Store PKG e a conversão e upload de jogos dentro dos servidores da Dropbox para assim os fornecer em formato NO-HAN para os usuários, fornecemos dentro da Plataforma PlayStation3 jogos de PS2, PS2, PsP, Emuladores das mais diversas plataformas! Álem disto disponibilizamos aos usuários a experiencia de ter sites para download de jogos nas mais variadas paltaformas e em especial jogos de PS3 PKG tudo aberto gratuitamente a comunidade bem como este site e outros sites mencionados aqui e que encontram-se nos menus.`""",
                                      'markdown', reply_markup=keyboard.voltar_comandos_usuarios)
            # return True
        elif msg['data'] == 'info_requisitos_users':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      f"""```------ Para usar a TCXS Store PKG você precisa ter seu console exploitado ou desbloqueado, nossa loja funciona nos consoles CFW, OFW, nas versões HAN e HEN, porém precis atender alguns requisitos para usar a TCXS Store PKG:
        - Console Desbloqueado/exploitado.
        - Versão exploit Han/Hen.
        - Assinaturas previamente inseridas ( Raps’).
        - Configurações de internet corretas.
        - Espaço para download de jogos em seu hd.
        - Conhecer previamente tudo sobre seu sistema de desbloqueio/exploit.
        - Saber solucionar seus erros.
        - Estar ciente que ao doar para a TCXS Store você não esta fazendo uma compra e sim ajudando a pagar os servidores da Dropbox onde upamos os jogos.CONSIDERE SE PARTICIPANDO DE UMA VAQUINHA COLETIVA ONDE TODOS USUARIOS DA TCXS AJUDAM NESTA VAQUINHA PARA MANTER O SERVIDOR```""",
                                      'markdown', reply_markup=keyboard.voltar_comandos_usuarios)
            # return True
        elif msg['data'] == 'info_suporte_users':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      f"""```------ Prestamos suporte somente para nosso aplicativo e jogos para doadores, estejam cientes que:
        Suporte será prestado somente para a TCXS Store dos Doadores.
        Suporte será prestado somente para jogos que são convertidos pela equipe para Doadores.
        Por se tratar de copias modificadas de jogos nossos jogos constantemente são reupados.
        Por se tratar de copias modificadas ao cair dos links, os mesmos após conteúdo upado, são substitúidos na TCXS Store PKG para Doadores.
        Tenha ciencia de que links podem vir a cair ( não temos frequencia disto).
        Saiba que a administração não presta suporte para seu desbloqueio e exploit, mas aconselhamos levar em um técnico competente caso não saiba realizar as operações básicas e avançadas de seu console.
        Caso queira se aventurar em aprender tudo sobre seu desbloqueio ou exploit aconselhamos o fórum da PSX Place que são os desenvolvedores do desbloqueio e exploit, não iremos dar suporte ao material de terceiros ou erros cometidos por usuarios ou consoles vindo de tecnicos que não fizeram um bom exploit ou um bom desbloqueio.```""",
                                      'markdown', reply_markup=keyboard.voltar_comandos_usuarios)
            # return True-------------------
















#COMANDOS ADMINS--------------------------------------------------------------------------------------->
        #COMANDOS PARA OS BOTOES DOS ADMINISTRADORES
        elif msg['data'] == 'comandos_admins':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"```------ Os comandos aqui listados funcionam apenas para administradores de grupos e o menu Desenvolvedor somente quem hospeda pode usar. ```",'markdown', reply_markup=keyboard.comandos_admins)
            #return True
        elif msg['data'] == 'gerenciar_grupos':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),"""/start - inicia o bot
/welcome -boas vindas
/ban -bane usuario
/unban -desbane usuario
/kick -kicka usuario
/mute -muta usuario
/unmute -desmuta usuario
/unwarn -remove advertencias
/warn -adverte usuario
/pin -fixa posts
/unpin -desfixa posts
/title -muda titulo grupo
/defregras -define regras
/regras -ler regras
/config -privado
/admdebug -debug admin
/id -id usuario
/ip -dados ip
/jsondump -retorna dados 
/stickerid -id sticker
/getsticker -baixa sticker
/criar_sticker -cria pacote stickers
/kibar -copia sticker para o pacote de stickers
/mark -repete o texto markdown
/html -repete o texto HTML
/request -requisição site
/recog - reconhecimento com IA (nem sempre disponivel)
/notepad - cria um site com o texto enviado
/crawler - pega todos links dentro de um site
/corrigir - corrige palavras erradas
/link - pega link de um arquivo use como resposta""", reply_markup=keyboard.voltar_comandos_admins)
            #return True
        elif msg['data'] == 'cadastrar_comandos':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),"""
💾***CADASTRO DE COMANDOS E REPOSTAS NA DATABASE***        
🤖`Para cadastrar um comando no banco de dados:`
#comando resposta que o usuário vai receber
🤖`Para recadastrar um comando no banco de dados:`
$comando resposta que o usuário vai receber
🤖`Para deletar um comando`
%comando 
""",'markdown', reply_markup=keyboard.voltar_comandos_admins)

            #return True
        elif msg['data'] == 'cadastrar_lojas':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),"""
💾***CADASTRAR ARQUIVOS LOJAS DOADORES/FREE*** 
```Este bot cadastra as lojas para doadores e free, cadastra também os fix pkg e os fix xml, para atualizar as lojas ou fix pkg e xml basta enviar elas no privado do bot, e ele cadastrará seus arquivos desde que estejam de acordo com as instruções abaixo. Pode ocorrer falhas na hora de cadastrar️, caso não tenha cadastrado envie novamente o arquivo, jamais envie mais de um arquivo por vez.```

🤖***Cadastrar Loja Free:*** `Cadastre a LOJA GRATUITA FREE PKG enviando ela no meu privado com nome terminando com free.pkg, antes disto você pode por qualquer coisa no nome no arquivo como exemplo:` ***TCXS_3.6_free.pkg***

🤖***Cadastrar Loja Doadores:*** `Cadastre a LOJA PARA DOADORES PKG enviando ela no meu privado com nome inicinando com TCXS, após este nome você pode escrever oque quiser no arquivo como  exemplo:` ***TCXS_Store3.9.pkg***

🤖***Cadastrar Fix HAN PKG:*** `Cadastre o FIX HAN PKG enviando ela no meu privado exatamente conforme exemplo:` ***FIX_HAN.pkg***

🤖***Cadastrar Fix HEN PKG:*** `Cadastre o FIX HEN PKG enviando ela no meu privado exatamente conforme exemplo:` ***FIX_HEN.pkg***

🤖***Cadastrar Fix CFW XML:*** `Cadastre o FIX CFW XML enviando ela no meu privado exatamente conforme exemplo:` ***category_network_tool2.xml***

🤖***Cadastrar Fix HEN XML:*** `Cadastre o FIX HEN XML enviando ela no meu privado exatamente conforme exemplo:` ***category_network.xml***
""",'markdown', reply_markup=keyboard.voltar_comandos_admins)

        elif  msg['data'] == 'restringir_doadores':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']), """
💾***RESTRINGIR | LIMPAR | RECADASTRAR DOADORES*** 
```---- Este bot cadastra os Doadores automáticamente, porém se por ventura ele falhar ou mesmo um administrador quiser Cadastar Manualmente o Doador por qualquer eventualidade, seja para conferir um cadastro automatico feito pelo Bot ou para poder dar mais dias de permanência ao Doador!```

🤖***Cadastro automático:*** `Automaticamente ao entrar em um grupo o doador é cadastrado com o prazo de 30 dias de permanencia.`

🤖***Conferir Doadores Cadastrados:*** `Para conferir os cadastros existentes no sistema basta digitar o comando consulta e o arroba do usuário marcando o mesmo que também poderá conferir seu prazo,lembrando que faltando 7 dias para o prazo de banimento do grupo o usuário será notificado sobre para assim poder ou não realizar uma doação e manter sua permanência, use o comando conforme exemplo:`
consulta @UserGamer

🤖***Descadastrar ou Deletar Doador:*** `Descadastrar ou deletar um Doador é necessário para que possa ser feita a inclusão de mais dias na sua conta, para isto basta usar o comando seguido do arroba do Doador conforme exemplo:`
limpar @Mst3Dz

🤖***Cadastrar Manualmente um Doador:*** `Para cadastrar manualmente o doador é necessário pegar sua ID, para isto basta pegar qualquer mensagem deste doador e responder com o comando /id, após ter a ID do Doador tenha certeza que o mesmo não existe no Banco de Dados, para isto realize uma consulta e caso o Doador esteja cadastrado delete ele conforme instruções para deletar. Caso usuário não conste no Banco de Dados ou já tenha sido deletado execute o comando conforme exemplos:` ***restringir @usuario id_usuario quantidade_dias***
`Exemplo na prática:` restringir @MsT3Dz 628238139 300000

🤖***Depois de Banido oque acontece:*** `Após o doador ser banido os administradores são notificados, o nome deste doador é limpo do banco de dados e da lista de restritos do grupo, caso ele faça uma nova doação basta adiciona-lo no grupo sem a necessidade de qualquer comando.`
    """, 'markdown', reply_markup=keyboard.voltar_comandos_admins)

        elif msg['data'] == 'perguntas_admins':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']), """
💾***SISTEMA DE PERGUNTAS E RESPOSTAS PARA ADMINS***
```---- Este bot grava todas perguntas desde que contenham ??, avise seus usuários que quando quiserem cadastrar uma pergunta usem duas interrogações no final da frase e automáticamente sua pergunta será cadstrada e assim que um administrador ver pode responder ou cadastrar ela no robo ensinando a Inteligência Artificial.```
🤖`Cadastrar pergunta exemplo:` Como faço para ser tao esperto como o robo?? 
🤖`Ver perguntas cadastradas apenas digite:` perguntas  
🤖`Limpar perguntas cadastradas ou já respondidas digite:` apagar perguntas
    """, 'markdown', reply_markup=keyboard.voltar_comandos_admins)

        elif msg['data'] == 'admin_frequencia':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),"""
💾***SOBRE A FREQUENCIA DE MENSAGENS*** 
```----  Este bot envia mensagens baseado em uma frequencia que deve ser setada entre 2 e 10, onde:```
🤖`frequencia 0 = mudo`
🤖`frequencia 2 = fala pouco`
🤖`frequencia 10 = fala muito`
    """,'markdown', reply_markup=keyboard.voltar_comandos_admins)

        elif msg['data'] == 'admin_proibicoes':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),"""
💾***SOBRE PROIBIR E PERMITIR PALAVRAS***
```----  Este bot pode restringir/permitir palavras com os comandos:```
🤖`proibir uma palavra:` proibir corno
🤖`permitir uma palavra:` permtir corno
🤖`ver palavras proibidas:` proibidas
    """,'markdown', reply_markup=keyboard.voltar_comandos_admins)

        elif msg['data'] == 'admin_inteligencia':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),"""
💾***SOBRE O ENVIO DE MENSAGENS DA IA*** 
```----  Este bot envia mensagens baseado em dois tipos de inteligência, uma local e outra global, onde a local é tudo que aprendeu naquele grupo e ja a global é oque ele aprendeu por onde passou, veja exemplos:```
🤖`inteligencia local = irá falar  somente sobre oque aprendeu neste grupo, comando:`
inteligencia local
🤖`inteligencia global = ira falar sobre tudo que aprendeu em todos os lugares que passou na internet`
inteligencia global
🤖`fale sobre = ele fala sobre determinado assunto, exemplo:`
fale sobre playstation
    """,'markdown', reply_markup=keyboard.voltar_comandos_admins)


        elif msg['data'] == 'admin_banimento':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']), """
👮‍***SOBRE O SISTEMA AUTOMATICO DE BANIMENTO DA IA*** 
```----  Este bot envia conta com um sistema de banimento automático que pode ser ativado ou desativado no menu de configurações. Quando ativado, cada usuário que entrar terá a permanencia de 35 dias cadastrado de forma automática e caso estes dias não sejam renovados/adicionados o usuário tomará ban, este sistema é util para grupos pagos ou grupos que tem doadores ou mensalidades.```
🤖`Sistema ativado = irá cadastar automaticamente e banir todos usuarios quando vencerem seu prazo, com 7 dias antes do vencimento a IA irá marcar o usuário no grupo avisando o mesmo.`

🤖`Sistema desativado = mesmo com sistema desativado ainda é possivel cadastrar usuários de forma manual e fazer a varredura para o banimento de forma manual, igualmente em um horario pre-determinado pelo desenvolvedor este bot irá aplicar o sistema de ban automatico então não precisa se preocupar em passar a verificação, basta apenas adicionar seus usuários manualmente ou inserir mais dias manualmente para eles conforme instruções no botao de Doadores.`
    """, 'markdown', reply_markup=keyboard.voltar_comandos_admins)

        elif msg['data'] == 'admin_reconhecimento':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']), """
🕵️‍️‍***SOBRE O SISTEMA DE RECONHECIMENTO DA IA*** 
```----  Este bot envia conta com um sistema de  reconhecimento com Deep e Machine Learning utilizando as Lib's Tensorflow, Keras e OpenCV.```
🤖`Para usar este sistema basta responder qualquer imagem com o comando /recog e aguardar a IA enviar sua imagem com os objetos reconhecidos nela. Esta opção nem sempre esta disponível devido uso de GPU de quem hospeda a IA.`
    """, 'markdown', reply_markup=keyboard.voltar_comandos_admins)





#AREA DE BOTOES DO DESENVOLVEDOR------------------------------------------------------------------------------->>>>>>>>>
        elif msg['data'] == 'area_dev':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"```------ Os comandos e configurações listadas nesta categoria funcionam apenas para quem desenvolve ou hospeda o Bot, nenhum ou muito destes comandos não funcionam com usuários nem administradores, igualmente é importante que todos saibam deles e em baso de algum bug envie:``` /bug seguido doque tem para reportar ao Desenvolvedor.",'markdown', reply_markup=keyboard.desenvolvedor)
        elif msg['data'] == 'dev_info':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      '''• Manicomio Bot

Version: {version}
Nosso site: <a href="https://tcxsproject.com.br">Manicomio TCXS Project</a>
Developers: <a href="https://github.com/gorpo">GorpoOrko</>

Partnerships:
 » <a href="https://t.me/tcxsproject2">telegram</>
©2020 - <a href="https://t.me/tcxsproject2">TCXS Project™</>
'''.format(version=version),parse_mode='html',reply_markup=keyboard.desenvolvedor, disable_web_page_preview=True)
        elif msg['data'] == 'dev_inteligencia':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      '''• Inteligencia Artificial | Versão: {version}

O sistema de Inteligência Artificial foi implantado unindo Banco de Dados Sqlite3 e algumas bibliotecas, este bot possui um sistema de envio de mensagens local e global, no qual ele se baseia no que aprendeu com oque os usuários falam ou cadastram manualmente em seu banco de dados, conta tambem com sistema de banimento automático ou com data marcada inseridos manualmente via comandos explicados claramente nos menus do bot. Além de falar, interagir e aprender com usuários, este bot também é capaz de restringir palavras ou frases proibindo elas como explicado nos menus do bot. Todas configurações inseridas no Bot foram feitas em Python com uso de Machine e Deep Learning, graças a este sistema este bot tem um sistema de reconhecimento visual onde quando respondida uma imagem com o comando "recog" ele irá aplicar o reconhecimento. Outra peculiaridade da IA é seu poder de converter voz em texto assim facilitando a comunicação dos grupos e pensando de forma global este bot pode traduzir inumeras linguas com seu comando /tr isto facilitará a comunicação com todo mundo! Falando um pouco sobre seu sistema de frequencia, este bot pode ser mutado, falar pouco ou muito dependendo das suas configurações de "frequencia" como listado nos menus. O Grande poder da IA também conta com um sistema de correção de texto onde quando respondido com comando "corrigir" ele irá buscar erros em uma frase e apontar os erros. Perguntas dos usuários do grupo jamais passarão em branco, pois este bot conta com um sistema de cadastro de perguntas, desde que o usuário faça sua pergunta e no final tenha duas interrogações "??". O Sistema de Cadastramento e Banimento automático pode ser facilmente ativado ou desativado em seu grupo, bem como usuários podem ser cadastrados automáticamente ao entrar no grupo ou de forma manual pelos administradores conforme explicações nos menus. Esta IA conta com um sistema global de pesquisas respondendo assim oque você quiser, basta executar o comando "fale sobre" e seu tema e ele irá responder! Caso a IA não responda sua pergunta por não conhecer a reposta ou não se comunique com você com um determinado tema, basta adicionar manualemente os comandos conforme explicado nos menus.
Criação de páginas Web pra rascunhos rápidos não é problema para nossa IA, ela posta seu codigo, texto ou conteudo nas plataformas Dogbin, Hastebin e Telegraph onde este ultimo é um site(página web). Ah quem não acredite mas esta IA é capaz de criar links diretos de arquivos do telegram desde que estes não passem de 20mb. Ele também é capaz de fazer varredura em links com Crawling (hacking), informar dados de IP dentre outras ferramentas hackers. Encurtar URL's com nossa IA não é problema e ainda ela te ajuda a saber o clima de sua cidade e varias informações da internet como pesquisar e baixar no youtube e outras plataformas. Crie seus pacotes de Stickers de forma automatizada com esta IA e tenha total acesso aos Avatar's de seus usuários com o comando /avatar . Todas ferramentas possíveis para Gerenciamento de Grupos podem ser encontradas em nossa IA, confira os menus. Quer restringir arquivos somente a pessoas que colaboram finaneceiramente com seu projeto, esta IA também faz isto separando seus usuários e limitando comandos. Nossa IA conta com os mais diversos Interpretadores de Linguagem de Programaçao Novas informações sempre serão passadas através dos menus, em caso de problemas ou bug's reporte ao Desenvolvedor com o comando /bug seguido de seu texto.

@GorpoOrko | Python Developer ©2020 - <a href="https://t.me/tcxsproject2">TCXS Project™</>'''.format(version=version), parse_mode='html', reply_markup=keyboard.desenvolvedor, disable_web_page_preview=True)


        elif msg['data'] == 'comandos_dev':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),"""
[*] COMANDOS APENAS PARA DESENVOLVEDOR [*]

Os comandos abaixo funcionam apenas para quem hospeda o bot, somente o desenvolvedor tem acesso a estes comandos!
            
!apagar mensagens - apaga tudo IA e faz backup da Database.
!backup - Faz backup do bot e upload para o Dropbox.
!update - Atualiza o bot de acordo com codigo postado no Github.
!cmd - Executa um comando.
!chat - Obtem infos de um chat.
!del - Deleta a mensagem respondida.
!doc - Envia um documento do server.
!eval - Executa uma função Python.
!exec - Executa um código Python.
!leave - O bot sai do chat.
!plist - Lista os plugins ativos.
!promote - Promove alguém a admin.
!restart - Reinicia o bot.
!upgrade - Atualiza a base do bot.(deprecated)
!upload - Envia um arquivo para o servidor.
!baixar - baixa um documento para o server
!dropbox - faz upload para o Dropbox
!link - gera um link direto do Telegram
  | - Define desligamento do bot, EX: 12|30""",'markdown', reply_markup=keyboard.voltar_comandos_admins)
            #return True







#FERRAMENTAS GERAIS------------------------------------------------------------------------------------------------------------------------------------------------->
        #menus de ferramentas:
        elif msg['data'] == 'ferramentas_gerais':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"```------ Informações extras ou complementares sobre o Bot ou Projeto TCXS Store PS3 Hacker Team.```",'markdown', reply_markup=keyboard.ferramentas_gerais)
            #return True
        elif msg['data'] == 'ferramenta_comandos':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),"""
/tr      -traduz um texto
/yt      -pesquisa videos no YouTube
/r       -pesquisa um termo no redit
/clima   -exibe informacoes de clima
/coub    -pesquisa de pequenas animações
/dados   -jogo de dados
/gif     -gif do giphy
/git     -usuario do github
/id      -id do usuario
/ip      -informa dados de um ip
/jsondump -retorna dados formatados
/stickerid -pega id de um sticker
/getsticker -baixa um sticker
/pypi -pesquisa libs python
/rextester -interpretador de varias linguagens de programação
/mark -repete o texto informado usando Markdown
/html -repete o texto informado usando HTML
/request -faz uma requisicao a um site
/rt -repete concordando com o usuario na reposta  
/fala -Repete o texto que voce pedir para ele falar
/print -gera um print doque falou
/dogbin - envia seu material em texto para o dogbin
/hastebin - envia seu material em texto para o hastebin
/echo - Repete o texto informado.    
/shorten - Encurta uma URL.
/recog - reconhecimento com IA (nem sempre disponivel)
/notepad - cria um site com o texto enviado
/crawler - pega todos links dentro de um site
/corrigir - corrige palavras erradas
/token - Exibe informaces de um token de outro bot.""", reply_markup=keyboard.voltar_ferramentas_gerais)
            #return True

        elif msg['data'] == 'ferramenta_reconhecimento':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']), """
        🕵️‍️‍***SOBRE O SISTEMA DE RECONHECIMENTO DA IA*** 
        ```----  Este bot envia conta com um sistema de  reconhecimento com Deep e Machine Learning utilizando as Lib's Tensorflow, Keras e OpenCV.```
        🤖`Para usar este sistema basta responder qualquer imagem com o comando /recog e aguardar a IA enviar sua imagem com os objetos reconhecidos nela.`
            """, 'markdown', reply_markup=keyboard.voltar_ferramentas_gerais)

        elif msg['data'] == 'ferramenta_perguntas':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']), """
💾***SISTEMA DE PERGUNTAS E RESPOSTAS PARA ADMINS***
```---- Este bot grava todas perguntas desde que contenham ??, avise seus usuários que quando quiserem cadastrar uma pergunta usem duas interrogações no final da frase e automáticamente sua pergunta será cadstrada e assim que um administrador ver pode responder ou cadastrar ela no robo ensinando a Inteligência Artificial.```
🤖`Cadastrar pergunta exemplo:` Como faço para ser tao esperto como o robo?? 
🤖`Ver perguntas cadastradas apenas digite:` perguntas  
🤖`Limpar perguntas cadastradas ou já respondidas digite:` apagar perguntas
    """, 'markdown', reply_markup=keyboard.voltar_ferramentas_gerais)

        elif msg['data'] == 'ferramenta_frequencia':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),"""
💾***SOBRE A FREQUENCIA DE MENSAGENS*** 
```----  Este bot envia mensagens baseado em uma frequencia que deve ser setada entre 2 e 10,este comando pode funcionar somente para administradores dependendo das configurações, seus comandos são:```
🤖`frequencia 0 = mudo`
🤖`frequencia 2 = fala pouco`
🤖`frequencia 10 = fala muito`
    """,'markdown', reply_markup=keyboard.voltar_ferramentas_gerais)

        elif msg['data'] == 'ferramenta_proibicoes':
            try:
                cursor_sqlite.execute("""SELECT * FROM proibido; """)
                mensagens_proibidas = cursor_sqlite.fetchall()
                todas_proibidas = []
                separador = ' \n'
                for result in mensagens_proibidas:
                    todas_proibidas.append(result['termo'])
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),"""
💾***SOBRE PROIBIR E PERMITIR PALAVRAS***
```----  Este bot pode restringir/permitir palavras, este comando pode funcionar somente para administradores dependendo das configurações, altere as proibições de palavras ou frases, link etc... com os comandos:```
🤖`proibir uma palavra:` proibir corno
🤖`permitir uma palavra:` permtir corno
🤖`ver palavras proibidas:` proibidas
    """,'markdown', reply_markup=keyboard.voltar_ferramentas_gerais)
                time.sleep(2)
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      f'`Palavras Proibidas:`\n ***{separador.join(map(str, todas_proibidas))}***\nPara proibir use `proibir` e para permitir use `permitir`.',
                                      'markdown', reply_markup=keyboard.voltar_ferramentas_gerais)
            except:
                pass


        elif msg['data'] == 'ferramenta_inteligencia':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),"""
💾***SOBRE O ENVIO DE MENSAGENS DA IA*** 
```----  Este bot envia mensagens baseado em dois tipos de inteligência, uma local e outra global, onde a local é tudo que aprendeu naquele grupo e ja a global é oque ele aprendeu por onde passou,este comando pode ser restrito a administradores, veja exemplos:```
🤖`inteligencia local = irá falar  somente sobre oque aprendeu neste grupo, comando:`
inteligencia local
🤖`inteligencia global = ira falar sobre tudo que aprendeu em todos os lugares que passou na internet`
inteligencia global
🤖`fale sobre = ele fala sobre determinado assunto, exemplo:`
fale sobre playstation
    """,'markdown', reply_markup=keyboard.voltar_ferramentas_gerais)

            # mostra os comandos cadastrados manualmente para os admins
        elif msg['data'] == 'ferramenta_comandos_manuais':
            adm = await is_admin(msg['message']['chat']['id'], msg['from']['id'], msg['from']['id'])
            if adm['user'] == True:
                try:
                    cursor_sqlite.execute("""SELECT * FROM comandos; """)
                    resultados = cursor_sqlite.fetchall()
                    todos_comandos = []
                    separador = ' \n'
                    for result in resultados:
                        todos_comandos.append(result['comando'])
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                              f'`Comandos cadastrados:`\n ***{separador.join(map(str, todos_comandos))}***',
                                              'markdown', reply_markup=keyboard.voltar_ferramentas_gerais)
                except Exception as e:
                    pass
        elif msg['data'] == 'ferramenta_lista_jogos':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      f"```------ Tenho esta lista de jogos em PKG para PlayStation3 todos com links diretos, estes jogos são originais, portanto precisam de Licenças ou como conhecemos precisam dos Rap's```\n`Basta clicar no botão que te trarei a lista com link direto para download, pedimos sua contribuição para que este projeto se mantenha vivo, Obrigado a todos da TCXS!` ",
                                      'markdown', reply_markup=keyboard.lista_jogos)

        elif msg['data'] == 'ferramenta_cria_xml':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']), """***Temos um programa de computador que cria lojas diretamente no console PlayStation3***
/tcxspyject -criar lojas

***Criar XML PSP Instruções:*** 
`comando:`/psp -cria xml para loja
    ```
    1 - meu comando sempre começa com /xml
    2 - eu não aceito espaços no nome de arquivo, nome de jogo e nem na descrição!
    3 - você pode copiar o caractere especial invisivel dentro das aspas abaixo para usar onde precisar de espaço!``` 
    `Copie de dentro das aspas o caractere invisivel:`"⠀"

    **VAMOS AO COMANDO EM SI**
    `Exemplo com caractere invisivel:`
    ``` gow god⠀of⠀war descriçao⠀usando⠀caractere⠀invisivel     www.linkdropbox.com```
    `Exemplo sem caractere visivel:`
    ``` /psp gow god_of_war descrição_sem_caractere_visivel   www.linkdropbox.com```
    **Onde cada campo:**
    `/psp` ```- chama comando```
    `gow` ```- nome do xml```
    `god_of_war` ```- nome do jogo, se quiser tirar os _ usar caractere especial no lugar```
    `descrição_do_jogo` ```- descrição, se quiser tirar os _ usar caractere especial no lugar``` 
    `www.linkdropbox.com` ```- Link do Dropbox```

***Criar XML PS1 Instruções:*** 
`comando:`/ps1 -cria xml para loja
    ```
    1 - meu comando sempre começa com /xml
    2 - eu não aceito espaços no nome de arquivo, nome de jogo e nem na descrição!
    3 - você pode copiar o caractere especial invisivel dentro das aspas abaixo para usar onde precisar de espaço!``` 
    `Copie de dentro das aspas o caractere invisivel:`"⠀"

    **VAMOS AO COMANDO EM SI**
    `Exemplo com caractere invisivel:`
    ``` gow god⠀of⠀war descriçao⠀usando⠀caractere⠀invisivel     www.linkdropbox.com```
    `Exemplo sem caractere visivel:`
    ``` /ps1 gow god_of_war descrição_sem_caractere_visivel   www.linkdropbox.com```
    **Onde cada campo:**
    `/ps1` ```- chama comando```
    `gow` ```- nome do xml```
    `god_of_war` ```- nome do jogo, se quiser tirar os _ usar caractere especial no lugar```
    `descrição_do_jogo` ```- descrição, se quiser tirar os _ usar caractere especial no lugar``` 
    `www.linkdropbox.com` ```- Link do Dropbox```

***Criar XML PS2 Instruções:*** 
`comando:`/ps2 -cria xml para loja
    ```
    1 - meu comando sempre começa com /xml
    2 - eu não aceito espaços no nome de arquivo, nome de jogo e nem na descrição!
    3 - você pode copiar o caractere especial invisivel dentro das aspas abaixo para usar onde precisar de espaço!``` 
    `Copie de dentro das aspas o caractere invisivel:`"⠀"

    **VAMOS AO COMANDO EM SI**
    `Exemplo com caractere invisivel:`
    ``` gow god⠀of⠀war descriçao⠀usando⠀caractere⠀invisivel     www.linkdropbox.com```
    `Exemplo sem caractere visivel:`
    ``` /ps2 gow god_of_war descrição_sem_caractere_visivel   www.linkdropbox.com```
    **Onde cada campo:**
    `/ps2` ```- chama comando```
    `gow` ```- nome do xml```
    `god_of_war` ```- nome do jogo, se quiser tirar os _ usar caractere especial no lugar```
    `descrição_do_jogo` ```- descrição, se quiser tirar os _ usar caractere especial no lugar``` 
    `www.linkdropbox.com` ```- Link do Dropbox```

***Criar XML PS3 Instruções:*** 
`comando:`/ps3 -cria xml para loja
    ```
     1 - meu comando sempre começa com /xml
     2 - eu não aceito espaços no nome de arquivo, nome de jogo e nem na descrição!
     3 - você pode copiar o caractere especial invisivel dentro das aspas abaixo para usar onde precisar de espaço!
     4 - meu sistema para por jogos de PS3 aceitam apenas 3 links preciso deles como exemplos.``` 
     `Copie de dentro das aspas o caractere invisivel:`"⠀"

     **VAMOS AO COMANDO EM SI**
     `Exemplo com caractere invisivel:`
     ``` gow god⠀of⠀war descriçao⠀usando⠀caractere⠀invisivel     www.linkdropbox.com  www.linkdropbox.com  www.linkdropbox.com```
     `Exemplo sem caractere visivel:`
     ``` /ps3 gow god_of_war descrição_sem_caractere_visivel   www.linkdropbox.com www.linkdropbox.com www.linkdropbox.com```
     **Onde cada campo:**
     `/ps3` ```- chama comando```
     `gow` ```- nome do xml```
     `god_of_war` ```- nome do jogo, se quiser tirar os _ usar caractere especial no lugar```
     `descrição_do_jogo` ```- descrição, se quiser tirar os _ usar caractere especial no lugar``` 
     `www.linkdropbox.com` ```- Link do Dropbox, preciso de 3 links separados por espaço```
/ps3 -cria xml para loja""", 'markdown', reply_markup=keyboard.voltar_ferramentas_gerais)


#INFORMAÇÕES E EXTRAS------------------->
        elif msg['data'] == 'infos_extras':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"```------ Aconselhamos que leia atentamente as regras, é de suma importancia saber as regras antes de doar para depois não haver reclamações tanto pela parte dos usuários como por parte da administração, somente após ler e concordar com todos os termos abaixo realize sua doação, ja deixamos claro que não prestamos reembolsos.```",'markdown', reply_markup=keyboard.info_extras)
            #return True
        elif msg['data'] == 'info_adquirir':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"```------ A TCXS Project fornece e desenvolve o aplicativo para PlayStation3 TCXS Store, para poder ter nosso aplicativo em seu console basta fazer uma doação nos botões deste bot ou pelo site, antes de doar leia atentamente a todas as regras, já quero explicar como funciona a doação, todo montante arrecadado fica preso em uma conta do Mercado Pago a qual é usada para pagar o servidor do Dropbox e outros serviços, ao doar você esta participando de uma vaquinha onde a união de todos doadores mantém a vaquinha no mercado pago assim possibilitando pagar os serviços que usamos, nossa loja não é paga e em momento algum você é obrigado a pagar, fornecemos jogos para download direto aqui neste bot bem como temos uma loja free que tem todos jogos das demais lojas free, a loja ficou definida apenas para doadores a pedido deles, pois o download fica muito mais rápido e não temos mais perda de jogos, ressalto que o grupo de doadores esta limitado apenas a 200 pessoas e caso esteja lotado você terá que esperar alguem sair, continuando... Logo após doar você deve ir em nosso grupo de telegram e procurar por @MsT3Dz ou @Odeiobot e mostrar seu comprovante de doação assim você estará dentro do grupo que contém as novidades, jogos e nossa TCXS Store PKG PlayStation3.```",'markdown', reply_markup=keyboard.voltar_info_extras)
            #return True
        elif msg['data'] == 'info_doacao':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"""```------ As doações são feitas pelo mercado pago, onde aceitamos todos os cartões, pagamentos online e boletos.
Não prestamos reembolsos pois se trata de doações e não uma venda direta para uso dos serviços!
O material completo é apenas para doadores. Além do projeto para PlayStation3  a TCXS Project conta com inumeros projetos e Sites para seu entreterimento. Após fazer sua doação basta ir no grupo de TELEGRAM e procurar pelo nosso administrador @MsT3Dz  ou @Odeiobot , enviar um print de seu comprovante de pagamento que ele irá fornecer acesso a todo material, exigimos que seja feito o pedido no grupo! Outros administradores não irão te responder no privado, contamos com seu bom senso e cordialidade! NÃO PRESTAMOS REEMBOLSOS!
Queremos deixar a todos cientes que as doações feitas são exclusivas para pagar os servidores da Dropbox e serviços como hospedagem de site, sendo assim nos adm’s declaramos não receber nenhum valor neste projeto sendo assim nosso trabalho voluntário e todo e qualquer que queira entrar na equipe para ajudar a contribuir de forma expontanêa é bem vindo. Nossa equipe desenvolve sem cobrar nada pela sua mão de obra os sites acima citados bem como o desenvolvimento da TCXS Store PKG e a conversão e upload de jogos dentro dos servidores da Dropbox para assim os fornecer em formato NO-HAN para os usuários, fornecemos dentro da Plataforma PlayStation3 jogos de PS2, PS2, PsP, Emuladores das mais diversas plataformas! Álem disto disponibilizamos aos usuários a experiencia de ter sites para download de jogos nas mais variadas paltaformas e em especial jogos de PS3 PKG tudo aberto gratuitamente a comunidade bem como este site e outros sites mencionados aqui e que encontram-se nos menus.```""",'markdown', reply_markup=keyboard.voltar_info_extras)
            #return True
        elif msg['data'] == 'info_requisitos':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"""```------ Para usar a TCXS Store PKG você precisa ter seu console exploitado ou desbloqueado, nossa loja funciona nos consoles CFW, OFW, nas versões HAN e HEN, porém precis atender alguns requisitos para usar a TCXS Store PKG:
- Console Desbloqueado/exploitado.
- Versão exploit Han/Hen.
- Assinaturas previamente inseridas ( Raps’).
- Configurações de internet corretas.
- Espaço para download de jogos em seu hd.
- Conhecer previamente tudo sobre seu sistema de desbloqueio/exploit.
- Saber solucionar seus erros.
- Estar ciente que ao doar para a TCXS Store você não esta fazendo uma compra e sim ajudando a pagar os servidores da Dropbox onde upamos os jogos.CONSIDERE SE PARTICIPANDO DE UMA VAQUINHA COLETIVA ONDE TODOS USUARIOS DA TCXS AJUDAM NESTA VAQUINHA PARA MANTER O SERVIDOR```""",'markdown', reply_markup=keyboard.voltar_info_extras)
            #return True
        elif msg['data'] == 'info_suporte':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"""```------ Prestamos suporte somente para nosso aplicativo e jogos, estejam cientes que:
Suporte será prestado somente para a TCXS Store.
Suporte será prestado somente para jogos que são convertidos pela equipe.
Por se tratar de copias modificadas de jogos nossos jogos constantemente são reupados.
Por se tratar de copias modificadas ao cair dos links, os mesmos após conteúdo upado, são substitúidos na TCXS Store PKG.
Tenha ciencia de que links podem vir a cair ( não temos frequencia disto).
Saiba que a administração não presta suporte para seu desbloqueio e exploit, mas aconselhamos levar em um técnico competente caso não saiba realizar as operações básicas e avançadas de seu console.
Caso queira se aventurar em aprender tudo sobre seu desbloqueio ou exploit aconselhamos o fórum da PSX Place que são os desenvolvedores do desbloqueio e exploit, não iremos dar suporte ao material de terceiros ou erros cometidos por usuarios ou consoles vindo de tecnicos que não fizeram um bom exploit ou um bom desbloqueio.```""",'markdown', reply_markup=keyboard.voltar_info_extras)
            #return True-------------------




        #------------------------------------------------------------------------------
        #CONFIGURAÇÕES DOS ADMINISTRADORES E DA IA DO BOT
        elif msg['data'] == 'btn_banimento':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"***{msg['from']['first_name']}, clique nos botões para ativar ou desativar o Sistema de Banimento Automático.***",'markdown', reply_markup=keyboard.configuracoes_banimento)
        elif msg['data'] == 'admin_configuracoes':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"***Configurações da Inteligência Artificial:***\n`Instruções nos menus anteriores.`",'markdown', reply_markup=keyboard.configuracoes)
        elif msg['data'] == 'btn_perguntas':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"***{msg['from']['first_name']}, clique nos botões e confira as perguntas cadastradas ou apague as perguntas da Inteligência Artificial.***",'markdown', reply_markup=keyboard.configuracoes_perguntas)
        elif msg['data'] == 'btn_frequencia':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"***{msg['from']['first_name']}, clique nos botões e a frequência de fala da Inteligência Artificial.***",'markdown', reply_markup=keyboard.configuracoes_frequencia)
        elif msg['data'] == 'btn_inteligencia':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"***{msg['from']['first_name']}, clique nos botões e altere o conhecimento Inteligência Artificial.***",'markdown', reply_markup=keyboard.configuracoes_inteligencia)
        elif msg['data'] == 'btn_logs':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"***{msg['from']['first_name']}, clique nos botões para baixar os logs salvos ou limpar e baixar os logs.***",'markdown', reply_markup=keyboard.configuracoes_logs)

        #ENTREGA DE LOGS COM BOTOES - APENAS ADMS
        elif msg['data'] == 'btn_verlogs':
            adm = await is_admin(msg['message']['chat']['id'], msg['from']['id'], msg['from']['id'])
            if adm['user'] == True:
                try:
                    cursor_logs.execute("""SELECT * FROM mensagens ; """)
                    mensagens_logs = cursor_logs.fetchall()
                    arquivo_logs = open('arquivos/logs.txt', 'a', encoding='utf-8')
                    arquivo_logs.write('-------[+] REGISTO DE MENSAGENS CAPTADAS PELO BOT NOS GRUPOS E PRIVADO [+]-------\n\n')
                    for mensagem in mensagens_logs:
                        grupo = mensagem['grupo']
                        tipo_grupo = mensagem['tipo_grupo']
                        id_grupo = mensagem['id_grupo']
                        usuario = mensagem['usuario']
                        id_usuario = mensagem['id_usuario']
                        linguagem = mensagem['linguagem']
                        tipo = mensagem['tipo']
                        data = mensagem['data']
                        id_mensagem = mensagem['id_mensagem']
                        mensagem = mensagem['mensagem']
                        try:
                            texto = f"Usuario: {usuario} |Id Usuario:{id_usuario} | Linguagem: {linguagem} | Grupo: {grupo} | Id Grupo: {id_grupo} | Tipo Grupo: {tipo_grupo} Tipo: {tipo} | Data: {data} ----->\nMensagem: {mensagem}\n"
                        except:
                            texto = ''
                        arquivo_logs.write(texto)
                    arquivo_logs.close()
                    await bot.sendDocument(msg['message']['chat']['id'], open('arquivos/logs.txt', 'rb'),reply_to_message_id=msg['message']['message_id'])
                    os.remove('arquivos/logs.txt')
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),'`Esta aqui o log de conversas que tenho armazenado:` ','markdown', reply_markup=keyboard.voltar_configuracoes)
                except Exception as e:
                    pass
            else:
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),'`Este comando é permitido somente para administradores.` ','markdown', reply_markup=keyboard.voltar_configuracoes)
        #ENTREGA DE LOGS COM BOTOES - APENAS ADMS
        elif msg['data'] == 'btn_limparlogs':
            adm = await is_admin(msg['message']['chat']['id'], msg['from']['id'], msg['from']['id'])
            if adm['user'] == True:
                try:
                    cursor_logs.execute("""SELECT * FROM mensagens; """)
                    mensagens_logs = cursor_logs.fetchall()
                    arquivo_logs = open('arquivos/logs.txt', 'a',encoding='utf-8')
                    arquivo_logs.write('-------[+] REGISTO DE MENSAGENS CAPTADAS PELO BOT NOS GRUPOS E PRIVADO [+]-------\n\n')
                    for mensagem in mensagens_logs:
                        grupo = mensagem['grupo']
                        tipo_grupo = mensagem['tipo_grupo']
                        id_grupo = mensagem['id_grupo']
                        usuario = mensagem['usuario']
                        id_usuario = mensagem['id_usuario']
                        linguagem = mensagem['linguagem']
                        tipo = mensagem['tipo']
                        data = mensagem['data']
                        id_mensagem = mensagem['id_mensagem']
                        mensagem = mensagem['mensagem']
                        try:
                            texto = f"Usuario: {usuario} |Id Usuario:{id_usuario} | Linguagem: {linguagem} | Grupo: {grupo} | Id Grupo: {id_grupo} | Tipo Grupo: {tipo_grupo} Tipo: {tipo} | Data: {data} ----->\nMensagem: {mensagem}\n"
                        except:
                            texto = ''
                        arquivo_logs.write(texto)
                    arquivo_logs.close()
                    await bot.sendDocument(msg['message']['chat']['id'], open('arquivos/logs.txt', 'rb'),reply_to_message_id=msg['message']['message_id'])
                    os.remove('arquivos/logs.txt')
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),'`Esta aqui o Backup de logs de conversas que tenho armazenado, caso preciso guarde este arquivo pois irei limpar a Database.` ','markdown', reply_markup=keyboard.voltar_configuracoes)
                    cursor_logs.execute("""DELETE FROM mensagens""")
                    conexao_logs.commit()
                    time.sleep(2)
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),'`Todos os logs dos usuários foram apagados da Database. Mantenha um backup deste arquivo!` ','markdown', reply_markup=keyboard.voltar_configuracoes)
                except Exception as e:
                    pass
            else:
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),'`Este comando é permitido somente para administradores.` ','markdown', reply_markup=keyboard.voltar_configuracoes)









        #mostra os comandos cadastrados manualmente para os admins
        elif msg['data'] == 'btn_comandos':
            adm = await is_admin(msg['message']['chat']['id'], msg['from']['id'], msg['from']['id'])
            if adm['user'] == True:
                try:
                    cursor_sqlite.execute("""SELECT * FROM comandos; """)
                    resultados = cursor_sqlite.fetchall()
                    todos_comandos = []
                    separador = ' \n'
                    for result in resultados:
                        todos_comandos.append(result['comando'])
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f'`Comandos cadastrados:`\n ***{separador.join(map(str, todos_comandos))}***\n `Veja como cadastrar comandos no menu de administradores` ','markdown', reply_markup=keyboard.voltar_configuracoes)
                except Exception as e:
                    pass

        elif msg['data'] == 'btn_proibicoes':
            adm = await is_admin(msg['message']['chat']['id'], msg['from']['id'], msg['from']['id'])
            if adm['user'] == True:
                try:
                    cursor_sqlite.execute("""SELECT * FROM proibido; """)
                    mensagens_proibidas = cursor_sqlite.fetchall()
                    todas_proibidas = []
                    separador = ' \n'
                    for result in mensagens_proibidas:
                        todas_proibidas.append(result['termo'])
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                              f'`Palavras Proibidas:`\n ***{separador.join(map(str, todas_proibidas))}***\nPara proibir use `proibir` e para permitir use `permitir`.',
                                              'markdown', reply_markup=keyboard.voltar_configuracoes)
                except:
                    pass


        # botoes que ativam ou desativam o banimento
        elif msg['data'] == 'btn_ativaban':
            adm = await is_admin(msg['message']['chat']['id'], msg['from']['id'], msg['from']['id'])
            if adm['user'] == True:
                try:
                    try:
                        grupo = f"https://t.me/{msg['message']['chat']['username']}"
                    except:
                        grupo = f"Secreto: {msg['message']['chat']['title']}"
                        pass
                    try:
                        admin = msg['message']['from']['username']
                    except:
                        admin = f"@{msg['message']['from']['id']}({msg['message']['from']['first_name']})"
                        pass
                    data = datetime.now().strftime('%d/%m/%Y %H:%M')
                    chat_type = msg['message']['chat']['type']
                    id_grupo = msg['message']['chat']['id']
                    id_admin = msg['message']['from']['id']
                    valor = 1
                    cursor_sqlite.execute(f"""DELETE FROM banimento WHERE id_grupo='{msg['message']['chat']['id']}' """)
                    cursor_sqlite.execute(f"""INSERT INTO banimento (int_id, grupo, tipo_grupo, id_grupo, admin, id_admin, data, valor)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{admin}','{id_admin}','{data}','{valor}')""")
                    conexao_sqlite.commit()
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🤖 `Sistema de Cadastramento Automático para Banimento:`***ATIVO***\nAgora todos usuários que entrarem no grupo receberão uma data limite de permanencia, caso queira remover restriçao do usuário ou inserir mais dias de permanência consulte /help", 'markdown',reply_markup=keyboard.configuracoes)
                except Exception as e:
                    pass

        # botoes que ativam ou desativam o banimento
        elif msg['data'] == 'btn_desativaban':
            adm = await is_admin(msg['message']['chat']['id'], msg['from']['id'], msg['from']['id'])
            if adm['user'] == True:
                try:
                    try:
                        grupo = f"https://t.me/{msg['message']['chat']['username']}"
                    except:
                        grupo = f"Secreto: {msg['message']['chat']['title']}"
                        pass
                    try:
                        admin = msg['message']['from']['username']
                    except:
                        admin = f"@{msg['message']['from']['id']}({msg['message']['from']['first_name']})"
                        pass
                    data = datetime.now().strftime('%d/%m/%Y %H:%M')
                    chat_type = msg['message']['chat']['type']
                    id_grupo = msg['message']['chat']['id']
                    id_admin = msg['message']['from']['id']
                    valor = 1
                    cursor_sqlite.execute(
                        f"""DELETE FROM banimento WHERE id_grupo='{msg['message']['chat']['id']}' """)
                    cursor_sqlite.execute(
                        f"""INSERT INTO banimento (int_id, grupo, tipo_grupo, id_grupo, admin, id_admin, data, valor)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{admin}','{id_admin}','{data}','{valor}')""")
                    conexao_sqlite.commit()
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']), f"🤖 `Sistema de Cadastramento Automático para Banimento:`***INATIVO***\nAgora todos usuários que entrarem no grupo não receberão uma data limite de permanncia, caso queira adicionar ou remover restriçao do usuário ou inserir mais dias de permanência de forma manual consulte /help",'markdown', reply_markup=keyboard.configuracoes)
                except Exception as e:
                    pass





        #botao para verificar as perguntas
        elif msg['data'] == 'ver_perguntas':
            try:  # VERIFICAR PERGUNTAS DOS USUARIOS----------------------------------------------------------->
                cursor_sqlite.execute("""SELECT * FROM perguntas""")
                resultados = cursor_sqlite.fetchall()
                if resultados == []:
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🤖 {msg['from']['first_name']} `não tenho perguntas cadastradas, tente outra hora ou cadastre algumas perguntas.`",'markdown', reply_markup=keyboard.configuracoes)
                else:
                    for resultado in resultados:
                        usuario = resultado['usuario']
                        pergunta = resultado['pergunta']
                        try:
                            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🤖 `Usuário:`{usuario}\n`Pergunta:`{pergunta}",'markdown', reply_markup=keyboard.configuracoes)
                            time.sleep(1)
                        except:
                            pass
            except Exception as e:
                pass
        #botao para apagar as perguntas
        elif msg['data'] == 'apagar_perguntas' :
            adm = await is_admin(msg['message']['chat']['id'], msg['from']['id'], msg['from']['id'])
            if adm['user'] == True:
                try:  # LIMPAR PERGUNTAS DOS USUARIOS------------------------------------------------------------->
                    cursor_sqlite.execute("""DELETE FROM perguntas""")
                    conexao_sqlite.commit()
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🤖 `Todas perguntas foram apagadas!`",'markdown', reply_markup=keyboard.configuracoes)
                except Exception as e:
                    pass

        #bota a frequencia da IA em baixa valor 1
        elif msg['data'] == 'frequencia_baixa':
            adm = await is_admin(msg['message']['chat']['id'], msg['from']['id'], msg['from']['id'])
            if adm['user'] == True:
                try:
                    grupo = f"https://t.me/{msg['message']['chat']['username']}"
                except:
                    grupo = f"Secreto: {msg['message']['chat']['title']}"
                    pass
                valor = '1'
                cursor_sqlite.execute("""SELECT * FROM frequencia; """)
                frequencias = cursor_sqlite.fetchall()
                comparar_vazio = []
                freq = list(frequencias)
                if freq == comparar_vazio:
                    cursor_sqlite.execute(f"""INSERT INTO frequencia(id_grupo, grupo, valor)VALUES('{msg['message']['chat']['id']}','{grupo}','{valor}')""")
                    conexao_sqlite.commit()
                else:
                    for frequencia in frequencias:  # loop em todos resultados da Database
                        if frequencia['id_grupo'] == msg['message']['chat']['id']:
                            cursor_sqlite.execute(f"""DELETE FROM frequencia WHERE id_grupo='{msg['message']['chat']['id']}'""")
                            conexao_sqlite.commit()
                            cursor_sqlite.execute(f"""INSERT INTO frequencia(id_grupo, grupo, valor)VALUES('{msg['message']['chat']['id']}','{grupo}','{valor}')""")
                            conexao_sqlite.commit()
                        if frequencia['id_grupo'] != msg['message']['chat']['id']:
                            cursor_sqlite.execute(f"""INSERT INTO frequencia(id_grupo, grupo, valor)VALUES('{msg['message']['chat']['id']}','{grupo}','{valor}')""")
                            conexao_sqlite.commit()
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🤖 `Frequencia alterada para {valor}, vou tentar falar pouco.`",'markdown', reply_markup=keyboard.configuracoes)


        # a frequencia alta faz com que o a IA fale mais este valor é multiplicado por 2 e entra em um random
        elif msg['data'] == 'frequencia_alta':
            adm = await is_admin(msg['message']['chat']['id'], msg['from']['id'], msg['from']['id'])
            if adm['user'] == True:
                try:
                    grupo = f"https://t.me/{msg['message']['chat']['username']}"
                except:
                    grupo = f"Secreto: {msg['message']['chat']['title']}"
                    pass
                valor = '6'
                cursor_sqlite.execute("""SELECT * FROM frequencia; """)
                frequencias = cursor_sqlite.fetchall()
                comparar_vazio = []
                freq = list(frequencias)
                if freq == comparar_vazio:
                    cursor_sqlite.execute(f"""INSERT INTO frequencia(id_grupo, grupo, valor)VALUES('{msg['message']['chat']['id']}','{grupo}','{valor}')""")
                    conexao_sqlite.commit()
                else:
                    for frequencia in frequencias:  # loop em todos resultados da Database
                        if frequencia['id_grupo'] == msg['message']['chat']['id']:
                            cursor_sqlite.execute(f"""DELETE FROM frequencia WHERE id_grupo='{msg['message']['chat']['id']}'""")
                            conexao_sqlite.commit()
                            cursor_sqlite.execute(f"""INSERT INTO frequencia(id_grupo, grupo, valor)VALUES('{msg['message']['chat']['id']}','{grupo}','{valor}')""")
                            conexao_sqlite.commit()
                        if frequencia['id_grupo'] != msg['message']['chat']['id']:
                            cursor_sqlite.execute(f"""INSERT INTO frequencia(id_grupo, grupo, valor)VALUES('{msg['message']['chat']['id']}','{grupo}','{valor}')""")
                            conexao_sqlite.commit()
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🤖 `Frequencia alterada para {valor}, vou tentar falar bastante.`",'markdown', reply_markup=keyboard.configuracoes)


        #frequecnia setada com 0 e deixa o bot mudo
        elif msg['data'] == 'frequencia_mudo':
            adm = await is_admin(msg['message']['chat']['id'], msg['from']['id'], msg['from']['id'])
            if adm['user'] == True:
                try:
                    grupo = f"https://t.me/{msg['message']['chat']['username']}"
                except:
                    grupo = f"Secreto: {msg['message']['chat']['title']}"
                    pass
                valor = '0'
                cursor_sqlite.execute("""SELECT * FROM frequencia; """)
                frequencias = cursor_sqlite.fetchall()
                comparar_vazio = []
                freq = list(frequencias)
                if freq == comparar_vazio:
                    cursor_sqlite.execute(f"""INSERT INTO frequencia(id_grupo, grupo, valor)VALUES('{msg['message']['chat']['id']}','{grupo}','{valor}')""")
                    conexao_sqlite.commit()
                else:
                    for frequencia in frequencias:  # loop em todos resultados da Database
                        if frequencia['id_grupo'] == msg['message']['chat']['id']:
                            cursor_sqlite.execute(f"""DELETE FROM frequencia WHERE id_grupo='{msg['message']['chat']['id']}'""")
                            conexao_sqlite.commit()
                            cursor_sqlite.execute(f"""INSERT INTO frequencia(id_grupo, grupo, valor)VALUES('{msg['message']['chat']['id']}','{grupo}','{valor}')""")
                            conexao_sqlite.commit()
                        if frequencia['id_grupo'] != msg['message']['chat']['id']:
                            cursor_sqlite.execute(f"""INSERT INTO frequencia(id_grupo, grupo, valor)VALUES('{msg['message']['chat']['id']}','{grupo}','{valor}')""")
                            conexao_sqlite.commit()
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🤖 `Frequencia alterada para {valor}, vou ficar mudo.`",'markdown', reply_markup=keyboard.configuracoes)


        #seta a IA local para os usuários receberem apenas mensagens daquele grupo.
        elif msg['data'] == 'inteligencia_local':
            adm = await is_admin(msg['message']['chat']['id'], msg['from']['id'], msg['from']['id'])
            if adm['user'] == True:
                try:
                    try:
                        grupo = f"https://t.me/{msg['message']['chat']['username']}"
                    except:
                        grupo = f"Secreto: {msg['message']['chat']['title']}"
                        pass
                    data = datetime.now().strftime('%d/%m/%Y %H:%M')
                    tipo = 'IA'
                    linguagem = 'nenhuma'
                    usuario = 'admin via botoes'
                    inteligencia = 'local'
                    chat_type = msg['message']['chat']['type']
                    id_grupo = msg['message']['chat']['id']
                    cursor_sqlite.execute(f"""DELETE FROM inteligencia WHERE id_grupo='{msg['message']['chat']['id']}' """)
                    cursor_sqlite.execute(f"""INSERT INTO inteligencia (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,inteligencia)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','{tipo}','{data}','{inteligencia}')""")
                    conexao_sqlite.commit()
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"`Inteligencia Artificial:`***{inteligencia}***\nAgora vocês irão receber coisas que aprendi nesta categoria.",'markdown', reply_markup=keyboard.configuracoes)
                except Exception as e:
                    pass

        #seta a IA Global para os usuarios receberem todos tipos de mensagem
        elif msg['data'] == 'inteligencia_global':
            adm = await is_admin(msg['message']['chat']['id'], msg['from']['id'], msg['from']['id'])
            if adm['user'] == True:
                try:
                    try:
                        grupo = f"https://t.me/{msg['message']['chat']['username']}"
                    except:
                        grupo = f"Secreto: {msg['message']['chat']['title']}"
                        pass
                    data = datetime.now().strftime('%d/%m/%Y %H:%M')
                    tipo = 'IA'
                    linguagem = 'nenhuma'
                    usuario = 'admin via botoes'
                    inteligencia = 'global'
                    chat_type = msg['message']['chat']['type']
                    id_grupo = msg['message']['chat']['id']
                    cursor_sqlite.execute(f"""DELETE FROM inteligencia WHERE id_grupo='{msg['message']['chat']['id']}' """)
                    cursor_sqlite.execute(f"""INSERT INTO inteligencia (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,inteligencia)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','{tipo}','{data}','{inteligencia}')""")
                    conexao_sqlite.commit()
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"`Inteligencia Artificial:`***{inteligencia}***\nAgora vocês irão receber coisas que aprendi nesta categoria.",'markdown', reply_markup=keyboard.configuracoes)
                except Exception as e:
                    pass









        #MODELO PARA NAO TER Q FICAR LIMPANDO CODIGO PARA CRIAR MAIS MENUS--------------->
        #elif msg['data'] == 'infos_extras':
            #await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"```------ Informações extras ou complementares sobre o Bot ou Projeto TCXS Store PS3 Hacker Team.```",'markdown', reply_markup=keyboard.infos_extras)
            #return True


















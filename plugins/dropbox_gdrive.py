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
import dropbox
import re
from config import bot,keys,sudoers
from datetime import datetime
from config import bot,sudoers
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
from datetime import datetime
from PIL import Image

async def dropbox_gdrive(msg):
    if msg.get('text') and msg['chat']['type'] != 'channel':
        if msg['from']['id']  in sudoers:
            chat_id = msg['chat']['id']
            texto = msg['text']
            token_dropbox = keys['token_dropbox']
            try:
                if 'document' in msg.get('reply_to_message') and texto.lower().startswith('dropbox'):
                    id_arquivo = msg.get('reply_to_message')['document']['file_id']
                    nome_arquivo = msg.get('reply_to_message')['document']['file_name']
                    tamanho = msg.get('reply_to_message')['document']['file_size']
                    if tamanho > 10000000:
                        await bot.sendMessage(chat_id, '🤖 `Tamanho maximo para envio de 10mb`', 'markdown',reply_to_message_id=msg['message_id'])
                    if tamanho < 10000000:
                        await bot.download_file(id_arquivo, f'arquivos/{nome_arquivo}')
                        await bot.sendMessage(chat_id,f"🤖 `{msg['from']['first_name']} acabei de baixar seu arquivo, vou upar ele para o Dropbox`",'markdown', reply_to_message_id=msg['message_id'])
                        targetfile = f"/Manicomio_bot/{nome_arquivo}"
                        d = dropbox.Dropbox(token_dropbox)
                        with open(f'arquivos/{nome_arquivo}', "rb") as f:
                            meta = d.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))
                        link = d.sharing_create_shared_link(targetfile)
                        url = link.url
                        dl_url = re.sub(r"\?dl\=0", "?dl=1", url)
                        await bot.sendMessage(chat_id,f"🤖 {msg['from']['first_name']} acabei upar seu arquivo no Dropbox:{dl_url}", reply_to_message_id=msg['message_id'])
                        os.remove(f'arquivos/{nome_arquivo}')
            except:
                pass

            try:
                if 'video' in msg.get('reply_to_message') and texto.lower().startswith('dropbox'):
                    id_arquivo = msg.get('reply_to_message')['video']['file_id']
                    data = datetime.now().strftime('%d_%m_%Y-%H_%M')
                    nome_arquivo = f'video_{data}.mp4'
                    tamanho = msg.get('reply_to_message')['video']['file_size']
                    if tamanho > 10000000:
                        await bot.sendMessage(chat_id, '🤖 `Tamanho maximo para envio de 10mb`', 'markdown',
                                        reply_to_message_id=msg['message_id'])
                    if tamanho < 10000000:
                        await bot.download_file(id_arquivo, f'arquivos/{nome_arquivo}')
                        await bot.sendMessage(chat_id,f"🤖 `{msg['from']['first_name']} acabei de baixar seu arquivo, vou upar ele para o Dropbox`",'markdown', reply_to_message_id=msg['message_id'])
                        targetfile = f"/Manicomio_bot/{nome_arquivo}"
                        d = dropbox.Dropbox(token_dropbox)
                        with open(f'arquivos/{nome_arquivo}', "rb") as f:
                            meta = d.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))
                        link = d.sharing_create_shared_link(targetfile)
                        url = link.url
                        dl_url = re.sub(r"\?dl\=0", "?dl=1", url)
                        await bot.sendMessage(chat_id,f"🤖 {msg['from']['first_name']} acabei upar seu arquivo no Dropbox:{dl_url}", reply_to_message_id=msg['message_id'])
                        os.remove(f'arquivos/{nome_arquivo}')
            except:
                pass

            try:
                if 'photo' in msg.get('reply_to_message') and texto.lower().startswith('dropbox'):
                    id_arquivo = msg.get('reply_to_message')['photo'][0]['file_id']
                    data = datetime.now().strftime('%d_%m_%Y-%H_%M')
                    nome_arquivo = f'imagem_{data}.jpg'
                    await bot.download_file(id_arquivo, f"arquivos/{nome_arquivo}")
                    await bot.sendMessage(chat_id,f"🤖 `{msg['from']['first_name']} acabei de baixar seu arquivo, vou upar ele para o Dropbox`",'markdown', reply_to_message_id=msg['message_id'])
                    targetfile = f"/Manicomio_bot/{nome_arquivo}"
                    d = dropbox.Dropbox(token_dropbox)
                    with open(f'arquivos/{nome_arquivo}', "rb") as f:
                        meta = d.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))
                    link = d.sharing_create_shared_link(targetfile)
                    url = link.url
                    dl_url = re.sub(r"\?dl\=0", "?dl=1", url)
                    await bot.sendMessage(chat_id,f"🤖 {msg['from']['first_name']} acabei upar seu arquivo no Dropbox:{dl_url}",reply_to_message_id=msg['message_id'])
                    os.remove(f'arquivos/{nome_arquivo}')
            except Exception as e:
                pass

#---------------------------------------GOOGLE DRIVE SISTEM -----------------------------------------------
            try:
                if 'document' in msg.get('reply_to_message') and texto.lower().startswith('gdrive'):
                    id_arquivo = msg.get('reply_to_message')['document']['file_id']
                    nome_arquivo = msg.get('reply_to_message')['document']['file_name']
                    tamanho = msg.get('reply_to_message')['document']['file_size']
                    if tamanho > 10000000:
                        await bot.sendMessage(chat_id, '🤖 `Tamanho maximo para envio de 10mb`', 'markdown',reply_to_message_id=msg['message_id'])
                    if tamanho < 10000000:
                       await bot.download_file(id_arquivo, f'arquivos/{nome_arquivo}')
                       await bot.sendMessage(chat_id,f"🤖 `{msg['from']['first_name']} acabei de baixar seu arquivo, vou upar ele para o Gdrive`",'markdown', reply_to_message_id=msg['message_id'])
                    # Inicia o sistema de login precisando ser so uma vez ativado assim ele
                    # salva os dados de acesso e um documento para usar sem precisar logar novamente
                    gauth = GoogleAuth("arquivos/settings_gdrive.yaml")
                    # Try to load saved client credentials
                    gauth.LoadCredentialsFile("arquivos/settings_gdrive.yaml")
                    if gauth.credentials is None:
                        # Authenticate if they're not there
                        # This is what solved the issues:
                        gauth.GetFlow()
                        gauth.flow.params.update({'access_type': 'offline'})
                        gauth.flow.params.update({'approval_prompt': 'force'})
                        gauth.LocalWebserverAuth()
                    elif gauth.access_token_expired:
                        # Refresh them if expired
                        gauth.Refresh()
                    else:
                        # Initialize the saved creds
                        gauth.Authorize()
                    # Save the current credentials to a file
                    #gauth.SaveCredentialsFile("mycreds.txt")
                    drive = GoogleDrive(gauth)
                    with open(f'arquivos/{nome_arquivo}', "r", encoding="utf8") as f:
                        file_drive = drive.CreateFile({'title': nome_arquivo,
                                                       'parents': [{
                                                           'kind': 'drive#fileLink',
                                                           'teamDriveId': '0AN5Ypubc4xZ9Uk9PVA',
                                                           'id': '1xu9izCBLkeABCS_oj8NMCAa1v4rAl8yP'}]})

                        file_drive.SetContentString(f.read())
                        file_drive.Upload(param={'supportsTeamDrives': True})
                        print("🤖 Arquivo: " + nome_arquivo + " upload Gdrive concluido.")
                    await bot.sendMessage(chat_id,f"🤖 {msg['from']['first_name']} acabei upar seu arquivo no Gdrive", reply_to_message_id=msg['message_id'])
                    os.remove(f'arquivos/{nome_arquivo}')
            except:
                pass


            try:
                if 'video' in msg.get('reply_to_message') and texto.lower().startswith('gdrive'):
                    id_arquivo = msg.get('reply_to_message')['video']['file_id']
                    data = datetime.now().strftime('%d%m%Y%H%M')
                    nome_arquivo = f'video_{data}.mp4'
                    await bot.download_file(id_arquivo, f'arquivos/{nome_arquivo}')
                    await bot.sendMessage(chat_id,f"🤖 `{msg['from']['first_name']} acabei de baixar seu arquivo, vou upar ele para o Gdrive`",'markdown', reply_to_message_id=msg['message_id'])
                    gauth = GoogleAuth("arquivos/settings_gdrive.yaml")
                    gauth.LoadCredentialsFile("arquivos/settings_gdrive.yaml")
                    if gauth.credentials is None:
                        # Authenticate if they're not there
                        # This is what solved the issues:
                        gauth.GetFlow()
                        gauth.flow.params.update({'access_type': 'offline'})
                        gauth.flow.params.update({'approval_prompt': 'force'})
                        gauth.LocalWebserverAuth()
                    elif gauth.access_token_expired:
                        # Refresh them if expired
                        gauth.Refresh()
                    else:
                        # Initialize the saved creds
                        gauth.Authorize()
                    # Save the current credentials to a file
                    #gauth.SaveCredentialsFile("mycreds.txt")
                    drive = GoogleDrive(gauth)
                    with open(f'arquivos/{nome_arquivo}', "r", encoding="utf8", errors='ignore') as f:

                        file_drive = drive.CreateFile({'title': nome_arquivo,'mimeType':'video/mp4',
                                                       'parents': [{
                                                           'kind': 'drive#fileLink',
                                                           'teamDriveId': '0AN5Ypubc4xZ9Uk9PVA',   #trocar pela id do seu drive compartilhado, para isto basta pegar o final do link quando estiver dentro do drive compartilhado
                                                           'id': '1PkykVCi8Xbs7pX3l84jc_TcLYL8bMPwC'}]}) #trocar pelo caminho de uma pasta em seu gdrive compartilhado

                        file_drive.SetContentString(f.read())
                        file_drive.Upload(param={'supportsTeamDrives': True})
                        print("🤖 Arquivo: " + nome_arquivo + " upload Gdrive concluido.")
                    await bot.sendMessage(chat_id,f"🤖 {msg['from']['first_name']} acabei upar seu arquivo no Gdrive", reply_to_message_id=msg['message_id'])
                    os.remove(f'arquivos/{nome_arquivo}')
            except Exception as e:
                pass

            try:
                if 'photo' in msg.get('reply_to_message') and texto.lower().startswith('gdrive'):
                    id_arquivo = msg.get('reply_to_message')['photo'][0]['file_id']
                    data = datetime.now().strftime('%d%m%Y%H%M')
                    nome_arquivo = f'imagem_{data}.jpeg'
                    await bot.download_file(id_arquivo, f"arquivos/{nome_arquivo}")
                    await bot.sendMessage(chat_id, f"🤖 `{msg['from']['first_name']} acabei de baixar seu arquivo, vou upar ele para o Gdrive`", 'markdown', reply_to_message_id=msg['message_id'])
                    # Inicia o sistema de login precisando ser so uma vez ativado assim ele
                    # salva os dados de acesso e um documento para usar sem precisar logar novamente
                    gauth = GoogleAuth("arquivos/settings_gdrive.yaml")
                    # Try to load saved client credentials
                    gauth.LoadCredentialsFile("arquivos/settings_gdrive.yaml")
                    if gauth.credentials is None:
                        # Authenticate if they're not there
                        # This is what solved the issues:
                        gauth.GetFlow()
                        gauth.flow.params.update({'access_type': 'offline'})
                        gauth.flow.params.update({'approval_prompt': 'force'})
                        gauth.LocalWebserverAuth()
                    elif gauth.access_token_expired:
                        # Refresh them if expired
                        gauth.Refresh()
                    else:
                        # Initialize the saved creds
                        gauth.Authorize()
                    # Save the current credentials to a file
                    # gauth.SaveCredentialsFile("mycreds.txt")
                    drive = GoogleDrive(gauth)
                    with open(f'arquivos/{nome_arquivo}', "r", encoding="utf8", errors='ignore') as f:
                        file_drive = drive.CreateFile({'title': nome_arquivo,'mimeType':'image/jpeg',
                                                       'parents': [{
                                                           'kind': 'drive#fileLink',
                                                           'teamDriveId': '0AN5Ypubc4xZ9Uk9PVA',  #trocar pela id do seu drive compartilhado, para isto basta pegar o final do link quando estiver dentro do drive compartilhado
                                                           'id': '1O-Jd7EXAWa7Upo30WPSIBxqcXUn3-Sa8'}]})  #pasta dentro do gdrive compartilhado

                        file_drive.SetContentString(f.read())
                        file_drive.Upload(param={'supportsTeamDrives': True})
                        print("🤖 Arquivo: " + nome_arquivo + " upload Gdrive concluido.")
                    await bot.sendMessage(chat_id, f"🤖 {msg['from']['first_name']} acabei upar seu arquivo no Gdrive", reply_to_message_id=msg['message_id'])
                    os.remove(f'arquivos/{nome_arquivo}')
            except Exception as e:
                pass








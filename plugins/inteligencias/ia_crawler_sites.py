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

import requests
from urllib.request import urlparse, urljoin
from bs4 import BeautifulSoup
from config import bot
import os



# armazena todas as urls internas e externas em um set
urls_internas = set()
urls_externas = set()
total_url_visitadas = 0

#Checka se a url é válida------------------>
def url_valida(url):
    url_analisada = urlparse(url)
    return bool(url_analisada.netloc) and bool(url_analisada.scheme)


#Retorna todos os URLs encontrados em `url 'nos quais pertence ao mesmo site------>
def todosLinks(url):
    # todos os URLs de `url`
    urls = set()
    # nome de domínio da URL sem o protocolo
    dominio_site = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        # href vazia----
        if href == "" or href is None:
            continue
        #adiciona a URL se for relativo e não o link absoluto
        href = urljoin(url, href)
        href_analisada = urlparse(href)
        #remova parâmetros de URL GET, fragmentos de URL etc.
        href = href_analisada.scheme + "://" + href_analisada.netloc + href_analisada.path
        # não é uma url valida
        if not url_valida(href):
            continue
        # já está no set
        if href in urls_internas:
            continue
        # capta links externos e internos do site
        if dominio_site not in href:
            if href not in urls_externas:
                urls_externas.add(href)
            continue
        urls.add(href)
        urls_internas.add(href)
    return urls


def crawler(url, max_urls=50):
    global total_url_visitadas
    total_url_visitadas += 1
    links = todosLinks(url)
    for link in links:
        if total_url_visitadas > max_urls:
            break
        crawler(link, max_urls=max_urls)
        #pega o nome de dominio do site
        nome_dominio = urlparse(url).netloc
        # salva os links internos em um arquivo
        with open(f"arquivos/links_internos.txt", "w") as f:
            for internal_link in urls_internas:
                   f.write(internal_link)
                   #print(internal_link.strip(), file=f)
            f.close()
        # salva os links externos em um arquivo
        with open(f"arquivos/links_externos.txt", "w") as f:
            for external_link in urls_externas:
                f.write(external_link)
                #print(external_link.strip(), file=f)
            f.close()





async def crawling(msg):
    try:
        chat_type = msg['chat']['type']
        chat_id = msg['chat']['id']
        if chat_type == 'supergroup':
            if msg['text'].split()[0] == 'crawler' or msg['text'].split()[0] == '/crawler':
                url = msg['text'].split()[1]
                try:
                    amax_urls = msg['text'].split()[2]
                    max_urls = amax_urls
                except:
                    max_urls = 2
                nome_dominio = urlparse(url).netloc
                b = await bot.sendMessage(chat_id,f'🤖 `Crawler no site {nome_dominio} iniciado aguarde...`','markdown', reply_to_message_id=msg['message_id'])
                a = crawler(url,max_urls)
                await bot.editMessageText((msg['chat']['id'], b['message_id']), f'🤖 `Crawler do site {nome_dominio} concluído, aqui estão os arquivos com os links:`','markdown')
                await bot.sendDocument(chat_id,document=open('arquivos/links_internos.txt','rb'))#,caption=f'Links internos que consegui captar no site {nome_dominio}',reply_to_message_id=msg['message_id'])
                await bot.sendDocument(chat_id, document=open('arquivos/links_externos.txt', 'rb'))#,caption=f'Links externos que consegui captar no site {nome_dominio}',reply_to_message_id=msg['message_id'])
                os.remove('arquivos/links_internos.txt')
                os.remove('arquivos/links_externos.txt')
    except Exception as e:
        pass



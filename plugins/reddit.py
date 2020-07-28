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


import re
import aiohttp
from config import bot
import urllib


def treattitle(title):
    title = title.replace("_", " ")
    title = title.replace("[", "(")
    title = title.replace("]", ")")
    title = title.replace("(", "(")
    title = title.replace(")", ")")
    return title


async def reddit(msg):
    if msg.get('text'):
        if msg['text'].split()[0] == '/r' or msg['text'].split()[0] == '!r':
            sub = msg['text'][3:]
            
            if sub:
                sub = re.findall(r'\S*', sub)
                sub = "r/" + sub[0] if sub[0:2] != "r/" else sub[0]
                url = "http://www.reddit.com/" + sub + "/.json?limit=6"
                subreddit = "http://www.reddit.com/" + sub
                async with aiohttp.ClientSession() as session:
                    request = await session.get(url, headers={'User-agent': 'testscript by /u/fakebot3'})
                    data = await request.json()
                posts = ""
                if request.status == 200:
                    for post in data['data']['children']:
                        domain = post['data']['domain']
                        title = treattitle(post['data']['title'])
                        purl = urllib.parse.quote_plus(post['data']['url'])
                        isnsfw_bool = post['data']['over_18']
                        permalink = "http://www.reddit.com" + post['data']['permalink']
                        if isnsfw_bool:
                            isnsfw = "nsfw"
                        else:
                            isnsfw = "sfw"
                        post = u"`> `[{title}]({pUrl})` <{nsfw}> - `[comments]({permalink})\n".format(title=title,
                                                                                                      permalink=permalink,
                                                                                                      nsfw=isnsfw,
                                                                                                      pUrl=purl,
                                                                                                      domain=domain)
                        posts += post
                    if posts:
                        await bot.sendMessage(msg['chat']['id'],
                                              "[{sub}]({subreddit})`:`\n\n".format(sub=sub,
                                                                                   subreddit=subreddit) + posts,
                                              reply_to_message_id=msg['message_id'], parse_mode="Markdown",
                                              disable_web_page_preview=True)
                    else:
                        await bot.sendMessage(msg['chat']['id'],
                                              u"`Não consegui achar {sub}, tente de novo`".format(sub=sub),
                                              reply_to_message_id=msg['message_id'], parse_mode="Markdown",
                                              disable_web_page_preview=True)
                elif request.status_code == 403:
                    await bot.sendMessage(msg['chat']['id'], "`Subreddit não existe verifique seu termo.`",
                                          reply_to_message_id=msg['message_id'], parse_mode="Markdown")
                else:
                    await bot.sendMessage(msg['chat']['id'],
                                          f"`Aconteceu um erro, o  {request.status_code} para ser especifico.`",
                                          reply_to_message_id=msg['message_id'],
                                          parse_mode="Markdown")
            else:
                await bot.sendMessage(msg['chat']['id'],
                                      "`Digite este comando para ter os top posts do reddit.\nEx: /r Awww`",
                                      parse_mode="Markdown", reply_to_message_id=msg['message_id'])

            return True




        if msg['text'].split()[0] == 'reddit':
                sub = msg['text'][7:]
                
                if sub:
                    sub = re.findall(r'\S*', sub)
                    sub = "r/" + sub[0] if sub[0:2] != "r/" else sub[0]
                    url = "http://www.reddit.com/" + sub + "/.json?limit=6"
                    subreddit = "http://www.reddit.com/" + sub
                    async with aiohttp.ClientSession() as session:
                        request = await session.get(url, headers={'User-agent': 'testscript by /u/fakebot3'})
                        data = await request.json()
                    posts = ""
                    if request.status == 200:
                        for post in data['data']['children']:
                            domain = post['data']['domain']
                            title = treattitle(post['data']['title'])
                            purl = urllib.parse.quote_plus(post['data']['url'])
                            isnsfw_bool = post['data']['over_18']
                            permalink = "http://www.reddit.com" + post['data']['permalink']
                            if isnsfw_bool:
                                isnsfw = "nsfw"
                            else:
                                isnsfw = "sfw"
                            post = u"`> `[{title}]({pUrl})` <{nsfw}> - `[comments]({permalink})\n".format(title=title,
                                                                                                          permalink=permalink,
                                                                                                          nsfw=isnsfw,
                                                                                                          pUrl=purl,
                                                                                                          domain=domain)
                            posts += post
                        if posts:
                            await bot.sendMessage(msg['chat']['id'],
                                                  "[{sub}]({subreddit})`:`\n\n".format(sub=sub,
                                                                                       subreddit=subreddit) + posts,
                                                  reply_to_message_id=msg['message_id'], parse_mode="Markdown",
                                                  disable_web_page_preview=True)
                        else:
                            await bot.sendMessage(msg['chat']['id'],
                                                  u"`Não consegui achar {sub}, tente de novo`".format(sub=sub),
                                                  reply_to_message_id=msg['message_id'], parse_mode="Markdown",
                                                  disable_web_page_preview=True)
                    elif request.status_code == 403:
                        await bot.sendMessage(msg['chat']['id'], "`Subreddit não existe verifique seu termo.`",
                                              reply_to_message_id=msg['message_id'], parse_mode="Markdown")
                    else:
                        await bot.sendMessage(msg['chat']['id'],
                                              f"`Aconteceu um erro, o  {request.status_code} para ser especifico.`",
                                              reply_to_message_id=msg['message_id'],
                                              parse_mode="Markdown")
                else:
                    await bot.sendMessage(msg['chat']['id'],
                                          "`Digite este comando para ter os top posts do reddit.\nEx: /r Awww`",
                                          parse_mode="Markdown", reply_to_message_id=msg['message_id'])
                return True
        if msg['text'].split()[0] == '/r@gorpo_bot':
                sub = msg['text'][13:]
                if sub:
                    sub = re.findall(r'\S*', sub)
                    sub = "r/" + sub[0] if sub[0:2] != "r/" else sub[0]
                    url = "http://www.reddit.com/" + sub + "/.json?limit=6"
                    subreddit = "http://www.reddit.com/" + sub
                    async with aiohttp.ClientSession() as session:
                        request = await session.get(url, headers={'User-agent': 'testscript by /u/fakebot3'})
                        data = await request.json()
                    posts = ""
                    if request.status == 200:
                        for post in data['data']['children']:
                            domain = post['data']['domain']
                            title = treattitle(post['data']['title'])
                            purl = urllib.parse.quote_plus(post['data']['url'])
                            isnsfw_bool = post['data']['over_18']
                            permalink = "http://www.reddit.com" + post['data']['permalink']
                            if isnsfw_bool:
                                isnsfw = "nsfw"
                            else:
                                isnsfw = "sfw"
                            post = u"`> `[{title}]({pUrl})` <{nsfw}> - `[comments]({permalink})\n".format(title=title,
                                                                                                          permalink=permalink,
                                                                                                          nsfw=isnsfw,
                                                                                                          pUrl=purl,
                                                                                                          domain=domain)
                            posts += post
                        if posts:
                            await bot.sendMessage(msg['chat']['id'],
                                                  "[{sub}]({subreddit})`:`\n\n".format(sub=sub,
                                                                                       subreddit=subreddit) + posts,
                                                  reply_to_message_id=msg['message_id'], parse_mode="Markdown",
                                                  disable_web_page_preview=True)
                        else:
                            await bot.sendMessage(msg['chat']['id'],
                                                  u"`Não consegui achar {sub}, tente de novo`".format(sub=sub),
                                                  reply_to_message_id=msg['message_id'], parse_mode="Markdown",
                                                  disable_web_page_preview=True)
                    elif request.status_code == 403:
                        await bot.sendMessage(msg['chat']['id'], "`Subreddit não existe verifique seu termo.`",
                                              reply_to_message_id=msg['message_id'], parse_mode="Markdown")
                    else:
                        await bot.sendMessage(msg['chat']['id'],
                                              f"`Aconteceu um erro, o  {request.status_code} para ser especifico.`",
                                              reply_to_message_id=msg['message_id'],
                                              parse_mode="Markdown")
                else:
                    await bot.sendMessage(msg['chat']['id'],
                                          "`Digite este comando para ter os top posts do reddit.\nEx: /r Awww`",
                                          parse_mode="Markdown", reply_to_message_id=msg['message_id'])
                return True
            
        

            








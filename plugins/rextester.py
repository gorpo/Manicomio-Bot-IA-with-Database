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


import aiohttp
from config import bot
import re
from amanobot.namedtuple import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton


languages = {"ada": "39",
             "bash": "38",
             "brainfuck": "44",
             "c_clang": "26",
             "c_gcc": "6",
             "c_vc": "29",
             "c#": "1",
             "c++_clang": "27",
             "c++_gcc": "7",
             "c++_vc++": "28",
             "d": "30",
             "elixir": "41",
             "erlang": "40",
             "f#": "3",
             "fortran": "45",
             "go": "20",
             "haskell": "11",
             "java": "4",
             "javascript": "17",
             "kotlin": "43",
             "lisp": "18",
             "lua": "14",
             "mysql": "33",
             "nasm": "15",
             "node.js": "23",
             "objective-c": "10",
             "ocaml": "42",
             "octave": "25",
             "oracle": "35",
             "pascal": "9",
             "perl": "13",
             "php": "8",
             "postgresql": "34",
             "prolog": "19",
             "python": "24",
             "python2": "5",
             "python3": "24",
             "py3": "24",
             "py2": "5",
             "r": "31",
             "ruby": "12",
             "scala": "21",
             "scheme": "22",
             "sql server": "16",
             "swift": "37",
             "tcl": "32",
             "vb.net": "2"}

compiler_args = {
    "c++_gcc": "-Wall -std=c++14 -O2 -o a.out source_file.cpp",
    "c++_clang": "-Wall -std=c++14 -stdlib=libc++ -O2 -o a.out source_file.cpp",
    "c++_vc++": "source_file.cpp -o a.exe /EHsc /MD /I C:\\boost_1_60_0 /link /LIBPATH:C:\\boost_1_60_0\\stage\\lib",
    "c_gcc": "-Wall -std=gnu99 -O2 -o a.out source_file.c",
    "c_clang": "-Wall -std=gnu99 -O2 -o a.out source_file.c",
    "c_vc": "source_file.c -o a.exe",
    "d": "source_file.d -ofa.out",
    "go": "-o a.out source_file.go",
    "haskell": "-o a.out source_file.hs",
    "objective-c": "-MMD -MP -DGNUSTEP -DGNUSTEP_BASE_LIBRARY=1 -DGNU_GUI_LIBRARY=1 -DGNU_RUNTIME=1 -DGNUSTEP_BASE_LIBRARY=1 -fno-strict-aliasing -fexceptions -fobjc-exceptions -D_NATIVE_OBJC_EXCEPTIONS -pthread -fPIC -Wall -DGSWARN -DGSDIAGNOSE -Wno-import -g -O2 -fgnu-runtime -fconstant-string-class=NSConstantString -I. -I /usr/include/GNUstep -I/usr/include/GNUstep -o a.out source_file.m -lobjc -lgnustep-base"
}


async def rextester(msg):
    if msg.get('text'):
        if msg['text'].startswith('/rextester'):
            text = msg['text'][10:]
            rex = re.split('[ |\n]+', text, 2)
            code = rex[2:]
            reply_id = msg['message_id']
            if not text:
                await bot.sendMessage(msg['chat']['id'], """💻Bem vindo ao meu interpretador de codigos, digite meu comando seguido de uma linguagem de programação seguido de seu codigo, ex: /rextester python seu_codigo!
                    
 💻Linguagens Suportadas: -ada -bash -brainfuck -c_clang -c_gcc -c_vc -c# -c++_clang -c++_gcc -c++_vc++ -d -elixir -erlang -f#  -fortran -go -haskell -java -javascript -kotlin -lisp -lua -mysql -nasm -node.js -objective-c -ocaml -octave -oracle -pascal -perl -php -postgresql -prolog -python -python2 -python3 -py3 -py2 -r -ruby  -scala -scheme -sql server -swift -tcl -vb.net """,
                                  reply_to_message_id=reply_id)
            elif len(code) == 0:
                await bot.sendMessage(msg['chat']['id'], '💻me de uma linguagem ex /rextester python seu_codigo',
                                  reply_to_message_id=reply_id)
            elif msg['text'].split()[1] not in languages:
                await bot.sendMessage(msg['chat']['id'], '💻linguagem errada.',
                                  reply_to_message_id=reply_id)
            else:
                langs = rex[1]
                program = ' '.join(code).strip()
                source = await rexec_aio(langs, program)
                result = source.results
                warning = source.warnings
                errors = source.errors
                stats = source.stats
                if warning and errors:
                    resp = f"*Source:*\n`{program}`\n\n*Warning:*\n`{warning}`\n\n*Errors:*\n`{errors}`"
                elif warning:
                    resp = f"*Source:*\n`{program}`\n\n*Results:*\n`{result}`\n\n*Warning:*\n`{warning}`"
                elif result and errors:
                    resp = f"*Source:*\n`{program}`\n\n*Results:*\n`{result}`\n*Errors:*\n`{errors}`"
                elif errors:
                    resp = f"*Source:*\n`{program}`\n\n*Errors:*\n`{errors}`"
                else:
                    resp = f"*Source:*\n`{program}`\n\n*Results:*\n`{result}`"
                if len(resp) > 4096:
                    await bot.sendMessage(msg['chat']['id'], 'muito longo!', reply_to_message_id=reply_id, parse_mode='markdown')
                else:
                    await bot.sendMessage(msg['chat']['id'], resp, reply_to_message_id=reply_id, parse_mode='markdown')
            return True

        if msg['text'].startswith('/codding'):
                text = msg['text'][8:]
                rex = re.split('[ |\n]+', text, 2)
                code = rex[2:]
                reply_id = msg['message_id']
                if not text:
                    await bot.sendMessage(msg['chat']['id'], """Bem vindo ao meu interpretador de codigos, digite meu comando seguido de uma linguagem de programação seguido de seu codigo, ex: /codding python seu_codigo.
 💻Linguagens Suportadas: -ada -bash -brainfuck -c_clang -c_gcc -c_vc -c# -c++_clang -c++_gcc -c++_vc++ -d -elixir -erlang -f#  -fortran -go -haskell -java -javascript -kotlin -lisp -lua -mysql -nasm -node.js -objective-c -ocaml -octave -oracle -pascal -perl -php -postgresql -prolog -python -python2 -python3 -py3 -py2 -r -ruby  -scala -scheme -sql server -swift -tcl -vbnet """,
                                      reply_to_message_id=reply_id)
                elif len(code) == 0:
                    await bot.sendMessage(msg['chat']['id'], '💻me de uma linguagem ex /codding python seu_codigo',
                                      reply_to_message_id=reply_id)
                elif msg['text'].split()[1] not in languages:
                    await bot.sendMessage(msg['chat']['id'], '💻linguagem errada.',
                                      reply_to_message_id=reply_id)
                else:
                    langs = rex[1]
                    program = ' '.join(code).strip()
                    source = await rexec_aio(langs, program)
                    result = source.results
                    warning = source.warnings
                    errors = source.errors
                    stats = source.stats
                    if warning and errors:
                        resp = f"*Source:*\n`{program}`\n\n*Warning:*\n`{warning}`\n\n*Errors:*\n`{errors}`"
                    elif warning:
                        resp = f"*Source:*\n`{program}`\n\n*Results:*\n`{result}`\n\n*Warning:*\n`{warning}`"
                    elif result and errors:
                        resp = f"*Source:*\n`{program}`\n\n*Results:*\n`{result}`\n*Errors:*\n`{errors}`"
                    elif errors:
                        resp = f"*Source:*\n`{program}`\n\n*Errors:*\n`{errors}`"
                    else:
                        resp = f"*Source:*\n`{program}`\n\n*Results:*\n`{result}`"
                    if len(resp) > 4096:
                        await bot.sendMessage(msg['chat']['id'], 'muito longo!', reply_to_message_id=reply_id, parse_mode='markdown')
                    else:
                        await bot.sendMessage(msg['chat']['id'], resp, reply_to_message_id=reply_id, parse_mode='markdown')
                return True


        if msg['text'].startswith('python'):
                text = msg['text'][7:]
                #rex = re.split('[ |\n]+', text, 2)
                rex = ['','python',f'{text}']
                code = rex[2:]
                reply_id = msg['message_id']
                if not text:
                    await bot.sendMessage(msg['chat']['id'], """💻Bem vindo ao meu interpretador de codigos, digite meu comando seguido de uma linguagem de programação seguido de seu codigo, ex: codding python3 seu_codigo!
                        
     💻Linguagens Suportadas: -ada -bash -brainfuck -c_clang -c_gcc -c_vc -c# -c++_clang -c++_gcc -c++_vc++ -d -elixir -erlang -f#  -fortran -go -haskell -java -javascript -kotlin -lisp -lua -mysql -nasm -node.js -objective-c -ocaml -octave -oracle -pascal -perl -php -postgresql -prolog -python -python2 -python3 -py3 -py2 -r -ruby  -scala -scheme -sql server -swift -tcl -vb.net """,
                                      reply_to_message_id=reply_id)
                elif len(code) == 0:
                    await bot.sendMessage(msg['chat']['id'], '💻me de uma linguagem ex /rextester python seu_codigo',
                                      reply_to_message_id=reply_id)
                elif rex[1] not in languages:
                    await bot.sendMessage(msg['chat']['id'], '💻linguagem errada.',
                                      reply_to_message_id=reply_id)
                else:
                    langs = rex[1]
                    program = ' '.join(code).strip()
                    source = await rexec_aio(langs, program)
                    result = source.results
                    warning = source.warnings
                    errors = source.errors
                    stats = source.stats
                    if warning and errors:
                        resp = f"*Source:*\n`{program}`\n\n*Warning:*\n`{warning}`\n\n*Errors:*\n`{errors}`"
                    elif warning:
                        resp = f"*Source:*\n`{program}`\n\n*Results:*\n`{result}`\n\n*Warning:*\n`{warning}`"
                    elif result and errors:
                        resp = f"*Source:*\n`{program}`\n\n*Results:*\n`{result}`\n*Errors:*\n`{errors}`"
                    elif errors:
                        resp = f"*Source:*\n`{program}`\n\n*Errors:*\n`{errors}`"
                    else:
                        resp = f"*Source:*\n`{program}`\n\n*Results:*\n`{result}`"
                    if len(resp) > 4096:
                        await bot.sendMessage(msg['chat']['id'], 'muito longo!', reply_to_message_id=reply_id, parse_mode='markdown')
                    else:
                        await bot.sendMessage(msg['chat']['id'], resp, reply_to_message_id=reply_id, parse_mode='markdown')
                return True       

        if msg['text'].startswith('-'):
                
                text = msg['text'][1:]
                rex = re.split('[ |\n]+', text, 2)
                code = rex[2:]
                reply_id = msg['message_id']
                if not text:
                    await bot.sendMessage(msg['chat']['id'], """💻Bem vindo ao meu interpretador de codigos, digite meu comando seguido de uma linguagem de programação seguido de seu codigo, ex: - python3 seu_codigo!
                        
     💻Linguagens Suportadas: -ada -bash -brainfuck -c_clang -c_gcc -c_vc -c# -c++_clang -c++_gcc -c++_vc++ -d -elixir -erlang -f#  -fortran -go -haskell -java -javascript -kotlin -lisp -lua -mysql -nasm -node.js -objective-c -ocaml -octave -oracle -pascal -perl -php -postgresql -prolog -python -python2 -python3 -py3 -py2 -r -ruby  -scala -scheme -sql server -swift -tcl -vb.net """,
                                      reply_to_message_id=reply_id)
                elif len(code) == 0:
                    await bot.sendMessage(msg['chat']['id'], '💻me de uma linguagem ex /rextester python seu_codigo',
                                      reply_to_message_id=reply_id)
                elif msg['text'].split()[1] not in languages:
                    await bot.sendMessage(msg['chat']['id'], '💻linguagem errada.',
                                      reply_to_message_id=reply_id)
                else:
                    langs = rex[1]
                    program = ' '.join(code).strip()
                    source = await rexec_aio(langs, program)
                    result = source.results
                    warning = source.warnings
                    errors = source.errors
                    stats = source.stats
                    if warning and errors:
                        resp = f"*Source:*\n`{program}`\n\n*Warning:*\n`{warning}`\n\n*Errors:*\n`{errors}`"
                    elif warning:
                        resp = f"*Source:*\n`{program}`\n\n*Results:*\n`{result}`\n\n*Warning:*\n`{warning}`"
                    elif result and errors:
                        resp = f"*Source:*\n`{program}`\n\n*Results:*\n`{result}`\n*Errors:*\n`{errors}`"
                    elif errors:
                        resp = f"*Source:*\n`{program}`\n\n*Errors:*\n`{errors}`"
                    else:
                        resp = f"*Source:*\n`{program}`\n\n*Results:*\n`{result}`"
                    if len(resp) > 4096:
                        await bot.sendMessage(msg['chat']['id'], 'muito longo!', reply_to_message_id=reply_id, parse_mode='markdown')
                    else:
                        await bot.sendMessage(msg['chat']['id'], resp, reply_to_message_id=reply_id, parse_mode='markdown')
                return True               
                




    elif msg.get('query'):
        if msg['query'].split()[0].lower() == 'run' and len(msg['query'].split()) >= 2:
            rex = re.split('[ |\n]+', msg['query'], 2)
            if len(rex) == 2:
                articles = [InlineQueryResultArticle(
                    id='a', title='give me code',
                    input_message_content=InputTextMessageContent(message_text='give me code'))]
            elif rex[1].lower() not in languages:
                articles = [InlineQueryResultArticle(
                    id='a', title='unknown Lang',
                    input_message_content=InputTextMessageContent(message_text='unknown lang'))]
            else:
                langs = rex[1]
                program = rex[2]
                source = await rexec_aio(langs, program)
                result = source.results
                warning = source.warnings
                errors = source.errors
                stats = source.stats
                if warning and errors:
                    resp = f"*Language:*\n`{langs}`\n\n*Source:*\n`{program}`\n\n*Warning:*\n`{warning}`\n\n*Errors:*\n`{errors}`"
                    desc = errors
                elif warning:
                    resp = f"*Language:*\n`{langs}`\n\n*Source:*\n`{program}`\n\n*Results:*\n`{result}`\n\n*Warning:*\n`{warning}`"
                    desc = result or 'NULL'
                elif result and errors:
                    resp = f"*Language:*\n`{langs}`\n\n*Source:*\n`{program}`\n\n*Results:*\n`{result}`\n\n*Errors:*\n`{errors}`"
                    desc = result or 'NULL'
                elif errors:
                    resp = f"*Language:*\n`{langs}`\n\n*Source:*\n`{program}`\n\n*Errors:*\n`{errors}`"
                    desc = errors
                else:
                    resp = f"*Language:*\n`{langs}`\n\n*Source:*\n`{program}`\n\n*Results:*\n`{result}`"
                    desc = result or 'NULL'
                #print(shorten_stats(stats))
                #print(len(shorten_stats(stats)))
                #print(stats)
                #print(len(stats))
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Stats', callback_data='rstats '+shorten_stats(stats))],
               ])
                articles = [InlineQueryResultArticle(
                    id='a', title=langs, description=desc,
                    input_message_content=InputTextMessageContent(message_text=resp, parse_mode='markdown'), reply_markup=keyboard)]

            return await bot.answerInlineQuery(msg['id'], results=articles, cache_time=60, is_personal=True)

    elif msg.get('data'):
        if msg['data'].startswith('rstats '):
            await bot.answerCallbackQuery(msg['id'], unshorten_stats(msg['data'][7:]), show_alert=True)
























def shorten_stats(stats):
    stats = stats.replace('Absolute running time: ', 'Art')
    stats = stats.replace('absolute running time: ', 'Art')
    stats = stats.replace('Compilation time: ', 'CT')
    stats = stats.replace('cpu time: ', 'Ct')
    stats = stats.replace('memory peak: ', 'Mp')
    stats = stats.replace('absolute service time: ', 'Ast')
    stats = stats.replace(', ', '\n')
    return stats


def unshorten_stats(stats):
    stats = stats.replace('Art', 'Absolute running time: ')
    stats = stats.replace('CT', 'Compilation time: ')
    stats = stats.replace('Ct', 'CPU time: ')
    stats = stats.replace('Mp', 'Memory peak: ')
    stats = stats.replace('Ast', 'Absolute service time: ')
    return stats


# aio rextester forked from https://github.com/nitanmarcel/rextester_py/blob/master/rextester_py/rextester_aio.py
async def __fetch(session, url, data):
    async with session.get(url, data=data) as response:
        return await response.json()


async def rexec_aio(lang, code, stdin=None):
    data = {
        "LanguageChoice": languages.get(
            lang.lower()),
        "Program": code,
        "Input": stdin,
        "CompilerArgs": compiler_args.get(
            lang.lower())}

    async with aiohttp.ClientSession(raise_for_status=True) as session:
        response = await __fetch(session, "https://rextester.com/rundotnet/api", data)
        return RextesterResult(response.get("Result"),
                               response.get("Warnings"),
                               response.get("Errors"),
                               response.get("Stats"),
                               response.get("Files"))

class RextesterResult(object):
    def __init__(self, results, warnings, errors, stats, files):
        self.results = results
        self.warnings = warnings
        self.errors = errors
        self.stats = stats
        self.files = files

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


import os
from config import bot, version, bot_username, git_repo, logs,sudoers
import sqlite3
from datetime import datetime

async def tcxs(msg):
    #variaveis iniciais---------------------:
    conexao_sqlite = sqlite3.connect('bot_database.db')
    conexao_sqlite.row_factory = sqlite3.Row
    cursor_sqlite = conexao_sqlite.cursor()
    data = datetime.now().strftime('%d/%m/%Y %H:%M')
    try:#SISTEMA DE CADASTRO LOJA PARA DOADORES PAGA   | $$$$$ | $$$$$$-------------------------------------->
        if msg['chat']['type'] == 'private' and msg.get('document') and msg['from']['id'] == logs or msg['chat']['type'] == 'private' and msg.get('document') and msg['from']['id'] == 758600965 or msg['chat']['type'] == 'private' and msg.get('document') and msg['from']['id'] == 628238139: #id_mit = 758600965   id_ted = 628238139
            if msg['document']['file_name'].split('.')[-1] == 'pkg' and 'tcxs' in msg['document']['file_name'].lower():
                if 'free' in msg['document']['file_name'].lower():
                    pass
                else:
                    id_pkg = msg['document']['file_id']
                    nome_pkg = msg['document']['file_name']
                    uploader = msg['from']['username']
                    cursor_sqlite.execute(f"INSERT INTO loja_doadores(int_id,uploader,versao,pkg,data)VALUES(null,'{uploader}','{nome_pkg}','{id_pkg}','{data}')")
                    conexao_sqlite.commit()
                    await bot.sendMessage(msg['chat']['id'],f'`Loja para Doadores atualizada na Database:` @{uploader} agora os usuarios irão receber a ***{nome_pkg}*** no grupo de doadores.','markdown',reply_to_message_id=msg['message_id'])
    except:
        pass
    try:#SISTEMA DE CADASTRO LOJA GRATUITA-------------------------------------->
        if msg['chat']['type'] == 'private' and msg.get('document') and msg['from']['id'] == logs or msg['chat']['type'] == 'private' and msg.get('document') and msg['from']['id'] == 758600965 or msg['chat']['type'] == 'private' and msg.get('document') and msg['from']['id'] == 628238139: #id_mit = 758600965   id_ted = 628238139
            if msg['document']['file_name'].split('.')[-1] == 'pkg' and 'free' in msg['document']['file_name'].lower():
                id_pkg = msg['document']['file_id']
                nome_pkg = msg['document']['file_name']
                uploader = msg['from']['username']
                cursor_sqlite.execute(f"INSERT INTO loja_free(int_id,uploader,versao,pkg,data)VALUES(null,'{uploader}','{nome_pkg}','{id_pkg}','{data}')")
                conexao_sqlite.commit()
                await bot.sendMessage(msg['chat']['id'],f'`Loja Gratuita atualizada na Database:` @{uploader} agora os usuarios irão receber a ***{nome_pkg}*** no grupo geral','markdown',reply_to_message_id=msg['message_id'])
    except:
        pass
    try:#SISTEMA DE CADASTRO FIX HAN-------------------------------------->
        if msg['chat']['type'] == 'private' and msg.get('document') and msg['from']['id'] == logs or msg['chat']['type'] == 'private' and msg.get('document') and msg['from']['id'] == 758600965 or msg['chat']['type'] == 'private' and msg.get('document') and msg['from']['id'] == 628238139: #id_mit = 758600965   id_ted = 628238139
            if msg['document']['file_name'].split('.')[0].lower() == 'fix_han' and msg['document']['file_name'].split('.')[-1].lower() == 'pkg':
                id_pkg = msg['document']['file_id']
                nome_pkg = msg['document']['file_name']
                uploader = msg['from']['username']
                cursor_sqlite.execute(f"INSERT INTO fix_han (int_id,uploader,versao,pkg,data)VALUES(null,'{uploader}','{nome_pkg}','{id_pkg}','{data}')")
                conexao_sqlite.commit()
                await bot.sendMessage(msg['chat']['id'],f'`Fix HAN atualizado na Database:` @{uploader} agora os usuarios irão receber a ***{nome_pkg}***','markdown',reply_to_message_id=msg['message_id'])
    except:
        pass
    try:#SISTEMA DE CADASTRO FIX HEN-------------------------------------->
        if msg['chat']['type'] == 'private' and msg.get('document') and msg['from']['id'] == logs or msg['chat']['type'] == 'private' and msg.get('document') and msg['from']['id'] == 758600965 or msg['chat']['type'] == 'private' and msg.get('document') and msg['from']['id'] == 628238139: #id_mit = 758600965   id_ted = 628238139
            if msg['document']['file_name'].split('.')[0].lower() == 'fix_hen' and msg['document']['file_name'].split('.')[-1].lower() == 'pkg':
                id_pkg = msg['document']['file_id']
                nome_pkg = msg['document']['file_name']
                uploader = msg['from']['username']
                cursor_sqlite.execute(f"INSERT INTO fix_hen (int_id,uploader,versao,pkg,data)VALUES(null,'{uploader}','{nome_pkg}','{id_pkg}','{data}')")
                conexao_sqlite.commit()
                await bot.sendMessage(msg['chat']['id'],f'`Fix HEN atualizado na Database:` @{uploader} agora os usuarios irão receber a ***{nome_pkg}***','markdown',reply_to_message_id=msg['message_id'])
    except:
        pass
    try:#SISTEMA DE CADASTRO FIX XML CFW-------------------------------------->
        if msg['chat']['type'] == 'private' and msg.get('document') and msg['from']['id'] == logs or msg['chat']['type'] == 'private' and msg.get('document') and msg['from']['id'] == 758600965 or msg['chat']['type'] == 'private' and msg.get('document') and msg['from']['id'] == 628238139: #id_mit = 758600965   id_ted = 628238139
            if msg['document']['file_name'].split('.')[0].lower() == 'category_network_tool2' and msg['document']['file_name'].split('.')[-1].lower() == 'xml':
                id_pkg = msg['document']['file_id']
                nome_pkg = msg['document']['file_name']
                uploader = msg['from']['username']
                cursor_sqlite.execute(f"INSERT INTO fix_cfw_xml (int_id,uploader,versao,pkg,data)VALUES(null,'{uploader}','{nome_pkg}','{id_pkg}','{data}')")
                conexao_sqlite.commit()
                await bot.sendMessage(msg['chat']['id'],f'`Fix XML para CFW atualizado na Database:` @{uploader} agora os usuarios irão receber a ***{nome_pkg}***','markdown',reply_to_message_id=msg['message_id'])
    except:
        pass
    try:#SISTEMA DE CADASTRO FIX XML HEN-------------------------------------->
        if msg['chat']['type'] == 'private' and msg.get('document') and msg['from']['id'] == logs or msg['chat']['type'] == 'private' and msg.get('document') and msg['from']['id'] == 758600965 or msg['chat']['type'] == 'private' and msg.get('document') and msg['from']['id'] == 628238139: #id_mit = 758600965   id_ted = 628238139
            if msg['document']['file_name'].split('.')[0].lower() == 'category_network' and msg['document']['file_name'].split('.')[-1].lower() == 'xml':
                id_pkg = msg['document']['file_id']
                nome_pkg = msg['document']['file_name']
                uploader = msg['from']['username']
                cursor_sqlite.execute(f"INSERT INTO fix_hen_xml (int_id,uploader,versao,pkg,data)VALUES(null,'{uploader}','{nome_pkg}','{id_pkg}','{data}')")
                conexao_sqlite.commit()
                await bot.sendMessage(msg['chat']['id'],f'`Fix XML para HEN atualizado na Database:` @{uploader} agora os usuarios irão receber a ***{nome_pkg}***','markdown',reply_to_message_id=msg['message_id'])
    except:
        pass

    if msg.get('text') and msg['chat']['type'] == 'supergroup' :
        try:
            # ----ATT PARA DOADORES TCXS PROJECT---------------------------------------->
            if   msg['text'].lower() == 'att' and msg['chat']['title'] == 'Doadores TCXS 2020':
                await bot.sendMessage(msg['chat']['id'],f"🤖 ***Olá*** @{msg['from']['username']}\n```-------->> Bem vindo a TCXS Project ,agora você faz parte dela, entenda que as doações sao mensais e nossa equipe nao ganha nada por este projeto, todo dinheiro arrecadado neste grupo é para pagar os servidores dos quais dispomos jogos. Logo a PSN STUFF IRÁ ACABAR POIS OS SERVIDORES SERÃO DESLIGADOS e assim nao terá mais os jogos gratuitos por ai, restando apenas este acervo que é mantido por voces doadores!     Vamos a Instalação!!!  --> Espero que tenha um pendrive em mãos!  --> copie os arquivos da VERSÃO 3.6 e caso use o fix de acordo com seu Exploit/Desbloqueio, se voce tem han ou CFW use o FIX HAN, caso contrário e seja o Exploit HEN em seu console use o FIX HEN, é necessaria a instalacao deste arquivo para que a loja apareca em seu console! Ative seu HAN/HEN e instale o FIX, após o FIX instalado instale a TCXS Store PKG, recomendamos reiniciar o console após este processo!!```",'markdown')
                await bot.sendMessage(msg['chat']['id'],'🤖`TUTORIAL DE COMO INSTALAR A LOJA EXPLOIT HAN E HEN!!`  https://cos.tv/videos/play/1586413688272059934','markdown')
                await bot.sendMessage(msg['chat']['id'],'🤖`COMO USAR A XML CATEGORY_NETWORK!` https://cos.tv/videos/play/1586411677524278797','markdown')
                await bot.sendMessage(msg['chat']['id'],'🤖`Tutorial Download em Segundo Plano` https://cos.tv/videos/play/1586815808334907474','markdown')
                await bot.sendMessage(msg['chat']['id'],'🤖`COMO USAR A XML CATEGORY_NETWORK! CONSOLES CFW ` https://cos.tv/videos/play/1586411677524278797','markdown')
                await bot.sendMessage(msg['chat']['id'],'🤖`PORQUE DEVE USAR PROXY NO PS3!!` https://cos.tv/videos/play/1586410545470952204','markdown')
                #LOJA PARA DOADORES LIGADA A Database-------------------------------------------------------------------------------------------------->
                cursor_sqlite.execute("""SELECT * FROM loja_doadores""")
                resultados = cursor_sqlite.fetchall()
                if resultados == []:
                    await bot.sendMessage(msg['chat']['id'], f"🤖 {msg['from']['first_name']} `não tenho lojas cadastradas, insira o banco de dados com dados ou cadastre um PKG enviando ela no meu privado com nome inicinando com TCXS, exemplo:` ***TCXS_Store_3.9.pkg***", 'markdown')
                else:
                    for resultado in resultados:
                        id_pkg = resultado['pkg']
                        nome_pkg = resultado['versao']
                        data_att = resultado['data']
                        uploader_id = resultado['uploader']
                    await bot.sendDocument(msg['chat']['id'],document=id_pkg, caption=f'{nome_pkg} upada em {data_att} por @{uploader_id}')
                #FIX HAN DATABASE-------------------------------------------------------------------------------------------------->
                cursor_sqlite.execute("""SELECT * FROM fix_han""")
                resultados = cursor_sqlite.fetchall()
                if resultados == []:
                    await bot.sendMessage(msg['chat']['id'],f"🤖 {msg['from']['first_name']} `não tenho o fix han, insira o banco de dados com dados ou cadastre um PKG enviando ele no meu privado com nome de:` ***FIX_HAN.pkg***",'markdown')
                else:
                    for resultado in resultados:
                        id_pkg = resultado['pkg']
                    await bot.sendDocument(msg['chat']['id'],document=id_pkg,caption='Fix para usuários HAN')
                # FIX HEN DATABASE-------------------------------------------------------------------------------------------------->
                cursor_sqlite.execute("""SELECT * FROM fix_hen""")
                resultados = cursor_sqlite.fetchall()
                if resultados == []:
                    await bot.sendMessage(msg['chat']['id'],f"🤖 {msg['from']['first_name']} `não tenho o fix hen, insira o banco de dados com dados ou cadastre um PKG enviando ele no meu privado com nome de:` ***FIX_HEN.pkg***",'markdown')
                else:
                    for resultado in resultados:
                        id_pkg = resultado['pkg']
                    await bot.sendDocument(msg['chat']['id'], document=id_pkg,caption='Fix para usuários HEN')
                #XML EXCLUSIVO PARA CFW-------------------------------------------------------------------------------------------------->
                cursor_sqlite.execute("""SELECT * FROM fix_cfw_xml""")
                resultados = cursor_sqlite.fetchall()
                if resultados == []:
                    await bot.sendMessage(msg['chat']['id'],f"🤖 {msg['from']['first_name']} `não tenho o fix xml para cfw, insira o banco de dados com dados ou cadastre um XML enviando ele no meu privado com nome de:` ***category_network_tool2.xml***",'markdown')
                else:
                    for resultado in resultados:
                        id_pkg = resultado['pkg']
                    await bot.sendDocument(msg['chat']['id'],document=id_pkg,caption='XML exclusivo para quem usa CFW')
                # XML EXCLUSIVO PARA HEN-------------------------------------------------------------------------------------------------->
                cursor_sqlite.execute("""SELECT * FROM fix_hen_xml""")
                resultados = cursor_sqlite.fetchall()
                if resultados == []:
                    await bot.sendMessage(msg['chat']['id'],f"🤖 {msg['from']['first_name']} `não tenho o fix xml para hen, insira o banco de dados com dados ou cadastre um XML enviando ele no meu privado com nome de:` ***category_network.xml***",'markdown')
                else:
                    for resultado in resultados:
                        id_pkg = resultado['pkg']
                    await bot.sendDocument(msg['chat']['id'], document=id_pkg,caption='XML exclusivo para quem usa HEN')

        except Exception as e:
            pass

        #LOJA PARA USUARIOS GRATUITOS ------------------------------------------------------------------->
        if msg.get('text').lower() == 'att' and not msg['chat']['title'] == 'Doadores TCXS 2020':#cagueta q tao roubando a loja kkkk
            await bot.sendMessage(msg['chat']['id'],f"***{msg['from']['first_name']} você esta tentando roubar a TCXS Store, cara vou pegar seu ip e te hackear agora mesmo!!!*** ",'markdown', reply_to_message_id=msg['message_id'])

        if msg['text'] == 'loja gratis' or msg['text'] == '/freepkg' or msg['text'] == 'free pkg' or msg['text'] == f"/freepkg@{bot_username}" or msg['text'] == 'gratis' or msg['text'] == 'Gratis' or msg['text'] == 'Free pkg':
            await bot.sendMessage(msg['chat']['id'],'Salve, venho trazer a você nossa nova att GRATUITA, espero que goste!      ----    ----     ----   Caso tenha dificuldades com o download em segundo plano confira este tutorial exclusivo feito para você doador amado que contribui para este projeto se manter em pe: https://youtu.be/_21a5REKhBc',reply_to_message_id=msg['message_id'])
            await bot.sendMessage(msg['chat']['id'],'Espero que tenha um pendrive em mãos e saiba usar a loja, não daremos suporte para USUARIOS GRATUITOS, agora  copie os arquivos abaixo para a raiz de um pendrive e coloque na USB direita do seu console, caso use HAN ative o debug ou se usa HEN ative o hen. ESTA ATT NAO USA NENHUM TIPO DE PATCH OU FIX!',reply_to_message_id=msg['message_id'])
            await bot.sendDocument(msg['chat']['id'],document='BQACAgEAAx0CTd0y0QABAfACXkmA716o7XaNW82C3Mr7O2c0bX8AApEAA0oQUUaFcnOHb037rhgE',reply_to_message_id=msg['message_id'])
        # DEMAIS INSTRUÇOES PARA USUARIOS
        if msg['text'].split()[0] == 'doadores' or msg['text'].split()[0] == '/doadores' or msg['text'].split()[0] == f"/doadores@{bot_username}":
            await bot.sendMessage(msg['chat']['id'],'`Aqui tem tudo que os doadores precisam saber:` http://tcxsproject.com.br/doadores-tcxs-store-regras/','markdown', reply_to_message_id=msg['message_id'])
        # video de bluetooth do ted
        if msg['text'] == 'bluetooth':
            await bot.sendMessage(msg['chat']['id'], 'https://www.youtube.com/watch?v=_wYG7iMa5uY',reply_to_message_id=msg['message_id'])
        # videos dos jogos
        if msg['text'] == 'ps1':
            await bot.sendVideo(msg['chat']['id'], video='BAACAgEAAx0EUYaz7wACEbVe_lDehK8EitSnLO-jP2SIqZ00PAACsgADGepZRCV_bEET9yWbGgQ', reply_to_message_id=msg['message_id'])
        if msg['text'] == 'ps2':
            await bot.sendVideo(msg['chat']['id'],video='BAACAgEAAx0EUYaz7wACEbde_lDfbzhCcTg7M1iPa0_G_rF6UQACsgADGepZRCV_bEET9yWbGgQ',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'ps3':
            await bot.sendVideo(msg['chat']['id'],video='AAMCAQADHQRRhrPvAAIS0V7_9mwf8l1awkJia_vSIK-7I4a7AAKzAAMZ6llEdIdHMW_ukXk1cHhIFwADAQAHbQADKkcAAhoE',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'exclusivos':
            await bot.sendVideo(msg['chat']['id'], video='BAACAgEAAx0EUYaz7wACEbhe_lDfqKXeXTKts9b5692tHUMg7gACsAADGepZRO4jb6TTGEoWGgQ',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'emuladores':
            await bot.sendVideo(msg['chat']['id'],video='BAACAgEAAx0CUYaz7wACEbJe_lDe2zzPbEQaW7cmwysAAbjSkPYAAgYBAAKPeSlGO3j50bdxrn8aBA',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'psp':
            await bot.sendVideo(msg['chat']['id'],video='BAACAgEAAx0CUYaz7wACEbBe_lDeo13PNB4kKRDH4sAFdn8g2AACBwEAAo95KUbzplnZj4OTAAEaBA', reply_to_message_id=msg['message_id'])
        if msg['text'] == 'tcxs' or msg['text'] == "/tcxs" or msg['text'] == f"/tcxs@{bot_username}" or msg['text'] == 'tcxs project' or msg['text'] == 'TCXS' or msg['text'] == 'TCXS Project':
            await bot.sendMessage(msg['chat']['id'], '`{} O nome TCXS foi criado com base nos botoes do PlayStation3, TRIANGLE - CIRCLE - X - SQUARE, ou seja, triangulo, bolinha, x e quadrado, kkk. Como nosso dev era publicitario e odiava a cena vendo alguns imbecis AUTO PROMOVER seu nome criando lojas e projetos, ele decidiu entrar na cena com uma nomenclatura que lembrasse a cena hacker, ou seja, siglas! Siglas esyão no cotidiano de todo mundo e é facil sua absorção bem como dentro da parte web e publicitaria a sigla tem um forte papel facilitando a digitacao e pesquisa, entao com este intuito nos denominados de TCXS Project, a palavra Project veio da vontade de que nunca morra, sendo assim um projeto qualquer um que tiver habilidade e capacidade pode entrar na equipe e ajudar a coordenar bem como tocar o projeto, ja vimos na cena varios adms passarem pela TCXS, ela e um projeto feito a varias maos e cada um doa de forma gratuita seu tempo e conhecimento para disponibilizar tudo que temos em nossas redes e arquivos. Ficamos gratos a todos que passaram por esta equipe seja dos adms aos users e seria impossivel enumerar todos, voces que sao a TCXS Project e formam este projeto que ja esta indo para seu terceiro ano!  OBRIGADO COMUNIDADE GAMER, HACKER, EXPLOITER, DEVS, USUARIOS E SIMPATIZANTES, SEM VOCES NAO EXISTIRIAMOS!`'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'proxy' or msg['text'] == f"/proxy@{bot_username}" or msg['text'] == "/proxy" or msg['text'] == 'Proxy' :
            await bot.sendMessage(msg['chat']['id'], '{} quer aumentar a velocidade dos downloads no seu PS3? Primeiro quero que saiba que o PS3 é de 2006 e sua placa de rede trabalha com um protocolo bem lento, logo nao adianta vc ter 100mb de net fibra full, pois sua placa de rede nao le neste tempo, bem como a gravaçao no HD do PS3 tambem é lenta, lembre que ele usa HDD e nao SSD assim eu te digo que  NAO ADIANTA TUA NET SER 100MB e de fibra se seu hd antigo e ja capenga grava no maximo a 30mb/s, porem vc sabia que antes de gravar no hd tudo fica na ram e so depois passa para o HD, tendo isto como afirmaçao entenda que o ps3 tem 256mb de ram e mtos slots desta ram estao ocupados, entao nao espere que o PS3 seja uma super maquina de download, ele era do tempo do final da Internet Discada e inicio da internet a Radio e ADLS na epoca da esturura dele em 2006 a maior velocidade de internet vigente como estavel era em torno de 1mb! Tendo isto em mente siga nosso tutorial de proxy para melhorar sua conexao, o serviço proxy é utilizar de outra maquina para que sua conexao esteja com o IP mais proximo do servidor e um cache seja armazenado neste -proxy- fazendo assim seu download melhorar significativamente, segue tutorial: https://youtu.be/l4o8ySk1Do4'.format(msg['from']['first_name']),reply_to_message_id=msg['message_id'])
        if msg['text'].lower() == 'fix' or msg['text'] == f"/fix@{bot_username}" or msg['text'] == "/fix":
            await bot.sendMessage(msg['chat']['id'], '`{} vejo que esta precisando do fix para sua loja aparecer, instale este pkg em seu console e a loja começara aparecer.`'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
            await bot.sendDocument(msg['chat']['id'], document='BQACAgEAAx0CWJNTSQACC7FeXTrapHT8zx-Yz6Rm85I7s6BU2gACxQADxKN4RV4960o0M9ruGAQ', reply_to_message_id=msg['message_id'])
        if msg['text'] == 'torrent' or msg['text'] == "/torrent" or msg['text'] == f"/torrent@{bot_username}" or msg['text'] == 'Torrent' or msg['text'] == 'torrents' or msg['text'] == 'Torrents':
            await bot.sendMessage(msg['chat']['id'], '{} aqui nosso canal de torrents com pkg para download: https://t.me/tcxsp'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'codigo de erro' or msg['text'] == f"/codigoerro@{bot_username}" or msg['text'] == '/codigoerro' or msg['text'] == 'lista de erros' or msg['text'] == 'erro psn' or msg['text'] == 'estou com erro' or msg['text'] == 'ta dando erro' or msg['text'] == 'deu erro' or msg['text'] == 'meu videogame ta com problema':
            await bot.sendMessage(msg['chat']['id'], '`Querido usúario do sistema PlayStation3 e praticamente impossivel decorar ou trazer a minha base de dados todos os erros, imagina entao se um humano saberia o erro por um codigo, entao vou te fornecer aqui o site oficial da sony e na lista voce podera encontrar seu erro e solucao, caso seu erro persista seu erro esta ocorrendo com o exploit, ai aconselho que voce refaca todo o seu exploit novamente, nao e dificil mas antes veja aqui se seu erro tem solucao:` https://www.playstation.com/pt-pt/get-help/#!/error-code/ ','markdown',reply_to_message_id=msg['message_id'])
        if msg['text'].lower() == 'rap' or msg['text'] == '/rap' or msg['text'] == f"/rap@{bot_username}" or msg['text'] == 'raps' or 'licença' in msg['text']  or msg['text'] == '14.000' or msg['text'] == 'assinatura':
            await bot.sendMessage(msg['chat']['id'], 'Agora precisamos apenas do PKG das licenças, no HEN as mesmas licenças servem para todos! Tutorial:https://www.youtube.com/watch?v=EYr_MKaL1Tg    Download: https://www.mediafire.com/file/23nzljx8w83dbl0/14Mil-raps-.pkg/file',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'desbloqueio' or msg['text'] == '/desbloqueio' or msg['text'] == f"/desbloqueio@{bot_username}" or msg['text'] == 'o meu ps3' or msg['text'] == 'Desbloqueio' or msg['text'] == 'desbloquear o ps3' or msg['text'] == 'desbloquear' or msg['text'] == 'desbloquear meu videogame' or msg['text'] == 'desbloquear o meu ps3' or msg['text'] == 'desbloquear o playstation' or msg['text'] == 'desbloquear o meu console' or msg['text'] == 'desbloqueei meu videogame' or msg['text'] == 'desbloqueei meu console':
            await bot.sendMessage(msg['chat']['id'], '`{} Tem certeza que ele foi feito de forma correta? O Joao PSX alem de fornecer arquivos bugados e ate mesmo mostrar bugs de mais ao vivo acaba nao fornecendo um material confiavel bem como ele nao tem total dominio doque faz como podemos ver nos videos a quantidade de erros ( ele podia editar os videos), enfim aconselho que veja, reveja e se possivel faça o exploit em cima deste tutorial:` https://www.youtube.com/watch?v=XUUieW4bv_Y'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        if 'mercado' in msg['text'] or msg['text'] == "/mercadopago" or msg['text'] == f"/mercadopago@{bot_username}" or msg['text'] == 'Mercado Pago' or msg['text'] == 'Mercado pago':
            await bot.sendMessage(msg['chat']['id'],  'Olá que bom que você quer doar, {} aqui esta o link de pagamento  ----->   https://www.mercadopago.com.br/checkout/v1/redirect?pref_id=354396246-315fce8c-d8f9-4aa0-8583-95d678936375'.format(msg['from']['first_name']),reply_to_message_id=msg['message_id'])
        if msg['text'] == 'tutorial segundo plano' or msg['text'] == "/segundoplano" or msg['text'] == f"/segundoplano@{bot_username}" or msg['text'] == 'download segundo plano' or msg['text'] == 'downloads em segundo plano' or msg['text'] == 'Tutorial' or msg['text'] == 'Download em segundo plano' or msg['text'] == 'Downloads em segundo plano'or msg['text'] == 'download em segundo plano':
            await bot.sendMessage(msg['chat']['id'], '{} O nosso admin @MsT3Dz  criou um tutorial exclusivo de como fazer os downloads na TCXS Project, bem como os downloads em segundo plano. Confira o tutorial completo: https://youtu.be/_21a5REKhBc'.format(msg['from']['first_name']),reply_to_message_id=msg['message_id'])
        if msg['text'] == 'tutorial' or msg['text'] == "/tutorial" or msg['text'] == f"/tutorial@{bot_username}" or msg['text'] == 'instalar' or msg['text'] == 'instalar a loja' or msg['text'] == 'instalar  loja' or msg['text'] == 'como instalar a loja' or msg['text'] == 'Como instalar a loja' or msg['text'] == 'Como instalo a loja'or msg['text'] == 'Instalação' or msg['text'] == 'Tutorial de instalação' or msg['text'] == 'Instalação da tcxs' or msg['text'] == 'instalar a tcxs' or msg['text'] == 'Instalação':
            await bot.sendMessage(msg['chat']['id'], '{} O nosso admin @MsT3Dz  criou um tutorial exclusivo de como instalar a loja: https://www.youtube.com/watch?v=aG1jLj8QuBY'.format(msg['from']['first_name']),reply_to_message_id=msg['message_id'])
        if msg['text'].lower() == 'dev' or msg['text'] == "/dev" or msg['text'] == f"/dev@{bot_username}" :
            await bot.sendMessage(msg['chat']['id'], '{} aqui esta a biblioteca dev, não vá se aventurar naquela loucura satanista anarquista lá.... https://tcxsproject.com.br/dev/'.format(msg['from']['first_name']),reply_to_message_id=msg['message_id'])
        if msg['text'].lower() == 'onion' or msg['text'] == "/onion" or msg['text'] == f"/onion@{bot_username}" :
            await bot.sendMessage(msg['chat']['id'], '{} este é nosso site na deep web, ele esta hospedado comigo por sinal, espero que isto nao de merda...\n http://5ct542hryncrbz7x3pveukcfzwf6qlhbwemsxnu4vtx2r7icjtimj6qd.onion'.format(msg['from']['first_name']),reply_to_message_id=msg['message_id'])
    if msg.get('text'):
        #SISTEMA DE CRIAÇÃO DE XML PARA LOJA
        if '/ps1' in msg['text']:
            try:
                nome_xml = msg['text'].split()[1]
                nome = msg['text'].split()[2]
                descricao = msg['text'].split()[3]
                link = msg['text'].split()[4]
                # string armazena o xml a ser gravado e printado
                arq = (f'''
    <XMBML version="1.0">
    <View id="ps1_items_link">
    <Attributes>
        <Table key="ps1_item_link">
        <Pair key="icon"><String>/dev_hdd0/game/TCXSPROJECT/USRDIR/arquivos/PS1/download.jpg</String></Pair>
        <Pair key="title"><String>TCXS - {nome} </String></Pair>
        <Pair key="info"><String>TCXS - {descricao} </String></Pair>
        <Pair key="module_name"><String>webrender_plugin</String></Pair>
        <Pair key="module_action"><String>{link}</String></Pair>
    </Table>
    </Attributes>
    <Items>
        <Query class="type:x-xmb/module-action" key="ps1_item_link" attr="ps1_item_link"/>
    </Items>
    </View>
    </XMBML>''')
                # bot envia mensagem

                await bot.sendMessage(msg['chat']['id'], (f'Seu xml de PlaysTation1 meu mestre ```{arq}```'),
                                      'markdown',
                                      reply_to_message_id=msg['message_id'])

                arq2 = (f'''Seu XML esta pronto, insira estas linhas no seu XML Pai:
        `Abaixo de <Attributes> cole:`
        ```
    <Table key="ps1_{nome_xml}">
        <Pair key="icon"><String>/dev_hdd0/game/TCXSPROJECT/USRDIR/arquivos/PS1/{nome_xml}.jpg</String></Pair>
        <Pair key="title"><String>TCXS - {nome} - TCXS</String></Pair>
        <Pair key="info"><String> {descricao}- TCXS</String></Pair>
    </Table>```
        `Abaixo de <Items> cole:`
        ```
    <Query class="type:x-xmb/folder-pixmap" key="ps1_{nome_xml}" attr="ps1_{nome_xml}" src="xmb://localhost/dev_hdd0/game/TCXSPROJECT/USRDIR/XMLS/PS1/{nome_xml}.xml#ps1_items_link" />```''')

                jon = open("arquivos/{}.xml".format(nome_xml), "w")
                for i in arq:
                    j = i.replace('', '')
                    jon.writelines(j)
                jon.close()

                await bot.sendMessage(msg['chat']['id'], arq2, 'markdown',
                                      reply_to_message_id=msg['message_id'])

                await bot.sendDocument(msg['chat']['id'],
                                       document=open("arquivos/{}.xml".format(nome_xml), 'rb'),
                                       reply_to_message_id=msg['message_id'])
                os.remove("arquivos/{}.xml".format(nome_xml))

            except:
                instrucao = '''Instruções: 
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

    '''
                await bot.sendMessage(msg['chat']['id'], instrucao, 'markdown',
                                      reply_to_message_id=msg['message_id'])
            return True

        if '/ps2' in msg['text']:
            try:
                nome_xml = msg['text'].split()[1]
                nome = msg['text'].split()[2]
                descricao = msg['text'].split()[3]
                link = msg['text'].split()[4]
                # string armazena o xml a ser gravado e printado
                arq = (f'''
    <XMBML version="1.0">
    <View id="ps2_items_link">
    <Attributes>
        <Table key="ps2_item_link">
        <Pair key="icon"><String>/dev_hdd0/game/TCXSPROJECT/USRDIR/arquivos/PS2/download.jpg</String></Pair>
        <Pair key="title"><String>TCXS - {nome} </String></Pair>
        <Pair key="info"><String>TCXS - {descricao} </String></Pair>
        <Pair key="module_name"><String>webrender_plugin</String></Pair>
        <Pair key="module_action"><String>{link}</String></Pair>
    </Table>
    </Attributes>
    <Items>
        <Query class="type:x-xmb/module-action" key="ps2_item_link" attr="ps2_item_link"/>
    </Items>
    </View>
    </XMBML>''')
                # bot envia mensagem

                await bot.sendMessage(msg['chat']['id'], (f'Seu xml de PlaysTation2 meu mestre ```{arq}```'),
                                      'markdown',
                                      reply_to_message_id=msg['message_id'])

                arq2 = (f'''Seu XML esta pronto, insira estas linhas no seu XML Pai:
                `Abaixo de <Attributes> cole:`
                ```
    <Table key="ps2_{nome_xml}">
        <Pair key="icon"><String>/dev_hdd0/game/TCXSPROJECT/USRDIR/arquivos/PS2/{nome_xml}.jpg</String></Pair>
        <Pair key="title"><String>TCXS - {nome} - TCXS</String></Pair>
        <Pair key="info"><String> {descricao}- TCXS</String></Pair>
    </Table>```
                `Abaixo de <Items> cole:`
                ```
    <Query class="type:x-xmb/folder-pixmap" key="ps2_{nome_xml}" attr="ps2_{nome_xml}" src="xmb://localhost/dev_hdd0/game/TCXSPROJECT/USRDIR/XMLS/PS2/{nome_xml}.xml#ps2_items_link" />```''')

                jon = open("arquivos/{}.xml".format(nome_xml), "w")
                for i in arq:
                    j = i.replace('', '')
                    jon.writelines(j)
                jon.close()

                await bot.sendMessage(msg['chat']['id'], arq2, 'markdown',
                                      reply_to_message_id=msg['message_id'])

                await bot.sendDocument(msg['chat']['id'],
                                       document=open("arquivos/{}.xml".format(nome_xml), 'rb'),
                                       reply_to_message_id=msg['message_id'])
                os.remove("arquivos/{}.xml".format(nome_xml))
            except:
                instrucao = '''Instruções: 
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

            '''
                await bot.sendMessage(msg['chat']['id'], instrucao, 'markdown',
                                      reply_to_message_id=msg['message_id'])
            return True

        if '/psp' in msg['text']:
            try:
                nome_xml = msg['text'].split()[1]
                nome = msg['text'].split()[2]
                descricao = msg['text'].split()[3]
                link = msg['text'].split()[4]
                # string armazena o xml a ser gravado e printado
                arq = (f'''
    <XMBML version="1.0">
    <View id="psp_items_link">
    <Attributes>
    <Table key="psp_item_link">
        <Pair key="icon"><String>/dev_hdd0/game/TCXSPROJECT/USRDIR/arquivos/PSP/download.jpg</String></Pair>
        <Pair key="title"><String>TCXS - {nome} </String></Pair>
        <Pair key="info"><String>TCXS - {descricao} </String></Pair>
        <Pair key="module_name"><String>webrender_plugin</String></Pair>
        <Pair key="module_action"><String>{link}</String></Pair>
    </Table>
    </Attributes>
    <Items>
        <Query class="type:x-xmb/module-action" key="psp_item_link" attr="psp_item_link"/>
    </Items>
    </View>
    </XMBML>''')
                # bot envia mensagem

                await bot.sendMessage(msg['chat']['id'], (f'Seu xml meu mestre ```{arq}```'), 'markdown',
                                      reply_to_message_id=msg['message_id'])

                arq2 = (f'''Seu XML esta pronto, insira estas linhas no seu XML Pai:
                `Abaixo de <Attributes> cole:`
                ```
    <Table key="psp_{nome_xml}">
        <Pair key="icon"><String>/dev_hdd0/game/TCXSPROJECT/USRDIR/arquivos/PSP/{nome_xml}.jpg</String></Pair>
        <Pair key="title"><String>TCXS - {nome} - TCXS</String></Pair>
        <Pair key="info"><String> {descricao}- TCXS</String></Pair>
    </Table>```
                `Abaixo de <Items> cole:`
                ```
    <Query class="type:x-xmb/folder-pixmap" key="psp_{nome_xml}" attr="psp_{nome_xml}" src="xmb://localhost/dev_hdd0/game/TCXSPROJECT/USRDIR/XMLS/PSP/{nome_xml}.xml#psp_items_link" />```''')

                jon = open("arquivos/{}.xml".format(nome_xml), "w")
                for i in arq:
                    j = i.replace('', '')
                    jon.writelines(j)
                    # print(i)
                jon.close()

                await bot.sendMessage(msg['chat']['id'], arq2, 'markdown',
                                      reply_to_message_id=msg['message_id'])

                await bot.sendDocument(msg['chat']['id'],
                                       document=open("arquivos/{}.xml".format(nome_xml), 'rb'),
                                       reply_to_message_id=msg['message_id'])
                os.remove("arquivos/{}.xml".format(nome_xml))
            except:
                instrucao = '''Instruções: 
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

            '''
                await bot.sendMessage(msg['chat']['id'], instrucao, 'markdown',
                                      reply_to_message_id=msg['message_id'])
            return True

        if '/ps3' in msg['text']:
            try:
                nome_xml = msg['text'].split()[1]
                nome = msg['text'].split()[2]
                descricao = msg['text'].split()[3]
                link1 = msg['text'].split()[4]
                link2 = msg['text'].split()[5]
                link3 = msg['text'].split()[6]

                # string armazena o xml a ser gravado e printado
                arq = (f'''<XMBML version="1.0">
    <View id="ps3_items_link">
    <Attributes>
         <Table key="ps3_item_0">
            <Pair key="icon"><String>/dev_hdd0/game/TCXSPROJECT/USRDIR/arquivos/DLCS/download.png</String></Pair>
            <Pair key="title"><String>TCXS Parte1 GAME- {nome}</String></Pair>
            <Pair key="info"><String>TCXS - {descricao}</String></Pair>
            <Pair key="module_name"><String>webrender_plugin</String></Pair>
            <Pair key="module_action"><String>{link1}</String></Pair>
        </Table>
        <Table key="ps3_item_1">
            <Pair key="icon"><String>/dev_hdd0/game/TCXSPROJECT/USRDIR/arquivos/DLCS/download.png</String></Pair>
            <Pair key="title"><String>TCXS Parte GAME+LIC- {nome}</String></Pair>
            <Pair key="info"><String>TCXS - {descricao}</String></Pair>
            <Pair key="module_name"><String>webrender_plugin</String></Pair>
            <Pair key="module_action"><String>{link2}</String></Pair>
        </Table>
        <Table key="ps3_item_2">
            <Pair key="icon"><String>/dev_hdd0/game/TCXSPROJECT/USRDIR/arquivos/DLCS/download.png</String></Pair>
            <Pair key="title"><String>TCXS Parte GAME+LIC- {nome}</String></Pair>
            <Pair key="info"><String>TCXS - {descricao}</String></Pair>
            <Pair key="module_name"><String>webrender_plugin</String></Pair>
            <Pair key="module_action"><String>{link3}</String></Pair>
        </Table>
    </Attributes>
    <Items>
        <Query class="type:x-xmb/module-action" key="ps3_item_0" attr="ps3_item_0"/>
        <Query class="type:x-xmb/module-action" key="ps3_item_1" attr="ps3_item_1"/>
        <Query class="type:x-xmb/module-action" key="ps3_item_2" attr="ps3_item_2"/>
    </Items>
    </View>
    </XMBML>''')
                # bot envia mensagem

                await bot.sendMessage(msg['chat']['id'], (f'Seu xml meu mestre ```{arq}```'), 'markdown',
                                      reply_to_message_id=msg['message_id'])

                arq2 = (f'''Seu XML esta pronto, insira estas linhas no seu XML Pai:
             `Abaixo de <Attributes> cole:`
             ```
    <Table key="ps3_{nome_xml}">
        <Pair key="icon"><String>/dev_hdd0/game/TCXSPROJECT/USRDIR/arquivos/PS3/{nome_xml}.jpg</String></Pair>
        <Pair key="title"><String>TCXS - {nome} - TCXS</String></Pair>
        <Pair key="info"><String>{descricao} - TCXS</String></Pair>
    </Table>```
             `Abaixo de <Items> cole:`
             ```
    <Query class="type:x-xmb/folder-pixmap" key="ps3_{nome_xml}" attr="ps3_{nome_xml}" src="xmb://localhost/dev_hdd0/game/TCXSPROJECT/USRDIR/XMLS/PS3/{nome_xml}.xml#ps3_items_link" />```''')

                jon = open("arquivos/{}.xml".format(nome_xml), "w")
                for i in arq:
                    j = i.replace('', '')
                    jon.writelines(j)
                    # print(i)
                jon.close()

                await bot.sendMessage(msg['chat']['id'], arq2, 'markdown',
                                      reply_to_message_id=msg['message_id'])

                await bot.sendDocument(msg['chat']['id'],
                                       document=open("arquivos/{}.xml".format(nome_xml), 'rb'),
                                       reply_to_message_id=msg['message_id'])
                os.remove("arquivos/{}.xml".format(nome_xml))
            except:
                instrucao = '''Instruções: 
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

         '''
                await bot.sendMessage(msg['chat']['id'], instrucao, 'markdown',
                                      reply_to_message_id=msg['message_id'])




























            return True

      

        


























        
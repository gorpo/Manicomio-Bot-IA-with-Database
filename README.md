[![Build](https://img.shields.io/badge/dev-gorpo-brightgreen.svg)]()
[![Stage](https://img.shields.io/badge/Release-Stable-brightgreen.svg)]()
[![Build](https://img.shields.io/badge/python-v3.7-blue.svg)]()
[![Build](https://img.shields.io/badge/windows-7%208%2010-blue.svg)]()
[![Build](https://img.shields.io/badge/Linux-Ubuntu%20Debian-orange.svg)]()
[![Build](https://img.shields.io/badge/arquiterura-64bits-blue.svg)]()
<h2 align="center">Manicomio Artificial Inteligence with Database GUI</h2>
<img src="https://raw.githubusercontent.com/gorpo/Bases-python/master/images/banner_mani_telegram.jpg" width="100%"></img><br>
Bot desenvolvido para monitorar e auxiliar nos grupos recebendo participantes e os cadastrando automaticamente em um banco de dados, no qual após determinada data os usuários são banidos, a data de permanencia padrão é de 35 dias. 
Confira os Plugins e Comandos da Inteligencia Artificial para compreender tudo que este bot pode fazer.<br>
ATENÇÃO: Alguns comandos listados devem ser escritos em minusculo e sem acentos conforme explicação de cada comando logo abaixo.

<h2>Instruções:</h2>
1. Edite no arquivo config se quer rodar o bot local ou no heroku, comente e descomente as linhas.<br>
2. Edite requeriments.txt caso tenha adicionado novas libs.<br>
3. Especifique a versão do python no arquivo runtime, também é necessário criar um arquivo "Procfile" e outro "Aptfile" na raiz do seu projeto, eles receberão um o comando dobot e outro comandos apt para instalar pacotes linux -  confira as versões de python disponiveis no heroku https://devcenter.heroku.com/articles/python-runtimes<br>
4. Crie um bot no Botfather e pegue o token do bot.<br>
5. Insira este bot em um canal e pegue o id do canal, ele servirá para os logs.<br>
6. Pegue sua id ela servirá para você ser adm master.<br>
7. Instale os requirements.txt para ter todas bibliotecas em ordem, caso falte alguma veja o arquivo de log's e instale manualmente.<br>
8. Para aumentar a memória virtual quando da erro de memória no torch no windows ir em: computador > propriedades> configurações avançadas so sistema > avançado > desempenho > configurações > avançado > memoria virtual e definir como 16.000 e 50.000. 
<p>Para rodar arquivos no Heroku é necessário criar um arquivo chamado "Procfile" e nele inserir o tipo de comando que será enviado para o dino do heroku<code>bot: python3 bot.py</code> Crie também um arquivo chamado runtime.txt e nele especifique sua versão do python a ser usada, tenha este arquivo na raiz do seu projeto
<code>python-3.7.7</code>, esta source ja conta com estes arquivos.</p>
<h2>Comandos para Desenvolvedor ou quem Hospeda o Bot:</h2>
<code>!apagar mensagens - apaga tudo IA e faz backup da Database.</code><br>
<code>!backup - Faz backup do bot e upload para o Dropbox.</code><br>
<code>!update - Atualiza o bot de acordo com codigo postado no Github.</code><br>
<code>!cmd - Executa um comando.</code><br>
<code>!chat - Obtem infos de um chat.</code><br>
<code>!del - Deleta a mensagem respondida.</code><br>
<code>!doc - Envia um documento do server.</code><br>
<code>!eval - Executa uma função Python.</code><br>
<code>!exec - Executa um código Python.</code><br>
<code>!leave - O bot sai do chat.</code><br>
<code>!plist - Lista os plugins ativos.</code><br>
<code>!promote - Promove alguém a admin.</code><br>
<code>!restart - Reinicia o bot.</code><br>
<code>!upgrade - Atualiza a base do bot com base na branch master do github</code><br>
<code>!upload - Envia um arquivo para o servidor.</code><br>
<code>!baixar - baixa um documento para o server</code><br>
<code>!dropbox - faz upload para o Dropbox</code><br>
<code>!link - gera um link direto do Telegram</code><br>
<code>  | - Define desligamento do bot, EX: 12|30</code><br>

<h2>Comandos para administradores:</h2>
<code>/start - inicia o bot</code><br>
<code>/welcome -boas vindas</code><br>
<code>/ban -bane usuario</code><br>
<code>/unban -desbane usuario</code><br>
<code>/kick -kicka usuario</code><br>
<code>/mute -muta usuario</code><br>
<code>/unmute -desmuta usuario</code><br>
<code>/unwarn -remove advertencias</code><br>
<code>/warn -adverte usuario</code><br>
<code>/pin -fixa posts</code><br>
<code>/unpin -desfixa posts</code><br>
<code>/title -muda titulo grupo</code><br>
<code>/defregras -define regras</code><br>
<code>/regras -ler regras</code><br>
<code>/config -privado</code><br>
<code>/admdebug -debug admin</code><br>
<code>/id -id usuario</code><br>
<code>/ip -dados ip</code><br>
<code>/jsondump -retorna dados</code><br> 
<code>/stickerid -id sticker</code><br>
<code>/getsticker -baixa sticker</code><br>
<code>/criar_sticker -cria pacote stickers</code><br>
<code>/kibar -copia sticker para o pacote de stickers</code><br>
<code>/mark -repete o texto markdown</code><br>
<code>/html -repete o texto HTML</code><br>
<code>/request -requisição site</code><br>
<code>/recog - reconhecimento com IA (nem sempre disponivel)</code><br>
<code>/notepad - cria um site com o texto enviado</code><br>
<code>/crawler - pega todos links dentro de um site</code><br>
<code>/corrigir - corrige palavras erradas</code><br>
<code>/link - pega link de um arquivo use como resposta</code><br><br>

<h2>Ferramentas Built-in:</h2>
<code>/tr      -traduz um texto</code><br>
<code>/yt      -pesquisa videos no YouTube</code><br>
<code>/r       -pesquisa um termo no redit</code><br>
<code>/clima   -exibe informacoes de clima</code><br>
<code>/coub    -pesquisa de pequenas animações</code><br>
<code>/dados   -jogo de dados</code><br>
<code>/gif     -gif do giphy</code><br>
<code>/git     -usuario do github</code><br>
<code>/id      -id do usuario</code><br>
<code>/ip      -informa dados de um ip</code><br>
<code>/jsondump -retorna dados formatados</code><br>
<code>/stickerid -pega id de um sticker</code><br>
<code>/getsticker -baixa um sticker</code><br>
<code>/pypi -pesquisa libs python</code><br>
<code>/rextester -interpretador de varias linguagens de programação</code><br>
<code>/mark -repete o texto informado usando Markdown</code><br>
<code>/html -repete o texto informado usando HTML</code><br>
<code>/request -faz uma requisicao a um site</code><br>
<code>/rt -repete concordando com o usuario na reposta  </code><br>
<code>/fala -Repete o texto que voce pedir para ele falar</code><br>
<code>/print -gera um print doque falou</code><br>
<code>/dogbin - envia seu material em texto para o dogbin</code><br>
<code>/hastebin - envia seu material em texto para o hastebin</code><br>
<code>/echo - Repete o texto informado</code><br>
<code>/shorten - Encurta uma URL.</code><br>
<code>/recog - reconhecimento com IA (nem sempre disponivel devido uso de GPU)</code><br>
<code>/notepad - cria um site com o texto enviado</code><br>
<code>/crawler - pega todos links dentro de um site</code><br>
<code>/corrigir - corrige palavras erradas</code><br>
<code>/token - Exibe informaces de um token de um outro bot</code><br>

<h2>Comandos para usuários:</h2>
<code>/start   -inicia o bot</code><br>
<code>/regras  -leia nossas regras</code><br>
<code>/admin   -admins do grupo</code><br>
<code>/freepkg -loja gratuita PS3 </code><br>
<code>/fix -fix han</code><br>
<code>/tutorial -como instalar a loja</code><br>
<code>/rap -licenças dos jogos  </code><br>
<code>/desbloqueio -desbloquear PS3</code><br>
<code>/segundoplano -download </code><br>
<code>/codigoerro  -codigos PSN/PS3</code><br>
<code>/listajogos -download direto</code><br>
<code>/doadores -instruções</code><br>
<code>/mercadopago -doar/loja </code><br>
<code>/tcxs -informações sobre </code><br>
<code>/tcxspyject -criar lojas</code><br>
<code>/ps1 -cria xml para loja</code><br>
<code>/ps2 -cria xml para loja </code><br>
<code>/psp -cria xml para loja</code><br>
<code>/ps3 -cria xml para loja</code><br>
<code>/proxy -velocidade no PS3</code><br>
<code>/tr      -traduz um texto</code><br>
<code>/yt      -pesquisa videos no YouTube</code><br>
<code>/r       -pesquisa um termo no redit</code><br>
<code>/clima   -exibe informacoes de clima</code><br>
<code>/coub    -pesquisa de pequenas animacoes</code><br>
<code>/dados   -jogo de dados</code><br>
<code>/gif     -gif do giphy</code><br>
<code>/git     -usuario do github</code><br>
<code>/id      -id do usuario</code><br>
<code>/ip      -informa dados de um ip</code><br>
<code>/jsondump -retorna dados formatados</code><br>
<code>/stickerid -pega id de um sticker</code><br>
<code>/getsticker -baixa um sticker</code><br>
<code>/pypi -pesquisa libs python</code><br>
<code>/rextester -interpretador de varias linguagens de programação</code><br>
<code>/mark -repete o texto informado usando Markdown</code><br>
<code>/html -repete o texto informado usando HTML</code><br>
<code>/request -faz uma requisicao a um site</code><br>
<code>/rt -repete concordando com o usuario na reposta</code><br>  
<code>/fala -Repete o texto que voce pedir para ele falar</code><br>
<code>/print -gera um print doque falou</code><br>
<code>/dogbin - envia seu material em texto para o dogbin</code><br>
<code>/hastebin - envia seu material em texto para o hastebin</code><br>
<code>/echo - Repete o texto informado.</code>    <br>
<code>/shorten - Encurta uma URL.</code><br>
<code>/recog - reconhecimento com IA (nem sempre disponivel)</code><br>
<code>/notepad - cria um site com o texto enviado</code><br>
<code>/crawler - pega todos links dentro de um site</code><br>
<code>/corrigir - corrige palavras erradas</code><br>
<code>/token - Exibe informaces de um token de bot.</code><br>
<br>
***SOBRE O ENVIO DE MENSAGENS DA IA***<br> 
```-->  Este bot envia mensagens baseado em dois tipos de inteligência, uma local e outra global, onde a local é tudo que aprendeu naquele grupo e ja a global é oque ele aprendeu por onde passou, veja exemplos:```<br>
`inteligencia local = irá falar  somente sobre oque aprendeu neste grupo, comando:`<br>
inteligencia local<br>
`inteligencia global = ira falar sobre tudo que aprendeu em todos os lugares que passou na internet`<br>
inteligencia global<br>
`fale sobre = ele fala sobre determinado assunto, exemplo:`<br>
fale sobre playstation<br>

***SOBRE A FREQUENCIA DE MENSAGENS*** <br>
```-->  Este bot envia mensagens automáticas de tudo que ele aprendeu em sua vida, desde que esteja gravado na database, mantenha um backup da database para não perder seu aprendizado, para controlar a quantidade de mensagens e o quanto o bot vai falar ele usa um sistema baseado em uma frequencia que deve ser setada entre 2 e 10, onde:```<br>
`frequencia 0 =` mudo<br>
`frequencia 2 =` fala pouco<br>
`frequencia 10 =` fala muito<br>

***SOBRE PROIBIR E PERMITIR PALAVRAS***<br>
```----  Este bot pode restringir/permitir palavras com os comandos:```<br>
`proibir uma palavra:` proibir corno<br>
`permitir uma palavra:` permtir corno<br>
`ver palavras proibidas:` proibidas<br>

‍***SOBRE O SISTEMA AUTOMATICO DE BANIMENTO DA IA*** <br>
```-->  Este bot envia conta com um sistema de banimento automático que pode ser ativado ou desativado no menu de configurações. Quando ativado, cada usuário que entrar terá a permanencia de 35 dias cadastrado de forma automática e caso estes dias não sejam renovados/adicionados o usuário tomará ban, este sistema é util para grupos pagos ou grupos que tem doadores ou mensalidades.```<br>
`ativar_banimento =` irá cadastar automaticamente e banir todos usuarios quando vencerem seu prazo, com 7 dias antes do vencimento a IA irá marcar o usuário no grupo avisando o mesmo.<br>
`desativar_banimento =` mesmo com sistema desativado ainda é possivel cadastrar usuários de forma manual e fazer a varredura para o banimento de forma manual, igualmente em um horario pre-determinado pelo desenvolvedor este bot irá aplicar o sistema de ban automatico então não precisa se preocupar em passar a verificação, basta apenas adicionar seus usuários manualmente ou inserir mais dias manualmente para eles conforme instruções no botao de Doadores.<br>
<br>

***RESTRINGIR | LIMPAR | RECADASTRAR USUÁRIOS COM PRAZO DE EXPIRAÇÃO*** <br>
```--> Este bot cadastra seus usuários automáticamente com o prazo de permanencia de 35 dias, porém se por ventura ele falhar ou mesmo um administrador quiser Cadastar Manualmente o Doador por qualquer eventualidade, seja para conferir um cadastro automatico feito pelo Bot ou para poder dar mais dias de permanência ao Doador!```<br>
***Cadastro automático:*** `Automaticamente ao entrar em um grupo o doador é cadastrado com o prazo de 30 dias de permanencia.`<br>
***Conferir Doadores Cadastrados:*** `Para conferir os cadastros existentes no sistema basta digitar o comando consulta e o arroba do usuário marcando o mesmo que também poderá conferir seu prazo,lembrando que faltando 7 dias para o prazo de banimento do grupo o usuário será notificado sobre para assim poder ou não realizar uma doação e manter sua permanência, use o comando conforme exemplo:`<br>
consulta @UserGamer<br>
***Descadastrar ou Deletar Doador:*** `Descadastrar ou deletar um Doador é necessário para que possa ser feita a inclusão de mais dias na sua conta, para isto basta usar o comando seguido do arroba do Doador conforme exemplo:`<br>
limpar @Mst3Dz<br>
***Cadastrar Manualmente um Doador:*** `Para cadastrar manualmente o doador é necessário pegar sua ID, para isto basta pegar qualquer mensagem deste doador e responder com o comando /id, após ter a ID do Doador tenha certeza que o mesmo não existe no Banco de Dados, para isto realize uma consulta e caso o Doador esteja cadastrado delete ele conforme instruções para deletar. Caso usuário não conste no Banco de Dados ou já tenha sido deletado execute o comando conforme exemplos:` ***restringir @usuario id_usuario quantidade_dias***<br>
`Exemplo na prática:` restringir @MsT3Dz 628238139 300000<br>
***Depois de Banido oque acontece:*** `Após o doador ser banido os administradores são notificados, o nome deste doador é limpo do banco de dados e da lista de restritos do grupo, caso ele faça uma nova doação basta adiciona-lo no grupo sem a necessidade de qualquer comando.`<br>

***SISTEMA DE PERGUNTAS E RESPOSTAS PARA ADMINS***<br>
```--> Este bot grava todas perguntas desde que contenham ??, avise seus usuários que quando quiserem cadastrar uma pergunta usem duas interrogações no final da frase e automáticamente sua pergunta será cadstrada e assim que um administrador ver pode responder ou cadastrar ela no robo ensinando a Inteligência Artificial.```<br>
`Cadastrar pergunta exemplo:` Como faço para ser tao esperto como o robo??<br> 
`Ver perguntas cadastradas apenas digite:` perguntas  <br>
`Limpar perguntas cadastradas ou já respondidas digite:` apagar perguntas<br>

***CADASTRO DE COMANDOS E REPOSTAS NA DATABASE***  
```Para cadastrar um comando no banco de dados use # sem aspas:```<br>
'#'Comando resposta <br>
```Para recadastrar um comando no banco de dados:```<br>
$comando resposta que o usuário vai receber<br>
```Para deletar um comando```<br>
%comando <br>

‍***SOBRE O SISTEMA DE RECONHECIMENTO DA IA***<br> 
```-->  Este bot envia conta com um sistema de  reconhecimento com Deep e Machine Learning utilizando as Lib's Tensorflow, Keras e OpenCV.```<br>
`Para usar este sistema basta responder qualquer imagem com o comando /recog e aguardar a IA enviar sua imagem com os objetos reconhecidos nela. Esta opção nem sempre esta disponível devido uso de GPU de quem hospeda a IA.(o codigo master não dispoe esta opção, veja outros branches pois existe ate uma versão co IA de DeepFake, basta incluir os codigos.`<br>


***CADASTRAR ARQUIVOS LOJAS DOADORES/FREE***<br> 
```--> Este bot cadastra as lojas/arquivos para doadores/colaboradores e usuarios na modalidade free separadamente assim você poderá negociar arquivos de forma descomplicada, cadastra também os fix pkg e os fix xml, para atualizar as lojas ou fix pkg e xml basta enviar elas no privado do bot, e ele cadastrará seus arquivos desde que estejam de acordo com as instruções abaixo. Pode ocorrer falhas na hora de cadastrar️, caso não tenha cadastrado envie novamente o arquivo, jamais envie mais de um arquivo por vez.```<br>
***Cadastrar Loja Free:*** `Cadastre a LOJA GRATUITA FREE PKG enviando ela no meu privado com nome terminando com free.pkg, antes disto você pode por qualquer coisa no nome no arquivo como exemplo:` ***TCXS_3.6_free.pkg***<br>
***Cadastrar Loja Doadores:*** `Cadastre a LOJA PARA DOADORES PKG enviando ela no meu privado com nome inicinando com TCXS, após este nome você pode escrever oque quiser no arquivo como  exemplo:` ***TCXS_Store3.9.pkg***<br>
***Cadastrar Fix HAN PKG:*** `Cadastre o FIX HAN PKG enviando ela no meu privado exatamente conforme exemplo:` ***FIX_HAN.pkg***<br>
***Cadastrar Fix HEN PKG:*** `Cadastre o FIX HEN PKG enviando ela no meu privado exatamente conforme exemplo:` ***FIX_HEN.pkg***<br>
***Cadastrar Fix CFW XML:*** `Cadastre o FIX CFW XML enviando ela no meu privado exatamente conforme exemplo:` ***category_network_tool2.xml***<br>
***Cadastrar Fix HEN XML:*** `Cadastre o FIX HEN XML enviando ela no meu privado exatamente conforme exemplo:` ***category_network.xml***<br>


<img src="https://raw.githubusercontent.com/gorpo/Bases-python/master/images/banner_manicom_terminal.jpg" width="100%"></img><br>
<h2>Caso queira automatizar seu upload para o heroku use o arquivo bat da source ou basta criar um arquivo .bat com o código abaixo:</h2>
<code>call heroku login</code><br>
<code>call heroku create --region us manicomio </code><br>
<code>call git init</code><br>
<code>call git add *</code><br>
<code>call git commit -m "Primeiro commit!"</code><br>
<code>call heroku git:remote -a manicomio</code><br>
<code>call git push heroku master</code><br> 
<code>call heroku buildpacks:add --index 1 heroku-community/apt</code>br
<code>call heroku ps:scale bot=1 </code><br>
<code>call heroku logs --tail</code><br>

<h2>Deploy no Heroku Via linha de comando - CLI</h2><br>
<code>cd manicomio_bot_heroku</code><br>
<code>heroku login</code><br>
<code>heroku create --region us manicomio</code> seta us como regiao e nome_do_app defina o nome do  app no heroku<br>
<code>git init</code><br>
<code>git add *</code><br>
<code>git commit -m "Primeiro commit!"</code><br>
<code>heroku git:remote -a manicomio</code><br>
<code>git push heroku master</code>              deploy do programa no heroku<br>
<code>heroku config:set TELEGRAM_TOKEN=1186597860:AAHZTQT--xYhNHhkO8SbxlSxrdwVnkvi38s</code> seta as config vars, insira seu token<br>
<code>heroku config:set LOGS=-1001215401730</code> seta a id do canal de logs que o bot ja deve estar e ter admin<br>
<code>heroku config:set SUDOERS=522510051</code> seta o sudo ou seja adm master do bot<br>
<code>heroku ps:scale bot=1</code> start bot dyno - inicia seu bot<br>
<code>call heroku buildpacks:add --index 1 heroku-community/apt</code> instala pacotes apt no linux do heroku
<code>heroku logs --tail</code> tiva os logs no terminal ou cmd<br>
<code>heroku ps:stop bot</code> para o bot dyno  - para seu bot
<code>heroku apps:destroy -a manicomio</code> - deleta a aplicação no heroku

<h2>Deploying via Heroku Dashboard</h2><br>
1. Fork este repositorio.<br>
2. Vá para https://dashboard.heroku.com, faça login, Pressione _Novo_ e escolha _Criar novo aplicativo._<br>
3. Preencha um _App Name_ e escolha _Runtime Region._<br>
4. Conecte seu repositório GitHub na página _Deploy_.<br>
5. Configuração Automatics deploys(opcional)<br>
6. _Implante uma filial do GitHub._<br>
7. Em seguida, vá para uma página _Settings_, clique em _Reveal Config Vars_ e adicione seus próprios, por exemplo:<br>
7.1. TELEGRAM_TOKEN  =  token telegram <br>
7.2. LOGS= id do canal do bot<br>
7.3. SUDOERS  = sua id<br>
8.   Vá para a página _Resources_.<br>
8.1. Instale o _Heroku Redis_ add-on(opcional)<br>
8.2. Pressione um botão pequeno da caneta, mova o controle deslizante e clique em _Confirmar_, que iniciará o bot dyno.<br>
8.3. Simplesmente mova o controle deslizante para trás se precisar parar o bot dyno, lembre-se de clicar em _Confirmar_.<br>
8.4. Se, por algum motivo, não estiver funcionando, verifique os logs.<br>

<h2>links uteis</h2><br>
- https://devcenter.heroku.com/articles/dynos<br>
- https://devcenter.heroku.com/articles/config-vars<br>
- https://devcenter.heroku.com/articles/heroku-redis<br>
- https://devcenter.heroku.com/articles/error-codes<br>



<h1> Comandos auxiliares Github - CLI </h1><br>
<b>email:</b><br>
	<code>git config --global user.email "gorpoorko@protonmail.com"</code><br>
<b>username:</b><br>
	<code>git config --global user.name "gorpoorko"</code><br>
	
<b>Adicionar um arquivo em específico</b><br>
	<code>git add meu_arquivo.txt</code><br>
<b>Adicionar um diretório em específico</b><br>
	<code>git add meu_diretorio</code><br>
<b>Adicionar todos os arquivos/diretórios</b><br>
	<code>git add .	</code><br>
<b>Adicionar um arquivo do gitignore -  git add -f arquivo_no_gitignore.txt</b><br>

<b>Comitar um arquivo</b><br>
	<code>git commit meu_arquivo.txt</code><br>
<b>Comitar vários arquivos</b><br>
	<code>git commit meu_arquivo.txt meu_outro_arquivo.txt</code><br>
<b>Comitar informando mensagem</b><br>
	<code>git commit meuarquivo.txt -m "minha mensagem de commit"</code><br>

<b>Remover arquivo</b><br>
	<code>git rm meu_arquivo.txt</code><br>
<b>Remover diretório</b><br>
	<code>git rm -r diretorio</code><br>

<b>O primeiro push de um repositório deve conter o nome do repositório remoto e o branch.</b><br>
	<code>git push -u origin master</code><br>
<b>Os demais pushes não precisam dessa informação</b><br>
	<code>git push</code><br>
<b>Atualizar repositório local de acordo com o repositório remoto</b><br>
<b>Atualizar os arquivos no branch atual</b><br>
	<code>git pull</code><br>
<b>Buscar as alterações, mas não aplica-las no branch atual</b><br>
	<code>git fetch</code><br>

<b>Criando um novo branch</b><br>
	<code>git branch bug-123</code><br>
	<code>git branch gh-pages    - para sites</code><br>
<b>Trocando para um branch existente</b><br>
	<code>git checkout bug-123</code><br>
<b>Neste caso, o ponteiro principal HEAD esta apontando para o branch chamado bug-123.</b><br>
<b>Criar um novo branch e trocar</b><br>
	<code>git checkout -b bug-456</code><br>
<b>Voltar para o branch principal (master)</b><br>
	<code>git checkout master</code><br>

<b>Upando algo para um branch ja existente</b><br>
	<code>git remote add origin <"link do git seja master ou branch"></code><br>
<b>Adicione os arquivos</b><br>
	<code>git add . ou nome do arquivo ou pasta</code><br>
<b>Comente oque foi adicionado</b><br>
	<code>git commit -m "comentario"</code><br>
<b>Fazer as atualizações no repositorio online</b><br>
	<code>git fetch</code><br>
<b>Adicionando a historia do repositorio online</b><br>
	<code>git pull origin master --allow-unrelated-histories</code><br>

<b>Resolver merge entre os branches</b><br>
	<code>git merge bug-123</code><br>
<b>Para realizar o merge, é necessário estar no branch que deverá receber as alterações. O merge pode automático ou manual. O merge automático será feito em arquivos textos que não sofreram alterações nas mesmas linhas, já o merge manual será feito em arquivos textos que sofreram alterações nas mesmas linhas. A mensagem indicando um merge manual será:<br>
Automerging meu_arquivo.txt<br>
CONFLICT (content): Merge conflict in meu_arquivo.txt<br>
Automatic merge failed; fix conflicts and then commit the result.</b><br>
<b>Apagando um branch</b><br>
	<code>git branch -d bug-123</code><br>
<b>Listar branches</b><br>
	<code>git branch</code><br>
<b>Listar branches com informações dos últimos commits</b><br>
	<code>git branch -v</code><br>
<b>Listar branches que já foram fundidos (merged) com o master</b><br>
	<code>git branch --merged</code><br>
<b>Listar branches que não foram fundidos (merged) com o master</b><br>
	<code>git branch --no-merged</code><br>

<b>Criando um branch remoto com o mesmo nome</b><br>
	<code>git push origin bug-123</code><br>
<b>Criando um branch remoto com nome diferente</b><br>
	<code>git push origin bug-123:new-branch</code><br>
<b>Baixar um branch remoto para edição</b><br>
	<code>git checkout -b bug-123 origin/bug-123</code><br>
<b>Apagar branch remoto</b><br>
	<code>git push origin:bug-123</code><br>
<b>Fazendo o rebase entre um o branch bug-123 e o master.</b><br>
	<code>git checkout experiment</code><br>
	<code>git rebase master</code><br>

Nosso site: <a href="https://tcxsproject.com.br">Manicomio TCXS Project</a> | Developers: <a href="https://github.com/gorpo">GorpoOrko</a> | Partnerships:» <a href="https://t.me/tcxsproject2">telegram</a> | ©2020 | <a href="https://t.me/tcxsproject2">TCXS Project Hacker Team™</a><br>
<img src="https://raw.githubusercontent.com/gorpo/Manicomio-Boot-Theme/master/manicomio/boot.png" width="50%"></img>

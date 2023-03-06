## Desafio Tech Biopark 2023

### Requisitos

- O sistema deve permitir cadastrar edifícios e apartamentos
- O sistema deve permitir visualizar a disponibilidade dos apartamentos
- O sistema deve permitir alugar um apartamento para um locatário
- O sistema deve permitir visualizar o locatário do apartamento

### Premissas

- Cada apartamento do ecossistema pertence a um edifício
- Cada apartamento alugado deve ter um locatário
- Cada apartamento alugado deve ter o valor de aluguel mensal cadastrado
- Considere o Biopark como locador dos apartamentos

<hr>

## Descrição

Baseado nas premissas e requisitos do projeto, foi solicitado a criação de um sistema para apresentação de imóveis 
disponíveis para locação, onde deve ter os dados deles, porém também deve ter os dados de seus clientes, e quando 
locatários, um vínculo entre eles.
Levando em consideração a todas essas informações, optei por desenvolver um sistema onde  todos os dados sempre será 
registrado e acompanhado por pessoas autorizadas, com exceção da página de imóveis disponíveis, pois levando em conta os 
meios utilizados da maior parte das imobiliárias no mercado, para que haja uma contratação, seria necessário a troca de 
documentos e autenticações por meios legais, sendo assim um cadastro direto pelo usuário talvez não seja a melhor pratica, 
porque a aprovação pode ser complicada, e caso não aprovada, teria dados inúteis no banco, sem contar todos os dados de 
pessoas que podem desistir durante o processo.

<hr>

### Orientações para teste de Projeto

- Qualquer duvida pode entrar em contato, estou a disposição. 
- Na pasta imagem fora do projeto, possui imagens do projeto final carregado para terem noções do resultado final.

<hr>

### Observação
Para facilitar os teste, e verificações do funcionamento do sistema, o cadastrar do sistema está como super usuário, porém 
se fosse utilizar o mesmo, seria recomendado modificar o cadastro para usuário comum, e posteriormente ser autorizado 
os acessos por um administrador.

<hr>

### Tecnologias

- Linguagem utilizada: Backend (Python e Django), Frontend (HTML, CSS e Bootstrap)
- Banco utilizado: PostgreSQL
- IDE utilizada: Pycharm

<hr>

### Foi utilizado sistema operacional windows

- Para evitar imprevistos, recomendo usar o mesmo sistema.

<hr>

### Instalar Pycharm
- Deve ser usado a versão profissional
- Pode ser usada por 30 dias gratuito, ou 1 ano como estudante.
- Somente acessar o site, baixar, instalar e realizar o cadastro.
- Cadastro pode ser realizado após instalação no primeiro acesso.

link para download pycharm:

https://www.jetbrains.com/pt-br/pycharm/download/#section=windows

### Após instalação pycharm - Clonar projeto github

- Abrir o pycharm
- No menu superior localize o git
- Clique no mesmo e depois em clone ...
- Adicione a url do clone do plojeto do github
- https://github.com/romuloptmota/sistema-imoveis.git
- Em diretorio selecione onde quer salvar
- Na tela que aparecer clique em Trust Project
- Em seguida ira perguntar como abrir, e pode ser new windows
- Nisso ira perguntar sobre criar ambiente virtual, clique em ok
- Irá começar a instalar alguns pacotes, e é só aguardar

<hr>

### Configurar banco de dados
- Abra seu gerenciado de banco do postgre
- Crie um banco limpo como desejar, e anote o nome do banco criado. 
- Tambem precisaremos do usuario, senha, host e porta das configurações de seu postgre.


### Configurar banco no pycharm
- Na aplicação Biopark do lado esquerdo acesse settings
- Localize Database e substitua os dados do mesmo pelos seus que foi anotado anteriormente.
- NAME, USER, PASSWORD, HOST e PORT 
- obs. Não altere 'ENGINE': 'django.db.backends.postgresql', pois ela que define as configurações do banco que estamos usando, no caso o postgre.

### Subir o banco da aplicação
- Mais antes tesmos que limpar a as migrations anteriores
- acesse pasta migrations na aplicação core do lado esquerdo,  e se tiver arquivos, delete todos arquivos exceto init.py

- Agora abra o terminal do pycharm que fica na parte inferior, somente clicar no terminal
- Em seguida coloque os seguintes comandos um por vez na mesma ordem
- python manage.py makemigrations
- python manage.py migrate

<hr>

### Testar aplicação 
- no terminal do pycharm coloque o comando
- python manage.py runserver
- Ira aparecer o link http://127.0.0.1:8000/
- clique nele e aplicação já esta funcionado, porem sem dados
- Mais antes temos que criar um usuario administrador para ter acesso a area administrativa
- Temos duas maneira abaixo

<hr>

### Criando usuario administrador

- 1º Com sistema aberto clique em criar conta, pois deixei como administrador para facilitar
- Adicione um usuario, senha, confirme a senha, email e clique em cadastrar
- Aparecera a mensagem cadastrado com sucesso
- 2º o segundo modo é pelo terminal do pycharm
- Digite o comando
- python manage.py createsuperuser
- mesmo modo, adicione os seus dados solicitados um por vez ate finalizar
- Pronto, agora temos usuario administrador e podemos carregar o sistema

obs. Para fazer o sistema parar de rodar, selecionado o terminal, pressione Ctrl + C, e para rodar novamente, mesmo comando anterior no terminal python manage.py runserver

<hr>

### Acessando area administrativa do sistema
- Tambem podemos acessar de duas maneiras 
- Com o sitema rodando clique em login e acesse com os dados criado
- ou no navegado adicione /admin ex. http://127.0.0.1:8000/admin e informe os dados criados
- Agora estamos na area administrativa onde podemos carregar o site

### Carregando o site
- Após acessar estara visualizando alguns links que vamos usar, o Edificios, Apartamentos e Clientes
- Para ver o que já foi cadastrado é só clicar no link
- E para cadastrar é somente clicar em adicionar, ou caso queira modificar
- No caso no momento esta vazio, então vamos iniciar os cadastros

### Informações area administrativa
- Antes de cadastrar os apartamentos, deve cadastrar os edificios
- Todos clientes que deseja vincular a imoveis alocados deve cadastrar em clientes
- Nisso cadastre os clientes
- Quando for adicionar os apartamentos, selecione um dos edificios que o mesmo pertence
- Preencha os dados , e adicione as cinco imagens do mesmo
- Agora o checkbox disponivel irá desmarcar sempre que for vincular um cliente
- Abaixo no disponivel que ira selecionar o nome do cliente
- Importante, esse checkbox que irar determinar os imoveis que aparecera disponivel no site, ou na area restrita locatarios
- Não deixe de desmarcar se vincular ao um cliente/locatario

obs. para ver como esta ficando no site, somente clicar na parte superior esquerda ver o site, que volta para o mesmo, porem agora com opções novas no menu

- Clientes para visualizar todos Locatarios e seus dados, essa tela ficará somente visivel para pessoas logadas no sistema
- E o botão cadastrar, para voltar para a area adiministrativa
- Quando quiser terminar pode clicar em logou, ou em encerrar sessão na area administrativa.

#### Espero ter passado todas as infomrações necessario, mais de qualquer forma, estou a disposição para qualquer duvida.

<hr>
<hr>

### Instalar bibliotecas:

#### Somente se paresentar algum erro em alguma biblioteca usada, pode tentar reinstalar

- obs. caso apareceça a mensagem ao tenta instalr as bibliotecas abaico
- To update, run: python.exe -m pip install --upgrade pip
- Use esse comando antes de instalar a biblioteca
- python.exe -m pip install --upgrade pip

- No terminal do pycharm
- pip install django
- pip install psycopg2-binary
- pip install dj-static
- pip install django-stdimage
- pip install django-bootstrap4

Somente informando para que serve cada uma:

- django: desenvolvimento web
- psycopg2-binary: para usar o postgre
- dj-static: para manipular arquivos estaticos
- django-stdimage: para manipular imagens





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

### Após instalação pycharm

- Abrir o projeto
- Podemos realizar de duas maneria, escolha a que preferir.

#### 1º Após abrir pycharm
- Clique na guia git no topo > Clone ... > adicione url do clone git > clique no botao clone

#### 2º Após abrir pycharm

- Baixar o clone do projeto direto do github > clicar em file > Open > selecionar onde projeto foi baixado

<hr>

### Instalar bibliotecas:

Abra o terminal na parte inferior do pycharm, e adicione os seguintes comandos

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

<hr>

### Configurar banco de dados
- Abra seu gerenciado de banco do postgre
- Crie um banco limpo como deseja, e anote o nome do banco criado. 
- Tambem precisaremos do usuario, senha, host e porta das configurações de seu postgre.

### Configurar banco no pycharm
- Na aplicação Biopark acesse settings
- Localize Database e substitua os dados do mesmo pelos seus que foi anotado anteriormente.
- obs. Não altere 'ENGINE': 'django.db.backends.postgresql',



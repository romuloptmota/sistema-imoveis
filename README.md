### Linguagem utilizada: Python

### Foi utilizado sistema windows

- Para evitar imprevistos, recomendo usar o mesmo sistema.

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
- CLique na guia git no topo > Clone ... > adicione url do clone git > clique no botao clone

#### 2º Após abrir pycharm

- Baixar o clone do projeto direto do github > clicar em file > Open > selecionar onde pjojeto foi baixado


### Instalar bibliotecas:

Abra o terminal na parte inferior do pycharm, e adicione os seguintes comandos

- pip install django
- pip install psycopg2-binary
- pip install dj-static
- pip install django-stdimage

Somente informando para que serve cada uma:

- django: desenvolvimento web
- psycopg2-binary: para usar o postgre
- dj-static: para manipular arquivos staticos
- django-stdimage: para manipular imagens

### Configurar banco de dados
- Abra seu gerenciado de banco do postgre
- Crie um banco limpo como deseja, e anote o nome do banco criado. 
- Tambem precisaremos do seu usuario, senha, host e porta das consfigurações de seu postgre.

### Configurar banco no pycharm
- Na aplicação Biopark acesse settings
- Localize Database e substitua os dados do mesmo pelos seus
- obs. Não altere 'ENGINE': 'django.db.backends.postgresql',



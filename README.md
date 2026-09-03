CRUD - Sistema de Cadastro

Aplicação web desenvolvida com Python e Django para gerenciamento de cadastros, autenticação de usuários e operações CRUD.






Sobre o projeto

O CRUD - Sistema de Cadastro é um projeto desenvolvido para colocar em prática conceitos fundamentais do desenvolvimento web utilizando o framework Django.

A aplicação conta com uma estrutura modular, incluindo sistema de autenticação, cadastro de informações e painel de gerenciamento.

O projeto foi desenvolvido com foco em aprendizado e aplicação prática dos conceitos de desenvolvimento web com Python.

Funcionalidades
Sistema de autenticação de usuários
Cadastro de informações
Visualização de registros
Edição de registros
Exclusão de registros
Painel de gerenciamento
Integração com banco de dados através do Django ORM
Sistema de migrations
Interface baseada em templates Django
Área administrativa do Django
Tecnologias
Tecnologia	Utilização
Python	Linguagem de programação
Django 6.1	Framework web
Django ORM	Comunicação com o banco de dados
HTML	Estrutura das páginas
Django Templates	Renderização das páginas
Git	Controle de versão
GitHub	Hospedagem do código
Estrutura do projeto
crud_aula_12.08/
│
├── app/
│
├── cadastro/
│   ├── migrations/
│   ├── templates/
│   │   └── cadastro/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── login/
│   ├── migrations/
│   ├── templates/
│   │   └── login/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── painel/
│
├── sistema/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .gitignore
├── manage.py
├── notas.txt
└── requirements.txt

Requisitos

Antes de iniciar o projeto, certifique-se de possuir instalado:

Python 3.x
pip
Git
Instalação
1. Clone o repositório
git clone https://github.com/gustayath/crud_aula_12.08.git

2. Entre no diretório
cd crud_aula_12.08

3. Crie um ambiente virtual
Windows
python -m venv venv


Ative o ambiente:

venv\Scripts\activate

Linux / macOS
python3 -m venv venv


Ative o ambiente:

source venv/bin/activate

4. Instale as dependências
pip install -r requirements.txt

5. Execute as migrations
python manage.py migrate

6. Inicie o servidor
python manage.py runserver


A aplicação estará disponível em:

http://127.0.0.1:8000/

Criando um superusuário

Para acessar o painel administrativo do Django, execute:

python manage.py createsuperuser


Informe o nome de usuário, e-mail e senha solicitados pelo Django.

Após criar o usuário, acesse:

http://127.0.0.1:8000/admin/

Comandos úteis
Iniciar o servidor
python manage.py runserver

Criar migrations
python manage.py makemigrations

Aplicar migrations
python manage.py migrate

Criar superusuário
python manage.py createsuperuser

Executar os testes
python manage.py test

Django Apps

O projeto está dividido em diferentes aplicações para facilitar a organização do código.

cadastro

Responsável pelas funcionalidades relacionadas ao cadastro e gerenciamento dos registros.

login

Responsável pelo sistema de autenticação e acesso dos usuários.

painel

Responsável pela área principal do sistema após o usuário realizar o login.

sistema

Contém as configurações principais do projeto Django, incluindo:

Configurações do projeto
URLs principais
WSGI
ASGI
Banco de dados

O projeto utiliza o Django ORM para comunicação com o banco de dados.

As alterações na estrutura dos modelos devem ser aplicadas utilizando o sistema de migrations do Django:

python manage.py makemigrations
python manage.py migrate

Objetivo acadêmico

Este projeto tem como objetivo praticar os principais conceitos necessários para o desenvolvimento de aplicações web utilizando Django.

Entre os conceitos trabalhados estão:

Estrutura de projetos Django
Criação e configuração de aplicações
Models
Views
Templates
URLs
Django ORM
Migrations
Autenticação
CRUD
Organização de projetos
Controle de versão com Git
Aprendizados

Durante o desenvolvimento do projeto, foram aplicados conceitos relacionados à construção de uma aplicação web completa utilizando Python e Django.

O projeto também proporciona prática com a organização de aplicações Django, integração entre diferentes componentes do framework e utilização do GitHub para versionamento e compartilhamento do código.

Autor

Gustayath

GitHub:
https://github.com/gustayath

Repositório

O código-fonte deste projeto está disponível no GitHub:

https://github.com/gustayath/crud_aula_12.08

Licença

Este projeto foi desenvolvido para fins educacionais e de aprendizado.

CRUD - Sistema de Cadastro

Projeto desenvolvido em Django com o objetivo de praticar a construção de uma aplicação web com operações de CRUD (Create, Read, Update e Delete), sistema de login e painel de gerenciamento.

Sobre o projeto

Este projeto foi desenvolvido como atividade prática para aprendizado do framework Django e dos principais conceitos de desenvolvimento web com Python.

A aplicação possui uma estrutura organizada em diferentes módulos, incluindo:

Login — gerenciamento da autenticação dos usuários.
Cadastro — gerenciamento dos registros da aplicação.
Painel — área principal do sistema após o acesso.
Sistema — configurações e URLs principais do projeto.

O projeto utiliza o sistema de templates do Django e possui estrutura para migrations, models, views e testes.

Tecnologias utilizadas
Python
Django 6.1
Django ORM
HTML / Templates Django
Git e GitHub
Dependências

As principais dependências estão definidas no arquivo requirements.txt:

asgiref==3.12.1
Django==6.1
sqlparse==0.5.5
tzdata==2026.3

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

Instalação
1. Clone o repositório
git clone https://github.com/gustayath/crud_aula_12.08.git

2. Acesse a pasta do projeto
cd crud_aula_12.08

3. Crie um ambiente virtual

No Windows:

python -m venv venv


Ative o ambiente virtual:

venv\Scripts\activate


No Linux/macOS:

python3 -m venv venv
source venv/bin/activate

4. Instale as dependências
pip install -r requirements.txt

5. Execute as migrations
python manage.py migrate

6. Inicie o servidor
python manage.py runserver


Depois, acesse no navegador:

http://127.0.0.1:8000/

Criando um superusuário

Para acessar o painel administrativo do Django, crie um superusuário utilizando:

python manage.py createsuperuser


Depois, siga as instruções exibidas no terminal.

O painel administrativo poderá ser acessado em:

http://127.0.0.1:8000/admin/

Funcionalidades
 Estrutura baseada em Django
 Sistema de login
 Área de cadastro
 Painel do sistema
 Models utilizando Django ORM
 Migrations
 Templates HTML
 Integração com Git/GitHub
 Operações CRUD
Objetivo

O principal objetivo deste projeto é colocar em prática conceitos fundamentais do desenvolvimento de aplicações web utilizando Python e Django, especialmente:

Arquitetura de projetos Django;
Criação de aplicações;
Models e banco de dados;
Views;
Templates;
URLs;
Autenticação;
Operações CRUD;
Migrations;
Organização de código.
Aprendizados

Durante o desenvolvimento, foram trabalhados conceitos importantes para a criação de sistemas web, desde a configuração inicial de um projeto Django até a criação de páginas, modelos, views e funcionalidades de autenticação.

Autor

Gustayath

GitHub: https://github.com/gustayath

Licença

Este projeto foi desenvolvido para fins educacionais e de aprendizado.

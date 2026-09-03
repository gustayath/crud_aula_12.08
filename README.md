> Aplicação web desenvolvida com Python e Django para gerenciamento de cadastros, autenticação de usuários e operações CRUD completas.

---

## 📌 Sobre o Projeto

O **CRUD - Sistema de Cadastro** é um projeto desenvolvido para colocar em prática conceitos fundamentais do desenvolvimento web utilizando o framework **Django**.

A aplicação conta com uma estrutura modular, incluindo sistema de autenticação de usuários, cadastro de informações, painel de gerenciamento e persistência de dados. O projeto foi desenvolvido com foco em aprendizado e aplicação prática dos conceitos de desenvolvimento web com Python.

---

## ✨ Funcionalidades

- 🔐 Sistema de autenticação de usuários (Login/Logout)
- 📝 Cadastro, visualização, edição e exclusão de registros (CRUD)
- 📊 Painel de gerenciamento exclusivo
- 🗄️ Integração com banco de dados através do **Django ORM**
- 🔄 Sistema de *migrations* para controle de esquema do banco de dados
- 🎨 Interface baseada em **Django Templates**
- 🛡️ Área administrativa nativa do Django (`/admin`)

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Utilização |
| :--- | :--- |
| ![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white) | Linguagem de programação |
| ![Django](https://img.shields.io/badge/Django-6.1-green?style=flat-square&logo=django&logoColor=white) | Framework web |
| **Django ORM** | Comunicação com o banco de dados |
| **HTML / CSS** | Estruturação e estilização das páginas |
| **Django Templates** | Renderização dinâmica das páginas |
| ![Git](https://img.shields.io/badge/Git-Controle_de_Versão-orange?style=flat-square&logo=git&logoColor=white) | Controle de versão |
| ![GitHub](https://img.shields.io/badge/GitHub-Hospedagem-black?style=flat-square&logo=github&logoColor=white) | Hospedagem do código-fonte |

---

## 📁 Estrutura do Projeto

```text
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

```

---

## ⚙️ Pré-requisitos

Antes de iniciar o projeto, certifique-se de possuir instalado em sua máquina:

* [Python 3.14](https://www.python.org/)
* Gerenciador de pacotes `pip`
* [Git](https://git-scm.com/)

---

## 📥 Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto localmente:

### 1. Clone o repositório

```bash
git clone [https://github.com/gustayath/crud_aula_12.08.git](https://github.com/gustayath/crud_aula_12.08.git)

```

### 2. Entre no diretório do projeto

```bash
cd crud_aula_12.08

```

### 3. Crie e ative um ambiente virtual

* **Windows:**
```bash
python -m venv venv
venv\\Scripts\\activate

```


* **Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate

```



### 4. Instale as dependências

```bash
pip install -r requirements.txt

```

### 5. Execute as migrations do banco de dados

```bash
python manage.py migrate

```

### 6. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver

```

A aplicação estará disponível no navegador em:
🔗 `http://127.0.0.1:8000/`

---

## 👑 Criando um Superusuário (Painel Admin)

Para acessar a área administrativa do Django, crie um superusuário executando o comando:

```bash
python manage.py createsuperuser

```

Informe o nome de usuário, e-mail e senha solicitados. Após a criação, acesse o painel em:
🔗 `http://127.0.0.1:8000/admin/`

---

## ⌨️ Comandos Úteis

| Comando | Descrição |
| --- | --- |
| `python manage.py runserver` | Inicia o servidor de desenvolvimento local |
| `python manage.py makemigrations` | Cria novos arquivos de migração baseados nos modelos alterados |
| `python manage.py migrate` | Aplica as migrações no banco de dados |
| `python manage.py createsuperuser` | Cria um usuário administrador do sistema |
| `python manage.py test` | Execula os testes automatizados do projeto |

---

## 🧩 Django Apps

O projeto está modularizado nas seguintes aplicações:

* **`cadastro`**: Responsável pelas regras de negócio, formulários, views e templates relacionados ao cadastro e gerenciamento dos registros.
* **`login`**: Responsável pelo sistema de autenticação, controle de acesso e sessão dos usuários.
* **`painel`**: Responsável pela área principal do sistema exibida após o login bem-sucedido.
* **`sistema`**: Contém as configurações globais do projeto Django (`settings.py`, roteamento de URLs principal, WSGI e ASGI).

---

## 🗄️ Banco de Dados e ORM

O projeto utiliza o **Django ORM** para comunicação nativa com o banco de dados de forma orientada a objetos. Qualquer modificação estrutural nos dados deve ser refletida utilizando o ciclo padrão de migrações:

```bash
python manage.py makemigrations
python manage.py migrate

```

---

## 🎯 Objetivo Acadêmico

Este projeto tem como objetivo principal praticar e consolidar conceitos essenciais para o desenvolvimento web full-stack com Django:

* Estruturação e arquitetura de projetos Django
* Criação e modularização de aplicações
* Manipulação de Models, Views, Templates e URLs
* Mapeamento objeto-relacional com Django ORM
* Gerenciamento de banco de dados via Migrations
* Implementação de sistema de Autenticação e Autorização
* Desenvolvimento de operações CRUD completas
* Controle de versão utilizando Git e GitHub

---

## 💡 Aprendizados

Durante o desenvolvimento, foi possível exercitar a construção de uma aplicação web robusta, entendendo a integração entre os componentes do framework Django e a organização de código limpo. O uso do Git e GitHub garantiu o versionamento correto do código-fonte e o aprendizado de fluxo de trabalho profissional.

---

## 👤 Autor

* **Gustayath**
* GitHub: [@gustayath](https://github.com/gustayath)
* Repositório do Projeto: [crud_aula_12.08](https://github.com/gustayath/crud_aula_12.08)

---

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais e de aprendizado. Sinta-se à vontade para utilizá-lo, modificá-lo e estudá-lo!
"""

```

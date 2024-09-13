
# Gerenciador de Tarefas

Um **Gerenciador de Tarefas** simples e eficiente, desenvolvido com **Flask** e **Python**, que permite que os usuários criem, editem, atribuam e acompanhem o progresso de suas tarefas. Este projeto foi feito com a intenção de facilitar a organização e colaboração em atividades.

## Funcionalidades

- **Autenticação de Usuário**: Registro, login e logout.
- **Gerenciamento de Tarefas**: Criação, edição, exclusão e atribuição de tarefas a múltiplos usuários.
- **Status das Tarefas**: As tarefas podem ter diferentes status como "pendente", "em andamento" ou "concluída".
- **Painel de Controle**: Cada usuário pode visualizar e gerenciar as tarefas atribuídas a ele.

## Instalação

### Pré-requisitos

Certifique-se de ter o **Python 3.x** e o **pip** instalados em sua máquina.

### Passos para Instalação

1. **Clonar o Repositório:**

   Clone o repositório para sua máquina local:

   ```bash
   git clone https://github.com/seu-usuario/gerenciador-tarefas.git
   cd gerenciador-tarefas
   ```

2. **Criar o Ambiente Virtual:**

   Crie e ative um ambiente virtual para isolar as dependências:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scriptsctivate     # Para Windows
   ```

3. **Instalar as Dependências:**

   Instale todas as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar o Banco de Dados:**

   Inicialize o banco de dados e aplique as migrações:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. **Configurar as Variáveis de Ambiente:**

   Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

   ```bash
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=sua-chave-secreta
   ```

6. **Executar o Projeto:**

   Inicie o servidor Flask com o comando:

   ```bash
   flask run
   ```

   Acesse o aplicativo no navegador em `http://127.0.0.1:5000`.

## Uso

### 1. Registro de Usuário

- Acesse `http://127.0.0.1:5000/register` para criar um novo usuário.

### 2. Login

- Após o registro, vá para `http://127.0.0.1:5000/login` para realizar o login.

### 3. Painel de Controle

- No painel, você poderá visualizar suas tarefas, criar novas, editar ou excluir as existentes.

### 4. Criar Tarefa

- Acesse `http://127.0.0.1:5000/create_task` para criar uma nova tarefa, onde você pode definir o título, a descrição, o status e atribuir a outros usuários.

## Estrutura do Projeto

```
gerenciador-tarefas/
│
├── instance/            # Banco de dados SQLite
├── routes/              # Rotas principais do aplicativo
│   ├── main_routes.py
├── templates/           # Templates HTML
│   ├── index.html
│   ├── dashboard.html
│   ├── create_task.html
│   ├── edit_task.html
├── static/              # Arquivos estáticos (CSS, JS)
├── app.py               # Arquivo principal do aplicativo
├── models.py            # Definição dos modelos (User, Task)
├── forms.py             # Definição dos formulários com Flask-WTF
├── config.py            # Configurações da aplicação
├── run.py               # Script para rodar o Flask
├── requirements.txt     # Lista de dependências
└── README.md            # Documentação do projeto
```

## Tecnologias Utilizadas

- **Python** 3.x
- **Flask** - Framework web
- **Flask-WTF** - Gerenciamento de formulários
- **Flask-Login** - Autenticação de usuários
- **Flask-Migrate** - Migração do banco de dados
- **SQLite** - Banco de dados leve
- **Jinja2** - Engine de templates para o Flask
- **Bootstrap** - Framework CSS para design responsivo

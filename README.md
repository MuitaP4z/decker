# decker
Decker - Protótipo de gerenciador para coleção de cartas

Antes da execução do projeto com o docker, é importante instalar o python e configurar um ambiente virtual com o venv:
1. Na pasta raiz do projeto, execute:
python -m venv venv
2. Ative o ambiente:
Linux/macOS:
source venv/bin/activate

Windows:
venv\Scripts\activate

3. Instale as depedências com
pip install -r requirements.txt

Instruções para execução do projeto utilizando Docker:
1. Abra o prompt de comando na pasta do projeto;
2. Execute 'docker compose up --build'
3. Abra o site em http://localhost:8000

Para acessar o site, crie um superusuário para a base de dados recem criada com:
python manage.py createsuperuser


## Autenticação e Fluxo do Site
1. Tela Inicial (Greeter) — Página de boas-vindas.
2. Login — Autenticação para usuários cadastrados.
3. Dashboard — Painel principal do sistema.
4. Django Admin — Área administrativa para gerenciar cartas, coleções e usuários.


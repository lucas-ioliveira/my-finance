# MyFinance.

Nesse repositório contém um projeto fullstack realizado o front-end com Html, Css, BootStrap 4, JavaScript e o back-end com Python e o framework Django.

O projeto consiste em um sistema para controle financeiro pessoal, é possível acompanhar toda a sua vida financeira em um só lugar, o sistema permite gerenciar despesas, receitas e investimentos. Também contém funcionalidades de relatório, como por exemplo, baixar uma planilha em excel com os dados das despesas, receitas e investimentos de acordo com os filtros escolhidos pelo usuário.

### Pré-requisitos

- Python instalado;
- Criação do ambiente virtual (Linux: python3 -m venv venv ou no Windows: python -m venv venv);
- Ativação do ambiente criado anteriormente (Linux: source venv/bin/activate ou no Windows: venv\Scripts\activate);
- Instalação dos requirements.txt disponibilizados (pip insall -r requirements.txt);
- O banco de dados é de sua escolha, mas nesse projeto utilizei o SQLite (Caso escolha um banco de dados diferente do padrão não esqueça de realizar as alterações no arquivo settings.py);
- OBS¹: Caso tenha o Docker intalado será o suficiente e apenas precisará rodar o docker compose disponibilizado
(No diretório do projeto rodar o comando: docker compose -f docker-compose.yml up -d --build);
- OBS²: Caso opte por rodar o projeto sem usar o docker, é necessário remover algumas configurações de variáveis de ambiente existente no settings.py e deixar padrão;

### Execução do sistema

- Basta entrar no diretório do projeto e no terminal rodar o comando: python manage.py runserver ou docker compose -f docker-compose.yml up -d --build;
- O servidor será executado e se acessar localhost:8006 acessará a página inicial do sistema onde poderá realizar o cadastro ou o login;

### Exemplo da execução

- Obs: As páginas são acessíveis somente com o usuário autenticado, obviamente, a home, login e cadastro são de livre acesso.

- Home

![Home](docs/img/home.png)

- Login

![Home](docs/img/login.png)

- Cadastre-se

![Home](docs/img/cadastro.png)

#### Dashboard

- Ao realizar o login, o usuário é redirecionado para o seu dashboard

![Dashboard ](docs/img/logado.png)

- Algumas informações relevantes são apresentadas, como o valor total de receitas, despesas, investimentos e o saldo (Equivalente a subtração das despesas e investimentos). Também conta com informações de câmbio, trazendo a cotação do dia das principais moedas e atividades recentes que são as ações do usuário no sistema.

![Dashboard ](docs/img/dashboard.png)

- No dashboard também conta com um filtro de períodos onde o usuário pode filtrar as datas que deseja e os cards com os valores serão atualizados de acordo com o filtro.

![Modal de período ](docs/img/filtrar.png)

#### Perfil

##### Gerenciamento do perfil

- Visualização geral do perfil

![Perfil](docs/img/perfil.png)

- Alterar senha

![Perfil - Alterar senha](docs/img/alterar_senha.png)

- Alterar informações pessoais

![Perfil - Alterar info pessoais](docs/img/alterar_info_pessoal.png)

- Alterar endereço
- Obs: Ao alterar o endereço, basta digitar somente o cep que os demais campos serão preenchidos automáticamente. 

![Perfil - Alterar endereço](docs/img/alterar_endereco.png)


#### Categorias

##### Gerenciamento de categorias

- Lista de categorias cadastradas

![Categorias - lista](docs/img/categorias.png)

- Adicionar categoria

![Categorias - modal para adicionar](docs/img/add_categoria.png)

- Editar categoria

![Categorias - modal para editar](docs/img/editar_categoria.png)

- Excluir categoria

![Categorias - alerta para excluir](docs/img/excluir_categoria.png)


#### Despesas

##### Gerenciamento de despesas

- Lista de despesas cadastradas

![Despesas - lista](docs/img/despesa_lista.png)

- Adicionar despesas

![Despesas - modal para adicionar](docs/img/add_despesa.png)

- Editar despesas

![Despesas - modal para editar](docs/img/edit_despesa.png)

- Excluir despesas

![Despesas - alerta para excluir](docs/img/alerta_despesa.png)


#### Receitas

##### Gerenciamento de receitas

- Lista de receita cadastradas

![Receita - lista](docs/img/receita_lista.png)

- Adicionar receita

![Receita - modal para adicionar](docs/img/add_receita.png)

- Editar receita

![Receita - modal para editar](docs/img/editar_receita.png)

- Excluir receita

![Receita - alerta para excluir](docs/img/alerta_receita.png)


#### Investimentos

##### Gerenciamento de investimentos

- Lista de investimentos cadastradas

![Investimentos - lista](docs/img/investimentos.png)

- Adicionar investimentos

![Investimentos - modal para adicionar](docs/img/add_investimento.png)

- Editar investimentos

![Investimentos - modal para editar](docs/img/editar_investimento.png)

- Excluir investimentos

![Investimentos - alerta para excluir](docs/img/alerta_investimento.png)


#### Relatórios

##### Download excel

- Exportar Despesa

![Investimentos - lista](docs/img/exportar_despesa.png)

- Exportar Receita

![Investimentos - modal para adicionar](docs/img/exportar_receita.png)

- Exportar investimentos

![Investimentos - modal para editar](docs/img/exportar_investimento.png)


### Modelagem e arquitetura

- Modelagem do banco de dados

![Tabelas do banco](docs/img/modelagem.png)

- schema

![Tabelas do banco](docs/img/schema.png)





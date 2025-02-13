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

![Home](doc/img/home.png)

- Login

![Home](doc/img/login.png)

- Cadastre-se

![Home](doc/img/cadastro.png)

#### Dashboard

- Ao realizar o login, o usuário é redirecionado para o seu dashboard

![Dashboard ](doc/img/logado.png)

![Dashboard ](doc/img/dashboard.png)

#### Perfil

##### Gerenciamento do perfil

- Visualização geral do perfil

![Perfil](doc/img/perfil.png)

- Alterar senha

![Perfil - Alterar senha](doc/img/alterar_senha.png)

- Alterar informações pessoais

![Perfil - Alterar info pessoais](doc/img/alterar_info_pessoal.png)

- Alterar endereço
- Obs: Ao alterar o endereço, basta digitar somente o cep que os demais campos serão preenchidos automáticamente. 

![Perfil - Alterar endereço](doc/img/alterar_endereco.png)


#### Categorias

##### Gerenciamento de categorias

- Lista de categorias cadastradas

![Categorias - lista](doc/img/categorias.png)

- Adicionar categoria

![Categorias - modal para adicionar](doc/img/add_categoria.png)

- Editar categoria

![Categorias - modal para editar](doc/img/editar_categoria.png)

- Excluir categoria

![Categorias - alerta para excluir](doc/img/excluir_categoria.png)


#### Despesas

##### Gerenciamento de despesas

- Lista de despesas cadastradas

![Despesas - lista](doc/img/despesa_lista.png)

- Adicionar despesas

![Despesas - modal para adicionar](doc/img/add_despesa.png)

- Editar despesas

![Despesas - modal para editar](doc/img/edit_despesa.png)

- Excluir despesas

![Despesas - alerta para excluir](doc/img/alerta_despesa.png)


#### Receitas

##### Gerenciamento de receitas

- Lista de receita cadastradas

![Receita - lista](doc/img/receita_lista.png)

- Adicionar receita

![Receita - modal para adicionar](doc/img/add_receita.png)

- Editar receita

![Receita - modal para editar](doc/img/editar_receita.png)

- Excluir receita

![Receita - alerta para excluir](doc/img/alerta_receita.png)


#### Investimentos

##### Gerenciamento de investimentos

- Lista de investimentos cadastradas

![Investimentos - lista](doc/img/investimentos.png)

- Adicionar investimentos

![Investimentos - modal para adicionar](doc/img/add_investimento.png)

- Editar investimentos

![Investimentos - modal para editar](doc/img/editar_investimento.png)

- Excluir investimentos

![Investimentos - alerta para excluir](doc/img/alerta_investimento.png)


#### Relatórios

##### Download excel

- Exportar Despesa

![Investimentos - lista](doc/img/exportar_despesa.png)

- Exportar Receita

![Investimentos - modal para adicionar](doc/img/exportar_receita.png)

- Exportar investimentos

![Investimentos - modal para editar](doc/img/exportar_investimento.png)






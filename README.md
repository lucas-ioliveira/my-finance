# MyFinance.

Nesse repositório contém um projeto fullstack realizado o front-end com Html, Css, BootStrap 4, JavaScript e o back-end com Python e o framework Django.

O projeto consiste em um sistema para controle financeiro pessoal, é possível acompanhar toda a sua vida financeira em um só lugar, o sistema permite gerenciar despesas, receitas e investimentos. Também contém funcionalidades de relatório, como por exemplo, baixar uma planilha em excel com os dados das despesas, receitas e investimentos de acordo com os filtros escolhidos pelo usuário.

<br>

<h2>Pré-requisitos</h2>

- [Docker](https://www.docker.com/) 

<br>

<h2>Clone</h2>

```bash
git clone https://github.com/lucas-ioliveira/my-finance.git
```

<br>

<h2 id="started">🚀 Primeiros passos</h2>

<p>Basta entrar no diretório do projeto e no terminal rodar o comando:</p> 


```bash
docker compose -f docker-compose.yml up -d --build
```

<p>Isso fará com que todas as dependências sejam instaladas e um container docker seja executado.</p>

<br>

<p>Verifique se o container está em execução com o comando:</p>

```bash
docker ps -a
```

<br>

<h2 id="routes">📍Rotas</h2>

<p>As páginas são acessíveis somente com o usuário autenticado, obviamente, a home, login e cadastro são de livre acesso.</p>

**Home**

![Home](docs/img/home.png)

<br>

**Login**

![Home](docs/img/login.png)

<br>

**Cadastre-se**

![Home](docs/img/cadastro.png)

<br>

**Dashboard**

<p>Ao realizar o login, o usuário é direcionado para o seu dashboard</p>

![Dashboard ](docs/img/logado.png)

<br>

<p>Algumas informações relevantes são apresentadas, como o valor total de receitas, despesas, investimentos e o saldo (Equivalente a subtração das despesas e investimentos). Também conta com informações de câmbio, trazendo a cotação do dia das principais moedas e atividades recentes que são as ações do usuário no sistema.</p>

![Dashboard ](docs/img/dashboard.png)

<br>

<p>No dashboard também conta com um filtro de períodos onde o usuário pode filtrar as datas que deseja e os cards com os valores serão atualizados de acordo com o filtro.</p>

![Modal de período ](docs/img/filtrar.png)

<br>

**Perfil**

<p>Visualização geral do perfil</p>

![Perfil](docs/img/perfil.png)

<br>

<p>Alterar senha</p>

![Perfil - Alterar senha](docs/img/alterar_senha.png)

<br>

<p>Alterar informações pessoais</p>

![Perfil - Alterar info pessoais](docs/img/alterar_info_pessoal.png)

<br>

<p>Alterar endereço</p>
<p>Obs: Ao alterar o endereço, basta digitar somente o cep que os demais campos serão preenchidos automáticamente.</p>

![Perfil - Alterar endereço](docs/img/alterar_endereco.png)

<br>

**Categorias**

<p>Lista de categorias cadastradas</p>

![Categorias - lista](docs/img/categorias.png)

<br>

<p>Adicionar categoria</p>

![Categorias - modal para adicionar](docs/img/add_categoria.png)

<br>

<p>Editar categoria</p>

![Categorias - modal para editar](docs/img/editar_categoria.png)

<br>

<p>Excluir categoria</p>

![Categorias - alerta para excluir](docs/img/excluir_categoria.png)

<br>

**Despesas**


<p>Lista de despesas cadastradas</p>

![Despesas - lista](docs/img/despesa_lista.png)

<br>

<p>Adicionar despesas</p>

![Despesas - modal para adicionar](docs/img/add_despesa.png)

<br>

<p>Editar despesas</p>

![Despesas - modal para editar](docs/img/edit_despesa.png)

<br>

<p>Excluir despesas</p>

![Despesas - alerta para excluir](docs/img/alerta_despesa.png)

<br>

**Receitas**

<p>Lista de receita cadastradas</p>

![Receita - lista](docs/img/receita_lista.png)

<br>

<p>Adicionar receita</p>

![Receita - modal para adicionar](docs/img/add_receita.png)

<br>

<p>Editar receita</p>

![Receita - modal para editar](docs/img/editar_receita.png)

<br>

<p>Excluir receita</p>

![Receita - alerta para excluir](docs/img/alerta_receita.png)

<br>

**Investimentos**

<p>Lista de investimentos cadastradas</p>

![Investimentos - lista](docs/img/investimentos.png)

<br>

<p>Adicionar investimentos</p>

![Investimentos - modal para adicionar](docs/img/add_investimento.png)

<br>

<p>Editar investimentos</p>

![Investimentos - modal para editar](docs/img/editar_investimento.png)

<br>

<p>Excluir investimentos</p>

![Investimentos - alerta para excluir](docs/img/alerta_investimento.png)

<br>

**Relatórios**

##### Download para excel

<p>Exportar Despesa</p>

![Investimentos - lista](docs/img/exportar_despesa.png)

<br>

<p>Exportar Receita</p>

![Investimentos - modal para adicionar](docs/img/exportar_receita.png)

<br>

<p>Exportar investimentos</p>

![Investimentos - modal para editar](docs/img/exportar_investimento.png)

<br>

**Modelagem e arquitetura**

<p>Modelagem do banco de dados</p>

![Tabelas do banco](docs/img/modelagem.png)

<br>

<p>schema</p>

![Tabelas do banco](docs/img/schema.png)





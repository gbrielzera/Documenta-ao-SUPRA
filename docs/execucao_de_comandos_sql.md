# Execução de Comandos SQL

Caminho: Guia para Administradores > Execução de Comandos SQL

No Supravizio temos uma funcionalidade de execução de comandos SQL localizada em Menu Principal | Relatórios | Execução de Comandos SQL:

Execução de comandos SQL

Na tela para a execução de comandos SQL, na aba "Comando SQL" inserimos os comandos e podemos contar com o recurso que auxilia com as sintaxes SQL e também das tabelas e colunas do banco de dados do Supravizio. Esse recurso filtra os comandos conforme é inserido algumas letra, ou pressionando Ctrl + Espaço:

Editor de Comandos SQL - Supravizio Windows

Ao inserir uma query, temos que clicar em "Executar", então abrirá na aba "Dados" ao lado o resultado.

No exemplo a seguir, executamos a query: SELECT * FROM PESSOA

Editor de Comandos SQL

Menu da tela Execução de comandos SQL

Query Builder

Podemos contar também com o Query Builder, através do botão "Query Builder". Este recurso auxilia a edição da consulta por um meio gráfico, arrastando as tabelas, habilitando as colunas, criando as relações, etc.

Neste exemplo, incluímos a tabela PESSOA e a tabela ÓRGÃO, arrastando-as da coluna da direita, checkamos os campos NOME e EMAIL de PESSOA e DESCRICAO de ORGAO. Criamos a relação, arrastando o campo ID_ORGAO de PESSOA até o campo ID_ORGAO de ORGAO.

Podemos reparar que no canto inferior da tela o query builder foi automaticamente montando a query:

Query Builder

Basta então clicar em Ok e voltará a tela de Edição de Comando SQL, podemos perceber que a query foi inserida no editor:

Execução de Comando SQL

Devemos clicar em Executar, então é exibido o resultado da consulta:

Resultado da Consulta

Salvando e Recuperando uma consulta

Através do botão salvar, nós podemos salvar a consulta em um arquivo de extensão .sql para podermos reutilizá-la num outro momento através do botão Recuperar.

Obs: No ambiente de Produção só é possível realizar os comando de seleção, ou seja, o SELECT.

Já no [Ambiente de Qualidade](ambiente_de_qualidade), podemos executar, além do SELECT, os comandos de INSERT, UPDATE e DELETE.

Log de Execução de Comandos SQL

O Supravizio possui um relatório que lista as execuções dos comandos SQL, localizado em Menu Principal | Relatórios | Administração do Sistema | Log de Execução de Comandos SQL:

Log de Execução de Comandos SQL

No relatório basta filtrar as datas para o relatório e clicar em Consultar, então listará todos os comando executados neste intervalo:

Relatório de execuções de comandos SQL

Editor de Comandos SQL no Supravizio Web

No Supravizio Web a página do Editor de Comandos SQL possui três áreas:

- A primeira é o próprio editor de query, com o botão "Executar" logo acima;
- Logo abaixo encontra-se o grid onde será exibido os resultados da query;
- E por fim, o grid "Histórico de comandos executados pelo usuário conectado" apresenta os comandos executados anteriormente pelo usuário logado.

Editor de Comandos SQL - Supravizio Web

# Objeto DB

Caminho: Recursos Avançados > Objeto DB

O objeto DB contém funções que possibilitam manipular dados no Sistema Gerenciador de Banco de Dados (SGDB) como inserir, remover ou alterar registros.

Este objeto possui os seguintes métodos:

**Funções:**

| **Nome** | **Função** |
|---|---|
| **ExecuteDataTable**(string commandText) | Retorna um objeto DataTable (tabela de dados do ADO.NET) contendo o resultado da consulta fornecida como parâmetro. Se ocorrer algum erro durante a gravação da mensagem é levantada uma Exceção. |
| **ExecuteDataTable**(string commandText, string database) | Retorna um objeto DataTable (tabela de dados do ADO.NET) contendo o resultado da consulta fornecida como parâmetro. Se ocorrer algum erro durante a gravação da mensagem é levantada uma Exceção. |
| **ExecuteNonQuery**(string commandText) | Executa um comando SQL de modificação (Insert, Update ou Delete). Se ocorrer algum erro durante a gravação da mensagem é levantada uma Exceção. |
| **ExecuteNonQuery**(string commandText, string | Executa um comando SQL de modificação (Insert, Update ou Delete). Se ocorrer algum erro durante a gravação da mensagem é levantada uma Exceção. A string de conexão fornecida como parâmetro é configurada na camada servidora no arquivo \".config\". |
| **ExecuteScalar**(string commandText) | Retorna a primeira coluna da primeira linha contendo o resultado da consulta fornecida como parâmetro. Se ocorrer algum erro durante a gravação da mensagem é levantada uma Exceção. |
| **ExecuteScalar**(string commandText, string database) | Retorna a primeira coluna da primeira linha contendo o resultado da consulta fornecida como parâmetro. Se ocorrer algum erro durante a gravação da mensagem é levantada uma Exceção. A string de conexão fornecida como parâmetro é configurada na camada servidora no arquivo \".config\". |
| **ExecuteStoredProc**(string storedProcName) | Executa uma Stored procedure. |
| **ExecuteStoredProc**(string storedProcName, DbParameter parametro1) | Executa uma Stored procedure passando 1 parâmetro. |
| **ExecuteStoredProc**(string storedProcName, DbParameter parametro1, DbParameter parametro2) | Executa uma Stored procedure passando 2 parâmetros. |
| **ExecuteStoredProc**(string storedProcName, DbParameter parametro1, DbParameter parametro2, DbParameter parametro3) | Executa uma Stored procedure passando 3 parâmetros. |
| **ExecuteStoredProc**(string storedProcName, DbParameter[] parametros) | Executa uma Stored procedure fornecendo um array de parâmetros. |
| **ExecuteStoredProc**(string storedProcName, string database) | Executa uma Stored procedure em um banco de dados externo. |
| **ExecuteStoredProc**(string storedProcName, string database, DbParameter[] parametros) | Executa uma Stored procedure em um banco de dados externo fornecendo parâmetros. |

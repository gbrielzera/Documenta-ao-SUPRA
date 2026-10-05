# Consulta de relatório

Caminho: Janelas > Utilitários > Relatórios > Consulta de relatório

Consulta criada pelo usuário para recuperação dos dados que serão apresentados pelo relatório. No caso de consultas do banco de dados do produto o usuário contará com o recurso Query Builder.

Na tabela abaixo temos os principais campos deste cadastro:

## Campos do cadastro

| **Nome da consulta** | Corresponde ao nome da banda do relatório associada com a consulta. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna NAME da tabela [SV_REPORT_QUERY](dados_sv_report_query). |
|---|---|
| **SQL** | Comando SQL Select utilizado para recuperar os dados do relatório. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna SQL da tabela [SV_REPORT_QUERY](dados_sv_report_query). |
| **Banco de dados externo** | Conexão de banco de dados externo Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |

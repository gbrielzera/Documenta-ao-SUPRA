# APROVACAO

Caminho: Customização > Modelo de dados > Processo > APROVACAO

Registro de Aprovação por Aprovador

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PESSOA** | Identificador da Pessoa responsável pela Aprovação | int | number(6,0) | Não |
| **VERSAO** | Sequencial gerado automaticamente pelo sistema para cada Assunto de uma determinada Ordem de Serviço | int | number(6,0) | Não |
| **ID_ASSUNTO_APROVACAO** | Assunto para Aprovação associado | int | number(6,0) | Não |
| **DATA_HORA_EVIDENCIA** | Data e hora em que foi realizado o último evento. | datetime | date | Não |
| **MOTIVO** | Motivo ou Comentário feito pelo Cliente durante a realização da Aprovação, Reprovação ou Cancelamento (estados terminais para o processo). | varchar(500) | varchar(500) | Sim |
| **SITUACAO** | Situação para a Versão a ser Aprovada. | varchar(250) | varchar(250) | Não |
| **DESC_PAPEL_APROVADOR** | Descrição do Papel que o Aprovador possui no Processo. | varchar(500) | varchar(500) | Sim |
| **ID_APROVADOR_REAL** | Identificador da Pessoa que realizou a Aprovação | int | number(6,0) | Sim |
| **PASSO** | Passo do aprovador em aprovações por hierarquia | int | number(6,0) | Não |
| **EXPLIC_APROVADOR** | Texto explicativo sobre o aprovador. | varchar(500) | varchar(500) | Sim |
| **UTILIZOU_PRE_APROV** | Foi utilizado algum critério de pré-aprovação | char(3) | char(3) | Não |

Tabelas referenciadas por APROVACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **APROVACAO** \| \|---\|---\| \| ID_PESSOA \| ID_APROVADOR_REAL \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **APROVACAO** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA \| |
| [VERSAO_APROVACAO](dados_versao_aprovacao) | \| **VERSAO_APROVACAO** \| **APROVACAO** \| \|---\|---\| \| ID_ASSUNTO_APROVACAO \| ID_ASSUNTO_APROVACAO \| \| VERSAO \| VERSAO \| |

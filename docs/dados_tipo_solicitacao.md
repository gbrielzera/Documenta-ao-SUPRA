# TIPO_SOLICITACAO

Caminho: Customização > Modelo de dados > Processo > TIPO_SOLICITACAO

Agrupamento de solicitações exibido em um dos primeiros passos da Abertura de Ordens de Serviço do Autoatendimento.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_TIPO_SOLICITACAO** | Número sequencial gerado automaticamente pelo sistema para Identificar um TipoSolicitacao | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do TipoSolicitacao | varchar(500) | varchar(500) | Não |

Tabelas que dependem de TIPO_SOLICITACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **TIPO_SOLICITACAO** \| \|---\|---\| \| ID_TIPO_SOLICITACAO \| ID_TIPO_SOLICITACAO \| |

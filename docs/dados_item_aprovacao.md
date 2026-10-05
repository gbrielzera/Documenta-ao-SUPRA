# ITEM_APROVACAO

Caminho: Customização > Modelo de dados > Processo > ITEM_APROVACAO

Item de Configuração sujeito a Aprovação.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ASSUNTO_APROVACAO** | Número sequencial gerado automaticamente pelo sistema para Identificar um AssuntoAprovacao | int | number(6,0) | Não |
| **VERSAO** | Sequencial gerado automaticamente pelo sistema para cada Assunto de uma determinada Ordem de Serviço | int | number(6,0) | Não |
| **ID_ITEM** | Identificador do ItemConfiguracao associado | int | number(6,0) | Não |

Tabelas referenciadas por ITEM_APROVACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM](dados_item) | \| **ITEM** \| **ITEM_APROVACAO** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |
| [VERSAO_APROVACAO](dados_versao_aprovacao) | \| **VERSAO_APROVACAO** \| **ITEM_APROVACAO** \| \|---\|---\| \| ID_ASSUNTO_APROVACAO \| ID_ASSUNTO_APROVACAO \| \| VERSAO \| VERSAO \| |

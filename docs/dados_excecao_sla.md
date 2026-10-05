# EXCECAO_SLA

Caminho: Customização > Modelo de dados > Recurso > EXCECAO_SLA

Redefinição do tempo de atendimento para períodos de exceção em um mês ou ano.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_EXCECAO_SLA** | Número sequencial gerado automaticamente pelo sistema para Identificar um ExcecaoSLA | int | number(6,0) | Não |
| **ID_ITEM_SLA** | Número sequencial gerado automaticamente pelo sistema para Identificar um ItemSLA | int | number(6,0) | Não |
| **PERIODO** | Tipo de Período de Exceção que pode ser um período compreendido em um Mês (dias de um mês para exceção) ou Ano (meses do ano para exceção). | varchar(250) | varchar(250) | Não |
| **INICIO** | Dia de início se o período for Mês ou mês de início se o período for Ano. | int | number(6,0) | Não |
| **FIM** | Dia de fim se o período for Mês ou mês de fim se o período for Ano. | int | number(6,0) | Não |
| **TEMPO_ATEND** | Tempo de atendimento (em minutos) para Ordens de Serviço enquadradas no critério de período de exceção. | int | number(6,0) | Não |

Tabelas referenciadas por EXCECAO_SLA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM_SLA](dados_item_sla) | \| **ITEM_SLA** \| **EXCECAO_SLA** \| \|---\|---\| \| ID_ITEM_SLA \| ID_ITEM_SLA \| |

**Exemplo 1: join com a tabela ITEM_SLA**

```
select EXCECAO_SLA.*
from EXCECAO_SLA, ITEM_SLA
where EXCECAO_SLA.ID_ITEM_SLA = ITEM_SLA.ID_ITEM_SLA
```

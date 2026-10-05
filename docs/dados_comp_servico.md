# COMP_SERVICO

Caminho: Customização > Modelo de dados > Processo > COMP_SERVICO

Item de Configuração Componente de Serviço

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_SERVICO** | Identificador do Serviço | int | number(6,0) | Não |
| **ID_ITEM** | Identificador do ItemConfiguracao associado | int | number(6,0) | Não |
| **IMPACTO_PAR_INC** | Impacto na disponibilização do Serviço em caso de falhas ou mudanças. Este impacto é utilizado no cálculo de Análise de Impacto e determinará se o componente tornará o serviço indisponível. | varchar(250) | varchar(250) | Não |

Tabelas referenciadas por COMP_SERVICO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM](dados_item) | \| **ITEM** \| **COMP_SERVICO** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |
| [SERVICO](dados_servico) | \| **SERVICO** \| **COMP_SERVICO** \| \|---\|---\| \| ID_SERVICO \| ID_SERVICO \| |

**Exemplo 1: join com a tabela SERVICO**

```
select COMP_SERVICO.*
from COMP_SERVICO, SERVICO
where COMP_SERVICO.ID_SERVICO = SERVICO.ID_SERVICO
```

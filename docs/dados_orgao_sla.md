# ORGAO_SLA

Caminho: Customização > Modelo de dados > Recurso > ORGAO_SLA

Órgão atendido por um ANS

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ORGAO** | Identificador do Orgao associado | int | number(6,0) | Não |
| **ID_SLA** | Identificador do AcordoNivelServico associado | int | number(6,0) | Não |
| **INCLUI_SUBAREAS** | Indica que o acordo é extendido para sub-áreas. | char(3) | char(3) | Não |

Tabelas referenciadas por ORGAO_SLA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ORGAO](dados_orgao) | \| **ORGAO** \| **ORGAO_SLA** \| \|---\|---\| \| ID_ORGAO \| ID_ORGAO \| |
| [SLA](dados_sla) | \| **SLA** \| **ORGAO_SLA** \| \|---\|---\| \| ID_SLA \| ID_SLA \| |

**Exemplo 1: join com a tabela ORGAO**

```
select ORGAO_SLA.*, ORGAO.DESCRICAO
from ORGAO_SLA, ORGAO
where ORGAO_SLA.ID_ORGAO = ORGAO.ID_ORGAO
```

**Exemplo 2: join com a tabela SLA**

```
select ORGAO_SLA.*
from ORGAO_SLA, SLA
where ORGAO_SLA.ID_SLA = SLA.ID_SLA
```

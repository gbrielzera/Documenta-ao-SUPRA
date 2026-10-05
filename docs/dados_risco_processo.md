# RISCO_PROCESSO

Caminho: Customização > Modelo de dados > Processo > RISCO_PROCESSO

Risco de Subprocesso

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_RISCO** | Identificador do Risco associado | int | number(6,0) | Não |
| **ID_SUB_PROCESSO** | Identificador do Tipo de Subprocesso | int | number(6,0) | Não |
| **TITULO** | Título do Risco | varchar(500) | varchar(500) | Não |
| **DESCRICAO** | Descrição | varchar(500) | varchar(500) | Sim |
| **AVALIACAO_RISCO** | Avaliação do Risco | varchar(250) | varchar(250) | Sim |
| **IMPACTO_RISCO** | Impacto do Risco | varchar(250) | varchar(250) | Sim |
| **PROB_OCORR** | Probabilidade de ocorrência do Risco | varchar(250) | varchar(250) | Sim |

Tabelas referenciadas por RISCO_PROCESSO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [RISCO](dados_risco) | \| **RISCO** \| **RISCO_PROCESSO** \| \|---\|---\| \| ID_RISCO \| ID_RISCO \| |
| [SUB_PROCESSO](dados_sub_processo) | \| **SUB_PROCESSO** \| **RISCO_PROCESSO** \| \|---\|---\| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| |

Tabelas que dependem de RISCO_PROCESSO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CONTROLE](dados_controle) | \| **CONTROLE** \| **RISCO_PROCESSO** \| \|---\|---\| \| ID_RISCO \| ID_RISCO \| \| ID_SUB_PROC_RISCO \| ID_SUB_PROCESSO \| |
| [RISCO_GAP](dados_risco_gap) | \| **RISCO_GAP** \| **RISCO_PROCESSO** \| \|---\|---\| \| ID_RISCO \| ID_RISCO \| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| |
| [RISC_PROC_AFIRM](dados_risc_proc_afirm) | \| **RISC_PROC_AFIRM** \| **RISCO_PROCESSO** \| \|---\|---\| \| ID_RISCO \| ID_RISCO \| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| |

**Exemplo 1: join com a tabela RISCO**

```
select RISCO_PROCESSO.*, RISCO.DESCRICAO
from RISCO_PROCESSO, RISCO
where RISCO_PROCESSO.ID_RISCO = RISCO.ID_RISCO
```

**Exemplo 2: join com a tabela SUB_PROCESSO**

```
select RISCO_PROCESSO.*
from RISCO_PROCESSO, SUB_PROCESSO
where RISCO_PROCESSO.ID_SUB_PROCESSO = SUB_PROCESSO.ID_SUB_PROCESSO
```

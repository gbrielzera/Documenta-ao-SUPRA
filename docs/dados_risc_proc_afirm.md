# RISC_PROC_AFIRM

Caminho: Customização > Modelo de dados > Processo > RISC_PROC_AFIRM

Afirmações

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_RISCO** | Identificador do Risco associado | int | number(6,0) | Não |
| **ID_SUB_PROCESSO** | Identificador do Tipo de Subprocesso | int | number(6,0) | Não |
| **ID_AFIRM_FIANC** | Identificador da AfirmacaoFinanceira associada | int | number(6,0) | Não |

Tabelas referenciadas por RISC_PROC_AFIRM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [AFIRM_FINANC](dados_afirm_financ) | \| **AFIRM_FINANC** \| **RISC_PROC_AFIRM** \| \|---\|---\| \| ID_AFIRM_FIANC \| ID_AFIRM_FIANC \| |
| [RISCO_PROCESSO](dados_risco_processo) | \| **RISCO_PROCESSO** \| **RISC_PROC_AFIRM** \| \|---\|---\| \| ID_RISCO \| ID_RISCO \| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| |

Tabelas que dependem de RISC_PROC_AFIRM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CONTROL_AFIRM](dados_control_afirm) | \| **CONTROL_AFIRM** \| **RISC_PROC_AFIRM** \| \|---\|---\| \| ID_RISCO \| ID_RISCO \| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| \| ID_AFIRM_FIANC \| ID_AFIRM_FIANC \| |

**Exemplo 1: join com a tabela AFIRM_FINANC**

```
select RISC_PROC_AFIRM.*, AFIRM_FINANC.DESCRICAO
from RISC_PROC_AFIRM, AFIRM_FINANC
where RISC_PROC_AFIRM.ID_AFIRM_FIANC = AFIRM_FINANC.ID_AFIRM_FIANC
```

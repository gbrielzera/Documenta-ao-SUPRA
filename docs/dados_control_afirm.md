# CONTROL_AFIRM

Caminho: Customização > Modelo de dados > Processo > CONTROL_AFIRM

Afirmações

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CONTROLE** | Número sequencial gerado automaticamente pelo sistema para Identificar um Controle | int | number(6,0) | Não |
| **ID_RISCO** | Identificador da RiscoProcessoAfirmaca associada | int | number(6,0) | Não |
| **ID_SUB_PROCESSO** | Identificador da RiscoProcessoAfirmaca associada | int | number(6,0) | Não |
| **ID_AFIRM_FIANC** | Identificador da RiscoProcessoAfirmaca associada | int | number(6,0) | Não |

Tabelas referenciadas por CONTROL_AFIRM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [RISC_PROC_AFIRM](dados_risc_proc_afirm) | \| **RISC_PROC_AFIRM** \| **CONTROL_AFIRM** \| \|---\|---\| \| ID_RISCO \| ID_RISCO \| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| \| ID_AFIRM_FIANC \| ID_AFIRM_FIANC \| |
| [CONTROLE](dados_controle) | \| **CONTROLE** \| **CONTROL_AFIRM** \| \|---\|---\| \| ID_CONTROLE \| ID_CONTROLE \| |

**Exemplo 1: join com a tabela CONTROLE**

```
select CONTROL_AFIRM.*
from CONTROL_AFIRM, CONTROLE
where CONTROL_AFIRM.ID_CONTROLE = CONTROLE.ID_CONTROLE
```

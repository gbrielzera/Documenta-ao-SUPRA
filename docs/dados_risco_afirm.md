# RISCO_AFIRM

Caminho: Customização > Modelo de dados > Processo > RISCO_AFIRM

Afirmações Financeiras do Risco

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_AFIRM_FIANC** | Identificador da AfirmacaoFinanceira associada | int | number(6,0) | Não |
| **ID_RISCO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Risco | int | number(6,0) | Não |

Tabelas referenciadas por RISCO_AFIRM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [AFIRM_FINANC](dados_afirm_financ) | \| **AFIRM_FINANC** \| **RISCO_AFIRM** \| \|---\|---\| \| ID_AFIRM_FIANC \| ID_AFIRM_FIANC \| |
| [RISCO](dados_risco) | \| **RISCO** \| **RISCO_AFIRM** \| \|---\|---\| \| ID_RISCO \| ID_RISCO \| |

**Exemplo 1: join com a tabela AFIRM_FINANC**

```
select RISCO_AFIRM.*, AFIRM_FINANC.DESCRICAO
from RISCO_AFIRM, AFIRM_FINANC
where RISCO_AFIRM.ID_AFIRM_FIANC = AFIRM_FINANC.ID_AFIRM_FIANC
```

**Exemplo 2: join com a tabela RISCO**

```
select RISCO_AFIRM.*
from RISCO_AFIRM, RISCO
where RISCO_AFIRM.ID_RISCO = RISCO.ID_RISCO
```

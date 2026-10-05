# AFIRM_FINANC

Caminho: Customização > Modelo de dados > Processo > AFIRM_FINANC

Afirmações Financeiras

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_AFIRM_FIANC** | Número sequencial gerado automaticamente pelo sistema para Identificar um AfirmacaoFinanceira | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do AfirmacaoFinanceira | varchar(500) | varchar(500) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |

Tabelas que dependem de AFIRM_FINANC

| **Tabela** | **Colunas de ligação** |
|---|---|
| [RISCO_AFIRM](dados_risco_afirm) | \| **RISCO_AFIRM** \| **AFIRM_FINANC** \| \|---\|---\| \| ID_AFIRM_FIANC \| ID_AFIRM_FIANC \| |
| [RISC_PROC_AFIRM](dados_risc_proc_afirm) | \| **RISC_PROC_AFIRM** \| **AFIRM_FINANC** \| \|---\|---\| \| ID_AFIRM_FIANC \| ID_AFIRM_FIANC \| |

# PRIOR_ENTIDADE

Caminho: Customização > Modelo de dados > Processo > PRIOR_ENTIDADE

Configuração de Fatores de Priorização para Entidade do sistema.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PRIORIZACAO_ENTIDADE** | Número sequencial gerado automaticamente pelo sistema para Identificar uma PriorizacaoEntidade | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada da PriorizacaoEntidade | varchar(500) | varchar(500) | Não |
| **CODIGO** | Código para recuperação de objetos reconhecidos pelo fabricante do software. | varchar(500) | varchar(500) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |

Tabelas que dependem de PRIOR_ENTIDADE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [FATOR_PRIORIDADE](dados_fator_prioridade) | \| **FATOR_PRIORIDADE** \| **PRIOR_ENTIDADE** \| \|---\|---\| \| ID_PRIORIZACAO_ENTIDADE \| ID_PRIORIZACAO_ENTIDADE \| |

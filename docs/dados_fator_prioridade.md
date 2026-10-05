# FATOR_PRIORIDADE

Caminho: Customização > Modelo de dados > Processo > FATOR_PRIORIDADE

Fator utilizado no cálculo de Prioridade

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_FATOR_PRIORIDADE** | Número sequencial gerado automaticamente pelo sistema para Identificar um FatorPrioridade | int | number(6,0) | Não |
| **ID_PRIORIZACAO_ENTIDADE** | Número sequencial gerado automaticamente pelo sistema para Identificar uma PriorizacaoEntidade | int | number(6,0) | Não |
| **SEQUENCIAL** | Sequencial de apresentação do Fator. | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do FatorPrioridade | varchar(500) | varchar(500) | Não |
| **VALOR** | Peso atribuído ao fator quando utilizado em cálculo de Prioridade de Ocorrências. | int | number(6,0) | Não |
| **ATIVO** | Quando inativo o Fator não é utilizado em Expressões para Cálculo e também não é visualizado como opção na configuração de Entidades que possuem suporte a cálculo de Prioridade. | char(3) | char(3) | Não |

Tabelas referenciadas por FATOR_PRIORIDADE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PRIOR_ENTIDADE](dados_prior_entidade) | \| **PRIOR_ENTIDADE** \| **FATOR_PRIORIDADE** \| \|---\|---\| \| ID_PRIORIZACAO_ENTIDADE \| ID_PRIORIZACAO_ENTIDADE \| |

Tabelas que dependem de FATOR_PRIORIDADE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SERVICO](dados_servico) | \| **SERVICO** \| **FATOR_PRIORIDADE** \| \|---\|---\| \| ID_FATOR_PRIORIDADE \| ID_FATOR_PRIORIDADE \| |
| [CLASSE_SERVICO](dados_classe_servico) | \| **CLASSE_SERVICO** \| **FATOR_PRIORIDADE** \| \|---\|---\| \| ID_FATOR_PRIORIDADE \| ID_FATOR_PRIORIDADE \| |
| [CLASSE_SUB_PROCESSO](dados_classe_sub_processo) | \| **CLASSE_SUB_PROCESSO** \| **FATOR_PRIORIDADE** \| \|---\|---\| \| ID_FATOR_PRIORIDADE \| ID_FATOR_PRIORIDADE \| |
| [PROCESSO](dados_processo) | \| **PROCESSO** \| **FATOR_PRIORIDADE** \| \|---\|---\| \| ID_FATOR_PRIORIDADE \| ID_FATOR_PRIORIDADE \| |

**Exemplo 1: join com a tabela PRIOR_ENTIDADE**

```
select FATOR_PRIORIDADE.*
from FATOR_PRIORIDADE, PRIOR_ENTIDADE
where FATOR_PRIORIDADE.ID_PRIORIZACAO_ENTIDADE = PRIOR_ENTIDADE.ID_PRIORIZACAO_ENTIDADE
```

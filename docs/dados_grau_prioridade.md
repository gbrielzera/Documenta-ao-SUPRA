# GRAU_PRIORIDADE

Caminho: Customização > Modelo de dados > Processo > GRAU_PRIORIDADE

Graus de Prioridade

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_GRAU_PRIORIDADE** | Número sequencial gerado automaticamente pelo sistema para Identificar um GrauPrioridade | int | number(6,0) | Não |
| **ID_METODO_PRIORIZACAO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Método de Priorização. | int | number(6,0) | Não |
| **SEQUENCIAL** | Número de Sequencia para o Nível | int | number(6,0) | Não |
| **LIM_SUP_CALCULO** | Limite superior para determinar seleção do Grau de Prioridade a partir do valor retornado pela Expressão de Cálculo do Método de Priorização. Para determinar o Grau de Prioridade é realizado primeiramente a ordenação dos Graus existentes com base no campo sequência. Em seguida os Graus são comparados com o Limite Superior e é selecionado aquele que apresentar o Limite Superior maior ou igual que o cálculo base. | int | number(6,0) | Sim |
| **DESCRICAO** | Descritivo associado ao Grau de Prioridade | varchar(500) | varchar(500) | Não |
| **COR_INDICADOR** | Cor associada ao nível de ANS. Na tela da de Fila de Ordens de Serviço é exibido um ícone nesta cor indicando o Nível atual de ANS. | varchar(250) | varchar(250) | Sim |

Tabelas referenciadas por GRAU_PRIORIDADE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [METODO_PRIORIZACAO](dados_metodo_priorizacao) | \| **METODO_PRIORIZACAO** \| **GRAU_PRIORIDADE** \| \|---\|---\| \| ID_METODO_PRIORIZACAO \| ID_METODO_PRIORIZACAO \| |

Tabelas que dependem de GRAU_PRIORIDADE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ORDEM_SERVICO](dados_ordem_servico) | \| **ORDEM_SERVICO** \| **GRAU_PRIORIDADE** \| \|---\|---\| \| ID_GRAU_PRIOR_SELEC \| ID_GRAU_PRIORIDADE \| |
| [ORDEM_SERVICO](dados_ordem_servico) | \| **ORDEM_SERVICO** \| **GRAU_PRIORIDADE** \| \|---\|---\| \| ID_GRAU_PRIOR_CALC \| ID_GRAU_PRIORIDADE \| |

**Exemplo 1: join com a tabela METODO_PRIORIZACAO**

```
select GRAU_PRIORIDADE.*
from GRAU_PRIORIDADE, METODO_PRIORIZACAO
where GRAU_PRIORIDADE.ID_METODO_PRIORIZACAO = METODO_PRIORIZACAO.ID_METODO_PRIORIZACAO
```

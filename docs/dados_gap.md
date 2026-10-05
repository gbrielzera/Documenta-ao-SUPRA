# GAP

Caminho: Customização > Modelo de dados > Processo > GAP

Gaps encontrado durante testes de Controles.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_OCORRENCIA** | Número sequencial gerado automaticamente pelo sistema para Identificar um Ocorrência | int | number(6,0) | Não |
| **SEQUENCIAL** | Sequencial | int | number(6,0) | Não |
| **RESUMO** | Resumo do Gap | text | clob | Não |
| **ID_CLASSE_GAP** | Identificador do(a) ClasseGAP associado(a) | int | number(6,0) | Não |
| **SITUACAO** | Situação do Gap | varchar(250) | varchar(250) | Não |
| **MOTIVO_CANCELA** | Motivo de cancelamento | varchar(500) | varchar(500) | Sim |
| **DEF_DESIGN** | O Controle não pode ser executado conforme descrito na documentação ou não foi possível alcançar seu objetivo. | char(3) | char(3) | Não |
| **DEF_FALTA_EVID** | Inexistência de documentação suporte que comprove a execução do Controle. | char(3) | char(3) | Não |
| **DEF_OPERACIONAL** | O Controle não opera da forma que foi desenhado ou a mesma pessoa que realiza o controle não tem autoridade ou qualificações necessárias. | char(3) | char(3) | Não |
| **TITULO** | Descrição sucinta sobre o Gap. É utilizado em cabeçalho de relatórios. | varchar(500) | varchar(500) | Não |
| **RECOMENDACAO** | Recomendação para resolução do Gap. | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por GAP

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_GAP](dados_classe_gap) | \| **CLASSE_GAP** \| **GAP** \| \|---\|---\| \| ID_CLASSE_GAP \| ID_CLASSE_GAP \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **GAP** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |

Tabelas que dependem de GAP

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ACAO_GAP](dados_acao_gap) | \| **ACAO_GAP** \| **GAP** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| \| SEQUENCIAL \| SEQUENCIAL \| |
| [RISCO_GAP](dados_risco_gap) | \| **RISCO_GAP** \| **GAP** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| \| SEQUENCIAL \| SEQUENCIAL \| |

**Exemplo 1: join com a tabela CLASSE_GAP**

```
select GAP.*, CLASSE_GAP.DESCRICAO
from GAP, CLASSE_GAP
where GAP.ID_CLASSE_GAP = CLASSE_GAP.ID_CLASSE_GAP
```

**Exemplo 2: join com a tabela OCORRENCIA**

```
select GAP.*
from GAP, OCORRENCIA
where GAP.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA
```

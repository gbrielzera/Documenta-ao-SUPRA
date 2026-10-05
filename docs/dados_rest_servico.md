# REST_SERVICO

Caminho: Customização > Modelo de dados > Processo > REST_SERVICO

Restringe a seleção de Serviços para uma determinado Tipo de Subprocesso (tipo de Solicitação). Esta restrição é visível no assistente de abertura de Ordens de Serviço da aplicação de Autoatendimento.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_RESTRICAO_SERVICO** | Número sequencial gerado automaticamente pelo sistema para Identificar um RestricaoServico | int | number(6,0) | Não |
| **ID_CLASSE_SUB_PROCESSO** | Identificador do Tipo de Subprocesso | int | number(6,0) | Não |
| **ID_SERVICO** | Identificador do Servico associado | int | number(6,0) | Sim |
| **ID_CLASSE_SERVICO** | Identificador do tipo de Serviço associado | int | number(6,0) | Não |

Tabelas referenciadas por REST_SERVICO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SERVICO](dados_servico) | \| **SERVICO** \| **REST_SERVICO** \| \|---\|---\| \| ID_SERVICO \| ID_SERVICO \| |
| [CLASSE_SERVICO](dados_classe_servico) | \| **CLASSE_SERVICO** \| **REST_SERVICO** \| \|---\|---\| \| ID_CLASSE_SERVICO \| ID_CLASSE_SERVICO \| |
| [CLASSE_SUB_PROCESSO](dados_classe_sub_processo) | \| **CLASSE_SUB_PROCESSO** \| **REST_SERVICO** \| \|---\|---\| \| ID_CLASSE_SUB_PROCESSO \| ID_CLASSE_SUB_PROCESSO \| |

**Exemplo 1: join com a tabela SERVICO**

```
select REST_SERVICO.*, SERVICO.DESCRICAO
from REST_SERVICO left outer join SERVICO on REST_SERVICO.ID_SERVICO = SERVICO.ID_SERVICO
```

**Exemplo 2: join com a tabela CLASSE_SUB_PROCESSO**

```
select REST_SERVICO.*
from REST_SERVICO, CLASSE_SUB_PROCESSO
where REST_SERVICO.ID_CLASSE_SUB_PROCESSO = CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO
```

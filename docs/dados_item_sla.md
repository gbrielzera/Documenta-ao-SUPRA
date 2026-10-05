# ITEM_SLA

Caminho: Customização > Modelo de dados > Recurso > ITEM_SLA

Conjunto prazos de atendimento de uma Ordem de Serviço com respectivos critérios de aplicação.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ITEM_SLA** | Número sequencial gerado automaticamente pelo sistema para Identificar um ItemSLA | int | number(6,0) | Não |
| **ID_SLA** | Número sequencial gerado automaticamente pelo sistema para Identificar um AcordoNivelServico | int | number(6,0) | Não |
| **ID_CLASSE_SERVICO** | Identificador do Tipo de Serviço associado | int | number(6,0) | Sim |
| **ID_SERVICO** | Identificador do Servico associado | int | number(6,0) | Sim |
| **ID_PERFIL_CLIENTE** | Identificador do Perfil de cliente | int | number(6,0) | Sim |
| **TEMPO_ATEND** | Script que define o tempo de atendimento, o resultado da execução do script deve ser um número que representa o número de minutos | text | clob | Não |
| **ID_GRAU_PRIORIDADE** | Identificador do Grau de Prioridade | int | number(6,0) | Sim |

Tabelas referenciadas por ITEM_SLA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_SERVICO](dados_classe_servico) | \| **CLASSE_SERVICO** \| **ITEM_SLA** \| \|---\|---\| \| ID_CLASSE_SERVICO \| ID_CLASSE_SERVICO \| |
| [SERVICO](dados_servico) | \| **SERVICO** \| **ITEM_SLA** \| \|---\|---\| \| ID_SERVICO \| ID_SERVICO \| |
| [PERFIL_CLIENTE](dados_perfil_cliente) | \| **PERFIL_CLIENTE** \| **ITEM_SLA** \| \|---\|---\| \| ID_PERFIL_CLIENTE \| ID_PERFIL_CLIENTE \| |
| [GRAU_PRIORIDADE](dados_grau_prioridade) | \| **GRAU_PRIORIDADE** \| **ITEM_SLA** \| \|---\|---\| \| ID_GRAU_PRIORIDADE \| ID_GRAU_PRIORIDADE \| |
| [SLA](dados_sla) | \| **SLA** \| **ITEM_SLA** \| \|---\|---\| \| ID_SLA \| ID_SLA \| |

Tabelas que dependem de ITEM_SLA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [EXCECAO_SLA](dados_excecao_sla) | \| **EXCECAO_SLA** \| **ITEM_SLA** \| \|---\|---\| \| ID_ITEM_SLA \| ID_ITEM_SLA \| |

**Exemplo 1: join com a tabela PERFIL_CLIENTE**

```
select ITEM_SLA.*, PERFIL_CLIENTE.DESCRICAO
from ITEM_SLA left outer join PERFIL_CLIENTE on ITEM_SLA.ID_PERFIL_CLIENTE = PERFIL_CLIENTE.ID_PERFIL_CLIENTE
```

**Exemplo 2: join com a tabela SLA**

```
select ITEM_SLA.*
from ITEM_SLA, SLA
where ITEM_SLA.ID_SLA = SLA.ID_SLA
```

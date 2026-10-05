# SLA_OS

Caminho: Customização > Modelo de dados > Processo > SLA_OS

Acordo de Nível de Serviço selecionado para Ordem de Serviço

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_OCORRENCIA** | Identificador da Ordem de Serviço | int | number(6,0) | Não |
| **ID_NIVEL_SLA** | Identificador da NivelSLA associada | int | number(6,0) | Não |
| **TEMPO** | Tempo em minutos para Nível de Serviço | int | number(6,0) | Não |
| **REFERENCIA** | Referência sobre o cálculo do Nível de Serviço | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por SLA_OS

| **Tabela** | **Colunas de ligação** |
|---|---|
| [NIVEL_SLA](dados_nivel_sla) | \| **NIVEL_SLA** \| **SLA_OS** \| \|---\|---\| \| ID_NIVEL_SLA \| ID_NIVEL_SLA \| |
| [ORDEM_SERVICO](dados_ordem_servico) | \| **ORDEM_SERVICO** \| **SLA_OS** \| \|---\|---\| \|  \| ID_OCORRENCIA \| |

**Exemplo 1: join com a tabela NIVEL_SLA**

```
select SLA_OS.*, NIVEL_SLA.SEQUENCIAL
from SLA_OS, NIVEL_SLA
where SLA_OS.ID_NIVEL_SLA = NIVEL_SLA.ID_NIVEL_SLA
```

**Exemplo 2: join com a tabela ORDEM_SERVICO**

```
select SLA_OS.*
from SLA_OS, ORDEM_SERVICO
where SLA_OS.ID_OCORRENCIA = ORDEM_SERVICO.
```

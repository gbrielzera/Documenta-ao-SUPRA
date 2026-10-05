# FLUXO_SEQUENCIA

Caminho: Customização > Modelo de dados > Processo > FLUXO_SEQUENCIA

Fluxo de Sequência entre duas Atividades

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_FLUXO_SEQUENCIA** | Número sequencial gerado automaticamente pelo sistema para Identificar um FluxoSequencia | int | number(6,0) | Não |
| **ID_ATIVIDADE_ORIGEM** | Atividade de Origem | int | number(6,0) | Sim |
| **ID_ATIVIDADE_DESTINO** | Atividade de Destino associada | int | number(6,0) | Não |
| **ACOP_ORIGEM** | Indica que um Evento está acoplado na atividade de origem. Válido somente para eventos intermediários. No caso de evento intermediário com este valor falso o evento significa um atraso programado no processo. | char(3) | char(3) | Não |

Tabelas referenciadas por FLUXO_SEQUENCIA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **FLUXO_SEQUENCIA** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE_DESTINO \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **FLUXO_SEQUENCIA** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE_ORIGEM \| |

**Exemplo 1: join com a tabela ATIVIDADE**

```
select FLUXO_SEQUENCIA.*
from FLUXO_SEQUENCIA, ATIVIDADE
where FLUXO_SEQUENCIA.ID_ATIVIDADE_ORIGEM = ATIVIDADE.ID_ATIVIDADE
```

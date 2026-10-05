# MOTIVO_APONTAMENTO

Caminho: Customização > Modelo de dados > Processo > MOTIVO_APONTAMENTO

Motivo Apontamento

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **SEQUENCIAL** | Sequencial gerado para identificar um Motivo de Apontamento | int | number(6,0) | Não |
| **DESCRICAO** | Descrição | varchar(500) | varchar(500) | Não |
| **CODIGO** | Código do motivo | varchar(500) | varchar(500) | Não |
| **ID_APONTAMENTO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Apontamento | int | number(6,0) | Não |

Tabelas referenciadas por MOTIVO_APONTAMENTO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [APONTAMENTO](dados_apontamento) | \| **APONTAMENTO** \| **MOTIVO_APONTAMENTO** \| \|---\|---\| \| ID_APONTAMENTO \| ID_APONTAMENTO \| |

**Exemplo 1: join com a tabela APONTAMENTO**

```
select MOTIVO_APONTAMENTO.*
from MOTIVO_APONTAMENTO, APONTAMENTO
where MOTIVO_APONTAMENTO.ID_APONTAMENTO = APONTAMENTO.ID_APONTAMENTO
```

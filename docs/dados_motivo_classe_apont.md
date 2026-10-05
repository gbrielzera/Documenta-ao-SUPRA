# MOTIVO_CLASSE_APONT

Caminho: Customização > Modelo de dados > Processo > MOTIVO_CLASSE_APONT

Motivos para Classe de Apontamento

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CLASSE_APONTAMENTO** | Número sequencial gerado automaticamente pelo sistema para Identificar um ClasseApontamento | int | number(6,0) | Não |
| **CODIGO** | Código do Motivo | varchar(500) | varchar(500) | Não |
| **DESCRICAO** | Descrição | varchar(500) | varchar(500) | Não |

Tabelas referenciadas por MOTIVO_CLASSE_APONT

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_APONTAMENTO](dados_classe_apontamento) | \| **CLASSE_APONTAMENTO** \| **MOTIVO_CLASSE_APONT** \| \|---\|---\| \| ID_CLASSE_APONTAMENTO \| ID_CLASSE_APONTAMENTO \| |

**Exemplo 1: join com a tabela CLASSE_APONTAMENTO**

```
select MOTIVO_CLASSE_APONT.*
from MOTIVO_CLASSE_APONT, CLASSE_APONTAMENTO
where MOTIVO_CLASSE_APONT.ID_CLASSE_APONTAMENTO = CLASSE_APONTAMENTO.ID_CLASSE_APONTAMENTO
```

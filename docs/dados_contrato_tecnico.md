# CONTRATO_TECNICO

Caminho: Customização > Modelo de dados > Recurso > CONTRATO_TECNICO

Grupos de trabalho onde estão lotados os Solucionadores correspondentes ao tipo de recurso do contrato.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_RECURSO_APLICADO** | Identificador do Recurso Aplicado | int | number(6,0) | Não |
| **ID_GRUPO_TRABALHO** | Identificador do GrupoTrabalho associado | int | number(6,0) | Não |

Tabelas referenciadas por CONTRATO_TECNICO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [GRUPO_TRABALHO](dados_grupo_trabalho) | \| **GRUPO_TRABALHO** \| **CONTRATO_TECNICO** \| \|---\|---\| \| ID_GRUPO_TRABALHO \| ID_GRUPO_TRABALHO \| |
| [RECURSO_APLICADO](dados_recurso_aplicado) | \| **RECURSO_APLICADO** \| **CONTRATO_TECNICO** \| \|---\|---\| \| ID_RECURSO_APLICADO \| ID_RECURSO_APLICADO \| |

**Exemplo 1: join com a tabela GRUPO_TRABALHO**

```
select CONTRATO_TECNICO.*, GRUPO_TRABALHO.DESCRICAO
from CONTRATO_TECNICO, GRUPO_TRABALHO
where CONTRATO_TECNICO.ID_GRUPO_TRABALHO = GRUPO_TRABALHO.ID_GRUPO_TRABALHO
```

**Exemplo 2: join com a tabela RECURSO_APLICADO**

```
select CONTRATO_TECNICO.*
from CONTRATO_TECNICO, RECURSO_APLICADO
where CONTRATO_TECNICO.ID_RECURSO_APLICADO = RECURSO_APLICADO.ID_RECURSO_APLICADO
```

# CLASSE_SUBPROC_INDICADOR

Caminho: Customização > Modelo de dados > Processo > CLASSE_SUBPROC_INDICADOR

Tipos de Subprocessos que serão utilizados como filtro das ocorrências utilizados no cálculo do indicador

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_INDICADOR** | Número sequencial gerado automaticamente pelo sistema para Identificar um Indicador | int | number(6,0) | Não |
| **ID_CLASSE_SUB_PROCESSO** | Identificador do Tipo de Subprocesso associado | int | number(6,0) | Não |

Tabelas referenciadas por CLASSE_SUBPROC_INDICADOR

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_SUB_PROCESSO](dados_classe_sub_processo) | \| **CLASSE_SUB_PROCESSO** \| **CLASSE_SUBPROC_INDICADOR** \| \|---\|---\| \| ID_CLASSE_SUB_PROCESSO \| ID_CLASSE_SUB_PROCESSO \| |
| [INDICADOR](dados_indicador) | \| **INDICADOR** \| **CLASSE_SUBPROC_INDICADOR** \| \|---\|---\| \| ID_INDICADOR \| ID_INDICADOR \| |

**Exemplo 1: join com a tabela CLASSE_SUB_PROCESSO**

```
select CLASSE_SUBPROC_INDICADOR.*, CLASSE_SUB_PROCESSO.DESCRICAO
from CLASSE_SUBPROC_INDICADOR, CLASSE_SUB_PROCESSO
where CLASSE_SUBPROC_INDICADOR.ID_CLASSE_SUB_PROCESSO = CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO
```

**Exemplo 2: join com a tabela INDICADOR**

```
select CLASSE_SUBPROC_INDICADOR.*
from CLASSE_SUBPROC_INDICADOR, INDICADOR
where CLASSE_SUBPROC_INDICADOR.ID_INDICADOR = INDICADOR.ID_INDICADOR
```

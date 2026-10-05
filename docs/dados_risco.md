# RISCO

Caminho: Customização > Modelo de dados > Processo > RISCO

Risco cadastrado na biblioteca de Riscos

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_RISCO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Risco | int | number(6,0) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do Risco | varchar(500) | varchar(500) | Não |
| **ID_CATEGORIA_RISCO** | Identificador do CategoriaRisco associado | int | number(6,0) | Não |
| **ID_AREA_RISCO** | Identificador do AreaRisco associado | int | number(6,0) | Não |

Tabelas referenciadas por RISCO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CATEGORIA_RISCO](dados_categoria_risco) | \| **CATEGORIA_RISCO** \| **RISCO** \| \|---\|---\| \| ID_CATEGORIA_RISCO \| ID_CATEGORIA_RISCO \| |
| [AREA_RISCO](dados_area_risco) | \| **AREA_RISCO** \| **RISCO** \| \|---\|---\| \| ID_AREA_RISCO \| ID_AREA_RISCO \| |

Tabelas que dependem de RISCO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [RISCO_CLASSE_CONTR](dados_risco_classe_contr) | \| **RISCO_CLASSE_CONTR** \| **RISCO** \| \|---\|---\| \| ID_RISCO \| ID_RISCO \| |
| [RISCO_PROCESSO](dados_risco_processo) | \| **RISCO_PROCESSO** \| **RISCO** \| \|---\|---\| \| ID_RISCO \| ID_RISCO \| |
| [RISCO_AFIRM](dados_risco_afirm) | \| **RISCO_AFIRM** \| **RISCO** \| \|---\|---\| \| ID_RISCO \| ID_RISCO \| |

**Exemplo 1: join com a tabela CATEGORIA_RISCO**

```
select RISCO.*, CATEGORIA_RISCO.DESCRICAO
from RISCO, CATEGORIA_RISCO
where RISCO.ID_CATEGORIA_RISCO = CATEGORIA_RISCO.ID_CATEGORIA_RISCO
```

**Exemplo 2: join com a tabela AREA_RISCO**

```
select RISCO.*, AREA_RISCO.DESCRICAO
from RISCO, AREA_RISCO
where RISCO.ID_AREA_RISCO = AREA_RISCO.ID_AREA_RISCO
```

# CLASSE_CONTROLE

Caminho: Customização > Modelo de dados > Processo > CLASSE_CONTROLE

Classificação de Controles

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CLASSE_CONTROLE** | Número sequencial gerado automaticamente pelo sistema para Identificar um ClasseControle | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do ClasseControle | varchar(500) | varchar(500) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **ID_CATEGORIA_CONTROLE** | Identificador da Categoria | int | number(6,0) | Não |
| **ID_AREA** | Identificador da Área | int | number(6,0) | Não |

Tabelas referenciadas por CLASSE_CONTROLE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CATEGORIA_RISCO](dados_categoria_risco) | \| **CATEGORIA_RISCO** \| **CLASSE_CONTROLE** \| \|---\|---\| \| ID_CATEGORIA_RISCO \| ID_CATEGORIA_CONTROLE \| |
| [AREA_RISCO](dados_area_risco) | \| **AREA_RISCO** \| **CLASSE_CONTROLE** \| \|---\|---\| \| ID_AREA_RISCO \| ID_AREA \| |

Tabelas que dependem de CLASSE_CONTROLE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CONTROLE](dados_controle) | \| **CONTROLE** \| **CLASSE_CONTROLE** \| \|---\|---\| \| ID_CLASSE_CONTROLE \| ID_CLASSE_CONTROLE \| |
| [RISCO_CLASSE_CONTR](dados_risco_classe_contr) | \| **RISCO_CLASSE_CONTR** \| **CLASSE_CONTROLE** \| \|---\|---\| \| ID_CLASSE_CONTROLE \| ID_CLASSE_CONTROLE \| |

**Exemplo 1: join com a tabela CATEGORIA_RISCO**

```
select CLASSE_CONTROLE.*, CATEGORIA_RISCO.DESCRICAO
from CLASSE_CONTROLE, CATEGORIA_RISCO
where CLASSE_CONTROLE.ID_CATEGORIA_CONTROLE = CATEGORIA_RISCO.ID_CATEGORIA_RISCO
```

**Exemplo 2: join com a tabela AREA_RISCO**

```
select CLASSE_CONTROLE.*, AREA_RISCO.DESCRICAO
from CLASSE_CONTROLE, AREA_RISCO
where CLASSE_CONTROLE.ID_AREA = AREA_RISCO.ID_AREA_RISCO
```

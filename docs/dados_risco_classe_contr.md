# RISCO_CLASSE_CONTR

Caminho: Customização > Modelo de dados > Processo > RISCO_CLASSE_CONTR

Riscos que são mitigados por um Controle

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CLASSE_CONTROLE** | Número sequencial gerado automaticamente pelo sistema para Identificar um ClasseControle | int | number(6,0) | Não |
| **ID_RISCO** | Identificador do Risco associado | int | number(6,0) | Não |

Tabelas referenciadas por RISCO_CLASSE_CONTR

| **Tabela** | **Colunas de ligação** |
|---|---|
| [RISCO](dados_risco) | \| **RISCO** \| **RISCO_CLASSE_CONTR** \| \|---\|---\| \| ID_RISCO \| ID_RISCO \| |
| [CLASSE_CONTROLE](dados_classe_controle) | \| **CLASSE_CONTROLE** \| **RISCO_CLASSE_CONTR** \| \|---\|---\| \| ID_CLASSE_CONTROLE \| ID_CLASSE_CONTROLE \| |

**Exemplo 1: join com a tabela RISCO**

```
select RISCO_CLASSE_CONTR.*, RISCO.DESCRICAO
from RISCO_CLASSE_CONTR, RISCO
where RISCO_CLASSE_CONTR.ID_RISCO = RISCO.ID_RISCO
```

**Exemplo 2: join com a tabela CLASSE_CONTROLE**

```
select RISCO_CLASSE_CONTR.*
from RISCO_CLASSE_CONTR, CLASSE_CONTROLE
where RISCO_CLASSE_CONTR.ID_CLASSE_CONTROLE = CLASSE_CONTROLE.ID_CLASSE_CONTROLE
```

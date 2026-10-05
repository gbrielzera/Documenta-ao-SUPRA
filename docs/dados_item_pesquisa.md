# ITEM_PESQUISA

Caminho: Customização > Modelo de dados > Processo > ITEM_PESQUISA

Item a ser avaliado em uma Pesquisa

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_QUESTAO** | Identificador da Questão associada | int | number(6,0) | Não |
| **ID_PESQUISA** | Identificador da Pesquisa | int | number(6,0) | Não |
| **ESCORE** | Valor atribuido ao Indicador como resposta a Pesquisa de Satisfação | int | number(6,0) | Sim |

Tabelas referenciadas por ITEM_PESQUISA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [QUESTAO_PESQUISA](dados_questao_pesquisa) | \| **QUESTAO_PESQUISA** \| **ITEM_PESQUISA** \| \|---\|---\| \| ID_QUESTAO \| ID_QUESTAO \| |
| [PESQUISA](dados_pesquisa) | \| **PESQUISA** \| **ITEM_PESQUISA** \| \|---\|---\| \| ID_PESQUISA \| ID_PESQUISA \| |

**Exemplo 1: join com a tabela QUESTAO_PESQUISA**

```
select ITEM_PESQUISA.*, QUESTAO_PESQUISA.DESCRICAO
from ITEM_PESQUISA, QUESTAO_PESQUISA
where ITEM_PESQUISA.ID_QUESTAO = QUESTAO_PESQUISA.ID_QUESTAO
```

**Exemplo 2: join com a tabela PESQUISA**

```
select ITEM_PESQUISA.*
from ITEM_PESQUISA, PESQUISA
where ITEM_PESQUISA.ID_PESQUISA = PESQUISA.ID_PESQUISA
```

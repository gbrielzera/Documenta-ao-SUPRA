# PAPEL_COMP

Caminho: Customização > Modelo de dados > Processo > PAPEL_COMP

Permite que um Papel seja definido pela composição de um ou mais Papéis. No primeiro caso ocorre um simples redirecionamento no instante de cálculo de Atores enquanto no segundo são retornados todos os Atores (soma) de todos os Papéis configurados na composição. A rotina de cálculo de Atores possui função de recursividade, ou seja, se o Papel A é composto por B e C, e B por sua vez composto por D e E, então o resultado total de A é igual a soma de C, D e E.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PAPEL_CLASSE_NEGOCIO** | Identificador do Papel de Classe de Negócio composto | int | number(6,0) | Não |
| **ID_PAPEL_COMPOSICAO** | Identificador do Papel utilizado na Composição | int | number(6,0) | Não |
| **PRIORIDADE** | Os papéis da composição serão ordenadas por Prioridade no sentido ascendente e o processamento será interrompido assim que o primeiro agrupamento da Prioridade retornar no mínimo uma pessoa. | int | number(6,0) | Não |

Tabelas referenciadas por PAPEL_COMP

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio) | \| **PAPEL_CLASSE_NEGOCIO** \| **PAPEL_COMP** \| \|---\|---\| \| ID_PAPEL_CLASSE_NEGOCIO \| ID_PAPEL_COMPOSICAO \| |
| [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio) | \| **PAPEL_CLASSE_NEGOCIO** \| **PAPEL_COMP** \| \|---\|---\| \| ID_PAPEL_CLASSE_NEGOCIO \| ID_PAPEL_CLASSE_NEGOCIO \| |

**Exemplo 1: join com a tabela PAPEL_CLASSE_NEGOCIO**

```
select PAPEL_COMP.*, PAPEL_CLASSE_NEGOCIO.NOME
from PAPEL_COMP, PAPEL_CLASSE_NEGOCIO
where PAPEL_COMP.ID_PAPEL_COMPOSICAO = PAPEL_CLASSE_NEGOCIO.ID_PAPEL_CLASSE_NEGOCIO
```

**Exemplo 2: join com a tabela PAPEL_CLASSE_NEGOCIO**

```
select PAPEL_COMP.*
from PAPEL_COMP, PAPEL_CLASSE_NEGOCIO
where PAPEL_COMP.ID_PAPEL_CLASSE_NEGOCIO = PAPEL_CLASSE_NEGOCIO.ID_PAPEL_CLASSE_NEGOCIO
```

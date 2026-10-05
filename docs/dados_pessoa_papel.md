# PESSOA_PAPEL

Caminho: Customização > Modelo de dados > Processo > PESSOA_PAPEL

Pessoas relacionadas para recuperação. A seleção destas pessoas ainda está condicionada a configuração de parâmetros complementadores no papel.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PAPEL_CLASSE_NEGOCIO** | Identificador do Papel proprietário da regra | int | number(6,0) | Não |
| **ID_PESSOA** | Identificador da pessoa relacionada | int | number(6,0) | Não |
| **CONS_PERIODOS_UTEIS** | A pessoa ou fila só será recuperada se o seu cadastro de períodos úteis possuir um período que contém a data/hora corrente do sistema. Se a pessoa ou fila não possuir um calendário ou este não possuir ainda definição de períodos úteis, então esta regra será ignorada considerando então que a mesma possui disponibilidade 24x7. | char(3) | char(3) | Não |
| **SOMENTE_MESMA_UND** | A pessoa só será incluída na recuperação se estiver localizada na mesma Unidade de Negócio do Cliente da ocorrência. Se o Cliente não possuir uma localidade definida então esta regra será ignorada. | char(3) | char(3) | Não |
| **PRIORIDADE** | As regras por Pessoas/filas serão ordenadas por Prioridade no sentido ascendente e o processamento será interrompido assim que o primeiro agrupamento da Prioridade retornar no mínimo uma pessoa ou fila. Durante o processamento de cada agrupamento serão levados em consideração os parâmetros de períodos úteis e Unidade de negócio. | int | number(6,0) | Não |

Tabelas referenciadas por PESSOA_PAPEL

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **PESSOA_PAPEL** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA \| |
| [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio) | \| **PAPEL_CLASSE_NEGOCIO** \| **PESSOA_PAPEL** \| \|---\|---\| \| ID_PAPEL_CLASSE_NEGOCIO \| ID_PAPEL_CLASSE_NEGOCIO \| |

**Exemplo 1: join com a tabela PAPEL_CLASSE_NEGOCIO**

```
select PESSOA_PAPEL.*
from PESSOA_PAPEL, PAPEL_CLASSE_NEGOCIO
where PESSOA_PAPEL.ID_PAPEL_CLASSE_NEGOCIO = PAPEL_CLASSE_NEGOCIO.ID_PAPEL_CLASSE_NEGOCIO
```

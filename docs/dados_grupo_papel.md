# GRUPO_PAPEL

Caminho: Customização > Modelo de dados > Processo > GRUPO_PAPEL

Grupos de Trabalho relacionados em um papel para recuperação de atores do tipo solucionador.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PAPEL_CLASSE_NEGOCIO** | Papel de processo proprietário da regra por Grupo de Trabalho | int | number(6,0) | Não |
| **ID_GRUPO_TRABALHO** | Identificador do Grupo Trabalho associado | int | number(6,0) | Não |
| **INCLUIR_SUB_NIVEIS** | Indica que grupos filhos devem ser incluídos na recuperação. | char(3) | char(3) | Não |
| **PRIORIDADE** | As regras por Grupo de Trabalho serão ordenadas por Prioridade no sentido ascendente e o processamento será interrompido assim que o primeiro agrupamento da Prioridade retornar no mínimo uma pessoa. | int | number(6,0) | Não |
| **CONS_PERIODOS_UTEIS** | Na recuperação das pessoas deve ser levando em consideração o cadastro de períodos úteis do calendário da pessoa versus a data/hora corrente do sistema. Se um solucionador recuperado não possuir um calendário ou se possui um calendário sem definição de períodos úteis, então esta regra será ignorada e será considerado que a pessoa possui disponibilidade 24x7. | char(3) | char(3) | Não |
| **SOMENTE_MESMA_UND** | São incluídas na recuperação apenas pessoas que estão localizadas na mesma Unidade de Negócio do Cliente da ocorrência. Se o Cliente não possuir uma localidade definida então esta regra será ignorada. | char(3) | char(3) | Não |
| **REGRA_RECUPERA** | Define quais colaboradores do grupo devem ser recuperados | varchar(250) | varchar(250) | Não |

Tabelas referenciadas por GRUPO_PAPEL

| **Tabela** | **Colunas de ligação** |
|---|---|
| [GRUPO_TRABALHO](dados_grupo_trabalho) | \| **GRUPO_TRABALHO** \| **GRUPO_PAPEL** \| \|---\|---\| \| ID_GRUPO_TRABALHO \| ID_GRUPO_TRABALHO \| |
| [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio) | \| **PAPEL_CLASSE_NEGOCIO** \| **GRUPO_PAPEL** \| \|---\|---\| \| ID_PAPEL_CLASSE_NEGOCIO \| ID_PAPEL_CLASSE_NEGOCIO \| |

**Exemplo 1: join com a tabela PAPEL_CLASSE_NEGOCIO**

```
select GRUPO_PAPEL.*
from GRUPO_PAPEL, PAPEL_CLASSE_NEGOCIO
where GRUPO_PAPEL.ID_PAPEL_CLASSE_NEGOCIO = PAPEL_CLASSE_NEGOCIO.ID_PAPEL_CLASSE_NEGOCIO
```

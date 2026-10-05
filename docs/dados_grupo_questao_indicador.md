# GRUPO_QUESTAO_INDICADOR

Caminho: Customização > Modelo de dados > Processo > GRUPO_QUESTAO_INDICADOR

Grupos de Questões para Filtro durante a Apuração de Pesquisas de Satisfação.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_INDICADOR** | Número sequencial gerado automaticamente pelo sistema para Identificar um Indicador | int | number(6,0) | Não |
| **ID_GRUPO_QUESTAO** | Identificador do GrupoQuestao associado | int | number(6,0) | Não |
| **ID_QUESTAO** | Identificador da QuestaoPesquisa associada | int | number(6,0) | Sim |

Tabelas referenciadas por GRUPO_QUESTAO_INDICADOR

| **Tabela** | **Colunas de ligação** |
|---|---|
| [GRUPO_QUESTAO](dados_grupo_questao) | \| **GRUPO_QUESTAO** \| **GRUPO_QUESTAO_INDICADOR** \| \|---\|---\| \| ID_GRUPO_QUESTAO \| ID_GRUPO_QUESTAO \| |
| [QUESTAO_PESQUISA](dados_questao_pesquisa) | \| **QUESTAO_PESQUISA** \| **GRUPO_QUESTAO_INDICADOR** \| \|---\|---\| \| ID_QUESTAO \| ID_QUESTAO \| |
| [INDICADOR](dados_indicador) | \| **INDICADOR** \| **GRUPO_QUESTAO_INDICADOR** \| \|---\|---\| \| ID_INDICADOR \| ID_INDICADOR \| |

**Exemplo 1: join com a tabela GRUPO_QUESTAO**

```
select GRUPO_QUESTAO_INDICADOR.*, GRUPO_QUESTAO.DESCRICAO
from GRUPO_QUESTAO_INDICADOR, GRUPO_QUESTAO
where GRUPO_QUESTAO_INDICADOR.ID_GRUPO_QUESTAO = GRUPO_QUESTAO.ID_GRUPO_QUESTAO
```

**Exemplo 2: join com a tabela QUESTAO_PESQUISA**

```
select GRUPO_QUESTAO_INDICADOR.*, QUESTAO_PESQUISA.DESCRICAO
from GRUPO_QUESTAO_INDICADOR left outer join QUESTAO_PESQUISA on GRUPO_QUESTAO_INDICADOR.ID_QUESTAO = QUESTAO_PESQUISA.ID_QUESTAO
```

**Exemplo 3: join com a tabela INDICADOR**

```
select GRUPO_QUESTAO_INDICADOR.*
from GRUPO_QUESTAO_INDICADOR, INDICADOR
where GRUPO_QUESTAO_INDICADOR.ID_INDICADOR = INDICADOR.ID_INDICADOR
```

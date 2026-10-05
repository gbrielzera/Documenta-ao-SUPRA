# QUESTAO_PESQUISA

Caminho: Customização > Modelo de dados > Processo > QUESTAO_PESQUISA

Uma Questão de Pesquisa pode ser utilizada na elaboração de Pesquisas de Satisfação enviadas para Clientes após a finalização de uma Ordem de Serviço.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_QUESTAO** | Identificador | int | number(6,0) | Não |
| **TEXTO** | Texto apresentado para o Cliente no momento de aplicação da Pesquisa de Satisfação | varchar(500) | varchar(500) | Não |
| **DESCRICAO** | Descrição do Indicador | varchar(500) | varchar(500) | Não |
| **ATIVO** | Indica que o Indicador está ativo. Somente Indicadores ativos são exibidos na Pesquisa de Satisfação | char(3) | char(3) | Não |
| **ID_GRUPO_QUESTAO** | Identificador do GrupoQuestao associado | int | number(6,0) | Não |

Tabelas referenciadas por QUESTAO_PESQUISA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [GRUPO_QUESTAO](dados_grupo_questao) | \| **GRUPO_QUESTAO** \| **QUESTAO_PESQUISA** \| \|---\|---\| \| ID_GRUPO_QUESTAO \| ID_GRUPO_QUESTAO \| |

Tabelas que dependem de QUESTAO_PESQUISA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM_PESQUISA](dados_item_pesquisa) | \| **ITEM_PESQUISA** \| **QUESTAO_PESQUISA** \| \|---\|---\| \| ID_QUESTAO \| ID_QUESTAO \| |
| [QUESTAO_CLASSE_PESQ](dados_questao_classe_pesq) | \| **QUESTAO_CLASSE_PESQ** \| **QUESTAO_PESQUISA** \| \|---\|---\| \| ID_QUESTAO \| ID_QUESTAO \| |
| [PESQUISA](dados_pesquisa) | \| **PESQUISA** \| **QUESTAO_PESQUISA** \| \|---\|---\| \| ID_QUESTAO_GERAL \| ID_QUESTAO \| |
| [CLASSE_PESQ_SATISF](dados_classe_pesq_satisf) | \| **CLASSE_PESQ_SATISF** \| **QUESTAO_PESQUISA** \| \|---\|---\| \| ID_QUESTAO_GERAL \| ID_QUESTAO \| |
| [GRUPO_QUESTAO_INDICADOR](dados_grupo_questao_indicador) | \| **GRUPO_QUESTAO_INDICADOR** \| **QUESTAO_PESQUISA** \| \|---\|---\| \| ID_QUESTAO \| ID_QUESTAO \| |

**Exemplo 1: join com a tabela GRUPO_QUESTAO**

```
select QUESTAO_PESQUISA.*, GRUPO_QUESTAO.DESCRICAO
from QUESTAO_PESQUISA, GRUPO_QUESTAO
where QUESTAO_PESQUISA.ID_GRUPO_QUESTAO = GRUPO_QUESTAO.ID_GRUPO_QUESTAO
```

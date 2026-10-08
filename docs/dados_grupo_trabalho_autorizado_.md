# GRUPO_TRABALHO_AUTORIZADO

Caminho: GRUPO_TRABALHO_AUTORIZADO

Grupos de Trabalho que estão autorizados a visualizar o resultado da apuração de indicadores.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PLANO_GESTAO** | Número sequencial gerado automaticamente pelo sistema para Identificar um PlanoGestao | int | number(6,0) | Não |
| **ID_GRUPO_TRABALHO** | Identificador do GrupoTrabalho associado | int | number(6,0) | Não |
| **INCLUI_SUB_NIVEIS** | Permite que sub-grupos acessem o Plano de Gestão. | char(3) | char(3) | Não |

Tabelas referenciadas por GRUPO_TRABALHO_AUTORIZADO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [GRUPO_TRABALHO](dados_grupo_trabalho) | \| **GRUPO_TRABALHO** \| **GRUPO_TRABALHO_AUTORIZADO** \| \|---\|---\| \| ID_GRUPO_TRABALHO \| ID_GRUPO_TRABALHO \| |
| [PLANO_GESTAO](dados_plano_gestao) | \| **PLANO_GESTAO** \| **GRUPO_TRABALHO_AUTORIZADO** \| \|---\|---\| \| ID_PLANO_GESTAO \| ID_PLANO_GESTAO \| |

**Exemplo 1: join com a tabela PLANO_GESTAO**

```
select GRUPO_TRABALHO_AUTORIZADO.*
from GRUPO_TRABALHO_AUTORIZADO, PLANO_GESTAO
where GRUPO_TRABALHO_AUTORIZADO.ID_PLANO_GESTAO = PLANO_GESTAO.ID_PLANO_GESTAO
```

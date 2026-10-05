# ENV_GRUPO

Caminho: Customização > Modelo de dados > Processo > ENV_GRUPO

Os Grupos de Trabalho envolvidos (incluindo seus sub-níveis) identificam todas as equipes que atuam Macroprocesso. A definição de Grupos envolvidos pode interferir na autorização para visualização de Ocorrências. A abertura de ocorrências de subprocessos contidos no Macroprocesso também está limitada a solucionadores lotados no grupo informado ou um dos seus sub-níveis.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_MACRO_PROCESSO** | Número sequencial gerado automaticamente pelo sistema para Identificar um MacroProcesso | int | number(6,0) | Não |
| **ID_GRUPO_TRABALHO** | Identificador do Grupo de Trabalho envolvido | int | number(6,0) | Não |

Tabelas referenciadas por ENV_GRUPO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [GRUPO_TRABALHO](dados_grupo_trabalho) | \| **GRUPO_TRABALHO** \| **ENV_GRUPO** \| \|---\|---\| \| ID_GRUPO_TRABALHO \| ID_GRUPO_TRABALHO \| |
| [MACRO_PROCESSO](dados_macro_processo) | \| **MACRO_PROCESSO** \| **ENV_GRUPO** \| \|---\|---\| \| ID_MACRO_PROCESSO \| ID_MACRO_PROCESSO \| |

**Exemplo 1: join com a tabela MACRO_PROCESSO**

```
select ENV_GRUPO.*
from ENV_GRUPO, MACRO_PROCESSO
where ENV_GRUPO.ID_MACRO_PROCESSO = MACRO_PROCESSO.ID_MACRO_PROCESSO
```

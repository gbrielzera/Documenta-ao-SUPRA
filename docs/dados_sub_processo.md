# SUB_PROCESSO

Caminho: Customização > Modelo de dados > Processo > SUB_PROCESSO

Subprocesso

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_SUB_PROCESSO** | Identificador do Tipo de Subprocesso | int | number(6,0) | Não |
| **ID_CLASSE_SUB_PROCESSO** | Identificador do Tipo de Subprocesso associado | int | number(6,0) | Não |
| **ID_DESENHO_PROCESSO** | Número sequencial gerado automaticamente pelo sistema para Identificar um DesenhoProcesso | int | number(6,0) | Não |

Tabelas referenciadas por SUB_PROCESSO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_SUB_PROCESSO](dados_classe_sub_processo) | \| **CLASSE_SUB_PROCESSO** \| **SUB_PROCESSO** \| \|---\|---\| \| ID_CLASSE_SUB_PROCESSO \| ID_CLASSE_SUB_PROCESSO \| |
| [DESENHO_PROCESSO](dados_desenho_processo) | \| **DESENHO_PROCESSO** \| **SUB_PROCESSO** \| \|---\|---\| \| ID_DESENHO_PROCESSO \| ID_DESENHO_PROCESSO \| |

Tabelas que dependem de SUB_PROCESSO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [DIAGRAMA](dados_diagrama) | \| **DIAGRAMA** \| **SUB_PROCESSO** \| \|---\|---\| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **SUB_PROCESSO** \| \|---\|---\| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **SUB_PROCESSO** \| \|---\|---\| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| |
| [GATEWAY](dados_gateway) | \| **GATEWAY** \| **SUB_PROCESSO** \| \|---\|---\| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| |
| [OUTPUT_SUB_PROC](dados_output_sub_proc) | \| **OUTPUT_SUB_PROC** \| **SUB_PROCESSO** \| \|---\|---\| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| |
| [CONTROLE](dados_controle) | \| **CONTROLE** \| **SUB_PROCESSO** \| \|---\|---\| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| |
| [RISCO_PROCESSO](dados_risco_processo) | \| **RISCO_PROCESSO** \| **SUB_PROCESSO** \| \|---\|---\| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| |

**Exemplo 1: join com a tabela CLASSE_SUB_PROCESSO**

```
select SUB_PROCESSO.*, CLASSE_SUB_PROCESSO.DESCRICAO
from SUB_PROCESSO, CLASSE_SUB_PROCESSO
where SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO = CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO
```

**Exemplo 2: join com a tabela DESENHO_PROCESSO**

```
select SUB_PROCESSO.*
from SUB_PROCESSO, DESENHO_PROCESSO
where SUB_PROCESSO.ID_DESENHO_PROCESSO = DESENHO_PROCESSO.ID_DESENHO_PROCESSO
```

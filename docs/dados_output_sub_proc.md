# OUTPUT_SUB_PROC

Caminho: Customização > Modelo de dados > Processo > OUTPUT_SUB_PROC

Parâmetros de Saída de Subprocesso

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_OUTPUT_SUB_PROC** | Número sequencial gerado automaticamente pelo sistema para Identificar um OutputSubProcesso | int | number(6,0) | Não |
| **ID_SUB_PROCESSO** | Identificador do Subprocesso proprietário do Output | int | number(6,0) | Não |
| **ID_PROPERTY** | Identificador do(a) Property associado(a) | int | number(6,0) | Sim |
| **ID_CUSTOM_PROPERTY** | Identificador do(a) CustomProperty associado(a) | int | number(6,0) | Sim |

Tabelas referenciadas por OUTPUT_SUB_PROC

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_PROPERTY](dados_sv_property) | \| **SV_PROPERTY** \| **OUTPUT_SUB_PROC** \| \|---\|---\| \| ID_PROPERTY \| ID_PROPERTY \| |
| [SV_CUSTOM_PROPERTY](dados_sv_custom_property) | \| **SV_CUSTOM_PROPERTY** \| **OUTPUT_SUB_PROC** \| \|---\|---\| \| ID_CUSTOM_PROPERTY \| ID_CUSTOM_PROPERTY \| |
| [SUB_PROCESSO](dados_sub_processo) | \| **SUB_PROCESSO** \| **OUTPUT_SUB_PROC** \| \|---\|---\| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| |

**Exemplo 1: join com a tabela SUB_PROCESSO**

```
select OUTPUT_SUB_PROC.*
from OUTPUT_SUB_PROC, SUB_PROCESSO
where OUTPUT_SUB_PROC.ID_SUB_PROCESSO = SUB_PROCESSO.ID_SUB_PROCESSO
```

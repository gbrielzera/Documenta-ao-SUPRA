# ITEM_OCORRENCIA

Caminho: Customização > Modelo de dados > Processo > ITEM_OCORRENCIA

Item de Configuração associado a uma ocorrência de processo.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_OCORRENCIA** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Ocorrência | int | number(6,0) | Não |
| **ID_ITEM** | Identificador do ItemConfiguracao associado | int | number(6,0) | Não |
| **DATA_HORA_ANEXADO** | Data e hora em que o Item foi anexado | datetime | date | Não |
| **ID_CLASSE_ANEXO** | Identificador da configuração de associação de Item de Configuração que gerou a associação. | int | number(6,0) | Sim |
| **EXPLICACAO** | Texto explicativo sobre a associação do item na Ocorrência. Pode ser utilizado para depuração de uma ocorrência de processo. | varchar(500) | varchar(500) | Sim |
| **ID_REPORT** | Identificador do relatório que foi utilizado para gerar o arquivo | int | number(6,0) | Sim |

Tabelas referenciadas por ITEM_OCORRENCIA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM](dados_item) | \| **ITEM** \| **ITEM_OCORRENCIA** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |
| [CLASSE_ANEXO](dados_classe_anexo) | \| **CLASSE_ANEXO** \| **ITEM_OCORRENCIA** \| \|---\|---\| \| ID_CLASSE_ANEXO \| ID_CLASSE_ANEXO \| |
| [SV_REPORT](dados_sv_report) | \| **SV_REPORT** \| **ITEM_OCORRENCIA** \| \|---\|---\| \| ID_REPORT \| ID_REPORT \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **ITEM_OCORRENCIA** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |

**Exemplo 1: join com a tabela OCORRENCIA**

```
select ITEM_OCORRENCIA.*
from ITEM_OCORRENCIA, OCORRENCIA
where ITEM_OCORRENCIA.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA
```

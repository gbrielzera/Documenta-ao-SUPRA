# ANEXO_EVNT_MSG

Caminho: Customização > Modelo de dados > Processo > ANEXO_EVNT_MSG

Tipos de arquivos que serão anexados no comunicado gerado pelo evento

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ATIVIDADE** | Identificador do evento intermediário que gerará o comunicado | int | number(6,0) | Não |
| **ID_CLASSE_CONFIGURACAO** | Identificador do tipo de arquivo que será anexado no comunicado | int | number(6,0) | Não |

Tabelas referenciadas por ANEXO_EVNT_MSG

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_CONFIGURACAO](dados_classe_configuracao) | \| **CLASSE_CONFIGURACAO** \| **ANEXO_EVNT_MSG** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **ANEXO_EVNT_MSG** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |

**Exemplo 1: join com a tabela ATIVIDADE**

```
select ANEXO_EVNT_MSG.*
from ANEXO_EVNT_MSG, ATIVIDADE
where ANEXO_EVNT_MSG.ID_ATIVIDADE = ATIVIDADE.ID_ATIVIDADE
```

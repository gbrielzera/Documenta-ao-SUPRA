# GATILHO_ASSOC

Caminho: Customização > Modelo de dados > Processo > GATILHO_ASSOC

Gatilhos disparados na ocorrência de um Evento

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ASSOCIACAO** | Identificador da Associação | int | number(6,0) | Não |
| **ID_TIPO_EVENTO** | Identificador do Tipo de Evento associado ao Gatilho | int | number(6,0) | Não |
| **SCRIPT** | Script que é executado como resposta do Gatilho | text | clob | Não |

Tabelas referenciadas por GATILHO_ASSOC

| **Tabela** | **Colunas de ligação** |
|---|---|
| [TIPO_EVENTO](dados_tipo_evento) | \| **TIPO_EVENTO** \| **GATILHO_ASSOC** \| \|---\|---\| \| ID_TIPO_EVENTO \| ID_TIPO_EVENTO \| |
| [ASSOCIACAO](dados_associacao) | \| **ASSOCIACAO** \| **GATILHO_ASSOC** \| \|---\|---\| \| ID_ASSOCIACAO \| ID_ASSOCIACAO \| |

**Exemplo 1: join com a tabela TIPO_EVENTO**

```
select GATILHO_ASSOC.*, TIPO_EVENTO.NOME
from GATILHO_ASSOC, TIPO_EVENTO
where GATILHO_ASSOC.ID_TIPO_EVENTO = TIPO_EVENTO.ID_TIPO_EVENTO
```

**Exemplo 2: join com a tabela ASSOCIACAO**

```
select GATILHO_ASSOC.*
from GATILHO_ASSOC, ASSOCIACAO
where GATILHO_ASSOC.ID_ASSOCIACAO = ASSOCIACAO.ID_ASSOCIACAO
```

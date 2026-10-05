# TOPICO_ARTIGO

Caminho: Customização > Modelo de dados > Ativos > TOPICO_ARTIGO

Tópico de Artigo

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ITEM** | Número sequencial gerado automaticamente pelo sistema para Identificar um Topico | int | number(6,0) | Não |
| **ID_TOPICO_CONH** | Identificador do template definido para o Tópico. Este template é criado no Tipo de Item de Configuração. | int | number(6,0) | Não |
| **CONT_HTML** | Conteúdo em formato texto mantido automaticamente pelo sistema. | text | clob | Sim |
| **CONT_TEXTO** | Conteúdo texto mantido automaticamente pelo sistema | text | clob | Sim |
| **CONT_RTF** | Conteúdo no formato RTF mantido pelo usuário | varbinary(4000) | blob | Sim |

Tabelas referenciadas por TOPICO_ARTIGO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [TOPICO_CONH](dados_topico_conh) | \| **TOPICO_CONH** \| **TOPICO_ARTIGO** \| \|---\|---\| \| ID_TOPICO_CONH \| ID_TOPICO_CONH \| |
| [CONHECIMENTO](dados_conhecimento) | \| **CONHECIMENTO** \| **TOPICO_ARTIGO** \| \|---\|---\| \|  \| ID_ITEM \| |

**Exemplo 1: join com a tabela TOPICO_CONH**

```
select TOPICO_ARTIGO.*, TOPICO_CONH.SUB_TITULO
from TOPICO_ARTIGO, TOPICO_CONH
where TOPICO_ARTIGO.ID_TOPICO_CONH = TOPICO_CONH.ID_TOPICO_CONH
```

**Exemplo 2: join com a tabela CONHECIMENTO**

```
select TOPICO_ARTIGO.*
from TOPICO_ARTIGO, CONHECIMENTO
where TOPICO_ARTIGO.ID_ITEM = CONHECIMENTO.
```

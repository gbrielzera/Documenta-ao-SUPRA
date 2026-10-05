# USUARIO_ITEM

Caminho: Customização > Modelo de dados > Ativos > USUARIO_ITEM

Usuários do Item de Configuração

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ITEM** | Número sequencial gerado automaticamente para Identificar um Item de Configuração | int | number(6,0) | Não |
| **ID_PESSOA** | Identificador da Pessoa associada | int | number(6,0) | Não |
| **DATA_HORA_ASSOC** | Data e hora de inclusão do Usuário | datetime | date | Não |
| **COMENTARIO** | Comentário | varchar(500) | varchar(500) | Sim |
| **ID_OCORRENCIA** | Identificador da Ocorrencia associada | int | number(6,0) | Sim |
| **ID_OCORRENCIA_DEVOLUCAO** | Identificador da Ocorrencia de devolução do Item de Configuração associado | int | number(6,0) | Sim |

Tabelas referenciadas por USUARIO_ITEM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **USUARIO_ITEM** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **USUARIO_ITEM** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **USUARIO_ITEM** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA_DEVOLUCAO \| |
| [ITEM](dados_item) | \| **ITEM** \| **USUARIO_ITEM** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |

**Exemplo 1: join com a tabela ITEM**

```
select USUARIO_ITEM.*
from USUARIO_ITEM, ITEM
where USUARIO_ITEM.ID_ITEM = ITEM.ID_ITEM
```

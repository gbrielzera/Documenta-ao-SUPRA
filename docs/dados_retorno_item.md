# RETORNO_ITEM

Caminho: Customização > Modelo de dados > Processo > RETORNO_ITEM

Configura uma regra de retorno de Itens de Configuração para Ordens de Serviço invocadas como Subprocessos ou link final. Quando uma Ordem de Serviço chamada é finalizada então os itens que atenderem a regra serão aidionado a Ordem de Serviço chamadora.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_RETORNO_ITEM** | Número sequencial gerado automaticamente pelo sistema para Identificar um RetornoItens | int | number(6,0) | Não |
| **ID_ATIVIDADE** | Identificador da Atividade | int | number(6,0) | Não |
| **SUPER_CLASSE** | Super tipo dos Itens de Configuraçao Itens que serão fornecidos para a Ordem de Serviço chamadora. Este retorno ocorre durante a finalização da Ordem de Serviço chamada. | varchar(500) | varchar(500) | Não |
| **ID_CLASSE_CONFIGURACAO** | Identificador do Tipo de Item de Configuração associado | int | number(6,0) | Sim |

Tabelas referenciadas por RETORNO_ITEM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_CONFIGURACAO](dados_classe_configuracao) | \| **CLASSE_CONFIGURACAO** \| **RETORNO_ITEM** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **RETORNO_ITEM** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |

**Exemplo 1: join com a tabela ATIVIDADE**

```
select RETORNO_ITEM.*
from RETORNO_ITEM, ATIVIDADE
where RETORNO_ITEM.ID_ATIVIDADE = ATIVIDADE.ID_ATIVIDADE
```

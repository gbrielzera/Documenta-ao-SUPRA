# PASSAGEM_ITEM

Caminho: Customização > Modelo de dados > Processo > PASSAGEM_ITEM

Configura uma regra de passagem de Itens de Configuração para Ordens de Serviço invocadas como Subprocessos ou link final.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PASSAGEM_ITEM** | Número sequencial gerado automaticamente pelo sistema para Identificar um PassagemItens | int | number(6,0) | Não |
| **ID_ATIVIDADE** | Identificador da Atividade | int | number(6,0) | Não |
| **SUPER_CLASSE** | Super tipo de Itens que serão fornecidos para a Ordem de Serviço chamada. Esta passagem de Itens ocorre na criação da Ordem de Serviço chamada. | varchar(500) | varchar(500) | Não |
| **ID_CLASSE_CONFIGURACAO** | Identificador do Tipo de Item de Configuração que terá itens passados como parâmetros para a rotina chamada. | int | number(6,0) | Sim |

Tabelas referenciadas por PASSAGEM_ITEM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_CONFIGURACAO](dados_classe_configuracao) | \| **CLASSE_CONFIGURACAO** \| **PASSAGEM_ITEM** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **PASSAGEM_ITEM** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |

**Exemplo 1: join com a tabela ATIVIDADE**

```
select PASSAGEM_ITEM.*
from PASSAGEM_ITEM, ATIVIDADE
where PASSAGEM_ITEM.ID_ATIVIDADE = ATIVIDADE.ID_ATIVIDADE
```

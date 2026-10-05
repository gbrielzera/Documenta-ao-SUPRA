# APLIC_CONH_SERV

Caminho: Customização > Modelo de dados > Ativos > APLIC_CONH_SERV

Escopo de aplicação de um Artigo da Base de Conhecimento em Serviços.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **APLIC_CONH_SERV** | Número sequencial gerado automaticamente pelo sistema para Identificar um AplicacaoConhecimentoServico | int | number(6,0) | Não |
| **ID_CLASSE_SERVICO** | Identificador do ClasseServico associado | int | number(6,0) | Não |
| **ID_SERVICO** | Identificador do Servico associado | int | number(6,0) | Sim |
| **ID_ITEM** | Identificador do Artigo proprietário da aplicação | int | number(6,0) | Não |

Tabelas referenciadas por APLIC_CONH_SERV

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_SERVICO](dados_classe_servico) | \| **CLASSE_SERVICO** \| **APLIC_CONH_SERV** \| \|---\|---\| \| ID_CLASSE_SERVICO \| ID_CLASSE_SERVICO \| |
| [SERVICO](dados_servico) | \| **SERVICO** \| **APLIC_CONH_SERV** \| \|---\|---\| \| ID_SERVICO \| ID_SERVICO \| |
| [CONHECIMENTO](dados_conhecimento) | \| **CONHECIMENTO** \| **APLIC_CONH_SERV** \| \|---\|---\| \|  \| ID_ITEM \| |

**Exemplo 1: join com a tabela CONHECIMENTO**

```
select APLIC_CONH_SERV.*
from APLIC_CONH_SERV, CONHECIMENTO
where APLIC_CONH_SERV.ID_ITEM = CONHECIMENTO.
```

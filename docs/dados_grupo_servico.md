# GRUPO_SERVICO

Caminho: Customização > Modelo de dados > Processo > GRUPO_SERVICO

Um Grupo de Serviço é o segundo mais elevado nível hierárquico de classificação de Serviços.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_GRUPO_SERVICO** | Número sequencial gerado automaticamente pelo sistema para Identificar um GrupoServico | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do GrupoServico | varchar(500) | varchar(500) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **ID_SUPER_CLASSE_SERVICO** | Identificador da Classe de Serviço associada | int | number(6,0) | Sim |

Tabelas referenciadas por GRUPO_SERVICO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SUPER_CLASSE_SERVICO](dados_super_classe_servico) | \| **SUPER_CLASSE_SERVICO** \| **GRUPO_SERVICO** \| \|---\|---\| \| ID_SUPER_CLASSE_SERVICO \| ID_SUPER_CLASSE_SERVICO \| |

Tabelas que dependem de GRUPO_SERVICO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_SERVICO](dados_classe_servico) | \| **CLASSE_SERVICO** \| **GRUPO_SERVICO** \| \|---\|---\| \| ID_GRUPO_SERVICO \| ID_GRUPO_SERVICO \| |

**Exemplo 1: join com a tabela SUPER_CLASSE_SERVICO**

```
select GRUPO_SERVICO.*, SUPER_CLASSE_SERVICO.DESCRICAO
from GRUPO_SERVICO left outer join SUPER_CLASSE_SERVICO on GRUPO_SERVICO.ID_SUPER_CLASSE_SERVICO = SUPER_CLASSE_SERVICO.ID_SUPER_CLASSE_SERVICO
```

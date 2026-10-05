# CLASSE_COMPONENTE

Caminho: Customização > Modelo de dados > Ativos > CLASSE_COMPONENTE

Tipos de Itens de Configuração que podem ser utilizadas como Componentes.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CLASSE_CONFIGURACAO** | Identificador do Tipo de Serviço que é proprietária das Classes relacionadas como Componentes | int | number(6,0) | Não |
| **ID_CLASSE_COMPONENTE** | Identificador do Tipo de Item de Configuração que é utilizada como Componente | int | number(6,0) | Não |

Tabelas referenciadas por CLASSE_COMPONENTE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_CONFIGURACAO](dados_classe_configuracao) | \| **CLASSE_CONFIGURACAO** \| **CLASSE_COMPONENTE** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_COMPONENTE \| |
| [CLASSE_CONFIGURACAO](dados_classe_configuracao) | \| **CLASSE_CONFIGURACAO** \| **CLASSE_COMPONENTE** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |

**Exemplo 1: join com a tabela CLASSE_CONFIGURACAO**

```
select CLASSE_COMPONENTE.*, CLASSE_CONFIGURACAO.DESCRICAO
from CLASSE_COMPONENTE, CLASSE_CONFIGURACAO
where CLASSE_COMPONENTE.ID_CLASSE_COMPONENTE = CLASSE_CONFIGURACAO.ID_CLASSE_CONFIGURACAO
```

**Exemplo 2: join com a tabela CLASSE_CONFIGURACAO**

```
select CLASSE_COMPONENTE.*
from CLASSE_COMPONENTE, CLASSE_CONFIGURACAO
where CLASSE_COMPONENTE.ID_CLASSE_CONFIGURACAO = CLASSE_CONFIGURACAO.ID_CLASSE_CONFIGURACAO
```

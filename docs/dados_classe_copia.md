# CLASSE_COPIA

Caminho: Customização > Modelo de dados > Ativos > CLASSE_COPIA

Tipos de Itens de Configuração que podem ser utilizadas como redundâncias.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CLASSE_CONFIGURACAO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Tipo de Item de Configuração | int | number(6,0) | Não |
| **ID_CLASSE_COPIA** | Identificador do Tipo de Item de Configuração que é utilizada como Cópia | int | number(6,0) | Não |

Tabelas referenciadas por CLASSE_COPIA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_CONFIGURACAO](dados_classe_configuracao) | \| **CLASSE_CONFIGURACAO** \| **CLASSE_COPIA** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_COPIA \| |
| [CLASSE_CONFIGURACAO](dados_classe_configuracao) | \| **CLASSE_CONFIGURACAO** \| **CLASSE_COPIA** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |

**Exemplo 1: join com a tabela CLASSE_CONFIGURACAO**

```
select CLASSE_COPIA.*, CLASSE_CONFIGURACAO.DESCRICAO
from CLASSE_COPIA, CLASSE_CONFIGURACAO
where CLASSE_COPIA.ID_CLASSE_COPIA = CLASSE_CONFIGURACAO.ID_CLASSE_CONFIGURACAO
```

**Exemplo 2: join com a tabela CLASSE_CONFIGURACAO**

```
select CLASSE_COPIA.*
from CLASSE_COPIA, CLASSE_CONFIGURACAO
where CLASSE_COPIA.ID_CLASSE_CONFIGURACAO = CLASSE_CONFIGURACAO.ID_CLASSE_CONFIGURACAO
```

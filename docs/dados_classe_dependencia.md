# CLASSE_DEPENDENCIA

Caminho: Customização > Modelo de dados > Ativos > CLASSE_DEPENDENCIA

Tipos de Itens de Configuração que podem ser associados como Dependências

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CLASSE_CONFIGURACAO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Tipo de Item de Configuração | int | number(6,0) | Não |
| **ID_CLASSE_DEPENDENCIA** | Identificador do Tipo de Item de Configuração que é utilizada como Dependente | int | number(6,0) | Não |

Tabelas referenciadas por CLASSE_DEPENDENCIA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_CONFIGURACAO](dados_classe_configuracao) | \| **CLASSE_CONFIGURACAO** \| **CLASSE_DEPENDENCIA** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_DEPENDENCIA \| |
| [CLASSE_CONFIGURACAO](dados_classe_configuracao) | \| **CLASSE_CONFIGURACAO** \| **CLASSE_DEPENDENCIA** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |

**Exemplo 1: join com a tabela CLASSE_CONFIGURACAO**

```
select CLASSE_DEPENDENCIA.*, CLASSE_CONFIGURACAO.DESCRICAO
from CLASSE_DEPENDENCIA, CLASSE_CONFIGURACAO
where CLASSE_DEPENDENCIA.ID_CLASSE_DEPENDENCIA = CLASSE_CONFIGURACAO.ID_CLASSE_CONFIGURACAO
```

**Exemplo 2: join com a tabela CLASSE_CONFIGURACAO**

```
select CLASSE_DEPENDENCIA.*
from CLASSE_DEPENDENCIA, CLASSE_CONFIGURACAO
where CLASSE_DEPENDENCIA.ID_CLASSE_CONFIGURACAO = CLASSE_CONFIGURACAO.ID_CLASSE_CONFIGURACAO
```

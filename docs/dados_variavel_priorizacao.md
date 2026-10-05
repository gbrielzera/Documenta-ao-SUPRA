# VARIAVEL_PRIORIZACAO

Caminho: Customização > Modelo de dados > Processo > VARIAVEL_PRIORIZACAO

Variável utilizada para cálculo de Prioridade.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **NOME** | Nome da Variável. Este nome pode ser referenciado pela Expressão que calcula o Grau de Prioridade. | varchar(100) | varchar(100) | Não |
| **ID_METODO_PRIORIZACAO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Método de Priorização. | int | number(6,0) | Não |
| **DESCRICAO** | Descrição apresentada para o usuário. Se for uma Variável reservada então este valor é alimentado automaticamente pelo conteúdo fornecido pelo fabricante. | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por VARIAVEL_PRIORIZACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [METODO_PRIORIZACAO](dados_metodo_priorizacao) | \| **METODO_PRIORIZACAO** \| **VARIAVEL_PRIORIZACAO** \| \|---\|---\| \| ID_METODO_PRIORIZACAO \| ID_METODO_PRIORIZACAO \| |

Tabelas que dependem de VARIAVEL_PRIORIZACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ENUM_VARIAVEL](dados_enum_variavel) | \| **ENUM_VARIAVEL** \| **VARIAVEL_PRIORIZACAO** \| \|---\|---\| \| NOME \| NOME \| \| ID_METODO_PRIORIZACAO \| ID_METODO_PRIORIZACAO \| |

**Exemplo 1: join com a tabela METODO_PRIORIZACAO**

```
select VARIAVEL_PRIORIZACAO.*
from VARIAVEL_PRIORIZACAO, METODO_PRIORIZACAO
where VARIAVEL_PRIORIZACAO.ID_METODO_PRIORIZACAO = METODO_PRIORIZACAO.ID_METODO_PRIORIZACAO
```

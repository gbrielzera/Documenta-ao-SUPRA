# CLASSE_CONF_INDICADOR

Caminho: Customização > Modelo de dados > Processo > CLASSE_CONF_INDICADOR

Relação de tipos de Itens de Configuração que serão recuperadaos para cálculo do indicador.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **SEQUENCIAL** | Sequencial | int | number(6,0) | Não |
| **ID_INDICADOR** | Número sequencial gerado automaticamente pelo sistema para Identificar um Indicador | int | number(6,0) | Não |
| **ID_CLASSE_CONFIGURACAO** | Identificador do Tipo de Item de Configuração associado | int | number(6,0) | Sim |
| **SUPER_CLASSE** | Super tipo de Itens de Configuração para Filtro | varchar(250) | varchar(250) | Não |

Tabelas referenciadas por CLASSE_CONF_INDICADOR

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_CONFIGURACAO](dados_classe_configuracao) | \| **CLASSE_CONFIGURACAO** \| **CLASSE_CONF_INDICADOR** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |
| [INDICADOR](dados_indicador) | \| **INDICADOR** \| **CLASSE_CONF_INDICADOR** \| \|---\|---\| \| ID_INDICADOR \| ID_INDICADOR \| |

**Exemplo 1: join com a tabela INDICADOR**

```
select CLASSE_CONF_INDICADOR.*
from CLASSE_CONF_INDICADOR, INDICADOR
where CLASSE_CONF_INDICADOR.ID_INDICADOR = INDICADOR.ID_INDICADOR
```

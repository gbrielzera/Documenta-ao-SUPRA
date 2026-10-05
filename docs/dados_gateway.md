# GATEWAY

Caminho: Customização > Modelo de dados > Processo > GATEWAY

Representa uma Decisão ou Merge a ser tomado durante a execução do Processo

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_GATEWAY** | Número sequencial gerado automaticamente pelo sistema para Identificar um Gateway | int | number(6,0) | Não |
| **DESCRICAO** | Rótulo que descreve a decisão. No caso de decisões baseadas em eventos este mesmo texto é utilizado como texto da pergunta para decisão. | varchar(500) | varchar(500) | Não |
| **TIPO** | Tipo de Gateway que pode ser Fork, Inclusive Decision etc. | varchar(250) | varchar(250) | Não |
| **ID_EMISSOR** | Número sequencial gerado automaticamente pelo sistema para Identificar um Emissor | int | number(6,0) | Sim |
| **ID_SUB_PROCESSO** | Identificador do Subprocesso | int | number(6,0) | Não |
| **EXPRESSAO_COMPARACAO** | Fórmula Python para Decisão. A expressão pode conter operadores e propriedades do item de processo (campos de Ordens de Serviço por exemplo) | text | clob | Sim |
| **REFERENCIA** | Texto descrevendo o processo de tomada de Decisão. Especificar principais entradas, saídas e Papéis envolvidos. | text | clob | Sim |
| **CODIGO** | Código utilizado por scripts para tomar alguma decisão ou gerar alguma informação após execução do Gateway. O código deve ser único dentro de uma versão do Subprocesso. | varchar(100) | varchar(100) | Sim |

Tabelas referenciadas por GATEWAY

| **Tabela** | **Colunas de ligação** |
|---|---|
| [EMISSOR](dados_emissor) | \| **EMISSOR** \| **GATEWAY** \| \|---\|---\| \| ID_EMISSOR \| ID_EMISSOR \| |
| [SUB_PROCESSO](dados_sub_processo) | \| **SUB_PROCESSO** \| **GATEWAY** \| \|---\|---\| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| |

Tabelas que dependem de GATEWAY

| **Tabela** | **Colunas de ligação** |
|---|---|
| [EMISSOR](dados_emissor) | \| **EMISSOR** \| **GATEWAY** \| \|---\|---\| \| ID_GATEWAY_SAIDA \| ID_GATEWAY \| |
| [RECEPTOR](dados_receptor) | \| **RECEPTOR** \| **GATEWAY** \| \|---\|---\| \| ID_GATEWAY_ENT \| ID_GATEWAY \| |
| [FIGURA](dados_figura) | \| **FIGURA** \| **GATEWAY** \| \|---\|---\| \| ID_GATEWAY \| ID_GATEWAY \| |
| [EMISSOR](dados_emissor) | \| **EMISSOR** \| **GATEWAY** \| \|---\|---\| \| ID_GATEWAY \| ID_GATEWAY \| |
| [RECEPTOR](dados_receptor) | \| **RECEPTOR** \| **GATEWAY** \| \|---\|---\| \| ID_GATEWAY \| ID_GATEWAY \| |

**Exemplo 1: join com a tabela SUB_PROCESSO**

```
select GATEWAY.*
from GATEWAY, SUB_PROCESSO
where GATEWAY.ID_SUB_PROCESSO = SUB_PROCESSO.ID_SUB_PROCESSO
```

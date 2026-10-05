# VALOR_INPUT

Caminho: Customização > Modelo de dados > Processo > VALOR_INPUT

Valores de Parâmetors de Entrada

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_VALOR_INPUT** | Número sequencial gerado automaticamente pelo sistema para Identificar um ValorInput | int | number(6,0) | Não |
| **ID_ATIVIDADE** | Atividade proprietária do Valor de Parâmetro de Entrada | int | number(6,0) | Não |
| **ID_PROPERTY** | Identificador do InputSubProcesso associado | int | number(6,0) | Sim |
| **EXP_VALOR** | Fórmula para determinar o Valor a ser fornecido como parâmetro. Se não definido é fornecido o mesmo valor do nível invocador. | varchar(500) | varchar(500) | Sim |
| **ID_CUSTOM_PROPERTY** | Identificador do(a) CustomProperty associado(a) | int | number(6,0) | Sim |

Tabelas referenciadas por VALOR_INPUT

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_PROPERTY](dados_sv_property) | \| **SV_PROPERTY** \| **VALOR_INPUT** \| \|---\|---\| \| ID_PROPERTY \| ID_PROPERTY \| |
| [SV_CUSTOM_PROPERTY](dados_sv_custom_property) | \| **SV_CUSTOM_PROPERTY** \| **VALOR_INPUT** \| \|---\|---\| \| ID_CUSTOM_PROPERTY \| ID_CUSTOM_PROPERTY \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **VALOR_INPUT** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |

**Exemplo 1: join com a tabela ATIVIDADE**

```
select VALOR_INPUT.*
from VALOR_INPUT, ATIVIDADE
where VALOR_INPUT.ID_ATIVIDADE = ATIVIDADE.ID_ATIVIDADE
```

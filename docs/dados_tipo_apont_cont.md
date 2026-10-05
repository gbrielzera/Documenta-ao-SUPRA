# TIPO_APONT_CONT

Caminho: Customização > Modelo de dados > Recurso > TIPO_APONT_CONT

Tipo de apontamento em um contrato.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CONTRATO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Contrato | int | number(6,0) | Não |
| **ID_TIPO_APONTAMENTO** | Identificador do TipoApontamento associado | int | number(6,0) | Não |
| **VARIACAO** | Variação percentual em relação a valor contratado (de 0% a 100%) que é aplicado no relatório de apropriações. | decimal(15,2) | number(15,2) | Não |

Tabelas referenciadas por TIPO_APONT_CONT

| **Tabela** | **Colunas de ligação** |
|---|---|
| [TIPO_APONTAMENTO](dados_tipo_apontamento) | \| **TIPO_APONTAMENTO** \| **TIPO_APONT_CONT** \| \|---\|---\| \| ID_TIPO_APONTAMENTO \| ID_TIPO_APONTAMENTO \| |
| [CONTRATO](dados_contrato) | \| **CONTRATO** \| **TIPO_APONT_CONT** \| \|---\|---\| \| ID_CONTRATO \| ID_CONTRATO \| |

Tabelas que dependem de TIPO_APONT_CONT

| **Tabela** | **Colunas de ligação** |
|---|---|
| [REST_HORA_APONT](dados_rest_hora_apont) | \| **REST_HORA_APONT** \| **TIPO_APONT_CONT** \| \|---\|---\| \| ID_CONTRATO \| ID_CONTRATO \| \| ID_TIPO_APONTAMENTO \| ID_TIPO_APONTAMENTO \| |

**Exemplo 1: join com a tabela TIPO_APONTAMENTO**

```
select TIPO_APONT_CONT.*, TIPO_APONTAMENTO.DESCRICAO
from TIPO_APONT_CONT, TIPO_APONTAMENTO
where TIPO_APONT_CONT.ID_TIPO_APONTAMENTO = TIPO_APONTAMENTO.ID_TIPO_APONTAMENTO
```

**Exemplo 2: join com a tabela CONTRATO**

```
select TIPO_APONT_CONT.*
from TIPO_APONT_CONT, CONTRATO
where TIPO_APONT_CONT.ID_CONTRATO = CONTRATO.ID_CONTRATO
```

# TIPO_APONTAMENTO

Caminho: Customização > Modelo de dados > Recurso > TIPO_APONTAMENTO

Um Tipo de Apontamento pode ser utilizado no cadastro de Contratos para definir um fator aplicado a um valor/recurso também registrado no contrato.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_TIPO_APONTAMENTO** | Identificador do Tipo de Apontamento | int | number(6,0) | Não |
| **DESCRICAO** | Descrição do Tipo de Apontamento | varchar(500) | varchar(500) | Não |

Tabelas que dependem de TIPO_APONTAMENTO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [TIPO_APONT_CONT](dados_tipo_apont_cont) | \| **TIPO_APONT_CONT** \| **TIPO_APONTAMENTO** \| \|---\|---\| \| ID_TIPO_APONTAMENTO \| ID_TIPO_APONTAMENTO \| |

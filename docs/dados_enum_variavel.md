# ENUM_VARIAVEL

Caminho: Customização > Modelo de dados > Processo > ENUM_VARIAVEL

Enumeração de valores para Variável. Quando não existir então o campo é numérico de livre digitação.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **NOME** | Nome da Variável. Este nome pode ser referenciado pela Expressão que calcula o Grau de Prioridade. | varchar(100) | varchar(100) | Não |
| **ID_METODO_PRIORIZACAO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Método de Priorização de Ocorrências. | int | number(6,0) | Não |
| **SEQUENCIAL** | Sequencia de apresentação da opção. | int | number(6,0) | Não |
| **DESCRICAO** | Descritivo da opção | varchar(500) | varchar(500) | Não |
| **VALOR** | Valor para a opção | int | number(6,0) | Não |

Tabelas referenciadas por ENUM_VARIAVEL

| **Tabela** | **Colunas de ligação** |
|---|---|
| [VARIAVEL_PRIORIZACAO](dados_variavel_priorizacao) | \| **VARIAVEL_PRIORIZACAO** \| **ENUM_VARIAVEL** \| \|---\|---\| \| NOME \| NOME \| \| ID_METODO_PRIORIZACAO \| ID_METODO_PRIORIZACAO \| |

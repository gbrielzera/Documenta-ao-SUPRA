# APONT_OCORRENCIA

Caminho: Customização > Modelo de dados > Processo > APONT_OCORRENCIA

Apontamento genérico para Ocorrências de Processo

Por se tratar de um tipo herdado de Apontamento, a tabela APONT_OCORRENCIA possui uma chave estrangeira apontando para a tabela [APONTAMENTO](dados_apontamento).

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_APONTAMENTO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Apontamento | int | number(6,0) | Não |
| **ID_OCORRENCIA** | Identificador da Ocorrência associada | int | number(6,0) | Não |

Tabelas referenciadas por APONT_OCORRENCIA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **APONT_OCORRENCIA** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |

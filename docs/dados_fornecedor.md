# FORNECEDOR

Caminho: Customização > Modelo de dados > Recurso > FORNECEDOR

Um Fornecedor é uma tipo especial de Empresa habilitada como prestador de serviços para a área.

Por se tratar de um tipo herdado de Empresa, a tabela FORNECEDOR possui uma chave estrangeira apontando para a tabela [EMPRESA](dados_empresa).

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_EMPRESA** | Número sequencial gerado por sistema para identificar uma Empresa | int | number(6,0) | Não |

Tabelas que dependem de FORNECEDOR

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CONTRATO](dados_contrato) | \| **CONTRATO** \| **FORNECEDOR** \| \|---\|---\| \| ID_FORNECEDOR \|  \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **FORNECEDOR** \| \|---\|---\| \| ID_FORNECEDOR \|  \| |

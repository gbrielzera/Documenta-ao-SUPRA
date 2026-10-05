# FABRICANTE

Caminho: Customização > Modelo de dados > Ativos > FABRICANTE

Fabricante de um Item de Configuração.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_FABRICANTE** | Número sequencial gerado automaticamente pelo sistema para Identificar um Fabricante | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do Fabricante | varchar(500) | varchar(500) | Não |
| **ATIVO** | Indica que o Fabricante está ativo no sistema | char(3) | char(3) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |

Tabelas que dependem de FABRICANTE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [MODELO](dados_modelo) | \| **MODELO** \| **FABRICANTE** \| \|---\|---\| \| ID_FABRICANTE \| ID_FABRICANTE \| |

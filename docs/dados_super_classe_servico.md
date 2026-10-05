# SUPER_CLASSE_SERVICO

Caminho: Customização > Modelo de dados > Processo > SUPER_CLASSE_SERVICO

Uma Classe de Serviço é o maior nível hierárquico de classificação de Serviços.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_SUPER_CLASSE_SERVICO** | Número sequencial gerado automaticamente pelo sistema para Identificar uma ClasseServico | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada da ClasseServico | varchar(500) | varchar(500) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |

Tabelas que dependem de SUPER_CLASSE_SERVICO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [GRUPO_SERVICO](dados_grupo_servico) | \| **GRUPO_SERVICO** \| **SUPER_CLASSE_SERVICO** \| \|---\|---\| \| ID_SUPER_CLASSE_SERVICO \| ID_SUPER_CLASSE_SERVICO \| |

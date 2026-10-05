# PERFIL_CLIENTE

Caminho: Customização > Modelo de dados > Recurso > PERFIL_CLIENTE

O Perfil de Cliente pode ser utilizado para definição de privilégios do Cliente em atendimentos diversos com impacto na definição de ANS.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PERFIL_CLIENTE** | Número sequencial gerado automaticamente pelo sistema para Identificar um Perfil de Cliente | int | number(6,0) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **DESCRICAO** | Texto que descreve claramente a utilização de um Perfil de Cliente. Este texto é utilizado na tela de Cadastro de Clientes para associação de Perfil com Cliente e também na tela de Ordem de Serviço para informar ao Solucionador o privilégio conferido. | varchar(500) | varchar(500) | Não |

Tabelas que dependem de PERFIL_CLIENTE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **PERFIL_CLIENTE** \| \|---\|---\| \| ID_PERFIL_CLIENTE \| ID_PERFIL_CLIENTE \| |
| [ITEM_SLA](dados_item_sla) | \| **ITEM_SLA** \| **PERFIL_CLIENTE** \| \|---\|---\| \| ID_PERFIL_CLIENTE \| ID_PERFIL_CLIENTE \| |

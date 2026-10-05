# GRUPO_EMPRESA

Caminho: Customização > Modelo de dados > Recurso > GRUPO_EMPRESA

Grupo empresarial controlador de empresas cadastradas no sistema. Na aplicação de Autoatendimento um grupo pode ser utilizado para restringir a seleção de pessoas do grupo onde está cadastrado o usuário conectado, evitando que um usuário acesse o cadastro de pessoas de outras empresas.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_GRUPO_EMPRESA** | Número sequencial gerado por sistema para Identificar um Grupo Empresarial | int | number(6,0) | Não |
| **DESCRICAO** | Nome do Grupo Empresarial | varchar(500) | varchar(500) | Não |
| **SIGLA** | Nome resumido utilizado para identificar um Grupo Empresarial. | varchar(50) | varchar(50) | Não |
| **ATIVO** | Indica que o Grupo Empresarial está Ativo. | char(3) | char(3) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |

Tabelas que dependem de GRUPO_EMPRESA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [EMPRESA](dados_empresa) | \| **EMPRESA** \| **GRUPO_EMPRESA** \| \|---\|---\| \| ID_GRUPO_EMPRESA \| ID_GRUPO_EMPRESA \| |

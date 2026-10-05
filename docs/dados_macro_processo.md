# MACRO_PROCESSO

Caminho: Customização > Modelo de dados > Processo > MACRO_PROCESSO

Agrupamento de processos endereçados a uma área de negócio

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_MACRO_PROCESSO** | Número sequencial gerado automaticamente pelo sistema para Identificar um MacroProcesso | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do MacroProcesso | varchar(500) | varchar(500) | Não |
| **DESCRICAO_CLIENTE** | Descritivo apresentado para o cliente no passo de seleção de macro-processos da função de Abertura de Ordens de Serviço do Autoatendimento. Se não for informado então o sistema utilizará o próprio descritivo do macro-processo. | varchar(500) | varchar(500) | Sim |

Tabelas que dependem de MACRO_PROCESSO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PROCESSO](dados_processo) | \| **PROCESSO** \| **MACRO_PROCESSO** \| \|---\|---\| \| ID_MACRO_PROCESSO \| ID_MACRO_PROCESSO \| |
| [ENV_GRUPO](dados_env_grupo) | \| **ENV_GRUPO** \| **MACRO_PROCESSO** \| \|---\|---\| \| ID_MACRO_PROCESSO \| ID_MACRO_PROCESSO \| |

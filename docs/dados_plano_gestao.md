# PLANO_GESTAO

Caminho: Customização > Modelo de dados > Processo > PLANO_GESTAO

O Plano de Gestão é utilizado para gerenciar Indicadores de Desempenho. Este plano pode ser utilizado para gestão de Indicadores de Desempenho Chave da área ou indicadores associados a Acordos de Nível de Serviço.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PLANO_GESTAO** | Número sequencial gerado automaticamente pelo sistema para Identificar um PlanoGestao | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do Plano de Gestão. Esta descrição é utilizada para seleção do Plao de Gestão na aplicação Executive Dashboard. | varchar(500) | varchar(500) | Não |
| **DATA_INICIO** | Data de início do plano. Quando modificado é atualizada a coleção de períodos de todos os Indicadores associados ao plano. | datetime | date | Não |
| **DATA_FIM** | Data fim do plano. Quando modificado é atualizada a coleção de períodos de todos os Indicadores associados ao plano. | datetime | date | Não |
| **INFO_RESTRITAS** | O solucionador logado só visualiza suas informações ou informações de subordinados. | char(3) | char(3) | Não |

Tabelas que dependem de PLANO_GESTAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [APURACAO_INDICADOR](dados_apuracao_indicador) | \| **APURACAO_INDICADOR** \| **PLANO_GESTAO** \| \|---\|---\| \| ID_PLANO_GESTAO \| ID_PLANO_GESTAO \| |
| [INDICADOR_PLANO](dados_indicador_plano) | \| **INDICADOR_PLANO** \| **PLANO_GESTAO** \| \|---\|---\| \| ID_PLANO_GESTAO \| ID_PLANO_GESTAO \| |
| [GRUPO_TRABALHO_AUTORIZADO](dados_grupo_trabalho_autorizado_) | \| **GRUPO_TRABALHO_AUTORIZADO** \| **PLANO_GESTAO** \| \|---\|---\| \| ID_PLANO_GESTAO \| ID_PLANO_GESTAO \| |

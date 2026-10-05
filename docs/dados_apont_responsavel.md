# APONT_RESPONSAVEL

Caminho: Customização > Modelo de dados > Processo > APONT_RESPONSAVEL

Mantém histórico de Responsáveis por Item de Processo

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_OCORRENCIA** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Ocorrência | int | number(6,0) | Não |
| **SEQUENCIAL** | Sequencial de responsabilidade para uma determinada Ordem de Serviço. | int | number(6,0) | Não |
| **ID_RESPONSAVEL** | Identificador do Solucionador Responsável | int | number(6,0) | Não |
| **DATA_HORA_INICIO** | Data e hora de início para o período no qual o Solucionador foi responsável | datetime | date | Não |
| **RESP_ATEND_PAPEL** | Indica que o usuário responsável atendeu aos requisitos de papeis definidos em processo. | char(3) | char(3) | Não |
| **EXPLIC_ATOR** | Texto explicativo sobre o cálculo de um ator na Ordem de Serviço. | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por APONT_RESPONSAVEL

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **APONT_RESPONSAVEL** \| \|---\|---\| \| ID_PESSOA \| ID_RESPONSAVEL \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **APONT_RESPONSAVEL** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |

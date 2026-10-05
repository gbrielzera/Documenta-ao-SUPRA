# TIME_SHEET

Caminho: Customização > Modelo de dados > Processo > TIME_SHEET

Apontamento de Horas Trabalhadas

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_OCORRENCIA** | Identificador da Ocorrência de Processo associada | int | number(6,0) | Não |
| **SEQUENCIAL** | Sequencial do apontamento em uma Ordem de Serviço | int | number(6,0) | Não |
| **DATA_HORA_INICIO** | Data/hora de início | datetime | date | Não |
| **DATA_HORA_FIM** | Data/hora de Fim | datetime | date | Não |
| **ID_TECNICO** | Identificador do Solucionador associado ao apontamento | int | number(6,0) | Não |
| **DATA_HORA_APONTAMENTO** | Data/hora em que foi feito o apontamento | datetime | date | Não |
| **DATA_HORA_ATUALIZACAO** | Data/hora de última atualização do Apontamento | datetime | date | Não |
| **OBSERVACAO** | Texto de Observação para detalhamento do apontamento. | varchar(500) | varchar(500) | Sim |
| **ID_GRUPO_TRABALHO** | Identfiicador do Grupo de Trabalho do Solucionador no instante em que foi realizado o apontamento | int | number(6,0) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **ID_ATIVIDADE** | Identificador do(a) Atividade associado(a) | int | number(6,0) | Sim |
| **ID_TIPO_APONTAMENTO** | Identificador do Tipo de Apontamento associado | int | number(6,0) | Sim |
| **FORMA_APONTAMENTO** | Forma de definição de apontamentos, se por total de horas ou por período | varchar(250) | varchar(250) | Não |
| **DURACAO_MINUTOS** | Duração de um apontamento em minutos | int | number(6,0) | Não |

Tabelas referenciadas por TIME_SHEET

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **TIME_SHEET** \| \|---\|---\| \| ID_PESSOA \| ID_TECNICO \| |
| [GRUPO_TRABALHO](dados_grupo_trabalho) | \| **GRUPO_TRABALHO** \| **TIME_SHEET** \| \|---\|---\| \| ID_GRUPO_TRABALHO \| ID_GRUPO_TRABALHO \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **TIME_SHEET** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **TIME_SHEET** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [TIPO_APONTAMENTO](dados_tipo_apontamento) | \| **TIPO_APONTAMENTO** \| **TIME_SHEET** \| \|---\|---\| \| ID_TIPO_APONTAMENTO \| ID_TIPO_APONTAMENTO \| |

Tabelas que dependem de TIME_SHEET

| **Tabela** | **Colunas de ligação** |
|---|---|
| [TIME_SHEET_APROPRIADO](dados_time_sheet_apropriado) | \| **TIME_SHEET_APROPRIADO** \| **TIME_SHEET** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| \| SEQUENCIAL \| SEQUENCIAL \| |

# REST_HORA_APONT

Caminho: Customização > Modelo de dados > Recurso > REST_HORA_APONT

Faixas de horários em dias da semana onde são possíveis apontamentos de um determinado tipo.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_REST_HORA_APONT** | Número sequencial gerado automaticamente pelo sistema para Identificar um RestricaoHorarioApontamento | int | number(6,0) | Não |
| **DIA_SEMANA** | Dia da semana em que é válida a regra de disponibilidade. | varchar(250) | varchar(250) | Não |
| **HORA_INICIO** | Hora de início do período de disponibilidade (0 a 23) | int | number(6,0) | Não |
| **MINUTO_INICIO** | Minuto de início (0 a 59) | int | number(6,0) | Não |
| **ID_CONTRATO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Contrato | int | number(6,0) | Não |
| **ID_TIPO_APONTAMENTO** | Identificador do TipoApontamento associado | int | number(6,0) | Não |
| **HORA_FIM** | Hora de fim do período de disponibilidade (0 a 23). Tentativas de apontamentos que excedem este limite serão bloqueadas e devem ser corrigidas pelo solucionador que está realizando o apontamento. | int | number(6,0) | Não |
| **MINUTO_FIM** | Minuto de fim da disponibilidade (0 a 59). Tentativas de apontamentos que excedem este limite serão bloqueadas e devem ser corrigidas pelo solucionador que está realizando o apontamento. | int | number(6,0) | Não |

Tabelas referenciadas por REST_HORA_APONT

| **Tabela** | **Colunas de ligação** |
|---|---|
| [TIPO_APONT_CONT](dados_tipo_apont_cont) | \| **TIPO_APONT_CONT** \| **REST_HORA_APONT** \| \|---\|---\| \| ID_CONTRATO \| ID_CONTRATO \| \| ID_TIPO_APONTAMENTO \| ID_TIPO_APONTAMENTO \| |

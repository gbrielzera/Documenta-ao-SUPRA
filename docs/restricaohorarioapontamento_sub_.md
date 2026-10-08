# Restrições de horários para apontamentos

Caminho: Restrições de horários para apontamentos

Faixas de horários em dias da semana onde são possíveis apontamentos de um determinado tipo.

Na tabela abaixo temos os principais campos deste cadastro:

## Campos do cadastro

| **Dia da semana** | Dia da semana em que é válida a regra de disponibilidade. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DIA_SEMANA da tabela [REST_HORA_APONT](dados_rest_hora_apont). |
|---|---|
| **Hora início** | Hora de início do período de disponibilidade (0 a 23) Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - A 'Hora início' deve ser maior ou igual a 0 - A 'Hora início' deve ser menor ou igual a 23 Este campo é mantido na coluna HORA_INICIO da tabela [REST_HORA_APONT](dados_rest_hora_apont). |
| **Minuto início** | Minuto de início (0 a 59) Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - O 'Minuto fim' deve ser maior ou igual a 0 - O 'Minuto início' deve ser menor ou igual a 59 Este campo é mantido na coluna MINUTO_INICIO da tabela [REST_HORA_APONT](dados_rest_hora_apont). |
| **Hora fim** | Hora de fim do período de disponibilidade (0 a 23). Tentativas de apontamentos que excedem este limite serão bloqueadas e devem ser corrigidas pelo solucionador que está realizando o apontamento. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - A 'Hora fim' deve maior ou igual a 0 - A 'Hora fim' deve ser menor ou igual a 23 Este campo é mantido na coluna HORA_FIM da tabela [REST_HORA_APONT](dados_rest_hora_apont). |
| **Minuto fim** | Minuto de fim da disponibilidade (0 a 59). Tentativas de apontamentos que excedem este limite serão bloqueadas e devem ser corrigidas pelo solucionador que está realizando o apontamento. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - O 'Minuto fim' deve ser maior ou igual a 0 - O 'Minuto fim' deve ser menor ou igual a 59 Este campo é mantido na coluna MINUTO_FIM da tabela [REST_HORA_APONT](dados_rest_hora_apont). |

# RestricaoHorarioApontamento

Caminho: Customização > Modelo de objetos > Recurso > RestricaoHorarioApontamento

Faixas de horários em dias da semana onde são possíveis apontamentos de um determinado tipo.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ContratoId** | Número sequencial gerado automaticamente pelo sistema para Identificar um Contrato | Inteiro |
| **HoraFim** | Hora de fim do período de disponibilidade (0 a 23). Tentativas de apontamentos que excedem este limite serão bloqueadas e devem ser corrigidas pelo solucionador que está realizando o apontamento. | Inteiro |
| **HoraInicio** | Hora de início do período de disponibilidade (0 a 23) | Inteiro |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um RestricaoHorarioApontamento | Inteiro |
| **MinutoFim** | Minuto de fim da disponibilidade (0 a 59). Tentativas de apontamentos que excedem este limite serão bloqueadas e devem ser corrigidas pelo solucionador que está realizando o apontamento. | Inteiro |
| **MinutoInicio** | Minuto de início (0 a 59) | Inteiro |
| **TipoApontamentoId** | Identificador do TipoApontamento associado | Inteiro |

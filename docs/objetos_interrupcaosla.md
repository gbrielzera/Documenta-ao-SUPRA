# InterrupcaoSLA

Caminho: Customização > Modelo de objetos > Processo > InterrupcaoSLA

Apontamento de interrupção de contagem de tempo estabelecido em Acordo de Nível de Serviço

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AcordoInterrupcaoSLA** | Acordo para Interrupção de cronometragem de tempo de atendimento de ocorrências. | [AcordoInterrupcaoSLA](objetos_acordointerrupcaosla) |
| **AcordoNivelServicoId** | Identificador do Acordo de Nível de Serviço | Inteiro |
| **AtividadeGeradora** | Atividade de Processo que gerou a interrupção de ANS | [Atividade](objetos_atividade) |
| **AtividadeGeradoraId** | Identificador da Atividade de Processo que gerou a interrupção de ANS | Inteiro |
| **Comentario** | Comentário ou justificativa sobre a interrupção. Este comentário é replicado como evento da Ordem de Serviço e em caso de motivo que exija aprovação esta informação é exibida na página de aprovçavação do Autoatendimento. | String |
| **DataHoraFim** | Data/hora de fim da interrupção | Data/hora |
| **DataHoraFimPrevisto** | Data e hora previsto para finalização da interrupção. Após este momento é reiniciada a contagem de tempo do acordo. | Data/hora |
| **DataHoraInicio** | Data/hora de início da interrupção | Data/hora |
| **EnviouAviso** | Indica que foi enviado o aviso prévio sobre fim da interrupção programada. | Booleano |
| **MotivoInterrupcaoId** | Identificador da AcordoInterrupcaoSLA associada | Inteiro |
| **OrdemServicoId** | Identificador da Ordem de Serviço | Inteiro |
| **QuantidadeHorasAvisoFimPrevisto** | Quantidade de horas anterior ao fim previsto utilizado para envio de aviso. O comunicado é configurado como um Tipo de Evento e visualizado na aba de comunicados da Ordem de Serviço. | Inteiro |
| **Situacao** | Situação | [SituacaoInterrupcaoSLA](enum_situacaointerrupcaosla) |
| **TempoInterrupcao** | Tempo de interrução (em minutos) resultado da interrupção. Neste tempo já é considerada a disponibilidade de serviço definida no Acordo de Nível de Serviço firmado com o Cliente. Este valor é calculado pela rotina de finalização de interrupção de ANS. | Inteiro |

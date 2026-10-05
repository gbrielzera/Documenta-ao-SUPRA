# AcordoInterrupcaoSLA

Caminho: Customização > Modelo de objetos > Recurso > AcordoInterrupcaoSLA

Motivos de interrupção habilitados para o Acordo de Nível de Serviço. Um motivo pode estar condicionado a uma aprovação.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AcordoNivelServicoId** | Identificador do Acordo de Nível de Serviço proprietário da regra de interrupção de cronometragem de tempo. | Inteiro |
| **Aprovadores** | Aprovadores para a interrupção. Interrupções sem definição de aprovador são automaticamente aprovadas e consideradas no tempo restante de atendimento. | [Lista de AprovadorInterrupcao](objetos_aprovadorinterrupcao) |
| **MotivoInterrupcao** | Motivo de interrupção da cronometragem de tempo de atendimento de uma ocorrência. | [MotivoInterrupcaoSLA](objetos_motivointerrupcaosla) |
| **MotivoInterrupcaoId** | Identificador do Motivo de interrução para cronometragem de tempo de atendimento. | Inteiro |

# FluxoSequencia

Caminho: Customização > Modelo de objetos > Processo > FluxoSequencia

Fluxo de Sequência entre duas Atividades

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AcopladoOrigem** | Indica que um Evento está acoplado na atividade de origem. Válido somente para eventos intermediários. No caso de evento intermediário com este valor falso o evento significa um atraso programado no processo. | Booleano |
| **AtividadeDestino** | Uma Atividade de Processo corresponde a Tarefas, Subprocessos e Eventos de Processos. | [Atividade](objetos_atividade) |
| **AtividadeDestinoId** | Atividade de Destino associada | Inteiro |
| **AtividadeOrigemId** | Atividade de Origem | Inteiro |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um FluxoSequencia | Inteiro |

# ExecucaoGateway

Caminho: Customização > Modelo de objetos > Processo > ExecucaoGateway

Execução Gateway

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AlternativaSelecionada** | Alternativa selecionada pela avaliação | [Emissor](objetos_emissor) |
| **Cancelado** | Indica que a execução do gateway foi cancelada pelo usuário utilizando o comando Voltar do assistente de processos. | Booleano |
| **DataHoraExecucao** | Data e hora em que foi executado o Gateway | Data/hora |
| **EmissorId** | Identificador do(a) Emissor associado(a) | Inteiro |
| **Motivo** | Motivo informado pelo usuário para tomada de decisão. | String |
| **OcorrenciaId** | Identificador da Ocorrência | Inteiro |
| **Responsavel** | Pessoa que realizou a Decisão. Pode ser nulo se a Decisão foi realizada automaticamente pelo sistema. | [Pessoa](objetos_pessoa) |
| **ResponsavelId** | Identificador do Responsável pela tomada de Decisão | Inteiro |
| **Sequencial** | Sequencial de execução do Gateway em uma Ordem de Serviço | Inteiro |

# Emissor

Caminho: Customização > Modelo de objetos > Processo > Emissor

Saída de um Gateway

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Atividade** | Atividade de destino do fluxo para a alternativa. | [Atividade](objetos_atividade) |
| **AtividadeId** | Identificador da Atividade de destino se for selecionada a alternativa. Se preenchido então obrigatoriamente o campo GatewaySaida será nulo. | Inteiro |
| **GatewayId** | Identificador do gateway proprietário da alternativa. | Inteiro |
| **GatewaySaida** | Gateway de destino da alternativa. Se preenchido então obrigatoriamente o campo Atividade será nulo. | [Gateway](objetos_gateway) |
| **GatewaySaidaId** | Identificador do Gateway de destino do fluxo se for selecionada a alternativa. Se preenchido então obrigatoriamente o campo Atividade será nulo. | Inteiro |
| **Id** | Identificador da alternativa. | Inteiro |
| **MotivoObrigatorio** | Indica que o preenchimento de um motivo é obrigatório se for selecionada a alternativa. Este campo só faz sentido no caso de decisões baseaadas em respostas do usuário. | Booleano |
| **PermiteCancelarPubAA** | Permite o cancelamento da publicação no Autoatendimento da resposta informada pelo solucionador. Caso não seja permitido cancelar, apenas os superiores do solucionador poderão cancelar a publicação (independente desse parâmetro). | Booleano |
| **PublicarRespostaAA** | A resposta informada pelo solucionador fica disponível no Autoatendimento para visualização dos interessados | Booleano |
| **ReferenciaDecision** | Texto utilizado para representar a decisão. No caso de decisões baseadas em eventos este mesmo texto é utilizado como opção de resposta para que o usuário tome sua decisão. | String |
| **RotuloMotivo** | Texto que é apresentado para o usuário quando este seleciona a alternativa. Este campo é válido somente para decisões baseadas em respostas. | String |
| **SequenciaAvaliacao** | Sequencia utilizada durante avaliação das alternativas. Esta sequência pode influenciar na lógica da decisão visto que o processo seguirá a primeira que atender a fórmula de seleção. | Inteiro |
| **ValorComparacaoDecision** | Fórmula Python utilizada para comparação com a outra fórmula definda na decisão | String |

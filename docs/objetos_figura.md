# Figura

Caminho: Customização > Modelo de objetos > Processo > Figura

Representa graficamente alguma ferramenta de modelagem BPMN - Business Processs Management Notation

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Atividade** | Uma Atividade de Processo corresponde a Tarefas, Subprocessos e Eventos de Processos. | [Atividade](objetos_atividade) |
| **AtividadeId** | Identificador da Atividade associada com a Figura | Inteiro |
| **ComentarioVisivelAA** | Indica que o comentário é visível nas páginas de abertura, consulta ou aprovação da aplicação de Autoatendimento. | Booleano |
| **Controle** | Controles | [Controle](objetos_controle) |
| **ControleId** | Identificador do(a) Controle associado(a) | Inteiro |
| **DataObjectEstado** | Indica a situação do Data Object antes ou após o processamento | String |
| **DataObjectProduzidoTermino** | Indica que o Data Object é produzido ao término da Atividade (Saída) | Booleano |
| **DataObjectRequeridoInicial** | Indica que o Data Object é requerido para início da Atividade (Entrada) | Booleano |
| **DiagramaId** | Número sequencial gerado automaticamente pelo sistema para Identificar um Diagrama | Inteiro |
| **EventosIntermediarios** | Eventos intermediários | [Lista de FiguraAtividadeEventoIntermediario](objetos_figuraatividadeeventointermediario) |
| **Gateway** | Representa uma Decisão ou Merge a ser tomado durante a execução do Processo | [Gateway](objetos_gateway) |
| **GatewayId** | Identificador do Gateway associado a Figura | Inteiro |
| **Height** | Altura da figura | Inteiro |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Figura | Inteiro |
| **Left** | Posição em X | Inteiro |
| **OperacaoAtividade** | Operação de uma Atividade | [OperacaoAtividade](objetos_operacaoatividade) |
| **OperacaoAtividadeId** | Identificador de uma Operação Atividade se for um Data Object | Inteiro |
| **Texto** | Texto livre sobre a informação | String |
| **Tipo** | Tipo de Figura | [TipoFigura](enum_tipofigura) |
| **TipoAtividade** | Tipo de Figura associada com atividade de processo | [TipoFiguraAtividade](enum_tipofiguraatividade) |
| **TipoDataObject** | Tipo de Data Object representado pela figura. Data Objects são representações gráficas de Operações de Atividades. | [TipoFiguraDataObject](enum_tipofiguradataobject) |
| **TipoEvento** | Tipo de evento (somente para Atividades do tipo Evento) | [TipoFiguraEvento](enum_tipofiguraevento) |
| **TipoGateway** | Tipo de Gateway representado pela figura. | [GatewayType](enum_gatewaytype) |
| **Top** | Posição em Y | Inteiro |
| **Width** | Largura da figura | Inteiro |

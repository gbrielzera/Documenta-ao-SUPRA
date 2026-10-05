# Gateway

Caminho: Customização > Modelo de objetos > Processo > Gateway

Representa uma Decisão ou Merge a ser tomado durante a execução do Processo

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Alternativas** | Alternativas | [Lista de Emissor](objetos_emissor) |
| **Codigo** | Código utilizado por scripts para tomar alguma decisão ou gerar alguma informação após execução do Gateway. O código deve ser único dentro de uma versão do Subprocesso. | String |
| **Descricao** | Rótulo que descreve a decisão. No caso de decisões baseadas em eventos este mesmo texto é utilizado como texto da pergunta para decisão. | String |
| **EmissorDefault** | Indica a saída default para Gateways do tipo Inclusive OR Decision | [Emissor](objetos_emissor) |
| **EmissorId** | Número sequencial gerado automaticamente pelo sistema para Identificar um Emissor | Inteiro |
| **Entradas** | Atividades de Entrada | [Lista de Receptor](objetos_receptor) |
| **ExpressaoComparacaoDecision** | Fórmula Python para Decisão. A expressão pode conter operadores e propriedades do item de processo (campos de Ordens de Serviço por exemplo) | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Gateway | Inteiro |
| **Referencia** | Texto descrevendo o processo de tomada de Decisão. Especificar principais entradas, saídas e Papéis envolvidos. | String |
| **SubProcessoId** | Identificador do Subprocesso | Inteiro |
| **Tipo** | Tipo de Gateway que pode ser Fork, Inclusive Decision etc. | [TipoGateway](enum_tipogateway) |

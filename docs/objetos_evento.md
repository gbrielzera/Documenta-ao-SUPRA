# Evento

Caminho: Customização > Modelo de objetos > Processo > Evento

Um Evento é um fato ocorridos durante o ciclo de vida de uma Ocorrência de Processo. Um evento pode ser utilizado para envio de um comunicado. Esta função pode ser configurada no cadastro do Tipo de Evento associado.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **DataHoraEvento** | Data e hora de ocorrência do Evento | Data/hora |
| **DisponivelAA** | Indica que o evento está disponível na página de consultas do Autoatendimento | Booleano |
| **Mensagem** | Mensagem detalhada do evento. A mensagem pode ser configurada por fórmula no Tipo de Evento associado. | String |
| **NomeAutor** | Nome da pessoa responsável pela geração do evento. | String |
| **OcorrenciaId** | Identificador da Ocorrência proprietária do Evento | Inteiro |
| **PermiteCancelarPublicacaoAA** | Permite o cancelamento da publicação no Autoatendimento da resposta informada pelo solucionador. Caso não seja permitido cancelar, apenas os superiores do solucionador poderão cancelar a publicação (independente desse parâmetro). | Booleano |
| **Responsavel** | Pessoa que gerou o Evento | [Pessoa](objetos_pessoa) |
| **ResponsavelId** | Identificador do Solucionador responsável associado ao Evento. | Inteiro |
| **TipoEvento** | Um Tipo de Evento define um marco (evento) ocorrido em uma Ocorrência de Processo. Este evento pode ser publicado para o Cliente para que este realize o acompanhamento da sua solicitação. Um Tipo de Evento pode representar também uma ferramenta de envio de comunicados para Pessoas diversas. | [TipoEvento](objetos_tipoevento) |
| **TipoEventoId** | Identificador do Tipo de Evento associado | Inteiro |

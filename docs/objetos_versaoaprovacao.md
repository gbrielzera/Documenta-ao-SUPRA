# VersaoAprovacao

Caminho: Customização > Modelo de objetos > Processo > VersaoAprovacao

Versão para Aprovação

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ApropriacoesAprovacao** | Versão da Aprovação | [Lista de ApropriacaoAprovacao](objetos_apropriacaoaprovacao) |
| **Aprovadores** | Aprovadores da Versão | [Lista de Aprovacao](objetos_aprovacao) |
| **AssuntoAprovacaoId** | Número sequencial gerado automaticamente pelo sistema para Identificar um AssuntoAprovacao | Inteiro |
| **DataHoraCriacao** | Data e hora de Criação da Versão | Data/hora |
| **DataHoraFim** | Data e hora de fim do processo de Aprovação. | Data/hora |
| **DataHoraInicio** | Data e hora de início do processo de Aprovação | Data/hora |
| **DataHoraUltimoComunicado** | Data e hora do último email de aprovação enviado. Dependendo da configuração do processo é possível repetir o envio e sempre que isto ocorrer esta propriedade será atualizada. | Data/hora |
| **Escopo** | Texto contendo o Escopo para Aprovação. Quando preenchido é apresentado para o usuário na aplicação de aprovação de Ocorrências. | String |
| **InterrupcaoSLA** | Apontamento de interrupção de contagem de tempo estabelecido em Acordo de Nível de Serviço | [InterrupcaoSLA](objetos_interrupcaosla) |
| **InterrupcaoSLAAcordoNivelServicoId** | Identificador da InterrupcaoSLA associada | Inteiro |
| **InterrupcaoSLADataHoraInicio** | Identificador da InterrupcaoSLA associada | Data/hora |
| **InterrupcaoSLAMotivoInterrupcaoId** | Identificador da InterrupcaoSLA associada | Inteiro |
| **InterrupcaoSLAOrdemServicoId** | Identificador da InterrupcaoSLA associada | Inteiro |
| **ItensAprovacao** | Itens para Aprovação | [Lista de ItemAprovacao](objetos_itemaprovacao) |
| **PassoCorrente** | Indica nível hierarquico de aprovação | Inteiro |
| **Situacao** | Situação para a Versão a ser Aprovada. | [SituacaoAprovacao](enum_situacaoaprovacao) |
| **Versao** | Sequencial gerado automaticamente pelo sistema para cada Assunto de uma determinada Ordem de Serviço | Inteiro |

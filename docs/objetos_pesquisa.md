# Pesquisa

Caminho: Customização > Modelo de objetos > Processo > Pesquisa

Uma Pesquisa de Satisfação é composta por um formulário enviado para Clientes após finalização de uma Ordem de Serviço. As respostas coletadas destas pesquisas podem ser utilizadas para construção de Indicadores de Desempenho - KPI's.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Assunto** | Assunto abordado pela Pesquisa de Satisfação | String |
| **Avaliador** | Avaliador da Pesquisa de Satisfação | [Pessoa](objetos_pessoa) |
| **AvaliadorId** | Identificador do Avaliador da Pesquisa | Inteiro |
| **ClassePesquisaSatisfacao** | Uma Classe de Pesquisa de Satisfação define um conjunto de configurações utilizado para geração de Pesquisas de Satisfação enviadas para clientes após finalização de uma Ordem de Serviço. O envio da pesquisa está condicionado ao evento terminador utilizado na definição do processo aplicado em Ordens de Serviço alvo da pesquisa. | [ClassePesquisaSatisfacao](objetos_classepesquisasatisfacao) |
| **ClassePesquisaSatisfacaoId** | Identificador do ClassePesquisaSatisfacao associado | Inteiro |
| **ComentarioAvaliador** | Comentário gravado pelo Avalidador no instante em que a Pesquisa é respondida | String |
| **DataHoraCriacao** | Data e hora que a Pesquisa de Satisfação foi gerada. | Data/hora |
| **DataHoraResposta** | Data e hora em que foi respondida a Pesquisa | Data/hora |
| **EscoreGeral** | Avaliação geral | Inteiro |
| **Id** | Identificador da Pesquisa de Satisfação. | Inteiro |
| **Itens** | Item a ser avaliado em uma Pesquisa | [Lista de ItemPesquisa](objetos_itempesquisa) |
| **MotivoCancelamento** | Motivo de Cancelamento da Pesquisa | String |
| **OrdemServico** | Uma Ordem de Serviço é uma ocorrência de Processo em atendimento a uma solicitação de serviço de Tecnologia da Informação. Ordens de Serviço podem ser abertas na aplicação de Autoatendimento ou na transação Workspace do sistema Supravizio. | [OrdemServico](objetos_ordemservico) |
| **OrdemServicoId** | Identificador do OrdemServico associado | Inteiro |
| **QuestaoGeral** | Questão que é exibida no fim da Pesquisa de Satisfação para obter a satisfação geral do Cliente | [QuestaoPesquisa](objetos_questaopesquisa) |
| **QuestaoGeralId** | Identificador da QuestaoPesquisa associada | Inteiro |
| **RespondidaAutoAtendimento** | Indica que a Pesquisa de Satisfação foi respondida pelo Cliente utilizando a aplicação de Autoatendimento. | Booleano |
| **ResponsavelCancelamento** | Pessoa responsável pelo Cancelamento da Pesquisa de Satisfação | [Pessoa](objetos_pessoa) |
| **ResponsavelCancelamentoId** | Identificador da Pessoa associada | Inteiro |
| **Situacao** | Indica a Situação da Pesquisa de Satisfação. | [SituacaoPesquisaSatisfacao](enum_situacaopesquisasatisfacao) |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Pesquisa Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Pesquisa | Pesquisa Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Pesquisa Carrega(string nomePropriedade, object valorPropriedade); |

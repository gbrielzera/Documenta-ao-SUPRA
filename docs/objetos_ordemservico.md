# OrdemServico

Caminho: Customização > Modelo de objetos > Processo > OrdemServico

Uma Ordem de Serviço é uma ocorrência de Processo em atendimento a uma solicitação de serviço de Tecnologia da Informação. Ordens de Serviço podem ser abertas na aplicação de Autoatendimento ou na transação Workspace do sistema Supravizio.

Este tipo herda atributos e funcionalidades do ancestral [Ocorrencia](objetos_ocorrencia)

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Categoria** | Classificação manual atribuída a Ordens de Serviço associadas com uma cor e com possibilidade de exibição na barra de rolagem de Ordens de Serviço. Para definição das cores é utilizado o modelo RGB que é baseado na teoria de visão colorida tricromática. | [Categoria](objetos_categoria) |
| **CategoriaId** | Identificador da Categoria atribuída manualmente a Ordem de Serviço. | Inteiro |
| **Causa** | Causa | String |
| **CelularCliente** | Telefone celular para contato com o Cliente | String |
| **ClassePesquisaSatisfacao** | Classe de Pesquisa de Satisfação para geração de Pesquisa. Esta referência é estabelecida na operação de Finalização e utilizada pela rotina que realiza o envio de Pesquisa de Satisfação. | [ClassePesquisaSatisfacao](objetos_classepesquisasatisfacao) |
| **ClassePesquisaSatisfacaoId** | Identificador do ClassePesquisaSatisfacao associado | Inteiro |
| **ComentarioContato** | Comentários gerais sobre contatos com o Cliente | String |
| **ContatoResponsavelFornecedor** | Informações de contato no Forncedor incluindo solucionador responsável, email e telefone quando possível. | String |
| **Contrato** | Contrato da Ordem de Serviço | [Contrato](objetos_contrato) |
| **ContratoId** | Identificador do Contrato associado | Inteiro |
| **DataHoraExecucaoMudanca** | Data/hora em que foi Executada a Mudança o ambiente | Data/hora |
| **DescricaoDetalhada** | Descrição detalhada da solicitação do Cliente | String |
| **ExpirouTempoSLA** | Indica que o tempo determinado para entrega do serviço foi vencido. Todos os níveis tiveram o seu tempo vencido sem que ocorresse resolução do incidente ou atendimento. | Booleano |
| **Favorecido** | Pessoa | [Pessoa](objetos_pessoa) |
| **FavorecidoId** | Identificador do Favorecido | Inteiro |
| **GrauPrioridadeCalculado** | Prioridade inicialmente definida para a Ordem de Serviço | [GrauPrioridade](objetos_grauprioridade) |
| **GrauPrioridadeCalculadoId** | Identificador do Grau da Prioridade inicialmente definido para a Ordem de Serviço. | Inteiro |
| **GrauPrioridadeSelecionado** | Grau Prioridade selecionado | [GrauPrioridade](objetos_grauprioridade) |
| **GrauPrioridadeSelecionadoId** | Identificador do Grau de Prioridade selecionado | Inteiro |
| **HardwareAutoAtendimento** | Computador identificado pela aplicação de Autoatendimento no instante da abertura do chamado | String |
| **Interrupcoes** | Interrupções de cronometragem de tempo de atendimento definido em Acordo de Nível de Serviço | [Lista de InterrupcaoSLA](objetos_interrupcaosla) |
| **ItemSLA** | Critério de atendimento escolhido no Acordo de Nível de Serviço estabelecido com a área do Cliente | [ItemSLA](objetos_itemsla) |
| **ItemSLAId** | Identificador do critério de atendimento escolhido no Acordo de Nível de Serviço estabelecido com a área do Cliente | Inteiro |
| **Justificativa** | Justificativa fornecida pelo Cliente para atendimento do Serviço | String |
| **LeituraResponsavel** | Indica que o responsável atual pela Ordem de Serviço leu o conteúdo da Ordem de Serviço (visualizou na tela de edição). | Booleano |
| **MetodoPriorizacao** | Método utilizado para Priorização da Ordem de Serviço | [MetodoPriorizacao](objetos_metodopriorizacao) |
| **MetodoPriorizacaoId** | Identificador do MetodoPriorizacao associado | Inteiro |
| **NivelSLA** | Nível de ANS define faixas de tempo para escalonamento de ANS em um Método de Priorização (por exemplo Incidentes). | [NivelSLA](objetos_nivelsla) |
| **NivelSLAId** | Identificador da NivelSLA associada | Inteiro |
| **NumeroReferenciaFornecedor** | Número de referência para Chamado registrado no Fornecedor do Serviço | String |
| **Origem** | Origem da Ordem de Serviço: Workspace, Autoatendimento ou Eventos do Processo | [OrigemOrdemServico](enum_origemordemservico) |
| **PesoPrioridadeCalculado** | Peso prioridade calculado | Inteiro |
| **PesoPrioridadeSelecionado** | Peso prioridade selecionado | Inteiro |
| **SegundoContato** | Segunda pessoa para contato com o Solicitante da Ordem de Serviço | String |
| **Servico** | Serviço prestado pela Ocorrência de Processo. | [Servico](objetos_servico) |
| **ServicoId** | Identificador do Serviço associado | Inteiro |
| **SintomaAnalisado** | Sintoma analisado por um Solucionador. Este texto é utilizado em Incidentes para associação de Incidentes pelo próprio Cliente no site de Autoatendimento. | String |
| **SituacaoPesquisa** | Situação quanto ao Envio de Pesquisa de Satisfação | [SituacaoEnvioPesquisaSatisfacao](enum_situacaoenviopesquisasatisfacao) |
| **SLA** | ANS calculado para Ordem de Serviço | [Lista de SLAOrdemServico](objetos_slaordemservico) |
| **Solucao** | Solução | String |
| **TelefoneCliente** | Telefone de contato do Cliente | String |
| **TelefoneSegundoContato** | Telefone do Segundo contato | String |
| **TempoInterrupcaoSLA** | Tempo total de interrupção da contagem de tempo do Acordo de Nível de Serviço. Este tempo é mantido pela inclusão/aprovação de registros de interrupção de ANS definidos no Acordo de Nível de Serviço. | Inteiro |
| **TempoSLA** | Tempo em minutos para ANS. | Inteiro |
| **UsuarioAutoAtendimento** | Usuário reconhecido pela aplicação de Autoatendimento. Este campo só é preenchido quando a Ordem de Serviço é aberta na aplicação de Autoatendimento. | String |
| **ValorChargeBack** | Valor para cobrança pela rotina de Charge-back. | Decimal |
| **VariaveisPriorizacao** | Valores utilizados nas variáveis de Priorização. | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **RegistraEntregaServico** | Registra a Entrega do Serviço informando a Data/hora de Execução de mudança no ambiente. Após o registro da entrega a cronometragem de ANS é finalizada. | Venki.Supravizio.Processo.OrdemServico RegistraEntregaServico(System.DateTime? dataHoraExecMudanca); |
| **ObtemMaiorValorFatorPrioridadeItensConfiguracao** | Obtem o maior Valor de Fator de Prioridade entre todos os Itens de Configuração associados com a Ordem de Serviço. Se nenhum Item de Configuração possui um Fator de Prioridade ou se a Ordem de Serviço não possui associação com Itens então retorna o valor default fornecido como parâmetro. | System.Int32 ObtemMaiorValorFatorPrioridadeItensConfiguracao(System.Int32 valorDefault); |
| **ObtemMenorValorFatorPrioridadeItensConfiguracao** | Obtem o menor Valor de Fator de Prioridade entre todos os Itens de Configuração associados com a Ordem de Serviço. Se nenhum Item de Configuração possui um Fator de Prioridade ou se a Ordem de Serviço não possui associação com Itens então retorna o valor default fornecido como parâmetro. | System.Int32 ObtemMenorValorFatorPrioridadeItensConfiguracao(System.Int32 valorDefault); |
| **Finaliza** | Finaliza uma Ordem de Serviço | Venki.Supravizio.Processo.Ocorrencia Finaliza(string codigoAtividade, string causa, string solucao,DateTime dataHoraExecucaoMudanca); |
| **ObtemServicosImpactados** | Este método retorna uma lista de Serviços impactados por mudanças ou falhas ocorridas nos Itens de Configuração associados na Ordem de Serviço. Com esta lista de Serviços é possível, por exemplo, identificar os gestores de sistemas ou serviços de rede que necessitam ser notificados sobre qualquer evento em TI. Para calcular esta lista o sistema utiliza a ferramenta de Análise de Impacto do módulo de Ativos que realiza uma consulta em todos os relacionamentos cadastrados. | Venki.Supravizio.Processo.ServicoList ObtemServicosImpactados(); |
| **ObtemUsuariosImpactados** | Este método retorna uma lista de Usuários impactados por mudanças ou falhas ocorridas nos Itens de Configuração associados na Ordem de Serviço. Para calcular esta lista o sistema utiliza a ferramenta de Análise de Impacto do módulo de Ativos que realiza uma consulta em todos os relacionamentos cadastrados. | Venki.Supravizio.Recurso.PessoaList ObtemUsuariosImpactados(); |
| **ObtemOrgaosImpactados** | Este método retorna uma lista de Órgãos impactados por mudanças ou falhas ocorridas nos Itens de Configuração associados na Ordem de Serviço. Para calcular esta lista o sistema utiliza a ferramenta de Análise de Impacto do módulo de Ativos que realiza uma consulta em todos os relacionamentos cadastrados. Os Órgãos impactados são aqueles onde estão lotados os usuários impactados. | Venki.Supravizio.Recurso.OrgaoList ObtemOrgaosImpactados(); |
| **ObtemVariavelPrioridade** | Recupera o valor atribuído a variável fornecida como parâmetro. A recuperação da variável utiliza comparação por nomes insensível a caixa de texto. Se não encontrar a variável então retorna o valor -1. | int ObtemVariavelPrioridade(string nomeVariavel); |
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | OrdemServico Carrega(int i); |
| **Novo** | Cria um novo registro do tipo OrdemServico | OrdemServico Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | OrdemServico Carrega(string nomePropriedade, object valorPropriedade); |

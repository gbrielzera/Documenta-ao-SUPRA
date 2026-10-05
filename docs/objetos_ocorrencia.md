# Ocorrencia

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia

Ocorrências de Processos

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AcoesExecutadasEmAcordos** | Ações configuradas em Acordos de Nível Operacional que foram executadas pela Ocorrência | [Lista de ExecucaoAcaoAcordo](objetos_execucaoacaoacordo) |
| **Assunto** | Texto resumido que descreve o assunto da ocorrência. | String |
| **Assuntos** | Assuntos | [Lista de AssuntoAprovacao](objetos_assuntoaprovacao) |
| **Atividade** | Atividade corrente na Ocorrência | [Atividade](objetos_atividade) |
| **AtividadeId** | Identificador da Atividade corrente da Ocorrência. | Inteiro |
| **AtividadesExecutadas** | Atividades Executadas | [Lista de ExecucaoAtividade](objetos_execucaoatividade) |
| **Atores** | Atores | [Lista de Ator](objetos_ator) |
| **ClasseNegocio** | Classe de Negócio que implementa a Token. Este valor é alimentado automaticamente pelo sistema assim que o item é Classficado. | [ClasseNegocio](enum_classenegocio) |
| **ClasseSubProcesso** | Um Tipo de Subprocesso mantém características de um fluxo que são invariáveis entre suas diversas versões. | [ClasseSubProcesso](objetos_classesubprocesso) |
| **ClasseSubProcessoId** | Identificador do tipo de Subprocesso da ocorrência. Este tipo se refere a um Subprocesso definido na versão de processo também associada a ocorrência e define os fluxos e responsabilidade de processo. | Inteiro |
| **ClasseSubProcessoInicial** | Tipo de de Subprocesso inicialmente atribuído para a Ocorrência. | [ClasseSubProcesso](objetos_classesubprocesso) |
| **ClasseSubProcessoInicialId** | Identificador do Tipo de Subprocesso inicialmente atribuído a Ocorrência. | Inteiro |
| **Cliente** | Cliente que solicitou o Serviço | [Pessoa](objetos_pessoa) |
| **ClienteId** | Identificador da pessoa que solicitou o serviço. | Inteiro |
| **DataHoraCriacao** | Data e hora de criação da ocorrência. Esta data é preenchida automaticamente pelo sistema e não pode ser modificada pelo usuário. | Data/hora |
| **DataHoraFimPlan** | Data e hora de fim de planejamento | Data/hora |
| **DataHoraFimPrevisto** | Data e hora prevista para términdo do atendimento. A previsão de fim pode sofrer diversas modificações no decorrer do atendimento. | Data/hora |
| **DataHoraFimPrevistoOriginal** | Data/hora original de finalização prevista | Data/hora |
| **DataHoraFimReal** | Data/hora fim real | Data/hora |
| **DataHoraInicioPlan** | Data e hora de início planejado | Data/hora |
| **DataHoraInicioPrevisto** | Data e hora de início previsto de atendimento. O início previsto pode sofrer diversas modificações no decorrer do atendimento. | Data/hora |
| **DataHoraInicioReal** | Data/hora início real | Data/hora |
| **DataHoraResponsavel** | Data/hora em que foi definido o Responsável corrente da ocorrência. | Data/hora |
| **DataHoraSolicitacao** | Data e hora de solicitação da ocorrência. Esta data é preenchida automaticamente pelo sistema usando a Data/hora corrente e pode ser modificada pelo usuário (se este possui autorização para modificação de dados). | Data/hora |
| **DataHoraUltimaAtualizacao** | Data e hora da última atualização | Data/hora |
| **DesenhoProcesso** | Versão de Processo atribuída a uma Ocorrência | [DesenhoProcesso](objetos_desenhoprocesso) |
| **DesenhoProcessoId** | Identificador da versão de Processo da Ocorrência. | Inteiro |
| **DesenhoProcessoInicial** | Versão de Processo inicialmente atribuída a Ocorrência. Este valor é preserva por todo o ciclo de vida da Ocorrência. | [DesenhoProcesso](objetos_desenhoprocesso) |
| **DesenhoProcessoInicialId** | Identificador da Versão de Processo inicialmente atribuída a Ocorrência. | Inteiro |
| **EsforcoEstimado** | Esforço (em horas) estimado para finalização do serviço. | Inteiro |
| **Eventos** | Eventos de uma Ocorrência de Processo | [Lista de Evento](objetos_evento) |
| **Finalizador** | Pessoa que finalizou o registro | [Pessoa](objetos_pessoa) |
| **FinalizadorId** | Identificador da pessoa que finalizou a ocorrência. | Inteiro |
| **Gaps** | Gaps encontrados durante teste de um Controle. | [Lista de Gap](objetos_gap) |
| **GatewaysExecutados** | Execução Gateway | [Lista de ExecucaoGateway](objetos_execucaogateway) |
| **GrupoTrabalho** | Grupo de Trabalho responsável | [GrupoTrabalho](objetos_grupotrabalho) |
| **GrupoTrabalhoId** | Identificador do GrupoTrabalho responsável pela ocorrência. Assim como o campo Responsável o Grupo de trabalho é mantido pelo sistema quando executada a função de encaminhamento ou segundo papel definido em atividades do processo. | Inteiro |
| **GrupoTrabalhoInicial** | Grupo de Trabalho que iniciou o atendimento da Ocorrência. | [GrupoTrabalho](objetos_grupotrabalho) |
| **GrupoTrabalhoInicialId** | Identificador do Grupo de Trabalho inicial | Inteiro |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Ocorrência | Inteiro |
| **ItensAnexados** | Itens Anexados | [Lista de ItemOcorrencia](objetos_itemocorrencia) |
| **JustificativaEsforco** | Justificativa para valor de Esforço estimado | String |
| **MotivoCancelamento** | Texto descrevendo motivo pelo qual o registro foi cancelado. | String |
| **Numero** | Número formatado da Ocorrência | String |
| **OcorrenciaPaiId** | Identificador da ocorrência que invocou o processo da ocorrência. Este campo pode ser diferente de OcorrenciaPrincipal se existirem mais de dois níveis de chamada. | Inteiro |
| **OcorrenciaPrincipalId** | Identificador da ocorrência principal correspondente ao macro-fluxo que invocou a ocorrência. | Inteiro |
| **OrgaoCliente** | Órgão Cliente da solicitação | [Orgao](objetos_orgao) |
| **OrgaoClienteId** | Identificador do Orgao Cliente | Inteiro |
| **Pai** | Ocorrência pai | [Ocorrencia](objetos_ocorrencia) |
| **PermiteRetormarResponsabilidade** | Indica que é permitido ao último responsável retormar responsabilidade de uma ocorrência encaminhada para outro solucionador, seja o encaminhamento manual ou automático por configuração de processos. | Booleano |
| **Principal** | Ocorrências de Processos | [Ocorrencia](objetos_ocorrencia) |
| **PublicaApontamentosAA** | Caso o subprocesso permita que sejam publicados os apontamentos (PublicacaoApontamentosAutoAtendimento diferente de Nunca ou Sempre), sendo verdadeira esta propriedade seram exibidos os apontamentos no Autoatendimento. | Booleano |
| **ReferenciaCircular** | Indica que em algum momento da execução do processo ocorrêu um Loop infinito caracterizando referência circular entre as atividades de processos. | Booleano |
| **Responsavel** | Pessoa | [Pessoa](objetos_pessoa) |
| **ResponsavelId** | Identificador do Responsável pela ocorrência. A mudança de responsabilidade pode ocorrer em virtude de encaminhamentos ou automatismo de processo (segundo papéis definidos em atividades). | Inteiro |
| **ResponsavelInicial** | Primeiro Solucionador responsável pelo atendimento da Ocorrência. | [Pessoa](objetos_pessoa) |
| **ResponsavelInicialId** | Identificador do Solucionador que foi o primeiro responsável pela Ocorrência. | Inteiro |
| **Situacao** | Situação da ocorrência. | [Situacao](enum_situacao) |
| **SubProcesso** | Subprocesso corrente | [SubProcesso](objetos_subprocesso) |
| **SubProcessoId** | Identificador do SubProcesso corrente da ocorrência. Esta informação pode ser obtida também pelo relacionamento da entidade Atividade e está aqui por questão de desempenho da aplicação. | Inteiro |
| **UsuarioAutenticado** | Usuário que foi autenticado pela aplicação de Autoatendimento durante a abertura. Esta autenticação só é possível se não for selecionada a opção de troca de Cliente no Autoatendimento. | [Pessoa](objetos_pessoa) |
| **UsuarioAutenticadoId** | Identificador do usuário autenticado | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Cancela** | Cancela a ocorrência. | Venki.Supravizio.Processo.Ocorrencia Cancela(string motivo); |
| **Reabre** | Reabre uma ocorrência já finalizada. | Venki.Supravizio.Processo.Ocorrencia Reabre(Venki.Supravizio.Recurso.Pessoa autor); |
| **PossuiPapel** | Obtem indicador de que a Pessoa passada como parâmetro possui determinado Papel no Processo. | bool PossuiPapel(int Ocorrencia, Venki.Supravizio.Recurso.Pessoa pessoa, int idPapel); |
| **IniciaAprovacao** | Inicia Workflow de Aprovação com base na última Versão em Elaboração | Venki.Supravizio.Processo.Ocorrencia IniciaAprovacao(); |
| **ValidaPendencias** | Realiza a Validação e retorna um valor Booleando indicando que existem ou não Pendências relativas ao Processo. Se NÃO existirem pendências então retorna Verdadeiro caso contrário retorna Falso. | bool ValidaPendencias(); |
| **ValidaPendenciasAprovacao** | Realiza a Validação e retorna um valor Booleando indicando que existem ou não Pendências relativas a Versão para Aprovação. Se NÃO existirem pendências então retorna Verdadeiro caso contrário retorna Falso. | bool ValidaPendenciasAprovacao(int idAssuntoAprovacao, int versao); |
| **ValidaPendenciasAtividadeExecucao** | Realiza a Validação e retorna um valor Booleando indicando que existem ou não Pendências relativas a Atividade em Execução no momento. Se NÃO existirem pendências então retorna Verdadeiro caso contrário retorna Falso. | bool ValidaPendenciasAtividadeExecucao(); |
| **ObtemDerivadas** | Recupera Derivadas | Venki.Supravizio.Processo.OcorrenciaList ObtemDerivadas(); |
| **ObtemDerivada** | Recupera a Derivada referente a um Subprocesso | Venki.Supravizio.Processo.Ocorrencia ObtemDerivada(int idClasseSubProcesso); |
| **ObtemPrincipal** | Obtem item Principal. Se o item já for o Principal então retorna referência 'this' | Venki.Supravizio.Processo.Ocorrencia ObtemPrincipal(); |
| **ObtemDerivadas** | Recupera Derivadas de uma determinado tipo de Subprocesso | Venki.Supravizio.Processo.OcorrenciaList ObtemDerivadas(Venki.Supravizio.Processo.ClasseSubProcesso classeSubProcesso); |
| **ObtemAssociadasComoAlvo** | Retorna uma lista de ocorrências invocadas pela Ordem de Serviço. Se não existirem tais associações então é retornada uma lista instanciada em memória e vazia. Se o nome da associação fornecido como parâmetro não corresponder a uma Associação existente ou se a consulta for incompatível com as configurações da Associação encontrada então é retornada uma mensagem de erro. | Venki.Supravizio.Processo.OcorrenciaList ObtemAssociadasComoAlvo(string nomeAssociacao); |
| **ObtemAssociacaoComoFonte** | Retorna uma lista de ocorrências chamadoras da Ordem de Serviço. Se não existirem tais associações então é retornada uma lista instanciada em memória e vazia. Se o nome da associação fornecido como parâmetro não corresponder a uma Associação existente ou se a consulta for incompatível com as configurações da Associação encontrada então é retornada uma mensagem de erro. | Venki.Supravizio.Processo.OcorrenciaList ObtemAssociadasComoFonte(string nomeAssociacao); |
| **Agenda** | Agenda o atendimento de uma Ocorrência | Venki.Supravizio.Processo.Ocorrencia Agenda(DateTime dataInicio); |
| **Reabre** | Reabre uma Ocorrência | Venki.Supravizio.Processo.Ocorrencia Reabre(); |
| **Aponta** | Registra apontamento genérico de Ordem de Serviço. | void Aponta(string codigoClasseApontamento, string String1, string String2, int? Inteiro1, int? Inteiro2, DateTime? DataHora1, DateTime? DataHora2, Decimal? Decimal1, Decimal? Decimal2, bool? Booleano1, bool? Booleano2); |
| **ObtemHorasApontadas** | Obtem total de horas apontadas na Ordem de Serviço em um determinado período. A rotina retorna um número decimal (contendo casas decimais) que pode incluir apontamentos de Ordens de Serviço derivadas (Subprocessos). O filtro por período compara a data de início maior ou igual ao inicio dos apontamentos e a data de fim menor que a data de fim dos apontamentos. | decimal ObtemHorasApontandatas(DateTime dataInicio, DateTime dataFim, bool incluiDerivadas); |
| **CancelaAprovacao** | Cancela aprovações existentes em uma determinada Atividade de processo identificada pelo seu código. Se não existir uma versão para aprovação ou se existir e esta já tenha sido cancelada então esta rotina não possui nenhuma ação. | void CancelaAprovacao(string codigoAtividade); |
| **Reprova** | Reprova a última versão de um Assunto contido em uma Atividade de Processo. | void Reprova(string codigoAtividade, string motivo); |
| **Aprova** | Aprova a última versão de um Assunto contido em uma Atividade de Processo. | void Aprova(string codigoAtividade); |
| **AssociaItemConfiguracao** | Associa a Ordem de Serviço o Item de Configuração cujo Identificador é fornecido como parâmetro. Se o Item já foi associado a Ordem de Serviço anteriormente então não é executada nenhuma ação. Se não existir um Item de Configuração com o Identificador fornecido então é gerada uma mensagem. | void AssociaItemConfiguracao(int idItem); |
| **PossuiAprovacao** | Verifica se a aprovação vinculada a atividade de código fornecido como parâmetro foi finalizada como Aprovada. Esta rotina é constantemente utilizada em decisões baseadas em fórmulas. | bool PossuiAprovacao(string codigoAtividade); |
| **ObtemMotivoReprovacao** | Obtem textor formatado contendo o motivo de reprovação de uma Atividade. Se a atividade não possui uma operação de aprovação ou não for encontrada uma Atividade com o código fornecido ( a comparação é insensível a caixa ) ou a solicitação não foi realmente reprovada, então é retornada uma string vazia. | string ObtemMotivoReprovacao(string codigoAtividade); |
| **ObtemHardware** | Obtem um único item do tipo de Equipamento anexado na ocorrência de processo. Se não existir um item deste tipo ou se existirem vários itens então é retornada uma mensagem de erro. | Venki.Supravizio.Configuracao.Hardware ObtemHardware(); |
| **ObtemSoftware** | Obtem um único item do tipo Software anexado na ocorrência de processo. Se não existir um item deste tipo ou se existirem vários itens então é retornada uma mensagem de erro. | Venki.Supravizio.Configuracao.Software ObtemSoftware(); |
| **ObtemArtefato** | Obtem um único item do tipo Artefato anexado na ocorrência de processo. Se não existir um item deste tipo ou se existirem vários itens então é retornada uma mensagem de erro. | Venki.Supravizio.Configuracao.Artefato ObtemArtefato(); |
| **ObtemDispositivoTelefonico** | Obtem um único item do tipo Dispositivo telefônico anexado na ocorrência de processo. Se não existir um item deste tipo ou se existirem vários itens então é retornada uma mensagem de erro. | Venki.Supravizio.Configuracao.DispositivoTelefonico ObtemDispositivoTelefonico(); |
| **PossuiArtefato** | Verifica existe um ou mais Artefatos associados na Ordem de Serviço. Se existir retorna Verdadeiro caso contrário retorna Falso. | bool PossuiArtefato(); |
| **PossuiHardware** | Verifica existe um ou mais Equipamentos associados na Ordem de Serviço. Se existir retorna Verdadeiro caso contrário retorna Falso. | bool PossuiHardware(); |
| **PossuiSoftware** | Verifica existe um ou mais Softwares associados na Ordem de Serviço. Se existir retorna Verdadeiro caso contrário retorna Falso. | bool PossuiSoftware(); |
| **PossuiDispositivoTelefonico** | Verifica existe um ou mais Dispositivos Telefonicos associados na Ordem de Serviço. Se existir retorna Verdadeiro caso contrário retorna Falso. | bool PossuiDispositivoTelefonico(); |
| **PossuiItem** | Verifica existe um ou mais Itens de Configuração do tipo fornecido como parâmetro associado na Ordem de Serviço. Se existir retorna Verdadeiro caso contrário retorna Falso. | bool PossuiItem(string siglaClasseConfiguracao); |
| **ObtemItem** | Obtem um Item de Configuração do tipo fornecido como parâmetro associado a Ocorrência. Se não existir um Item ou existirem vários então retorna mensagem de erro. | Venki.Supravizio.Configuracao.ItemConfiguracao ObtemItem(string siglaClasseConfiguracao); |
| **ContaExecucaoAtividade** | Retorna a quantidade de execuções da Atividade identificada pelo código fornecido como parâmetro. Se a Atividade não foi executada ou não existir uma Atividade com o código informado é retornado o valor zero. | int ContaExecucaoAtividade(string codigoAtividade); |
| **ContaExecucaoGateway** | Retorna a quantidade de execuções do Gateway identificado pelo código fornecido como parâmetro. Se o Gateway não foi executada ou não existir um Gateway com o código informado é retornado o valor zero. | int ContaExecucaoGateway(string codigoGateway); |
| **ContaExecucaoGateway** | Retorna a quantidade de execuções da alternativa do Gateway identificado identificado pelo código fornecido como parâmetro. Se o Gateway e respectiva alternativa não foram executados ou não existir um Gateway com o código informado é retornado o valor zero. | int ContaExecucaoGateway(string codigoGateway, string textoAlternativa); |
| **ObtemConhecimento** | Obtem um único item do tipo Conhecimento anexado na ocorrência de processo. Se não existir um item deste tipo ou se existirem vários itens então é retornada uma mensagem de erro. | Venki.Supravizio.Configuracao.Conhecimento ObtemConhecimento(); |
| **ObtemTodasAssociadas** | Obtem todas as ocorrências associadas, sejam elas alvo, origem e derivadas em relação todo-parte | Venki.Supravizio.Processo.OcorrenciaList ObtemTodasAssociadas(bool recursivo); |
| **AnexaArquivo** | Transfere o arquivo para o repositório e anexa na ocorrência. Se o arquivo possui tamanho superior ao limite configurado no tipo fornecido como parâmetro então é gerada uma mensagem de erro. | void AnexaArquivo(string nomeArquivo, string siglaTipoItem, bool apagarArquivoOriginal); |
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Ocorrencia Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Ocorrencia | Ocorrencia Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Ocorrencia Carrega(string nomePropriedade, object valorPropriedade); |

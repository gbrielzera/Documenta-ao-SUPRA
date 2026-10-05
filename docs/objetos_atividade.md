# Atividade

Caminho: Customização > Modelo de objetos > Processo > Atividade

Uma Atividade de Processo corresponde a Tarefas, Subprocessos e Eventos de Processos.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Acoes** | Ações configuradas em função do prazo do Acordo de Nível Operacional. | [Lista de AcaoAcordo](objetos_acaoacordo) |
| **AnexarTodosDocumentos** | Quando o evento é utilizado para envio esta propriedade indica que todos os arquivos da Ordem de Serviço serão anexados no email. Se o evento se refere a chegada de um email então todos os arquivos anexados na mensagem serão anexados na Ordem de Serviço. | Booleano |
| **Associacao** | Uma Associação define características de interface entre dois Subprocessos. Na associação encontramos a cardinalidade (um para um ou um para muitos) e frases que facilitam a navegação entre ocorrências existentes. | [Associacao](objetos_associacao) |
| **AssociacaoId** | Identificador do Associacao associado | Inteiro |
| **AssociacoesSubprocesso** | Associações entre Subprocessos em iniciadores do tipo LinkInicial que originarão novas Ocorrências associadas | [Lista de AssociacaoSubprocesso](objetos_associacaosubprocesso) |
| **Ativo** | Indica se a Atividade está ativa ou inativa | Booleano |
| **CaixaEmail** | Caixa de email monitorada pela máquina de processos. Mensagens remetidas para estas caixas são processadas e em seguida removidas da caixa. Não é permitido o uso da caixa utilizada pela rotina de envio de emails e redirecionamentos. | [CaixaMensagem](objetos_caixamensagem) |
| **CaixaEmailId** | Identificador da caixa de email monitorada pela máquina de processos para os eventos intermediário e inicial por mensagem | Inteiro |
| **ChamadaAssincrona** | Indica que não é possível avançar no processo até que o Subprocesso seja finalizado. Se for atribuído o valor falso então o sistema invocará o Subprocesso em questão e em seguida avançará para a próxima atividade automaticamente. | Booleano |
| **CicloAnualDiaMes** | Dia do mês para execução | Inteiro |
| **CicloAnualHora** | Hora para execução | Inteiro |
| **CicloAnualMes** | Mês para execução | Inteiro |
| **CicloAnualMinuto** | Minuto para execução | Inteiro |
| **CicloAnualUltimoDiaMes** | Executar no último dia do mês | Booleano |
| **CicloDiarioDomingo** | Gera ocorrências no Domingo | Booleano |
| **CicloDiarioHora** | Hora para execução | Inteiro |
| **CicloDiarioMinuto** | Minuto para execução de um Ciclo Diário. | Inteiro |
| **CicloDiarioQuarta** | Gera ocorrências na Quarta-feira | Booleano |
| **CicloDiarioQuinta** | Gera ocorrências na Quinta-feira | Booleano |
| **CicloDiarioSabado** | Gera ocorrências no Sábado | Booleano |
| **CicloDiarioSegunda** | Gera ocorrências na Segunda-feira | Booleano |
| **CicloDiarioSexta** | Gera ocorrências na Sexta-feira | Booleano |
| **CicloDiarioTerca** | Gera ocorrências na Terça-feira | Booleano |
| **CicloMensalAbril** | Gera ocorrências no mês de Abril | Booleano |
| **CicloMensalAgosto** | Gera ocorrências no mês de Agosto | Booleano |
| **CicloMensalDezembro** | Gera ocorrências no mês de Dezembro | Booleano |
| **CicloMensalDiaMes** | Dia do mês para execução | Inteiro |
| **CicloMensalFevereiro** | Gera ocorrências no mês de Fevereito | Booleano |
| **CicloMensalHora** | Hora para execução | Inteiro |
| **CicloMensalJaneiro** | Gera ocorrências no mês de Janeiro | Booleano |
| **CicloMensalJulho** | Gera ocorrências no mês de Julho | Booleano |
| **CicloMensalJunho** | Gera ocorrências no mês de Junho | Booleano |
| **CicloMensalMaio** | Gera ocorrências no mês de Maio | Booleano |
| **CicloMensalMarco** | Gera ocorrências no mês de Março | Booleano |
| **CicloMensalMinuto** | Minuto para execução | Inteiro |
| **CicloMensalNovembro** | Gera ocorrências no mês de Novembro | Booleano |
| **CicloMensalOutubro** | Gera ocorrências no mês de Outubro | Booleano |
| **CicloMensalSetembro** | Gera ocorrências no mês de Setembro | Booleano |
| **CicloMensalUltimoDiaMes** | Executar no último dia do mês | Booleano |
| **CicloSemanalDiaSemana** | Dia da semana para execução | [DiaSemana](enum_diasemana) |
| **CicloSemanalHora** | Hora para execução | Inteiro |
| **CicloSemanalMinuto** | Minuto para execução | Inteiro |
| **ClasseAnexoResposta** | Tipo de item que será gerado e anexado na ocorrência a partir de anexos de respostas | [ClasseConfiguracao](objetos_classeconfiguracao) |
| **ClasseAnexoRespostaId** | Identificador do tipo de arquivo retornado em anexo | Inteiro |
| **ClassePesquisaSatisfacao** | Formulário de Pesquisa de Satisfação que é enviado para o usuário assim que finalizada a Ordem de Serviço. | [ClassePesquisaSatisfacao](objetos_classepesquisasatisfacao) |
| **ClassePesquisaSatisfacaoId** | Identificador do ClassePesquisaSatisfacao associado | Inteiro |
| **ClasseSubProcesso** | Subprocesso invocado pela Atividade ou evento. Este Subprocesso deve estar contido em uma versão ativa do Processo configurado na Atividade ou Evento. | [ClasseSubProcesso](objetos_classesubprocesso) |
| **ClasseSubProcessoId** | Identificador do Tipo de Subprocesso associado | Inteiro |
| **ClientesAutorizados** | Relação de papéis de processo que definem os clientes autorizados a gerar uma solicitação pelo iniciador. | [Lista de ClienteAutorizado](objetos_clienteautorizado) |
| **Codigo** | Código utilizado para recuperação de dados sobre a execução da Atividade. Este código pode ser utilizado em scripts para determinar a realização de alguma ação prevista em processo (verificar se algo foi aprovado). O código deve ser único dentro de uma versão do Subprocesso. O código também é uma referência para a cópia de aprovações realizadas durante a reclassificação de versão do processo. | String |
| **ConfirmaResponsabilidade** | Em transições manuais para esta atividade será exibido o diálogo de encaminhamento para confirmação de responsabilidade. | Booleano |
| **Controle** | Controle de Atividade | [Controle](objetos_controle) |
| **ControleId** | Identificador do(a) Controle associado(a) | Inteiro |
| **Descricao** | Texto resumido que descreve uma Tarefa, Evento ou chamada de Subprocesso. Dependendo do tipo de objeto este descritivo é exibido no diagrama e no assistente de processos para faciliar o entendimento do fluxo. No caso de eventos intermediários do tipo mensagem este texto é utilizado no assunto do email enviado. | String |
| **DisponibilidadeAplicacoes** | Permite configurar a disponibilidade do iniciador nas diversas aplicações do sistema. | [VisibilidadeIniciador](enum_visibilidadeiniciador) |
| **EnderecoReply** | Conta configurada na mensagem para reply | String |
| **EnviaMensagemIndividual** | Indica se será enviada uma mensagem para cada destinatário (caso verdadeiro) ou se será enviada uma única mensagem para todos os destinatários (caso falso) | Booleano |
| **ExigeApontamento** | Exige que o usuário aponte horas trabalhadas na ocorrência. A validação é realizada ao término da atividade. | Booleano |
| **FinalizarInterrupcao** | Finaliza a interrupção de ANS corrente quando o cliente da ocorrência responder o comunicado. | Booleano |
| **FluxosSaida** | Fluxos de Saída para a Atividade | [Lista de FluxoSequencia](objetos_fluxosequencia) |
| **GrupoANO** | Nome do agrupamento de tarefas que compartilham a mesma configuração de Acordo de Nível Operacional. Todas as mudanças em configurações de ANO de uma tarefa do grupo são replicadas nas demais tarefas do agrupamento. | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Atividade | Inteiro |
| **ListaDestinatarios** | Relação de endereços de emails separados por ponto e vírgula que são utilizados como destinatários do comunicado. Pode ser preenchido em conjunto com o papel de processo de Destinatários. | String |
| **MaximoExecucao** | Define o número máximo de execuções do evento intermediário. Este atributo é válido apenas para eventos intermediários acoplados em atividades. | Inteiro |
| **ModeloComunicado** | Modelo de comunicado utilizado para compor o corpo da mensagem. | [ModeloComunicado](objetos_modelocomunicado) |
| **ModeloComunicadoId** | Identificador do Modelo de comunicado utilizado para gerar a mensagem | Inteiro |
| **MotivoInterrupcaoSLA** | Quando uma Ordem de Serviço entra nesta atividade seu ANS é automaticamente suspenso e o tempo só volta a ser medido após a finalização da atividade. | [MotivoInterrupcaoSLA](objetos_motivointerrupcaosla) |
| **MotivoInterrupcaoSLAId** | Identificador do Motivo de interrupção de tempo de atendimento definido em Acordo de Nível de Serviço | Inteiro |
| **MultiplasInstancias** | Permite a criação de múltiplas instâncias da Atividade do tipo Subprocesso. | Booleano |
| **NomeMensagem** | Nome resumido que identifica uma mensagem. Este nome é referênciado na chamada de Webservices. Na comparação dos nomes são descartados espaços em branco no início e fim do nome. A caixa (maiúsculo/minúsculo) também é ignorada. | String |
| **Opcoes** | Caracterísitcas da atividade que não são necessárias durante a execução do processo. | [Lista de OpcaoAtividade](objetos_opcaoatividade) |
| **Operacoes** | Regras de negócio configuradas na atividade ou evento. Estas regras podem ser: preenchimento de um campo, aprovação etc. | [Lista de OperacaoAtividade](objetos_operacaoatividade) |
| **PapelDestinatario** | Papel de processo que determina os destinatários do comunicado | [PapelProcesso](objetos_papelprocesso) |
| **PapelDestinatarioId** | Identificador do papel de processo utilizado para definir os destinatários do comunicado | Inteiro |
| **PapelResponsavel** | Papel de processo utilizado para selecionar responsáveis pela atividade ou evento. Durante a execução do processo esta configuração será utilizada para realizar encaminhamentos automáticos. | [PapelProcesso](objetos_papelprocesso) |
| **PapelResponsavelId** | Identificador do PapelProcesso associado | Inteiro |
| **PassagemItens** | Configura uma regra de passagem de Itens de Configuração para Ordens de Serviço invocadas como Subprocessos ou link final. | [Lista de PassagemItens](objetos_passagemitens) |
| **PassaTodosItens** | Em chamadas de Subprocessos ou link final todos os Itens anexados na Ordem de Serviço chamadora são atribuídos a nova Ordem de Serviço chamada. | Booleano |
| **PermissaoRestritaPapel** | Indica que somente usuários que possuem o papel configurado na atividade podem assumir responsabilidade. | Booleano |
| **PermiteCancelamentoAA** | Permite que o cliente cancele a solicitação utilizando a página de consulta do Autoatendimento. | Booleano |
| **PermiteVoltar** | Permite que o solucionador cancele a execução da atividade executando o comando Voltar do assistente de processos | Booleano |
| **PreencheClienteSolucionador** | Indica que o campo Cliente deve ser preenchido automaticamente com o solucionador conectado na aplicação. Este comportamento só é possível para iniciadores disponíveis somente no Workspace. | Booleano |
| **PreencheMotivoReprovacao** | Preenche o motivo de Cancelamento com o(s) motivo(s) de reprovação das aprovações executadas no processo. São desconsideradas aprovações relacionadas com interrupções de ANS. O preenchimento ocorre no instante em que a ocorrência inicia evento e o conteúdo prévio é desconsiderado se realmente existirem motivos de reprovação. | Booleano |
| **ProcessoAtividade** | Processo invocado pela Atividade. O Processo deve conter em uma versão ativa o Subprocesso também configurado na Atividade/Evento. | [Processo](objetos_processo) |
| **ProcessoId** | Identificador do Processo associado | Inteiro |
| **Referencia** | Texto descrevendo detalhes sobre a execução da Atividade. Este texto é exibido no assistente de processos e utilizado na geração de documentação do processo. | String |
| **Regra** | Em iniciadores por regra ou temporizador esta fórmula é retornada para identificar o momento de geração de novas ocorrências. Neste caso ele pode retornar um valor lógico indicando que é necessário gerar ocorrências ou uma tabela via comando SQL e, neste último caso, é gerada uma ocorrência para cada linha retornada. Em eventos intermediários utilizamos esta fórmula para retornar um valor lógico indicando que é necessário executar uma transição entre tarefas. | String |
| **RelatorioObrigatorio** | Indica que para avançar para a próxima atividade é necessário preencher um relatório de execução da atividade corrente. | Booleano |
| **Relatorios** | Lista de relatórios que serão utilizados como apoio na execução de alguma tarefa ou como anexo em alguma mensagem gerada pela execução do processo. No caso de relatórios de apoio é possível a sua publicação na página de consultas do Autoatendimento. | [Lista de RelatorioAtividade](objetos_relatorioatividade) |
| **RetornaTodosItens** | Em chamadas de Subprocessos e link final todos os Itens de Configuração são retornados para a chamadora. | Booleano |
| **RetornoItens** | Configura uma regra de retorno de Itens de Configuração para Ordens de Serviço invocadas como Subprocessos ou link final. Quando uma Ordem de Serviço chamada é finalizada então os itens que atenderem a regra serão aidionado a Ordem de Serviço chamadora. | [Lista de RetornoItens](objetos_retornoitens) |
| **ScriptEvento** | Script executado após uma transição de Atividade originada por um Fluxo ou Evento | String |
| **ScriptFim** | Script de Event executado quando uma Atividade é Finalizada | String |
| **ScriptInicio** | Script de Event executado quando uma Atividade é Iniciada | String |
| **ScriptValidacao** | Script para Validação da Atividade | String |
| **SincronizaCancelamento** | Cancela a ocorrência se todas as invocadas forem canceladas | Booleano |
| **SubProcessoId** | Identificador do Subprocesso | Inteiro |
| **TempoIntervalo** | Tempo máximo para início do evento. | Inteiro |
| **Temporalidade** | Define para eventos intermediários de mensagem após quantos dias a mensagem será excluída da base de dados. Se for 0 (zero) ela será excluída assim que o email for enviado. Se estiver sem preenchimento a mensagem não será excluída. | Inteiro |
| **Tipo** | Indica o Tipo de Atividade que pode ser uma Tarefa ou um Evento | [TipoAtividade](enum_tipoatividade) |
| **TipoAberturaLinkInicial** | Indica o tipo de abertura se for um LinkInicial | [TipoAberturaLinkInicial](enum_tipoaberturalinkinicial) |
| **TipoCiclo** | Tipo ciclo | [TipoCicloTimer](enum_tipociclotimer) |
| **TipoFinalizacao** | Tipo de finalização | [TipoFinalizacao](enum_tipofinalizacao) |
| **TipoMensagem** | Tipo de mensagem monitorada pelo evento. | [TipoMensagemEvento](enum_tipomensagemevento) |
| **TiposAnexosMensagem** | Tipos de arquivos que serão anexados no comunicado gerado pelo evento | [Lista de TipoAnexoMensagem](objetos_tipoanexomensagem) |
| **TipoSolicitacao** | Agrupamento do segundo passo da abertura de Ordens de Serviço do Autoatendimento | [TipoSolicitacao](objetos_tiposolicitacao) |
| **TipoSolicitacaoId** | Identificador do Tipo de solicitacao associado | Inteiro |
| **TransicaoAutomatica** | Habilita a transição automática para a próxima Atividade. Esta transição automática ocorre após Aprovações e Finalizações de Subprocessos. | Booleano |
| **UnidadeANO** | Unidade de medida para definição do Acordo de Nível Operacional. Se for selecionada a unidade 'Percentual ANS' então nenhum caminho pode totalizar o valor superior a 100%. | [UnidadeDefinicaoANO](enum_unidadedefinicaoano) |
| **ValoresInputs** | Definição de valores para parâmetros de entrada do Subprocesso alvo. Estes parâmetros são declarados no Subprocesso alvo (Modificar Subprocesso) e depois copiados para esta propriedade quando definimos o Subprocesso alvo. | [Lista de ValorInput](objetos_valorinput) |

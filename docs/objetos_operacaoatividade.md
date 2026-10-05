# OperacaoAtividade

Caminho: Customização > Modelo de objetos > Processo > OperacaoAtividade

Operação de uma Atividade

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Aprovadores** | Lista de papéis que definem as pessoas responsáveis pela aprovação | [Lista de Aprovador](objetos_aprovador) |
| **AtividadeId** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Atividade | Inteiro |
| **Ativo** | Quando Ativa uma Operação pode ser inicializada automaticamente (geração da solicitação de aprovação por exemplo). A Ativação da Operação também define o comportamento da rotina de Validação de Processo. Se Ativa a Validação é executada caso contrário é ignorada. | Booleano |
| **BloquearPendencia** | Não permite a transição para a próxima atividade se existirem pendências de processo. | Booleano |
| **Campos** | Campos que devem ser preenchidos pelo usuário ou solicitante. | [Lista de CampoPreenchimento](objetos_campopreenchimento) |
| **CamposAprovacao** | Campos visualizados pelo aprovador na tela de aprovação (somente leitura). Uma vez aprovados estes campos não podem ser modificados pelo atendente. | [Lista de CampoAprovacao](objetos_campoaprovacao) |
| **CamposPreenchimentoAprovacao** | Campos exibidos para o aprovador com possibilidade de preenchimento/modificação. Uma vez aprovados estes campos não podem ser modificados pelo atendente. | [Lista de CampoPreenchimentoAprovacao](objetos_campopreenchimentoaprovacao) |
| **ClassesAnexos** | Tipos de Itens de Configuração que devem ser anexados na Ordem Serviço. | [Lista de ClasseAnexo](objetos_classeanexo) |
| **ClassesAprovacao** | Tipos de Itens de Configuração que devem ser Anexados na aprovação | [Lista de ClasseAprovacao](objetos_classeaprovacao) |
| **CopiarAnexados** | Copiar para versão para aprovação todos os Itens associados na Ocorrência. Quando selecionado são ignoradas as configurações por Tipo de Item de Configuração. | Booleano |
| **DescricaoAssuntoAprovacao** | Descritivo para Assunto da Aprovação | String |
| **ExigeApropriacoes** | Exige que na aprovação sejam anexadas Apropriações de horas trabalhadas. | Booleano |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar uma OperacaoAtividade | Inteiro |
| **IniciaAutomatico** | Inicia automaticamente quando iniciar a tarefa. | Booleano |
| **MinimoAprovadores** | Quantidade mínima de aprovações para aprovação total da solicitação. A reprovação ocorre quando o número mínimo de aprovadores não pode ser atingido. Se este campo não for preenchido então a solicitação só é totalmente aprovada quando Todos aprovarem. | Inteiro |
| **Operacao** | Operação executada na Atividade. | [Operacao](objetos_operacao) |
| **OperacaoId** | Identificador do Operacao associado | Inteiro |
| **ReenvioEmailAprovacao** | Frequência em horas do reenvio do email de aprovação. | Inteiro |
| **Relatorios** | Relação de relatórios envolvidos em uma solicitação de aprovação ou programados para geração de arquivos anexados na ocorrência. Estes relatórios são disponibilizados como um link na página de aprovações do AA. Na configuração destes relatórios é necessário definir todos os eventuais parâmetros. | [Lista de RelatorioOperacao](objetos_relatoriooperacao) |
| **ReprovarImediato** | A solicitação é totalmente reprovada assim que o primeiro avalidador realizar a reprovação. | Booleano |
| **ReutilizaAprovacaoAnterior** | Reutiliza aprovações do mesmo aprovador em atividades anteriores no processo. São consideradas apenas solicitações aprovadas com sucesso. | Booleano |
| **RotuloBotaoAprovar** | Rótulo do botao 'Aprovar' existente na página de aprovações da aplicação de Autoatendimento e no diálogo de aprovação do módulo solucionador. | String |
| **RotuloBotaoReprovar** | Rótulo do botao 'Reprovar' existente na página de aprovações da aplicação de Autoatendimento e no diálogo de aprovação do módulo solucionador. | String |
| **RotuloPreenchimento** | Descritivo utilizado como rótulo no agrupamento de campos criado no assistente de processos para entrada de dados. | String |
| **Sequencia** | Sequência em que são apresentadas as operações de uma atividade. | Inteiro |
| **UtilizaIdentidadeSolicitante** | A solicitação é pré-aprovada pelo usuário que solicitou o serviço utilizando o portal de Autoatendimento ou a transação Workspace. No caso do Autoatendimento este recurso só estará habilitado se não for permitida a troca de Cliente na tela de abertura. | Booleano |

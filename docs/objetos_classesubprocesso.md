# ClasseSubProcesso

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso

Um Tipo de Subprocesso mantém características de um fluxo que são invariáveis entre suas diversas versões.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AcessoTotalAdmin** | Indica que usuários com o perfil Administrador possuem acesso total em ocorrências do Subprocesso. | Booleano |
| **Ativo** | Indica que o Tipo de Subprocesso está Ativo. Quando ativo o tipo é visível em formulários de entrada de dados para Ordens de Serviço ou Consultas diversas. | Booleano |
| **CriterioChargeBack** | Forma de Charge-back para Ocorrências do Subprocesso. | [CriterioChargeBackSubProcesso](enum_criteriochargebacksubprocesso) |
| **Descricao** | Texto que descreve claramente a utilização de um Tipo de Subprocesso | String |
| **DescricaoCliente** | Descritivo apresentado para o Cliente. Se não for preenchido é apresentado o Descritivo padrão do Tipo de Subprocesso. | String |
| **DisponivelConsultaConhecimento** | Ordens de Serviço deste Subprocesso podem ser recuperadas pela ferramenta de busca de base de conhecimento. | Booleano |
| **EmailsComunicadosManuais** | Serão enviados para este(s) email(s) os emails enviados manualmente relacionados com este Tipo de Subprocesso. Separar por ponto-e-vírgula (;). | String |
| **FatorPrioridade** | Fator utilizado no cálculo de Prioridade | [FatorPrioridade](objetos_fatorprioridade) |
| **FatorPrioridadeId** | Identificador do(a) FatorPrioridade associado(a) | Inteiro |
| **HabilitaConsultaAutomaticaBaseConhecimento** | Indica que Ordens de Serviço deste Subprocesso acionam a busca automática de artigos da Base de Conhecimento a partir dos campos Assunto, Descrição detalhada ou Sintoma analisado. Esta busca ocorre quando o usuário visualiza a tela de edição da Ordem de Serviço, quando os campos citados são utilizados como critério de recuperação por palavras-chave. | Booleano |
| **Id** | Número sequencial gerado automaticamente pelo sistema para identificar um Tipo de Subprocesso. Um Identificador não pode ser modificado pelo usuário. | Inteiro |
| **MetodoPriorizacao** | Método utilizado para Priorizar Ocorrências do Subprocesso. | [MetodoPriorizacao](objetos_metodopriorizacao) |
| **MetodoPriorizacaoId** | Identificador do MetodoPriorizacao associado | Inteiro |
| **Objetivo** | Texto de Referência sobre o Objetivo do Tipo de Subprocesso | String |
| **OrdemExibicao** | Ordem de exibição da Solicitação na página de Abertura de Ordens de Serviço da aplicação de Autoatendimento. Quando preenchido a Solicitação é exibida em um grupo denominado "Principais solicitações", caso contrário é agrupado em "Demais solicitações". Em caso de empate por ordenação deste campo então é adotado como segundo critério a ordenação alfabética por Descritivo do Cliente | Inteiro |
| **OrgaoDono** | Órgão responsável pelo Subprocesso. | [Orgao](objetos_orgao) |
| **OrgaoDonoId** | Identificador do Órgão proprietário do Processo | Inteiro |
| **PublicarApontamentosAA** | Indica a regra de publicação de apontamentos de horas trabalhadas no Autoatendimento | [PublicacaoApontamentosAutoAtendimento](enum_publicacaoapontamentosautoatendimento) |
| **ReaberturaAutoAtendimento** | Permite que clientes reabram a Ordem de Serviço utilizando a página de consulta do Autoatendimento. Esta permissão também está condicionada ao parâmetro 'Máximo dias para reabertura' da tela de Configurações. | Booleano |
| **RegraAutorizacao** | Regra de autorização para visualização de Ordens de Serviço do Subprocesso. Se este campo não for preenchido o sistema utilizará o parâmetro default cadastrado na tela de Configurações. | [RegraAutorizacao](enum_regraautorizacao) |
| **Responsavel** | Pessoa responsável pelo Subprocesso | [Pessoa](objetos_pessoa) |
| **ResponsavelId** | Identificador da Pessoa associada | Inteiro |
| **RestricoesServicos** | Serviços que estarão disponíveis para o Subprocesso. Deve ser preenchido somente quando for necessário restringir os Serviços. Se não for preenchido então todos os Serviços estarão disponívies. Tomar como exemplo o passo 3 do Autoatendimento. | [Lista de RestricaoServico](objetos_restricaoservico) |
| **Sigla** | Nome abreviado (código) que identifica um Tipo de Subprocesso. Este código pode ser utilizado em scripts para automatismo de processos. | String |
| **ValorChargeBack** | Valor para cobrança pela rotina de Charge-back. Se o critério de charge-back for 'Hora' então o valor total é obtido pela multiplicação do 'Valor' pela quantidade de horas apontadas no período de apuração. Se o critério de charge-back for 'Ocorrência' então o total é obtido pela multiplicação do 'Valor' pela quantidade total de ocorrências finalizadas no período de apuração. | Decimal |
| **VisibilidadeAutoAtendimento** | Indica o tipo de visibilidade das ocorrências deste tipo de subprocesso no Autoatendimento, levando em consideração o cliente ou favorecido como referência | [VisibilidadeAutoAtendimento](enum_visibilidadeautoatendimento) |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **ObtemValorFatorPrioridade** | Obtem Valor associado ao Fator de Prioridade do Tipo de Subprocesso. Se não existir uma definição de Fator de Prioridade na Classe então é retornado o valor default fornecido como parâmetro. | System.Int32 ObtemValorFatorPrioridade(System.Int32 valorDefault); |
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | ClasseSubProcesso Carrega(int i); |
| **Novo** | Cria um novo registro do tipo ClasseSubProcesso | ClasseSubProcesso Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | ClasseSubProcesso Carrega(string nomePropriedade, object valorPropriedade); |

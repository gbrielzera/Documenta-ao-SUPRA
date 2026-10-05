# Pessoa

Caminho: Customização > Modelo de objetos > Recurso > Pessoa

Uma Pessoa pode representar um Cliente, um Solucionador ou uma fila de atendimento. Um registro do tipo Pessoa deve obrigatoriamente estar associado a um Órgão, e por meio desta associação é possível determinar seu gestor. No cadastro de uma Ordem de Serviço encontramos os campos Cliente e Responsável que representam a pessoa que solicitou e a responsável pelo atendimento respectivamente.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ativo** | Indica que a Pessoa está Ativa no sistema. | Booleano |
| **Cargo** | Descrição do Cargo da Pessoa | String |
| **CelularEmpresa** | Telefone Celular fornecido pela empresa | String |
| **CelularParticular** | Telefone Celular particular da Pessoa | String |
| **CulturaCliente** | Cultura preferencial do Cliente. Esta Cultura é utilizada pela aplicação de Autoatendimento para configuração de idioma do usuário. | [Culture](objetos_culture) |
| **CulturaClienteId** | Identificador da Cultura preferencial do Cliente | Inteiro |
| **DataFimSubstituicao** | Data de Fim de validade para a autorização de substituição. Importante: a data de fim não está associada a data de início de aprovação (instante em que soliictação de aprovação é enviada para o aprovador) e sim com a data instantânea em que a página de aprovação é exibida para o Cliente. | Data/hora |
| **DataHoraUltimoAcessoAA** | Data/hora do último acesso ao Autoatendimento. | Data/hora |
| **DataInicioSubstituicao** | Data de Início de validade para a autorização de substituição. Importante: a data de início não está associada a data de início de aprovação (instante em que soliictação de aprovação é enviada para o aprovador) e sim com a data instantânea em que a página de aprovação é exibida para o Cliente. | Data/hora |
| **Email** | Email da Pessoa | String |
| **EmailAlternativo** | Email alternativo de contato para a Pessoa | String |
| **FatorPrioridade** | Fator utilizado para cálculo de Prioridade em Ocorrências. | [FatorPrioridade](objetos_fatorprioridade) |
| **FatorPrioridadeId** | Identificador do Fator de Prioridade utilizado em cálculos de Prioridade. | Inteiro |
| **Fornecedor** | Empresa Fornecedora responsável pelo Terceiro. Preencher este campo somente quando a Pessoa for um Terceiro. | [Fornecedor](objetos_fornecedor) |
| **FornecedorId** | Identificador do Fornecedor em caso de Terceiros. | Inteiro |
| **Id** | Número sequencial gerado automaticamente pelo sistema para identificar uma Pessoa. | Inteiro |
| **Local** | Local de trabalho da Pessoa | [Local](objetos_local) |
| **LocalId** | Identificador do Local de trabalho da Pessoa | Inteiro |
| **Nome** | Nome completo da Pessoa | String |
| **NomeAbreviado** | Nome abreviado da Pessoa | String |
| **Orgao** | Órgão onde a Pessoa está lotada. A lotação é de grande importância em processos que envolvem aprovações de chefias e hierárquica. | [Orgao](objetos_orgao) |
| **OrgaoId** | Identificador do Órgão onde a Pessoa está lotada | Inteiro |
| **PerfilCliente** | Perfil especial concedido a um Cliente para atendimento diferenciado | [PerfilCliente](objetos_perfilcliente) |
| **PerfilClienteId** | Identificador do(a) PerfilCliente associado(a) | Inteiro |
| **PessoaRegistroAprovacao** | Pessoa que realizou o registro do Substituto pela aprovação. Este pode ser o próprio Cliente quando realizado pelo site de Autoatendimento ou um Profissional utilizando a aplicação Supravizio. | [Pessoa](objetos_pessoa) |
| **PessoaRegistroAprovacaoId** | Identificador da Pessoa que realizou o registro de Substituição para Aprovação | Inteiro |
| **SegundoContato** | Segunda Pessoa para contato | String |
| **Senha** | Senha do usuário formada por no mínimo 4 caracteres que podem ser somente números ou letras. A comparação é insensível a letras minúsculas ou maiúsculas. Quando preenchida ignora validação de senha no Active Directory. | String |
| **SubstitutoAprovacao** | Pessoa autorizada a realizar aprovações como substituto. O Substituto pode ser registrado na aplicação Supravizio ou pelo próprio Cliente pelo site de Autoatendimento. A autorização de substituição em aprovações é válida por um período com data de início e data de fim que são obrigatórios no registro da substituição. | [Pessoa](objetos_pessoa) |
| **SubstitutoAprovacaoId** | Identificador do Substituto para Aprovação | Inteiro |
| **Telefone** | Número do Telefone (ramal) de contato. | String |
| **TelefoneSegundoContato** | Telefone da Segunda Pessoa de contato | String |
| **Tipo** | Cliente em Ordens de Serviço ou Fila de Grupos de Trabalho | [TipoPessoa](enum_tipopessoa) |
| **TipoColaborador** | Tipo de Colaborador que pode ser Empregado ou Terceiro. No caso de Terceiro é necessário informar a Empresa Fornecedora | [TipoColaborador](enum_tipocolaborador) |
| **UserId** | Identificador do Usuário associado | Inteiro |
| **Usuario** | Usuário relacionado com a Pessoa, caso esta seja um Solucionador | [User](objetos_user) |
| **UsuarioRede** | Nome do usuário de rede utilizado pela Pessoa para acesso a ambiente de rede | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **VerificaDisponibilidadeEncaminhamento** | Verifica a existência de registros de ausência para a Pessoa na data/hora corrente com opção de redirecionamento de Ordens de Serviço. Se não existir ausência então retorna a própria Pessoa. | Venki.Supravizio.Recurso.Pessoa VerificaDisponibilidadeEncaminhamento(); |
| **VerificaDisponibilidadeEm** | Verifica a existência de registros de ausência para a Pessoa na data/hora fornecida como parâmetro. Se não existir ausência então retorna a própria Pessoa. | Venki.Supravizio.Recurso.Pessoa VerificaDisponibilidadeEm(DateTime data); |
| **ObtemValorFatorPrioridade** | Obtem Valor associado ao Fator de Prioridade da Pessoa. Se não existir um Fator de Prioridade na Pessoa então é verificado a Empresa correspondente. Se na Empresa também não existir um fator então é retornado o valor default fornecido como parâmetro. Se não existir uma relação de Pessoa com Empresa então também é retornado o valor default. | System.Int32 ObtemValorFatorPrioridade(System.Int32 valorDefault); |
| **ObtemChefia** | Retorna chefia imediata da Pessoa. Se a Pessoa for Gestora do Órgão encontrado então a chefia pode ser ela mesmo ou seu gestor imediato. Esta decisão é definida pelo parâmetro 'chefiaGestor'. Se a lotação da Pessoa for nula ou o Gestor da lotação for nulo então é retornado o valor nulo. | Venki.Supravizio.Recurso.Pessoa ObtemChefia(bool chefiaGestor); |
| **ObtemChefia** | Retorna chefia da Pessoa considerando um limitador de busca fornecido como parâmetro. Se a Pessoa for Gestora do Órgão encontrado então a chefia pode ser ela mesmo ou seu gestor imediato. Esta decisão é definida pelo parâmetro 'chefiaGestor'. Se durante a busca for detectada referência circular entre os Órgãos então é levantada uma exceção do tipo 'ReferenciaCircularOrgaosException'. Se o Órgão delimitador de busca fornecido como parâmetro for nulo então é retornado o valor nulo. | Venki.Supravizio.Recurso.Pessoa ObtemChefia(Venki.Supravizio.Recurso.Orgao orgaoPai, bool chefiaGestor); |
| **ObtemTempoTotalApontado** | Retorna o tempo total apontado levando em consideração data/hora de início, data/hora fim. | System.TimeSpan ObtemTempoTotalApontado(DateTime inicio, DateTime fim); |
| **ObtemTempoTotalApontado** | Retorna o tempo total apontado levando em consideração data/hora de início, data/hora fim e um Processo específico. | System.TimeSpan ObtemTempoTotalApontado(DateTime inicio, DateTime fim, Venki.Supravizio.Processo.Processo processo); |
| **ObtemTempoTotalApontado** | Retorna o tempo total apontado levando em consideração data/hora de início, data/hora fim e uma Classe SubProcesso específica. | System.TimeSpan ObtemTempoTotalApontado(DateTime inicio, DateTime fim, Venki.Supravizio.Processo.ClasseSubProcesso classeSubProcesso); |
| **ObtemOcorrenciasAbertas** | Retorna uma lista de Ordens de Serviço onde a pessoa é Cliente e a situação seja Aberta ou Agendada. Os parâmetros Tipo de Subprocesso e Serviço são opcionais e se não forem fornecidos serão ignorados no filtro de seleção. Se não forem encontradas ocorrências para o filtro então é retornada uma lista vazia. | Venki.Supravizio.Processo.OcorrenciaList ObtemOcorrenciasAbertas(Venki.Supravizio.Processo.ClasseSubProcesso classeSubProcesso, Venki.Supravizio.Processo.Servico servico); |
| **ObtemSubordinados** | Obtem todas as pessoas que são subordinadas com opção de recuperação por sub-níveis. | Venki.Supravizio.Recurso.PessoaList ObtemSubordinados(bool incluiSubniveis, bool somenteAtivos); |
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Pessoa Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Pessoa | Pessoa Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Pessoa Carrega(string nomePropriedade, object valorPropriedade); |

# ItemConfiguracao

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao

Classe abstrata para todos os Itens de Configuração do CMDB

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Atores** | Atores | [Lista de AtoresItem](objetos_atoresitem) |
| **ClasseConfiguracao** | Tipo de Item de Configuração associado | [ClasseConfiguracao](objetos_classeconfiguracao) |
| **ClasseConfiguracaoId** | Identificador do Tipo de Item associado | Inteiro |
| **Comentario** | Comentário sobre o Item destinados ao Cliente. Para histórico de observações utilize a relação de Observações. | String |
| **Componentes** | Componentes de um Item de Configuração | [Lista de ItemComponente](objetos_itemcomponente) |
| **Copias** | Redundâncias existentes do Ativo. | [Lista de ItemCopia](objetos_itemcopia) |
| **CriterioChargeBack** | Critério para destino de custo no cálculo de Charge-back. | [CriterioChargeBackItem](enum_criteriochargebackitem) |
| **DataAceite** | Data de aceite do Item | Data/hora |
| **DataCadastro** | Data em que o Item de Configuração foi cadastrado no sistema. | Data/hora |
| **DataDesativacao** | Data de desativação do Item. | Data/hora |
| **DataEntrega** | Data em que o Item foi entregue | Data/hora |
| **DataExpiracaoGarantia** | Data para Expiração de uma eventual garantia | Data/hora |
| **DataProducao** | Data de entrada em Produção. | Data/hora |
| **Dependencias** | Itens de configuração que possuem relação de Dependência. | [Lista de ItemDependencia](objetos_itemdependencia) |
| **Descricao** | Descrição detalhada sobre o Item de configuração | String |
| **FatorPrioridade** | Fator utilizado para cálculo de Prioridade em Ocorrências. | [FatorPrioridade](objetos_fatorprioridade) |
| **FatorPrioridadeId** | Identificador do(a) FatorPrioridade associado(a) | Inteiro |
| **Fornecedor** | Fornecedor para o Item. Se for mantido por equipe própria então não preencher. | [Fornecedor](objetos_fornecedor) |
| **FornecedorId** | Identificador do Fornecedor | Inteiro |
| **HistoricoItem** | Histórico de modificações em arquivos. Válido apenas para artefatos do tipo arquivo mantido por transferência. | [Lista de HistoricoItem](objetos_historicoitem) |
| **Id** | Número sequencial gerado automaticamente para Identificar um Item de Configuração | Inteiro |
| **Localizacao** | Localização do Item. Pode ser um local físico ou pessoa que utiliza | String |
| **Modelo** | Modelo de Item de Configuração segundo especificação de um Fabricante. | [Modelo](objetos_modelo) |
| **ModeloId** | Identificador do Modelo | Inteiro |
| **NumeroSerie** | Número de série do Item | String |
| **Observacoes** | Observações a respeito do Item de Configuração | [Lista de ObservacaoItem](objetos_observacaoitem) |
| **Responsavel** | Usuário responsável pelo Item de Configuração. | [Pessoa](objetos_pessoa) |
| **ResponsavelId** | Identificador da Pessoa associada | Inteiro |
| **Situacao** | Configura todos os Estados possíveis para um Item do Tipo de Item de Configuração associada. | [SituacaoClasseConfiguracao](objetos_situacaoclasseconfiguracao) |
| **SituacaoId** | Identificador da Situação corrente do Item | Inteiro |
| **TipoPosse** | Tipo de Posse | [TipoPosse](objetos_tipoposse) |
| **TipoPosseId** | Identificador do Tipo de Posse | Inteiro |
| **Usuarios** | Usuários do Item de Configuração | [Lista de UsuarioItem](objetos_usuarioitem) |
| **ValorCustoAquisicao** | Custom total de aquisição do Item | Decimal |
| **ValorCustoManutencao** | Valor do Custo de Manutenção Mensal do Item | Decimal |
| **ValorPrecoAquisicao** | Preço de aquisição do Item para demonstrativo de custeio pela rotina de Charge-back. O valor de aquisição é lançado no charge-back de competência relativa a Data de Entrega do Ativo. | Decimal |
| **ValorPrecoManutencao** | Preço de Charge-back de manutenção mensal | Decimal |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **ObtemValorFatorPrioridade** | Obtem Valor associado ao Fator de Prioridade do Item de Configuração. Se não existir um Fator de Prioridade no Serviço então é verificado o Tipo de Item de Configuração. Se no Tipo de Item de Configuração também não existir um fator então é retornado o valor default fornecido como parâmetro. | System.Int32 ObtemValorFatorPrioridade(System.Int32 valorDefault); |
| **AdicionaComponentePorOcorrencia** | Adiciona um Componente a partir de uma Ocorrência. | Venki.Supravizio.Configuracao.ItemConfiguracao AdicionaComponentePorOcorrencia(Venki.Supravizio.Configuracao.ItemConfiguracao itemComponente, Venki.Supravizio.Processo.Ocorrencia ocorrencia, decimal tamanho); |
| **RemoveComponentePorOcorrencia** | Remove um Componente por meio de uma Ocorrência. | Venki.Supravizio.Configuracao.ItemConfiguracao RemoveComponentePorOcorrencia(Venki.Supravizio.Configuracao.ItemConfiguracao itemParaRemocao, Venki.Supravizio.Processo.Ocorrencia ocorrencia); |
| **AdicionaUsuarioPorOcorrencia** | Adiciona um usuário por meio de uma Ocorrência. Se o Item de Configuração não possui ainda definição de Usuário Responsável então este atributo é preenchido com o usuário fornecido como parâmetro. | Venki.Supravizio.Configuracao.ItemConfiguracao AdicionaUsuarioPorOcorrencia(Venki.Supravizio.Recurso.Pessoa usuario, Venki.Supravizio.Processo.Ocorrencia ocorrencia); |
| **RemoveUsuarioPorOcorrencia** | Remove um usuário por meio de uma Ocorrência. Se o usuário a ser removido for também o responsável pelo Item de Configuração, então a responsabilidade é transferida para seu Gestor. | Venki.Supravizio.Configuracao.ItemConfiguracao RemoveUsuarioPorOcorrencia(Venki.Supravizio.Recurso.Pessoa usuario, Venki.Supravizio.Processo.Ocorrencia ocorrencia); |
| **ModificaSituacao** | Modifica a situação para o valor fornecido como parâmetro. Se não existir uma situação com o mesmo nome então é retornado um erro. Se executada com sucesso a modificação já é gravada no banco de dados. | void ModificaSituacao(string nomeSituacao); |
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | ItemConfiguracao Carrega(int i); |
| **Novo** | Cria um novo registro do tipo ItemConfiguracao | ItemConfiguracao Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | ItemConfiguracao Carrega(string nomePropriedade, object valorPropriedade); |

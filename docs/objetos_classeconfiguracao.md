# ClasseConfiguracao

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao

Um Tipo de Item de Configuração é utilizado para classificar Itens de Configuração, que são ativos sujeitos a alteração (como entrada ou saída) em processos de negócio.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Acesso** | Define o mecanismo utilizado para acessar o arquivo, que pode ser por Compartilhamento de rede ou pelo mecanismo de Download/upload. No segundo caso o arquivo é transferido para a máquina local e, após modificações, deve ser enviado para atualização no servidor. O valor default deste campo está condicionado a configuração do tipo de acesso default existente na tela de Configurações (grupo Configuração) | [TipoAcesso](enum_tipoacesso) |
| **AgrupamentoItens** | Define a forma como itens de charge-back apurado são agrupados no relatório apresentado para gestores de áreas clientes. | [AgrupamentoItensChargeBack](enum_agrupamentoitenschargeback_) |
| **Ativo** | Indica que o Tipo de Item de Configuração está ativo no sistema. | Booleano |
| **ClassesComponentes** | Tipos de Itens de Configuração que podem ser utilizadas como Componentes. | [Lista de ClasseComponente](objetos_classecomponente) |
| **ClassesCopia** | Tipos de Itens de Configuração que podem ser utilizadas como redundâncias. | [Lista de ClasseCopia](objetos_classecopia) |
| **ClassesDependencias** | Tipos de Itens de Configuração que podem ser associados como Dependências | [Lista de ClasseDependencia](objetos_classedependencia) |
| **ComentarioObrigatorio** | Determina se o Item pertencente a esta Classe de Configuração terá o campo Comentário como Obrigatório | Booleano |
| **CriterioChargeBack** | Critério para destino de custo no cálculo de Charge-back. | [CriterioChargeBack](enum_criteriochargeback) |
| **Descricao** | Texto que descreve claramente a classificação de um Item de Configuração. No caso de tipos que representam arquivos este descritivo não pode conter os caracteres \\ / : > ? * " pois este descritivo é utilizado para nomear pastas no repositório de arquivos. | String |
| **FatorPrioridade** | Fator utilizado para cálculo de Prioridade em Ocorrências. | [FatorPrioridade](objetos_fatorprioridade) |
| **FatorPrioridadeId** | Identificador do(a) FatorPrioridade associado(a) | Inteiro |
| **FiltroServicoAssociacaoOcorrencia** | Sempre que um item deste tipo for associado a uma Ordem de Serviço (na tela de edição ou Autoatendimento) existirá um filtro implícito por componentes do Serviço informado na ocorrência de processo. | Booleano |
| **FonteDados** | Fonte de dados (válido somente para Artefatos) | [FonteDados](enum_fontedados) |
| **HabilitaRedefinicaoPapeis** | Habilita a redefinição de Papéis por Itens da Classe. Papéis possuem uma definição global de Atores que pode ser sobreposta por um Serviço. Este parâmetro indica que Itens de Configuração desta Classe podem acumular um segundo nível de redefinição de Papéis, que ainda está condicionada a parametrização do Serviço. | Booleano |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Tipo de Item de Configuração. Este identificador não pode ser modificado pelo usuário. | Inteiro |
| **IncluirBlackList** | Indica que itens deste tipo fazem parte de um blacklist | Booleano |
| **Sigla** | Nome abreviado (código) utilizado para recuperar um Tipo de Item de Configuração em comandos SQL de relatórios ou scripts de customização. Esta sigla deve contar apenas números e letras. | String |
| **Situacoes** | Situações possíveis para Itens da Classe | [Lista de SituacaoClasseConfiguracao](objetos_situacaoclasseconfiguracao) |
| **SuperClasse** | Nome do Super Tipo associado que pode ser ser um Equipamento, Software, Dispositivo telefônico, Artigo da Base de Conhecimento ou Artefato (tipo genérico). Para cada Super tipo existe uma tela de cadastro no módulo de Ativos. | [SuperClasse](enum_superclasse) |
| **TamanhoMaximo** | Tamanho máximo (em megabytes) permitido por arquivo deste tipo. | Inteiro |
| **TemplateTopicos** | Tópicos que devem ser preenchidos na criação de artigos para a Base de Conhecimento. Quando um artigo é criado todos os tópicos são inicializados com o template. | [Lista de TopicoConhecimento](objetos_topicoconhecimento) |
| **ValorCustoAquisicao** | Valor do Custo de Aquisição Padrão para Itens do tipo. Este valor pode ser redefinido com o campo correspondente no Item. | Decimal |
| **ValorCustoManutencao** | Valor do Custo de Manutenção Mensal Padrão para Itens da Classe. Este valor pode ser redefinido com o campo correspondente no Item. | Decimal |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **ObtemValorFatorPrioridade** | Obtem Valor do Fator de Prioridade do Tipo de Item de Configuração. Se não existir um Fator associado então retorna o valor default fornecido como parâmetro. | System.Int32 ObtemValorFatorPrioridade(System.Int32 valorDefault); |
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | ClasseConfiguracao Carrega(int i); |
| **Novo** | Cria um novo registro do tipo ClasseConfiguracao | ClasseConfiguracao Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | ClasseConfiguracao Carrega(string nomePropriedade, object valorPropriedade); |

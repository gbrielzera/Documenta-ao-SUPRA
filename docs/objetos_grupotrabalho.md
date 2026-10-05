# GrupoTrabalho

Caminho: Customização > Modelo de objetos > Recurso > GrupoTrabalho

Um Grupo de Trabalho define uma estrutura hierárquica de equipes contendo um coordenador e um ou mais solucionadores. O coordenador de um Grupo de Trabalho possui atribuições especiais podendo realizar diversas ações sobre Ordens de Serviço sob responsabilidade de seus subordinados. Um Grupo de Trabalho pode corresponder a um nível na hierarquia de Órgãos, porém não existe uma relação automática com este cadastro.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ativo** | Indica que o Grupo de Trabalho está ativo. Quando ativo o Grupo de Trabalho pode ser utilizado na implementação de Papéis de Processo ou para lotação de profissionais. Quando um Grupo de Trabalho se torna Inativo automaticamente todos os profissionais associados também são desativados. | Booleano |
| **Coordenador** | Coordenador do Grupo de Trabalho | [Pessoa](objetos_pessoa) |
| **CoordenadorId** | Identificador da Pessoa responsável pela Coordenação do Grupo de Trabalho. O coordenador possui atribuições especiais podendo realizar diversas operações e edições nas Ordens de Serviço sob responsabilidade dos seus subordinados. | Inteiro |
| **Descricao** | Texto que descreve claramente o objetivo do Grupo de Trabalho. Este texto é utilizado em diversas telas e relatórios da aplicação Supravizio. | String |
| **ExibeAlertaOSGrupo** | Regra de autorização para exibição de Ordens de Serviço no Painel de Alertas do Workspace. | [TipoAlertaOS](enum_tipoalertaos) |
| **GrupoTrabalhoPai** | Grupo de Trabalho que é o Ancestral na hierarquia. A hierarquia de Grupos de Trabalho não corresponde necessariamente a Estrutura Organizacional da Empresa. | [GrupoTrabalho](objetos_grupotrabalho) |
| **GrupoTrabalhoPaiId** | Identificador do Grupo de Trabalho Pai. Esta associação permite a criação de uma hierarquia de Grupos de Trabalho. | Inteiro |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um GrupoTrabalho | Inteiro |
| **PermiteCancelar** | Regra de autorização para execução da operação de Cancelamento de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho. | [AutorizacaoOperacao](enum_autorizacaooperacao) |
| **PermiteClassificar** | Regra de autorização para execução da operação de Classificação de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho. | [AutorizacaoOperacao](enum_autorizacaooperacao) |
| **PermiteEncaminhar** | Regra de autorização para execução da operação de Encaminhamento de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho. | [AutorizacaoOperacao](enum_autorizacaooperacao) |
| **PermiteInterromperANS** | Regra de autorização para execução da operação de adicionar uma Interrupção de ANS de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho. | [AutorizacaoOperacao](enum_autorizacaooperacao) |
| **PermitePriorizar** | Regra de autorização para execução da operação de Priorização de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho. | [AutorizacaoOperacao](enum_autorizacaooperacao) |
| **PermiteReabrir** | Regra de autorização para execução da operação de Reabertura de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho. | [AutorizacaoOperacao](enum_autorizacaooperacao) |
| **PermiteVisualizarOutrosGrupos** | Permite visualizar outros Grupos de Trabalho na árvore de Grupos de Trabalho. Caso esta propriedade seja desmarcada o solucionador deste grupo poderá visualizar apenas o seu grupo de trabalho e sub-grupos. | Booleano |
| **Sigla** | Nome resumido (código) utilizado para identificar um Grupo de Trabalho. | String |
| **Tecnicos** | Pessoas ou Filas do Grupo de Trabalho que atuam no atendimento de Ordens de Serviço | [Lista de Tecnico](objetos_tecnico) |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **ObtemTecnico** | Obtem Solucionador a partir de Identificador de Pessoa. O Solucionador retornado pode estar Desabilitado. Se não encontrar um Solucionador então retorna Nulo | Venki.Supravizio.Recurso.Tecnico ObtemTecnico(int idPessoa); |
| **ObtemCoordenados** | Obtem Solucionadores ativos coordenados pela pessoa fornecida como parâmetro. A pessoa deve ser um coordenador de grupo de trabalho. Se não existir coordenados então é retornada uma lista vazia. A consulta NÃO é recursiva e NÃO são incluídos no resultado membros do tipo Fila. | Venki.Supravizio.Recurso.PessoaList ObtemCoordenados(Venki.Supravizio.Recurso.Pessoa coordenador); |
| **ObtemSubGrupos** | Recupera todos os Sub-Grupos do nível inferiour ou, se for executado com a opção de recursividade, recupera todos os níveis inferiores. | Venki.Supravizio.Recurso.GrupoTrabalhoList ObtemSubGrupos(bool recursivo); |
| **ObtemCoordenados** | Obtem Solucionadores ativos coordenados pela pessoa fornecida como parâmetro. A pessoa deve ser um coordenador de grupo de trabalho. Se não existir coordenados então é retornada uma lista vazia. A consulta NÃO é recursiva e NÃO são incluídos no resultado membros do tipo Fila. Retorna ativos ou todos. | Venki.Supravizio.Recurso.PessoaList ObtemCoordenados(Venki.Supravizio.Recurso.Pessoa coordenador, bool apenasAtivos); |
| **ObtemTodosGruposCoordenados** | Obtem todos os grupos de trabalhos coordenados por uma pessoa. Recursivo. | Venki.Supravizio.Recurso.GrupoTrabalhoList ObtemTodosGruposCoordenados(Pessoa coordenador); |
| **ObtemTodosCoordenadores** | Recupera todos os coordenadores de Grupos de Trabalhos ativos. Os objetos retornados não podem ser modificados. | Venki.Supravizio.Recurso.PessoaList ObtemTodosCoordenadores(); |
| **ObtemSolucionadores** | Recupera todos os solucionadores de um grupo de trabalho com possibilidade de incluir subníveis. Permite excluir ou recuperar apenas Coordenadores. | Venki.Supravizio.Recurso.TecnicoList ObtemSolucionadores(bool incluSubniveis, bool somenteCoordenadores, bool excluiCoordenadores); |
| **ObtemGruposPais** | Recupera todos os grupos que estão acima na hierarquia. A recuperação é executada até que seja encontrado um grupo sem informação de grupo pai. | Venki.Supravizio.Recurso.GrupoTrabalhoList ObtemGruposPais(); |
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | GrupoTrabalho Carrega(int i); |
| **Novo** | Cria um novo registro do tipo GrupoTrabalho | GrupoTrabalho Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | GrupoTrabalho Carrega(string nomePropriedade, object valorPropriedade); |

# PapelClasseNegocio

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio

Um Papel representa uma importante ferramenta para configuração de responsabilidades em um Processo. Com este recurso é possível definir no Processo quem será, por exemplo, o responsável por uma determinada tarefa, quem realizará uma determinada aprovação e assim por diante. O Papel pode ser definido por referências de equipes, solucionadores, por scripts (recuperando registros do banco de dados) e também por composição de Papéis. Também é possível a redefinição de Atores de um Papel por Serviço.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ativo** | Indica que o Papel está ativo no Sistema. Quando inativo o Papel é ignorado pela rotina de cálculo de Atores. | Booleano |
| **AtorGrupoTrabalho** | Critério final de seleção de uma ou mais pessoas aplicado após regras de recuperação. | [AtorGrupoTrabalho](enum_atorgrupotrabalho) |
| **ClasseNegocio** | Classe de Negócio dos Processos onde será publicado o Papel. | [ClasseNegocio](enum_classenegocio) |
| **CodigoAtividade** | Código da atividade para recuperação de solucionadores envolvidos. | String |
| **EnvolvimentoAtividadeExecutada** | Recupera solucionadores pelo tipo de envolvimento na execução da atividade. | [EnvolvimentoAtividade](enum_envolvimentoatividade) |
| **ExcluiAprovacoes** | Exclui da contagem de Ocorrências aquelas que estiveram Pendentes de Aprovação. | Booleano |
| **FiltroAtivo** | Recupera pessoas pela situação cadastral (ativo e/ou inativo) | Booleano |
| **FiltroCargo** | Permite a recuperação pelo preenchimento do campo Cargo. | String |
| **FiltroCustomizados** | Relação de campos customizados do cadastro de Pessoas utilizados como filtro para recuperação | String |
| **FiltroEmpresa** | Relação de empresas onde estão lotadas as pessoas que serão recuperadas | String |
| **FiltroFornecedor** | Relação de empresas fornecedoras para recuperação de pessoas do tipo terceiros | String |
| **FiltroOrgao** | Relação de órgãos onde estão lotadas as pessoas para recuperação | String |
| **FiltroPerfilCliente** | Relação de perfis de clientes utilizados para recuperação de pessoas | String |
| **FiltroUnidadeNegocio** | Relação de Unidades de negócio onde estão localizadas as pessoas que serão recuperadas | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Papel. | Inteiro |
| **Nome** | Descritivo utilizado para nomear um Papel. | String |
| **NomeCampoOcorrencia** | Campo da ocorrência ou cadastro associado utilizado para obter um objeto do tipo Pessoa. | String |
| **OpcaoCampoOcorrencia** | Opção de seleção por hierarquia a partir do campo indicado para recuperação. | [OpcaoCampoPapel](enum_opcaocampopapel) |
| **PapeisComposicao** | Relação de papéis de processo que serão utilizados para compor este papel. O papel resultante é formado pela soma de todas as pessoas sem ocorrência de duplicidades. | [Lista de ComposicaoPapel](objetos_composicaopapel) |
| **PessoaItemConfiguracao** | Define qual campo do Item de Configuração deve ser utilizado para identificação da pessoa. | [PessoaItemPapel](enum_pessoaitempapel) |
| **Referencia** | Descritivo completo do Papel. Este descritivo é utilizado na geração de documentação de Processos. | String |
| **RelacaoGrupos** | Relação de grupos que define a regra de recuperação de solucionadores. | [Lista de GrupoPapel](objetos_grupopapel) |
| **RelacaoOrgaos** | Relação de órgãos que define a regra de recuperação de pessoas. | [Lista de OrgaoPapel](objetos_orgaopapel) |
| **RelacaoPessoas** | Relação de pessoas e filas que serão incluídas na recuperação. | [Lista de PessoaPapel](objetos_pessoapapel) |
| **ScriptSelecaoAtores** | Script para seleção de Atores de um Papel de Processo | String |
| **SomenteConectados** | Seleciona entre as pessoas recuperadas pela configuração aqueles que são usuários solucionadores conectados na aplicação Supravizio. | Booleano |
| **SomenteUltimaExecucao** | São considerados apenas os solucionadores envolvidos na última execução da atividade. | Booleano |
| **Tipo** | Forma de recuperação de pessoas utilizada no cálculo do papel de processo | [TipoPapel](enum_tipopapel) |
| **TipoItemAnexo** | Tipo de Item de Configuração que será utilizado para recuperar o responsável ou usuários que farão parte do papel. Durante o cálculo do papel serão utilizados todos os itens destes tipo que foram anexados na ocorrência. | [ClasseConfiguracao](objetos_classeconfiguracao) |
| **TipoItemAnexoId** | Identificador do Tipo de Item de Configuração | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | PapelClasseNegocio Carrega(int i); |
| **Novo** | Cria um novo registro do tipo PapelClasseNegocio | PapelClasseNegocio Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | PapelClasseNegocio Carrega(string nomePropriedade, object valorPropriedade); |

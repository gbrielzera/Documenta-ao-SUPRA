# ClasseServico

Caminho: Customização > Modelo de objetos > Processo > ClasseServico

Um Tipo de Serviço define classificações para Serviços. Registros deste cadastro são utilizados em diversas configurações do sistema incluindo durante a definição de Processos.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ativo** | Indica que o Tipo de Serviço está ativa no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema. | Booleano |
| **Descricao** | Descrição detalhada do Tipo de Serviço | String |
| **FatorPrioridade** | Fator utilizado no cálculo de Prioridade. É utlizado como valor default quando não for informado no nível de Serviço. | [FatorPrioridade](objetos_fatorprioridade) |
| **FatorPrioridadeId** | Identificador do Fator de Prioridade utilizado para priorizar uma ocorrência. Deve ser utilizado em conjunto com um Método de Priorização. | Inteiro |
| **GrupoServico** | Segundo nível hierárquico de classificação no qual o tipo de Serviço está inserido. | [GrupoServico](objetos_gruposervico) |
| **GrupoServicoId** | Identificador do Grupo de Servicos associado | Inteiro |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Classe de Servico | Inteiro |
| **Sigla** | Nome resumido (código) que identifica unicamente um Tipo de Item de Configuração | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **ObtemValorFatorPrioridade** | Obtem Valor do Fator de Prioridade do Tipo de Serviço. Se não existir um Fator associado então retorna o valor default fornecido como parâmetro. | System.Int32 ObtemValorFatorPrioridade(System.Int32 valorDefault); |
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | ClasseServico Carrega(int i); |
| **Novo** | Cria um novo registro do tipo ClasseServico | ClasseServico Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | ClasseServico Carrega(string nomePropriedade, object valorPropriedade); |

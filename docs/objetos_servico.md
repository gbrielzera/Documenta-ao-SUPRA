# Servico

Caminho: Customização > Modelo de objetos > Processo > Servico

Um Serviço pode ser definido como um sistema composto por Tecnologia, Facilidades, Processos e Pessoas que habilitam um processo de negócio.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ativo** | Define se o Serviço está Ativo. Por padrão o valor inicial é sempre Verdadeiro. | Booleano |
| **AtoresServico** | Sobrepõe a configuração global de Papéis em ocorrências do Serviço. | [Lista de AtoresServico](objetos_atoresservico) |
| **Beneficios** | Benefícios oferecidos pelo Serviço | String |
| **ClasseServico** | Classificação do Serviço. Este atributo é utilizado pelo Cliente na aplicação de Autoatendimento | [ClasseServico](objetos_classeservico) |
| **ClasseServicoId** | Identificador do tipo de Serviço associado | Inteiro |
| **Componentes** | Itens de Configuração que compoem o Serviço. | [Lista de ComponenteServico](objetos_componenteservico) |
| **Descricao** | Descrição detalhada do Produto | String |
| **DescricaoCliente** | Descritivo apresentado para Cliente no Catálogo de Serviços. Se não for preenchido é utilizado a Descrição padrão do Serviço | String |
| **Disponibilidade** | Disponibilidade que pode ser esperada pelo Cliente incluindo horários. | String |
| **DisponibilidadeAA** | Configuração da disponibilidade do Serviço na aplicação de Autoatendimento. Alguns Serviços são utilizados internamente pela área de Tecnologia da Informação e por isto nunca serão visíveis para o Cliente. | Booleano |
| **FatorPrioridade** | Fator utilizado no cálculo de Prioridade. Se não for preenchido é utilizado o valor atribuído a Classe do Serviço quando preenchido. | [FatorPrioridade](objetos_fatorprioridade) |
| **FatorPrioridadeId** | Identificador do(a) FatorPrioridade associado(a) | Inteiro |
| **Id** | Identificador do Serviço | Inteiro |
| **PrerequisitosDependencias** | Pré-requisitos ou Dependências para o perfeito funcionamento do Serviço. | String |
| **ProgramacaoManutencao** | Detalhes sobre a Programação de Manutenção do Serviço incluíndo janelas semanais de paradas. | String |
| **RedefinicaoPapeisItem** | Define o comportamento da rotina de resolução de Atores quando existirem redefinições de Papéis em Itens de Configuração associados em uma Ordem de Serviço. | [RedefinicaoPapeisItem](enum_redefinicaopapeisitem) |
| **Referencia** | Texto de Referência para utilização do Produto | String |
| **ResponsavelArea** | Gerência responsável pelo Serviço na área de negócio cliente do Serviço | [Pessoa](objetos_pessoa) |
| **ResponsavelAreaId** | Identificador da Pessoa responsável pela área de negócio cliente do Serviço | Inteiro |
| **ResponsavelTecnico** | Solucionador responsável pelo Serviço | [Pessoa](objetos_pessoa) |
| **ResponsavelTecnicoId** | Identificador do Solucionador responsável | Inteiro |
| **Sigla** | Nome resumido do Serviço | String |
| **SolicitacaoServicos** | Detalhes sobre procedimento de abertura de Chamados. Se não for preenchido é estabelecido o procedimento padrão por meio do Catálogo de Serviços. | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **ObtemValorFatorPrioridade** | Obtem Valor associado ao Fator de Prioridade do Serviço. Se não existir um Fator de Prioridade no Serviço então é verificado a Classe do Serviço. Se na Classe do Serviço também não existir um fator então é retornado o valor default fornecido como parâmetro. | System.Int32 ObtemValorFatorPrioridade(System.Int32 valorDefault); |
| **ObtemUsuarios** | Obtem usuários do Serviço. Para determinar os usuários do serviço a rotina realiza uma consulta em todos os Itens de Configuração componentes do Serviço e seus sub-componentes (busca recursiva). | Venki.Supravizio.Recurso.PessoaList ObtemUsuarios(); |
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Servico Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Servico | Servico Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Servico Carrega(string nomePropriedade, object valorPropriedade); |

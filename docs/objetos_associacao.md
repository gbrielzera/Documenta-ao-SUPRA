# Associacao

Caminho: Customização > Modelo de objetos > Processo > Associacao

Uma Associação define um relacionamento entre duas Ocorrências de Processo. Estas associações podem ser estabelecidas pelo usuário na tela de edição de Ordens de Serviço ou automaticamente por configuração de Processo. Para criação de uma Associação é necessário definir: um Tipo de Subprocesso para cada uma das ocorrências, uma frase para leitura da Associação, outra fase para leitura inversa da Associação e finalmente a cardinalidade desejada.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ativo** | Indica que a Associacao está ativa no Sistema. Se estiver inativa então não é possível a criação de novas associações desta natureza. | Booleano |
| **CardinalidadeAlvo** | Cardinalidade da Associação no sentido Fonte para Alvo. Indica que podemos ter várias ou uma única ocorrência como Alvo no relacionamento. | [CardinalidadeAssociacao](enum_cardinalidadeassociacao) |
| **CardinalidadeFonte** | Cardinalidade da Associação no sentido Alvo para Fonte | [CardinalidadeAssociacao](enum_cardinalidadeassociacao) |
| **ClasseAlvo** | Tipo de Subprocesso de Ocorrências que é alvo (terminador) em Associações. | [ClasseSubProcesso](objetos_classesubprocesso) |
| **ClasseAlvoId** | Identificador do Tipo de Subprocesso que é invocado pela associação. | Inteiro |
| **ClasseFonte** | Tipo de Subprocesso de Ocorrências que são fonte (iniciadores) em Associações. Indica que podemos ter várias ou uma única ocorrência como Fonte no relacionamento. | [ClasseSubProcesso](objetos_classesubprocesso) |
| **ClasseFonteId** | Identificador do Tipo de Subprocesso que é responsável por invocar uma outra ocorrência de processo (rotina chamadora). | Inteiro |
| **FraseAssociacao** | Frase utilizada para estabelecer a Associação. | String |
| **FraseInversaAssociacao** | Frase utilizada para representar o sentido inverso da Associação. | String |
| **Gatilhos** | Eventos que são disparados pelo sistema na ocorrência de um determinado Tipo de Evento. | [Lista de GatilhoAssociacao](objetos_gatilhoassociacao) |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Associacao | Inteiro |
| **Nome** | Nome para identificação e recuperação da Associação. O nome não pode conter espaços e deve conter apenas caracteres alfanuméricos. Também deve ser único entre todas as Associações e utilizado em scripts para recuperação da Associação. | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **AssociaOcorrencias** | Associa duas ocorrências | void AssociaOcorrencias(Venki.Supravizio.Processo.Ocorrencia fonte, Venki.Supravizio.Processo.Ocorrencia alvo); |
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Associacao Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Associacao | Associacao Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Associacao Carrega(string nomePropriedade, object valorPropriedade); |

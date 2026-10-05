# UnidadeNegocio

Caminho: Customização > Modelo de objetos > Recurso > UnidadeNegocio

A Unidade de Negócio define uma localização (site, filial etc) onde estão localizados os Clientes e Ativos. Para uma Unidade de Negócio é possível cadastrar Prédios e respectivos andares, salas e locais.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ativo** | Indica que a Unidade de Negócio está ativa | Booleano |
| **Calendario** | Um Acordo de Nível de Serviço define prazos de atendimento para solicitações de um cliente. Além de prazos o acordo define condições tais como períodos de disponibilidade, possibilidades de suspensão do tempo, cobertura por processos e remuneração por serviços. O Acordo de Nível de Serviço é atribuido automaticamente pelo sistema no instante em que abrimos uma Ordem de Serviço ou modificamos campos chave: Cliente, Itens de Configuração, Prioridades, Subprocessos, Data/hora de solicitação entre outros. A data/hora de solicitação é considerada o marco inicial da contagem de tempo e a data/hora de fim é o marco final. A data/hora de fim pode ser sobrescrita pela data/hora de entrega de serviço, que pode ser preenchida durante a execução da Ordem de Serviço. | [Calendario](objetos_calendario) |
| **CalendarioId** | Identificador do Calendário associado | Inteiro |
| **Descricao** | Texto que descreve claramente a localização ou finalidade da Unidade de Negócio | String |
| **Empresa** | Empresa para a qual a Unidade pertence. Este campo é utilizado como critério de filtro para os locais exibidos na abertura de Ordens de Serviço do Autoatendimento. Se o usuário conectado estiver associado a uma empresa pertencente a um grupo de empresas, então são exibidas todas as unidades do grupo. Se sua empresa não estiver associada a um grupo então são exibidas as unidades da empresa. | [Empresa](objetos_empresa) |
| **EmpresaId** | Identificador da Empresa associada | Inteiro |
| **Id** | Número sequencial gerado por sistema para identificar uma Unidade de Negócio. Este número não pode ser modificado pelo usuário do sistema. | Inteiro |
| **Localizacao** | Endereço, Cidade, Estado ou qualquer outra referência de Localização da Unidade de Negócio. | String |
| **Predios** | Prédios contidos na Unidade de Negócio | [Lista de Predio](objetos_predio) |
| **Sigla** | Nome resumido (código) utilizado para identificar uma Unidade de Negócio | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | UnidadeNegocio Carrega(int i); |
| **Novo** | Cria um novo registro do tipo UnidadeNegocio | UnidadeNegocio Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | UnidadeNegocio Carrega(string nomePropriedade, object valorPropriedade); |

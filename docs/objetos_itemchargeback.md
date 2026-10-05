# ItemChargeBack

Caminho: Customização > Modelo de objetos > Recurso > ItemChargeBack

Item combrado de uma área em Charge-back. Este item pode se tratar de uso de Ativo, Acordo de Nível de Serviço e Serviço prestado por Ordem de Serviço.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AcordoNivelServico** | Acordo de Nível de Serviço que prevê cobrança por Charge-back | [AcordoNivelServico](objetos_acordonivelservico) |
| **AcordoNivelServicoId** | Identificador do Acordo de Nível de Serviço que gera Charge-back | Inteiro |
| **ChargeBackOrgaoChargeBackId** | Número sequencial gerado automaticamente pelo sistema para Identificar um ChargeBack | Inteiro |
| **ChargeBackOrgaoOrgaoId** | Identificador do Orgao associado | Inteiro |
| **Descricao** | Descrição contendo detalhes do lançamento | String |
| **Favorecido** | Usuário favorecido pelo uso de um Ativo, atendimento de uma Ordem de Serviço ou Acordo de Nível de Serviço. No caso de Acordos de Nível de Serviço do com o critério 'Formula' ou 'Valor Fixo' o favorecido é o gestor da área atendida pelo acordo na ocasião da apuração de Charge-back. Nas demais situações onde existir uma Ordem de Serviço associada o favorecido é preenchido com o campo Favorecido da respectiva Ordem de Serviço. | [Pessoa](objetos_pessoa) |
| **FavorecidoId** | Identificador do usuário favorecido pelo uso de um Ativo, atendimento de uma Ordem de Serviço ou Acordo de Nível de Serviço. | Inteiro |
| **ItemConfiguracao** | Item de Configuração | [ItemConfiguracao](objetos_itemconfiguracao) |
| **ItemConfiguracaoId** | Identificador do Ativo que demanda Charge-back | Inteiro |
| **MemoriaCalculo** | Dados utilizados pelo sistema para obter o valor do Item. Estes dados podem variar em função da origem da informação (Acordo de Nível de Serviço, Ativo etc) | String |
| **OrdemServico** | Ordem de Serviço para serviço que gerou cobrança | [OrdemServico](objetos_ordemservico) |
| **OrdemServicoId** | Identificador da Ordem de Serviço que demanda charge-back. | Inteiro |
| **Sequencial** | Sequencial utilizado para identificar o item dentro do Charge-back de uma Área | Inteiro |
| **ValorItem** | Valor do lançamento que pode ser gerado por um preço de Ativo, valor estabelecido no ANS ou no campo Valor de Charge-back da Ordem de Serviço. | Decimal |

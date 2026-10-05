# ItemComponente

Caminho: Customização > Modelo de objetos > Ativos > ItemComponente

Componentes de um Item de Configuração

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ClasseConfiguracao** | Tipo de Item de Configuração do Componente. | [ClasseConfiguracao](objetos_classeconfiguracao) |
| **ClasseConfiguracaoId** | Identificador do Tipo de Item de Configuração do Componente | Inteiro |
| **CodigoOCS** | Código do componente original do banco de dados OCS | String |
| **Comentario** | Comentário sobre a relação Componente. Para conhecimento do autor do Comentário utilize a ferramenta de Consulta de Trilha de Modificações do Item. | String |
| **Componente** | Item Componente | [ItemConfiguracao](objetos_itemconfiguracao) |
| **DataEntrega** | Data de entrega do Componente | Data/hora |
| **Descricao** | Descritivo do componente | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Componente | Inteiro |
| **ItemComponenteId** | Identificador do Item de Configuração que é o Componente | Inteiro |
| **ItemConfiguracaoId** | Identificador do Item de Configuração proprietário do Componente | Inteiro |
| **Modelo** | Modelo de Item de Configuração segundo especificação de um Fabricante. | [Modelo](objetos_modelo) |
| **ModeloId** | Identificador do Modelo associado | Inteiro |
| **NumeroSerie** | Número de série | String |
| **Ocorrencia** | Ocorrência que gerou o componente | [Ocorrencia](objetos_ocorrencia) |
| **OcorrenciaId** | Identificador da Ocorrencia associada | Inteiro |
| **TabelaOCS** | Tabela original do OCS que gerou o componente | String |
| **Tamanho** | Tamanho do Componente | Decimal |
| **ValorCustoAquisicao** | Custom total de aquisição do Item | Decimal |
| **ValorCustoManutencao** | Valor do Custo de Manutenção Mensal do Componente | Decimal |
| **ValorPrecoAquisicao** | Preço de aquisição para Charge-Back do Componente. O valor de aquisição é lançado no charge-back de competência relativa a Data de Entrega do componente. | Decimal |
| **ValorPrecoManutencao** | Preço de Charge-back de manutenção mensal | Decimal |

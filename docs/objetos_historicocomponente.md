# HistoricoComponente

Caminho: Customização > Modelo de objetos > Recurso > HistoricoComponente

Histórico de componentes para um item de Configuração. Este histórico é gerado pela rotina de charge-back para rastreabilidade da base de cálculo.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ClasseConfiguracao** | Tipo de Item de Configuração | [ClasseConfiguracao](objetos_classeconfiguracao) |
| **ClasseConfiguracaoId** | Identificador do Tipo do Item de Configuração. Se for preenchida a propriedade Componente então esta propriedade é preenchida automaticamente com a mesma classe do componente informado. | Inteiro |
| **Componente** | Componente | [ItemConfiguracao](objetos_itemconfiguracao) |
| **ComponenteId** | Identificador do ItemConfiguracao associado | Inteiro |
| **HistoricoItemChargeBackId** | Identificador da apuração de Charge-back que gerou o histórico | Inteiro |
| **HistoricoItemItemConfiguracaoId** | Identificador do ItemConfiguracao associado | Inteiro |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um HistoricoComponente | Inteiro |
| **Tamanho** | Tamanho do Componente | Decimal |
| **ValorPrecoAquisicao** | Valor do Preço de aquisição do componente na ocasição da apuração de charge-back. | Decimal |
| **ValorPrecoManutencao** | Valor do Preço de manutenção do componente na ocasição da apuração de charge-back. | Decimal |

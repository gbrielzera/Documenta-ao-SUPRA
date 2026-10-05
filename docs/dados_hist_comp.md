# HIST_COMP

Caminho: Customização > Modelo de dados > Recurso > HIST_COMP

Histórico de componentes para um item de Configuração. Este histórico é gerado pela rotina de charge-back para rastreabilidade da base de cálculo.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_HIST_COMP** | Número sequencial gerado automaticamente pelo sistema para Identificar um HistoricoComponente | int | number(6,0) | Não |
| **ID_CHARGE_BACK** | Identificador da apuração de Charge-back que gerou o histórico | int | number(6,0) | Não |
| **ID_ITEM** | Identificador do ItemConfiguracao associado | int | number(6,0) | Não |
| **ID_COMPONENTE** | Identificador do ItemConfiguracao associado | int | number(6,0) | Sim |
| **TAMANHO** | Tamanho do Componente | decimal(15,2) | number(15,2) | Sim |
| **ID_CLASSE_CONFIGURACAO** | Identificador do Tipo do Item de Configuração. Se for preenchida a propriedade Componente então esta propriedade é preenchida automaticamente com a mesma classe do componente informado. | int | number(6,0) | Não |
| **PRECO_AQUISICAO** | Valor do Preço de aquisição do componente na ocasição da apuração de charge-back. | decimal(15,2) | number(15,2) | Sim |
| **PRECO_MANUTENCAO** | Valor do Preço de manutenção do componente na ocasição da apuração de charge-back. | decimal(15,2) | number(15,2) | Sim |

Tabelas referenciadas por HIST_COMP

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM](dados_item) | \| **ITEM** \| **HIST_COMP** \| \|---\|---\| \| ID_ITEM \| ID_COMPONENTE \| |
| [CLASSE_CONFIGURACAO](dados_classe_configuracao) | \| **CLASSE_CONFIGURACAO** \| **HIST_COMP** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |
| [HIST_ITEM](dados_hist_item) | \| **HIST_ITEM** \| **HIST_COMP** \| \|---\|---\| \| ID_CHARGE_BACK \| ID_CHARGE_BACK \| \| ID_ITEM \| ID_ITEM \| |

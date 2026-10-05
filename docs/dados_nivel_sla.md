# NIVEL_SLA

Caminho: Customização > Modelo de dados > Processo > NIVEL_SLA

Nível de ANS define faixas de tempo para escalonamento de ANS em um Método de Priorização (por exemplo Incidentes).

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_NIVEL_SLA** | Número sequencial gerado automaticamente pelo sistema para Identificar um NivelSLA | int | number(6,0) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **SEQUENCIAL** | Sequencial | int | number(6,0) | Não |
| **COR_INDICADOR** | Cor associada ao nível de ANS. Na tela da de Fila de Ordens de Serviço é exibido um ícone nesta cor indicando o Nível atual de ANS. | varchar(250) | varchar(250) | Não |
| **PERC_TEMPO** | Percentual do tempo total do Acordo de Nível de Serviço | int | number(6,0) | Sim |
| **VISIVEL_PAINEL_WS** | Indica que Ordens de Serviço neste nível serão exibidas no Painel de Alertas da transação Workspace. Esta configuração ainda está condicionada a regra de visualização do Grupo de Trabalho (veja as configurações do Grupo de Trabalho do solucionador). | char(3) | char(3) | Não |

Tabelas que dependem de NIVEL_SLA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ORDEM_SERVICO](dados_ordem_servico) | \| **ORDEM_SERVICO** \| **NIVEL_SLA** \| \|---\|---\| \| ID_NIVEL_SLA \| ID_NIVEL_SLA \| |
| [SLA_OS](dados_sla_os) | \| **SLA_OS** \| **NIVEL_SLA** \| \|---\|---\| \| ID_NIVEL_SLA \| ID_NIVEL_SLA \| |

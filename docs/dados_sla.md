# SLA

Caminho: Customização > Modelo de dados > Recurso > SLA

Um Calendário é um cadastro que contém feriados e períodos úteis de trabalho. O Calendário pode ser utilizado no cálculo de Acordos de Nível de Serviço quando este habilita o uso de feriados. O calendário é utilizado também no cálculo do Acordo de Nível Operacional servindo de referência para determinar tempos aplicados na execução de atividades. É importante que o solucionador tenha um calendário associado caso contrário o recurso terá sua disponibilidade equivalente a 24x7 (24 dias da semana x 7 dias da semana). Outra aplicação de um calendário está na apuração de indicadores de desempenho. Neste caso os calendários são utilizados para determinar a quantidade de dias úteis no mês apurado e influenciar no cálculo de ritmo.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_SLA** | Número sequencial gerado automaticamente pelo sistema para Identificar um AcordoNivelServico | int | number(6,0) | Não |
| **DESCRICAO** | Texto que descreve claramente a aplicação do Acordo de Nível de Serviço. Recomenda-se incluir o período de vigência e, quando possível, área atendida pelo Acordo. | varchar(500) | varchar(500) | Não |
| **DATA_INICIO_VALIDADE** | Data de início de validade do Acordo de Nível de Serviço. Uma Ordem de Serviço só pode ser associada a um acordo cuja data de validade seja maior ou igual a data de abertura da ocorrência. | datetime | date | Não |
| **DATA_FIM_VALIDADE** | Data de fim de validade do Acordo de Nível de Serviço. Uma Ordem de Serviço só pode ser associada a um acordo cuja data de fim de validade seja menor que a data de abertura da ocorrência. | datetime | date | Não |
| **CONSIDERA_FERIADOS** | Indica que todos os feriados do calendário associado com o Cliente são desconsiderados no cálculo de tempo (o intervalo referente ao feriado é excluído da contagem de tempo). Para consultar o calendário do cliente acesse o cadastro da Unidade onde está localizado o cliente (campo Local no cadastro da Pessoa). | char(3) | char(3) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **ID_PLANO_GESTAO** | Identificador do Plano de Gestao associado | int | number(6,0) | Sim |
| **VALOR_CHARGE_BACK** | Valor para cobrança pela rotina de Charge-back. Se o critério de charge-back for 'Hora' então o valor total é obtido pela multiplicação do 'Valor' pela quantidade de horas apontadas no período de apuração. Se o critério de charge-back for 'Ocorrência' então o total é obtido pela multiplicação do 'Valor' pela quantidade total de ocorrências finalizadas no período de apuração. Para o critério 'ValorFixo' o campo 'Valor' já indica o total de charge-back enquanto nos critérios 'Nenhum' ou 'Formula' não fazem uso desta informação. | decimal(15,2) | number(15,2) | Sim |
| **EXP_CHARGE_BACK** | Fórmula para cálculo de Charge-back em um determinado mês. Se o critério de Charge-back for 'Fórmula' ou 'ValorFixo' então esta fórmula é executada uma única vez e deve retornar o valor para Charge-back no período, caso contrário é executada para todo item calculado e permite a modificação do valor calculado inicialmente pelo sistema. | text | clob | Sim |
| **CRIT_CHARGE_BACK** | Forma de cálculo de Charge-back para o Acordo de Nivel de Serviço. | varchar(250) | varchar(250) | Não |
| **PENALIZACAO** | Penalização aplicada no valor de Charge-back caso existam Ordens de Serviço em que não foi cumprido o Acordo de Nível de Serviço. Esta regra é válida somente para as opções de Charge-back 'Ocorrencia' e 'Hora'. | int | number(6,0) | Sim |
| **PUBLICA_INFORMACOES_AA** | Permite publicar ou não informações sobre ANS no site de Autoatendimento. As informações são exibidas no Autoatendimento na página de consulta e na finalização de abertura de uma Ordem de Serviço. | char(3) | char(3) | Não |

Tabelas referenciadas por SLA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PLANO_GESTAO](dados_plano_gestao) | \| **PLANO_GESTAO** \| **SLA** \| \|---\|---\| \| ID_PLANO_GESTAO \| ID_PLANO_GESTAO \| |

Tabelas que dependem de SLA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM_CHARGE_BACK](dados_item_charge_back) | \| **ITEM_CHARGE_BACK** \| **SLA** \| \|---\|---\| \| ID_SLA \| ID_SLA \| |
| [ITEM_SLA](dados_item_sla) | \| **ITEM_SLA** \| **SLA** \| \|---\|---\| \| ID_SLA \| ID_SLA \| |
| [DISP_ATEND](dados_disp_atend) | \| **DISP_ATEND** \| **SLA** \| \|---\|---\| \| ID_SLA \| ID_SLA \| |
| [ACORDO_INTER_SLA](dados_acordo_inter_sla) | \| **ACORDO_INTER_SLA** \| **SLA** \| \|---\|---\| \| ID_SLA \| ID_SLA \| |
| [APLIC_PROCESSO](dados_aplic_processo) | \| **APLIC_PROCESSO** \| **SLA** \| \|---\|---\| \| ID_SLA \| ID_SLA \| |
| [ORGAO_SLA](dados_orgao_sla) | \| **ORGAO_SLA** \| **SLA** \| \|---\|---\| \| ID_SLA \| ID_SLA \| |

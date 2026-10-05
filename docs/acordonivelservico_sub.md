# Acordo de Nível de Serviço

Caminho: Janelas > Recurso > Acordo de Nível de Serviço

Um Calendário é um cadastro que contém feriados e períodos úteis de trabalho. O Calendário pode ser utilizado no cálculo de Acordos de Nível de Serviço quando este habilita o uso de feriados. O calendário é utilizado também no cálculo do Acordo de Nível Operacional servindo de referência para determinar tempos aplicados na execução de atividades. É importante que o solucionador tenha um calendário associado caso contrário o recurso terá sua disponibilidade equivalente a 24x7 (24 dias da semana x 7 dias da semana). Outra aplicação de um calendário está na apuração de indicadores de desempenho. Neste caso os calendários são utilizados para determinar a quantidade de dias úteis no mês apurado e influenciar no cálculo de ritmo.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Recurso | Acordos de Nível de Serviço | Acordos de Nível de Serviço**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Descrição** | Texto que descreve claramente a aplicação do Acordo de Nível de Serviço. Recomenda-se incluir o período de vigência e, quando possível, área atendida pelo Acordo. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRICAO da tabela [SLA](dados_sla). |
|---|---|
| **Data início validade** | Data de início de validade do Acordo de Nível de Serviço. Uma Ordem de Serviço só pode ser associada a um acordo cuja data de validade seja maior ou igual a data de abertura da ocorrência. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Data de início deve ser menor que a Data de fim de Validade Este campo é mantido na coluna DATA_INICIO_VALIDADE da tabela [SLA](dados_sla). |
| **Data fim validade** | Data de fim de validade do Acordo de Nível de Serviço. Uma Ordem de Serviço só pode ser associada a um acordo cuja data de fim de validade seja menor que a data de abertura da ocorrência. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DATA_FIM_VALIDADE da tabela [SLA](dados_sla). |
| **Considerar feriados no cálculo de tempo** | Indica que todos os feriados do calendário associado com o Cliente são desconsiderados no cálculo de tempo (o intervalo referente ao feriado é excluído da contagem de tempo). Para consultar o calendário do cliente acesse o cadastro da Unidade onde está localizado o cliente (campo Local no cadastro da Pessoa). Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna CONSIDERA_FERIADOS da tabela [SLA](dados_sla). |
| **Plano de Gestão** | Conjunto de Indicadores de Desempenho (meta e realizado) para gerenciar o cumprimento do Acordo de Nível de Serviço. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Publicar informações no Autoatendimento** | Permite publicar ou não informações sobre ANS no site de Autoatendimento. As informações são exibidas no Autoatendimento na página de consulta e na finalização de abertura de uma Ordem de Serviço. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna PUBLICA_INFORMACOES_AA da tabela [SLA](dados_sla). |

| **Horários de Serviço** | Disponibilidade de atendimento (horário de início e horário de fim) nos dias da semana. A disponibilidade é levada em consideração no cálculo do tempo restante de atendimento. Todos os registros desta coleção de dados são mantidos na tabela [DISP_ATEND](dados_disp_atend). |
|---|---|

| **Órgãos atendidos** | Relação de Órgãos atendidos pelo ANS Todos os registros desta coleção de dados são mantidos na tabela [ORGAO_SLA](dados_orgao_sla). |
|---|---|

| **Tempos de atendimento** | Itens do Acordo do Nível de Serviço que define o tempo de atendimento de uma Ordem de Serviço. Para determinar o Acordo de Nível de Serviço o sistema compara a Ordem de Serviço e os vários Critérios de Acordos cujo Cliente possui lotação relacionada (levando-se em conta hierarquia entre Órgãos e parâmetro de incluir sub-áreas de Acordos) são comparados levando-se em consideração aquele que apresenta o menor tempo de atendimento. Todos os registros desta coleção de dados são mantidos na tabela [ITEM_SLA](dados_item_sla). |
|---|---|

| **Interrupções** | Interrupções acordadas na cronometragem do tempo total de atendimento. Todos os registros desta coleção de dados são mantidos na tabela [ACORDO_INTER_SLA](dados_acordo_inter_sla). |
|---|---|

| **Processos acordados** | Processos em que o Acordo de Nível de Serviço será aplicado. Todos os registros desta coleção de dados são mantidos na tabela [APLIC_PROCESSO](dados_aplic_processo). |
|---|---|

| **Critério** | Forma de cálculo de Charge-back para o Acordo de Nível de Serviço. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna CRIT_CHARGE_BACK da tabela [SLA](dados_sla). |
|---|---|
| **Valor** | Valor para cobrança pela rotina de Charge-back. Se o critério de charge-back for 'Hora' então o valor total é obtido pela multiplicação do 'Valor' pela quantidade de horas apontadas no período de apuração. Se o critério de charge-back for 'Ocorrência' então o total é obtido pela multiplicação do 'Valor' pela quantidade total de ocorrências finalizadas no período de apuração. Para o critério 'ValorFixo' o campo 'Valor' já indica o total de charge-back enquanto nos critérios 'Nenhum' ou 'Formula' não fazem uso desta informação. |
| **Fórmula** | Fórmula para cálculo de Charge-back em um determinado mês. Se o critério de Charge-back for 'Fórmula' ou 'ValorFixo' então esta fórmula é executada uma única vez e deve retornar o valor para Charge-back no período, caso contrário é executada para todo item calculado e permite a modificação do valor calculado inicialmente pelo sistema. |
| **Penalização** | Penalização aplicada no valor de Charge-back caso existam Ordens de Serviço em que não foi cumprido o Acordo de Nível de Serviço. Esta regra é válida somente para as opções de Charge-back 'Ocorrencia' e 'Hora'. Para este campo existem as seguintes regras: - A Penalização deve ser maior ou igual a 0 - A Penalização deve ser menor ou igual a 100 Este campo é mantido na coluna PENALIZACAO da tabela [SLA](dados_sla). |

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Acordo de Nível de Serviço a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Acordo de Nível de Serviço se este for utilizado em um dos cadastros abaixo:

- Item de Charge-back apurado

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

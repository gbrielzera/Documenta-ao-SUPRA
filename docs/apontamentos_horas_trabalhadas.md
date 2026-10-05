# Apontamentos de Horas Trabalhadas

Caminho: Relatórios > Apontamentos de Horas Trabalhadas

O relatório de Apontamentos de Horas Trabalhadas tem por objetivo apresentar uma listagem dos apontamentos realizados em Ordens de Serviço por Solucionadores. Com este relatório é possível analisar o desempenho dos solucionadores com base nos apontamentos realizados.

## Parâmetros

Na figura abaixo podemos observar a tela de parâmetros para este relatório:

Parâmetros do relatório

| Contrato | Este parâmetro filtra os registros de acordo com o valor informado no campo Contrato da ocorrência. Se não for informado então este critério é desconsiderado na recuperação. |
|---|---|
| **Solucionador** | Este parâmetro filtra os registros de acordo com Solucionador responsável pelo Apontamento de Horas. Se não for informado então este critério é desconsiderado na recuperação. |
| **Data Início** | Data de início para recuperação dos apontamentos. Este parâmetro recupera os apontamentos cuja data de referência seja maior ou igual ao valor informado. |
| **Data Fim** | Data limite fim para recuperação dos apontamentos. Este parâmetro recupera os apontamentos cuja data de referência seja menor ou igual ao valor informado. |
| **Área Cliente** | Filtra os registros de acordo com o Área Cliente com o valor informado no campo Cliente da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Inclui Sub-áreas** | Este parâmetro é utilizado em conjunto com o de Área Cliente. Se este parâmetro estiver marcado incluirá o Sub-orgão do Orgão Cliente selecionado no campo anterior. |
| **Processo** | Filtra registros pelo Processo associado com a classificação da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Subprocesso** | Filtra registros de acordo com o Subprocesso associado com a classificação da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Serviço** | Filtra registros pelo valor informado no campo Serviço da ocorrência. Se não for informado então este critério é desconsiderado na recuperação. |
| **Exibir Gráficos** |  |

Este relatório de Apontamentos de Horas trabalhadas também está disponíveis na transação Workspace e é executado a partir da seleção de Ordens de Serviço.

No exemplo abaixo foi selecionado um conjunto reduzido de Ordens de Serviço para gerar o relatório:

Execução de relatórios a partir do Workspace

Além do filtro informado pelo usuário existe outro implícito onde:

- Se o usuário conectado possui o perfil Administrador então é possível recuperar apontamentos de todos os solucionadores
- Se o usuário não possui o perfil Administrador mas é coordenador de algum Grupo de Trabalho então ele visualiza seus próprios apontamentos e também de todos os seus coordenados incluindo sub-níveis.
- Se o usuário não é Administrador nem coordenador então ele visualiza apenas os seus apontamentos.

## Saídas

Após informar os parâmetros de recuperação, clique no botão **Consultar** para visualizar o conteúdo do relatório. O relatório de Apontamentos de Horas Trabalhadas exibe vários gráficos.

Veja abaixo um exemplo de saída para este relatório:

Gráficos apresentados na saída do relatório de Apontamentos de Horas Trabalhadas

Podemos visualizar no exemplo acima os seguintes gráficos:

| TOP 10 Serviços | Este gráfico apresenta o percentual de apontamentos realizados por Serviço informado na ocorrência. |
|---|---|
| **TOP 10 Tipos de Apontamentos** | Este gráfico apresenta o percentual de apontamentos realizados por [Tipo de Apontamentos](cadastro_tipo_apontamento_2) selecionado pelo solucionador ao apontar as horas. |
| **TOP 10 Processos** | Este gráfico apresenta o percentual de apontamentos realizados por Processo associado à classificação da Ordem de Serviço. |
| **TOP 10 Subprocessos** | Este gráfico apresenta o percentual de apontamentos realizados por Subprocesso associado à classificação da Ordem de Serviço. |
| **TOP 10 Contratos** | Este gráfico apresenta o percentual de apontamentos realizados por Contratos informado na ocorrência. |
| **TOP 10 Áreas** | Este gráfico apresenta o percentual de apontamentos realizados por Áreas ou Áreas de Clientes determinados pelo valor informado no campo Cliente da Ordem de Serviço. |

Em seguida são apresentados os dados relativos a cada solucionador que realizou os apontamentos:

Apontamentos dos Solucionadores

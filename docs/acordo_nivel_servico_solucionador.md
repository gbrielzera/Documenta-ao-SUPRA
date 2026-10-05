# Acordo de Nível de Serviço por Solucionador

Caminho: Relatórios > Acordo de Nível de Serviço por Solucionador

O relatório de Acordo de Nível de Serviço por Solucionador tem por objetivo apresentar um resumo quantitativo das Ordens de Serviços que foram atendidas ou não dentro do Acordo de Nível de Serviço de acordo com o Solucionador. Com este relatório é possível identificar se o Acordo de Nível de Serviço está sendo atendido ou não.

## Parâmetros

Na figura abaixo podemos observar a tela de parâmetros para este relatório:

Parâmetros do relatório

| Tipo Filtro | Este parâmetro está relacionado com a **Data início** e **Data fim** de recuperação e possui as seguintes opções: - **Abertas em**: recupera Ordens de Serviços abertas entre a data início e data fim, não importando a situação corrente do registro. - **Abertas e não solucionadas em**: recupera Ordens de Serviço abertas entra a data de início e data fim e que não foram finalizadas até o momento. Importante: a situação Cancelada é considerada uma finalização e portanto registros nesta situação não serão recuperados. - **Finalizadas em**: recupera Ordens de Serviço finalizadas entre a data início e data fim. Ordens de Serviço canceladas são desconsideradas nesta opção. - **Reabertas em**: recupera Ordens de Serviço reabertas entre a data início e data fim. São consideradas todos os eventos de reabertura, ou seja, uma Ordem de Serviço pode constar em diversos períodos consultados. |
|---|---|
| **Data Início** | Data de início para recuperação. Este parâmetro é utilizado em conjunto com o tipo de filtro e recupera os registros cuja data de referência seja maior ou igual ao valor informado. |
| **Data Fim** | Data limite fim para recuperação. Este parâmetro é utilizado em conjunto com o tipo de filtro e recupera os registros cuja data de referência seja menor ou igual ao valor informado. |
| **Grupo de Trabalho** | Filtra registros cujo responsável corrente ou último responsável seja do grupo informado. Se não for informado então este critério é desconsiderado na recuperação. |
| **Inclui sub-grupos** | Este parâmetro é utilizado em conjunto com o de Grupo de Trabalho. Se estiver marcado incluirá os sub-grupos do grupo selecionado no campo anterior. |
| **Acordo Nível de Serviço** | Filtra registros pelo Processo associado com a classificação da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Serviço** | Filtra registros pelo valor informado no campo Serviço da ocorrência. Se não for informado então este critério é desconsiderado na recuperação. |
| **Processo** | Filtra registros pelo Processo associado com a classificação da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Subprocesso** | Filtra registros de acordo com o Subprocesso associado com a classificação da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Tipo Item** | Recupera Ordens de Serviço que tenha um item associado do mesmo tipo informado neste campo. Se não for informado então este critério é desconsiderado. |
| **Solucionador** | Este parâmetro filtra os registros de acordo com Solucionador Responsável pela Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |

Este relatório também está disponível na transação Workspace e é executado a partir da seleção de Ordens de Serviço.

No exemplo abaixo foi selecionado um conjunto reduzido de Ordens de Serviço para gerar o relatório:

Execução de relatórios a partir do Workspace

Além do filtro de recuperação informado pelo usuário existe também outro implícito por macroprocessos, que é aplicado em consultas por usuários que não possuem o perfil Administrador. Na figura abaixo podemos observar a mensagem exibida no rodapé da tela de relatórios quando o usuário não possui o perfil Administrador:

IO

Alerta sobre filtro por macroprocessos

## Saídas

Após informar os parâmetros de recuperação clique no botão **Consultar** para visualizar o conteúdo do relatório. O relatório agrupa todos os Grupos de Trabalho que possuem atendimentos de Acordo de Nível de Serviço exibindo um gráfico com a quantidade de atendimentos do Acordo de Nível de Serviço por solucionadores.

Abaixo do gráfico é exibida uma listagem quantitativa de ANS atendido ou não atendido, de acordo com o atendente e o serviço registrado na ocorrência.

Veja abaixo um exemplo de saída deste relatório:

Gráficos apresentados na saída do relatório

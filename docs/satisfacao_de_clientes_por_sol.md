# Satisfação de Clientes por Solucionadores

Caminho: Relatórios > Satisfação de Clientes por Solucionadores

O relatório de Satisfação de Clientes por Solucionadores tem por objetivo apresentar um resumo quantitativo de respostas de pesquisa de satisfação agrupadas por Grupos de Trabalho e Solucionadores. Com este relatório é possível analisar o desempenho de equipes com base na qualidade atestada pelo Cliente.

## Parâmetros

Na figura abaixo podemos observar a tela de parâmetros para este relatório:

Parâmetros do relatório

| Tipo Filtro | Este parâmetro está relacionado com a **Data início** e **Data fim** de recuperação e possui as seguintes opções: - **Abertas em**: recupera Ordens de Serviços abertas entre a data início e data fim, não importando a situação corrente do registro. - **Abertas e não solucionadas em**: recupera Ordens de Serviço abertas entra a data de início e data fim e que não foram finalizadas até o momento. Importante: a situação Cancelada é considerada uma finalização e portanto registros nesta situação não serão recuperados. - **Finalizadas em**: recupera Ordens de Serviço finalizadas entre a data início e data fim. Ordens de Serviço canceladas são desconsideradas nesta opção. - **Canceladas em**: recupera Ordens de Serviço canceladas entre a data início e data fim, considerando para isto a data/hora do último cancelamento para o registro. Também são consideradas canceladas as ocorrências com finalização do tipo "Não- realizada". - **Reabertas em**: recupera Ordens de Serviço reabertas entre a data início e data fim. São consideradas todos os eventos de reabertura, ou seja, uma Ordem de Serviço pode constar em diversos períodos consultados. |
|---|---|
| **Data Início** | Data de início para recuperação. Este parâmetro é utilizado em conjunto com o tipo de filtro e recupera os registros cuja data de referência seja maior ou igual ao valor informado. |
| **Data Fim** | Data limite fim para recuperação. Este parâmetro é utilizado em conjunto com o tipo de filtro e recupera os registros cuja data de referência seja menor ou igual ao valor informado. |
| **Serviço** | Filtra registros pelo valor informado no campo Serviço da ocorrência. Se não for informado então este critério é desconsiderado na recuperação. |
| **Processo** | Filtra registros pelo processo associado com a classificação da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Grupo de Trabalho** | Filtra registros cujo responsável corrente ou último responsável seja do grupo informado. Se não for informado então este critério é desconsiderado na recuperação. |
| **Inclui sub-grupos** | Este parâmetro é utilizado em conjunto com o de Grupo de Trabalho. Se estiver marcado incluirá os sub-grupos do grupo selecionado no campo anterior. |
| **Tipo Item** | Recupera Ordens de Serviço que tenha um item associado do mesmo tipo informado neste campo. Se não for informado então este critério é desconsiderado. |

## Saídas

Após informar os parâmetros de recuperação clique no botão **Consultar** para visualizar o conteúdo do relatório. O relatório agrupa todos os Grupos de Trabalho avaliados exibindo um gráfico com avaliação de todos os solucionadores. Em seguida são apresentados os dados relativos a cada solucionador avaliado.

Veja abaixo um exemplo de saída para este relatório:

Avaliação do Grupo de Trabalho

Avaliação de um solucionador

# Análise de melhorias em Processos

Caminho: Relatórios > Análise de melhorias em Processos

O relatório de Análise de Melhorias em Processos tem por objetivo apresentar um resumo quantitativo das melhorias realizadas nos Processos. Através deste relatório podemos comparar a quantidade de avaliações positivas, atividades automáticas e conformidade de papéis das versões dos Processos.

## Parâmetros

Na figura abaixo podemos observar a tela de parâmetros para este relatório:

Parâmetros do relatório

| Versões | Este parâmetro filtra processos de acordo com a verão preenchida. Se não for informado então este critério é desconsiderado na recuperação. |
|---|---|
| **Processo** | Filtra registros do processo que for indicado. Se não for informado então este critério é desconsiderado na recuperação. |
| **Área cliente** | Filtra processos relacionados ao Área indicado. Se não for informado então este critério é desconsiderado na recuperação. |
| **Inclui sub-áreas** | Este parâmetro é utilizado em conjunto com o de Área. Se este parâmetro estiver marcado incluirá o Sub-orgão do Orgão selecionado no campo anterior. |
| **Serviço** | Filtra registros de processos relacionados ao serviço informado. Se não for informado então este critério é desconsiderado na recuperação. |
| **Tipo Filtro** | Este parâmetro está relacionado com a **Data início** e **Data fim** de recuperação e possui as seguintes opções: - **Abertas em**: recupera Ordens de Serviços abertas entre a data início e data fim, não importando a situação corrente do registro. - **Abertas e não solucionadas em**: recupera Ordens de Serviço abertas entra a data de início e data fim e que não foram finalizadas até o momento. Importante: a situação Cancelada é considerada uma finalização e portanto registros nesta situação não serão recuperados. - **Finalizadas em**: recupera Ordens de Serviço finalizadas entre a data início e data fim. Ordens de Serviço canceladas são desconsideradas nesta opção. - **Canceladas em**: recupera Ordens de Serviço canceladas entre a data início e data fim, considerando para isto a data/hora do último cancelamento para o registro. Também são consideradas canceladas as ocorrências com finalização do tipo "Não- realizada". - **Reabertas em**: recupera Ordens de Serviço reabertas entre a data início e data fim. São consideradas todos os eventos de reabertura, ou seja, uma Ordem de Serviço pode constar em diversos períodos consultados. |
| **Data Início** | Data de início para recuperação dos processos. Este parâmetro é utilizado em conjunto com o tipo de filtro e recupera os registros cuja data de referência seja maior ou igual ao valor informado. |
| **Data Fim** | Data limite fim para recuperação processos. Este parâmetro é utilizado em conjunto com o tipo de filtro e recupera os registros cuja data de referência seja menor ou igual ao valor informado. |

Além do filtro de recuperação informado pelo usuário existe também outro implícito por macroprocessos, que é aplicado em consultas por usuários que não possuem o perfil Administrador. Na figura abaixo podemos observar a mensagem exibida no rodapé da tela de relatórios quando o usuário não possui o perfil Administrador:

Alerta sobre filtro por macroprocessos

## Saídas

Após informar os parâmetros de recuperação clique no botão **Consultar** para visualizar o conteúdo do relatório.

Podemos observar nas figuras abaixo que este relatório apresenta um gráfico com a evolução de um processo ou subprocesso em suas diversas versões. Neste gráfico são apresentas três colunas:

**Avaliações positivas**: percentual de pesquisas de satisfação enviadas para clientes que foram respondidas positivamente ou não foram respondidas.

**Atividades automáticas**: tarefas do processo que foram executadas automaticamente pelo sistema. Como situações de automatismos podemos considerar: tarefas automatizadas por scripts python, aprovações configuradas e enviadas automaticamente, envio de emails por intermediários e muitos outros.

**Conformidade Papéis**: mede a aderência da execução das Ordens de Serviço quanto a responsabilidade configurada versus os solucionadores executantes. Para análises mais detalhadas utilizando Conformidade de Papéis verifique o tópico [Tabela Dinâmica de Atividades Executadas](tabela_dinamica_de_atividades_).

Gráficos apresentados na saída do relatório

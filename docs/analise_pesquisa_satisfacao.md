# Analise de Pesquisa de Satisfação por Clientes

Caminho: Relatórios > Analise de Pesquisa de Satisfação por Clientes

O Relatório de Analise de Pesquisa de Satisfação por Clientes tem por objetivo apresentar um resumo quantitativo de respostas de pesquisas de satisfação realizadas por clientes. Com este relatório é possível analisar o desempenho de equipes com base na qualidade atestada pelo cliente. Podemos obter o percentual de avaliações negativas na exibição de gráficos agrupados por Áreas, serviços e subprocessos. Através deste relatório também é possível visualizar uma listagem detalhada das Ordens de Serviço que obtiveram avaliações negativas em sua pesquisa de satisfação.

## Parâmetros

## Parâmetros do relatório

| **Tipo Filtro** | Este parâmetro está relacionado com a **Data início** e **Data fim** de recuperação e possui as seguintes opções: - **Respondidas em: **recupera Ordens de Serviço em que tenham respostas de Pesquisa de Satisfação entre a data início e data fim. - **Abertas em**: recupera Ordens de Serviços abertas entre a data início e data fim, não importando a situação corrente do registro. - **Abertas e não solucionadas em**: recupera Ordens de Serviço abertas entra a data de início e data fim e que não foram finalizadas até o momento. Importante: a situação Cancelada é considerada uma finalização e portanto registros nesta situação não serão recuperados. - **Finalizadas em**: recupera Ordens de Serviço finalizadas entre a data início e data fim. Ordens de Serviço canceladas são desconsideradas nesta opção. - **Reabertas em**: recupera Ordens de Serviço reabertas entre a data início e data fim. São consideradas todos os eventos de reabertura, ou seja, uma Ordem de Serviço pode constar em diversos períodos consultados. |
|---|---|
| **Data Início** | Data de início da resposta para recuperação. Este parâmetro é utilizado em conjunto com o tipo de filtro e recupera os registros cuja data de referência seja maior ou igual ao valor informado. |
| **Data Fim** | Data limite fim da resposta para recuperação. Este parâmetro é utilizado em conjunto com o tipo de filtro e recupera os registros cuja data de referência seja menor ou igual ao valor informado. |
| **Processo** | Filtra registros pelo Processo associado com a classificação da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Subprocesso** | Filtra registros de acordo com o Subprocesso associado com a classificação da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Serviço** | Filtra registros pelo valor informado no campo Serviço da ocorrência. Se não for informado então este critério é desconsiderado na recuperação. |
| **Área Cliente** | Filtra os registros de acordo com o Área Cliente cujo valor é informado no campo Cliente da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Inclui sub-áreas** | Este parâmetro é utilizado em conjunto com o de Área. Se este parâmetro estiver marcado incluirá o Sub-orgão do Orgão selecionado no campo anterior. |
| **Solucionador** | Este parâmetro filtra os registros de acordo com Solucionador Responsável pela Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Tipo Item ** | Recupera Ordens de Serviço que tenha um item associado do mesmo tipo informado neste campo. Se não for informado então este critério é desconsiderado. |
| **Pesquisa de Satisfação** | Filtra os registros de acordo com o Tipo de Pesquisa de Satisfação. Se não for informado então este critério é desconsiderado na recuperação. |
| **Listagem de Ordens de Serviço** | Recupera apenas registros que contenham determinado nível de avaliação. Como padrão, exibe apenas as que possuem avaliações negativas. |

Além do filtro de recuperação informado pelo usuário existe também outro implícito por macroprocessos, que é aplicado em consultas por usuários que não possuem o perfil Administrador. Na figura abaixo podemos observar a mensagem exibida no rodapé da tela de relatórios quando o usuário não possui o perfil Administrador:

Alerta sobre filtro por macroprocessos

## Saídas

Após informar os parâmetros de recuperação clique no botão Consultar para visualizar o conteúdo do relatório.

O primeiro relatório exibe uma tabela juntamente com o seu gráfico contendo o percentual das avaliações feitas por clientes por cada pesquisa de satisfação.

Veja abaixo um exemplo de saída do primeiro relatório apresentado:

Avaliações por pesquisas de satisfação

O segundo relatório apresenta um maior detalhamento devido à exibição das questões associadas aos escores das avaliações feitas pelo cliente.

Veja abaixo um exemplo de saída do segundo relatório apresentado:

Avaliações por pesquisas de satisfação

O terceiro relatório apresenta o percentual de avaliações negativas agrupados por Áreas, Serviços e Subprocessos.

Veja abaixo um exemplo das saídas do terceiro relatório apresentado:

Principais Áreas com avaliações negativas

Principais Serviços com avaliações negativas

Principais Subprocessos com avaliações

O quarto relatório apresenta uma listagem quantitativa de Ordens de Serviço com avaliações, para qualquer pesquisa de satisfação. Caso deseje obter mais informações sobre Ordens de Serviço, que possuem avaliações em pesquisas de satisfação dê um duplo clique no campo Ordem de Serviço e logo em seguida será aberto um detalhamento da ocorrência em questão.

Dependendo do parâmetro selecionado anteriormente, este relatório poderá exibir dados de Ordens de Serviço com avaliações positivas, negativas ou ambos.

Veja abaixo um exemplo das saídas do quarto relatório apresentado:

Listagem de Ordens de Serviço com avaliações

# Enviar uma Ordem de Serviço para outro solucionador

Caminho: Guia para Solucionadores > Workspace  > Workspace Ordens de Serviço > Enviar uma Ordem de Serviço para outro solucionador

O envio de uma Ordem de Serviço para outro solucionador é feito pelo comando "Encaminhar" localizado na barra de ferramentas superior da tela de Ordem de Serviço. Veja a figura abaixo:

Botão para Encaminhar a Ordem de Serviço para outro solucionador

Quando clicamos neste botão é apresentado um novo diálogo contendo os solucionadores que podem receber a Ordem de Serviço.

Diálogo de encaminhamento

Observando a tela acima podemos observar que existe um controle no canto superior direito onde podemos selecionar um dos os papéis utilizados no fluxo da Ordem de Serviço. Ao selecionar um dos itens disponíveis a listagem de solucionadores é atualizada contendo apenas aqueles que atendam o papel do processo. Caso exista inconformidade de papel, o evento ficará em destaque no [Histórico de Responsáveis](consluta_pes_os).

Para finalizar o encaminhamento selecione um solucionador e clique no botão Encaminhar. Feito isto o diálogo é finalizado e a tela de Ordem de Serviço atualizada onde consta o novo responsável. Para visualizar o Histórico de Responsáveis verifique no tópico [Consulta de pessoas envolvidas na Ordem de Serviço](consluta_pes_os). Dependendo de regras de autorização e edição configuradas no processo alguns controles da tela podem se tornar desabilitados indicando que o usuário corrente não pode mais editar a Ordem de Serviço:

Controles desabilitados após encaminhamento

Em outras situações pode ser apresentada uma mensagem indicando que o usuário conectado não pode mais visualizar os dados da Ordem de Serviço. Veja este exemplo na figura abaixo:

Mensagem de acesso restrito

Após realizar o encaminhamento o usuário conectado ainda terá a oportunidade de retomar a responsabilidade da Ordem de Serviço **enquanto a mesma não for lida pelo novo solucionador**. Esta possibilidade só não será válida em situações onde o usuário conectado não possui mais autorização de visualização conforme a última figura.

Para recuperar a Ordem de Serviço o solucionador deve clicar no botão "**Retomar responsabilidade**" que passa a ser exibido no assistente de processos.

Botão para retomar responsabilidade

### Seleção do novo Solucionador

No encaminhamento, é possível filtrar o solucionador que deseja encaminhar por papéis, por todos papéis do subprocesso ou também por todos os solucionadores do macroprocesso:

Seleção de novo solucionador

No filtro por "<Todos os Solucionadores do subprocesso>" o sistema exibe todos solucionadores utilizados no subprocesso que também são exibidos no combobox de filtro.

O filtro por Todos os Solucionadores do Macroprocesso funciona da seguinte forma: serão exibidas todas as pessoas que estão relacionadas em algum grupo de trabalho como solucionadores e estejam lotadas em um das áreas ou sub-áreas relacionados no macroprocesso onde está contida a OS. Para visualizar onde estão estas áreas do subprocesso utilize no editor de processos (no process explorer):

Verificar macroprocesso

Obs: Repare que foi selecionado o macroprocesso Tecnologia da Informação portanto essas configurações só se aplicam aos subprocessos pertencentes ao macroprocesso em questão.

No novo diálogo exibido verifique a aba de Grupos Envolvidos:

Grupos Envolvidos com o macroprocesso

Portanto para adicionar, modificar ou remover grupos envolvidos, basta adicionar nesta aba confirmar e fechar.

Com esta visualização concluímos que todos os Grupos de Trabalho e subgrupos de "Gerencia de TI" apareceriam, por exemplo, em um encaminhamento de incidente filtrado por "<Todos os Solucionadores do Macroprocesso>".

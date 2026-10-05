# Relatórios Consultando Diversas Tabelas

Caminho: Guia para Administradores > Editor de Relatórios > Criando Relatórios > Relatórios Consultando Diversas Tabelas

Este tópico tem como pré-requisito a execução do tópico [Criando um Relatório Simples](criando_um_relatorio_simples).

1. Após executar o tópico indicado acima, na listagem de Relatórios da transação Editor de Relatórios, selecione o relatório criado e clique no comando **Novo > Copiar registro selecionado**.

2. Preencha o campo Descrição conforme figura abaixo:

3. Selecione a aba "Layout". Após isso, clique no comando **Configurar dados | Principal**.

No quadro direito onde estão listadas as tabelas do Supravizio disponíveis, selecione a tabela [CLASSE_SUB_PROCESSO](dados_classe_sub_processo) e dê um duplo clique nela.

Utilize duplo clique também na tabela [OCORRENCIA](dados_ocorrencia), então no Query Builder, em OCORRENCIA procure pela propriedade ID_CLASSE_SUB_PROC, clique e arraste até a propriedade ID_CLASSE_SUB_PROCESSO de CLASSE_SUB_PROCESSO para criar uma associação entre as tabelas:

Após criar a associação, clique na coluna DESCRICAO da tabela CLASSE_SUB_PROCESSO. Pode ser interessante também atribuir ao campo DESCRICAO um "Apelido" (Alias) para a coluna caso existam tabelas com o mesmo nome de coluna sendo utilizadas na consulta. Vamos adicionar um Apelido à coluna DESCRICAO. Para isso, no próprio Query Builder, faça a alteração conforme figura:

Veja que o próprio Query Builder construiu a instrução SQL desejada:

Após associarmos as tabelas e incluirmos o campo de Descrição do Tipo de Subprocesso da Ordem de Serviço, vamos incluí-lo no relatório. Primeiramente, vamos diminuir o campo ASSUNTO criado através do relatório de origem ([Relatório de Ordens de Serviço Simplificado](criando_um_relatorio_simples)) para adicionarmos em seguida o novo campo. Na banda Detail, reduza o tamanho do campo ASSUNTO.

Após isso, na Lista de Campos, selecione o novo campo DESC_SUBPROCESSO e arraste-o e solte-o na região livre da banda Detail.

É necessário agora formatar o novo campo e redimensionar novamente a banda Detail.

Salve o novo relatório. Em seguida, clique no comando "Visualizar":

Para publicar este relatório no menu principal, leia o tópico [Relatórios no Menu Principal](relatorios_no_menu_principal).

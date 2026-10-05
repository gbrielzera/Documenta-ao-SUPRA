# Associando OrdemServico e Ocorrencia

Caminho: Guia para Administradores > Editor de Relatórios > Criando Relatórios > Associando OrdemServico e Ocorrencia

Este tópico ensinará como realizar associações entre a entidade OrdemServico e Ocorrencia.

Baseado em conceitos de Programação Orientada a Objetos (POO), a classe [OrdemServico](objetos_ordemservico) herda diretamente propriedades e funcionalidades da classe [Ocorrencia](objetos_ocorrencia). Isso indica que alguns dos campos de uma Ordem de Serviço não pertençam diretamente à classe OrdemServico. Como vimos no exemplo precedente a este tópico (Criando um Relatório Simples), para listarmos uma relação de Ordens de Serviço levando em consideração o Assunto e o Numero, utilizamos a tabela [OCORRENCIA](dados_ocorrencia). Porém, alguns dos campos utilizados na elaboração de relatórios levando em consideração Ordens de Serviço deverão contar também com a tabela [ORDEM_SERVICO](dados_ordem_servico). Um exemplo clássico de uso da tabela ORDEM_SERVICO é a utilização do campo ID_SERVICO. O Serviço é uma propriedade pertencente à classe OrdemServico e não à classe Ocorrencia. Neste caso, será necessário realizarmos uma consulta com as duas tabelas associadas.

Este tópico tem como pré-requisito a execução do tópico [Criando um Relatório Simples](criando_um_relatorio_simples).

1. Após executar o tópico indicado acima, na listagem de Relatórios da transação Editor de Relatórios, selecione o relatório criado e clique no comando **Novo > Copiar registro selecionado**.

2. Preencha o campo Descrição conforme figura abaixo:

3. Selecione a aba "Layout". Após isso, clique no comando **Configurar dados | Principal**.

No quadro direito onde estão listadas as tabelas do Supravizio disponíveis, selecione a tabela [ORDEM_SERVICO](dados_ordem_servico) e dê um duplo clique nela. Após isso, repita a mesma ação para a tabela [SERVICO](dados_servico).

Repare que, ao dar um duplo clique na nova tabela do relatório, automaticamente o Query Builder cria as associações entre as tabelas (Foreign Keys). Podemos relacionar as tabelas OCORRENCIA e ORDEM_SERVICO através dos campos ID_OCORRENCIA de ambas. Relacionamos as tabela ORDEM_SERVICO com a tabela SERVICO através dos campos ID_SERVICO de ambas.

Após remover o elemento, clique na coluna DESCRICAO da tabela SERVICO. Pode ser interessante também atribuir ao campo DESCRICAO um "Apelido" (Alias) para a coluna caso existam tabelas com o mesmo nome de coluna sendo utilizadas na consulta. Vamos adicionar um Apelido à coluna DESCRICAO. Para isso, no próprio Query Builder, faça a alteração conforme figura:

Veja que o próprio Query Builder construiu a instrução SQL desejada:

Após associarmos as tabelas e incluirmos o campo de Descrição do Serviço da Ordem de Serviço, vamos incluí-lo no relatório. Primeiramente, vamos diminuir o campo ASSUNTO criado através do relatório de origem ([Relatório de Ordens de Serviço Simplificado](criando_um_relatorio_simples)) para adicionarmos em seguida o novo campo. Na banda Detail, reduza o tamanho do campo ASSUNTO.

Após isso, na Lista de Campos, selecione o novo campo DESC_SERVICO e arraste-o e solte-o na região livre da banda Detail.

É necessário agora formatar o novo campo e redimensionar novamente a banda Detail.

Salve o novo relatório. Em seguida, clique no comando "Visualizar":

Para publicar este relatório no menu principal, leia o tópico [Relatórios no Menu Principal](relatorios_no_menu_principal).

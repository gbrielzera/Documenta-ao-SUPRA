# Desativando Cadastros de Pessoas

Caminho: Guia para Administradores > Roteiro de implantação > Realizando cadastros > Cadastro de Pessoas > Desativando Cadastros de Pessoas

Em determinados casos, pode ser necessário desativar Cadastros de Pessoas. No entanto, pode haver casos em que existam registros associados a este cadastro, impossibilitando realizar tal exclusão.

Nestas situações, o procedimento mais adequado seria apenas inativá-lo, conforme a propriedade indicada abaixo:

Propriedade no Cadastro de Pessoas

Caso o usuário possua Solucionador cadastrado, será necessário verificar se o mesmo não está associado a cadastros. A seguir, realizaremos a desativação do usuário 'Carlos Morais', que possui Solucionador e registros associados ao mesmo.

Para localizar os cadastros relacionados, entramos no relatório [Responsabilidades de Solucionadores e Clientes](responsabilidades_solucionadores_clientes).

Caminho do relatório

Selecionamos o usuário 'Carlos Morais' e clicamos em **Consultar**.

Relatório de responsabilidades

Através do relatório, podemos observar que o solucionador ainda possui responsabilidades em cadastros e subprocessos.

Portanto, devemos atualizar tais cadastros para que não sejam possa não sejam atribuídas novas responsabilidades para o usuário. Na tela abaixo, entramos no cadastro do [Grupo de Trabalho](definindo_grupos_de_trabalho) para atualizar seu Coordenador e retirá-lo da lista de Solucionadores:

Cadastro do Grupo de Trabalho

Realizamos as atualizações das responsabilidades para todos os itens do relatório e retornamos ao [Cadastro de Pessoas](cadastro_de_pessoas).

Listagem de Pessoas

Entrando no cadastro, agora basta clicar no botão **Remover Solucionador.**

Botão Remover Solucionador

Logo, será exibida um diálogo de confirmação:

Diálogo de confirmação

Clicando em Sim, o **Solucionador** cadastrado será removido. Feito isso, basta desabilitar a propriedade **Ativo** do cadastro e em seguida **Salvar**, assim o usuário ficará com status Inativo e todas as responsabilidades serão direcionadas para os solucionadores corretos.

Propriedade no cadastro

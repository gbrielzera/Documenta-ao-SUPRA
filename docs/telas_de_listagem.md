# Telas de Listagem

Caminho: Guia para Administradores > Roteiro de implantação > Realizando cadastros > Telas de Listagem

As telas de listagem dos cadastros do Supravizio contam com os seguintes recursos:

**Barra de Ferramentas**

**Barra de Ferramentas**

A barra de ferramentas das telas de listagem possuem um conjunto completo de comandos para inclusão, modificação, visualização, localização e navegação de registros. São estes:

**Novo**

Através deste comando o usuário cria um novo registro:

Além disso, a fim de facilitar a criação de registros, também há o comando **Clonar**, o qual permite criar um novo registro igual ao selecionado na listagem.

**Copiando de registro selecionado**

Sua finalidade é criar um novo registro preenchendo os campos com os valores dos campos do registro selecionado:

**Novo registro copiado**

**Modificar**

Permite a modificação do registro selecionado.

**Visualizar**

Exibe detalhes do registro selecionado.

Apagar

Apaga o registro selecionado.

**Filtro**

Neste campo devemos digitar o filtro para recuperação e clicar no botão de aplicação localizado a direita. O primeiro botão recupera os registros que atendam ao filtro informado no campo a esquerda. O segundo botão recupera todos os registros independente do filtro informado:

Critério de filtro

Para realizar uma busca mais avançada é possível usar os operadores & e | que funcionam respectivamente como operadores "and" e "or".

Nas imagens abaixo, realizamos uma busca usando o operador & e na busca foi verificado se as duas descrições digitadas eram verdadeiras e foi retornado o resultado:

Recuperação pelo operador &

No exemplo abaixo a recuperação foi realizada utilizando o operador | e foi verificado se pelo menos uma das descrições digitadas para a busca era verdadeira, sendo recupera os registros que correspondem a esta condição:

Recuperação pelo operador |

O texto que é digitado no campo de recuperação segue os seguintes critérios antes de retornar o registro:

- O texto digitado é comparado com todos os campos do tipo texto do cadastro, inclusive os [campos customizados](campos_customizados);
- O texto também é comparado com identificadores, os IDs. Se for digitado no campo de recuperação o ID de um registro existente no cadastro, o filtro recupera o registro correspondente ao ID;
- Os cadastros associados também podem ser recuperados. Para isso basta digitar o descritivo da associação do cadastro.

No exemplo abaixo usamos descritivo de áreas para recuperação dos registros associados:

Recuperação de registros por associação

**Selecionar Colunas**

Habilita uma janela para seleção se colunas a serem exibidas no grid.

Janela de seleção de campos

Para adicionar uma coluna, basta arrastar a coluna para a barra de títulos. Para remover uma coluna, basta mover a coluna de volta a listagem novamente.

**Restaurar colunas**

Clicando neste botão, o grid da listagem será revertido para o formato padrão da tela.

**Atualizar**

Recupera registros e atualiza a listagem.

Exportar

Permite realizar a exportação dos resultados para uma planilha em diversos formatos.

Ajuda

Permite obter informações de ajuda sobre o cadastro da transação exibida.

Ajuda da transação

**Botões de Navegação**

As telas de listagem do Supravizio possuem um conjunto de comandos para navegação nos registros de uma listagem.

Botões de navegação

Clicando nos números de páginas ou nas setas, é possível navegar entre as páginas de resultados.

É possível configurar um limite de registros para exibição na tela de Configurações. Para isso acesse **Utilitários | Configurações, **selecione na árvore Utilitários | Geral, e em **Quantidade máxima de registros para a recuperação em cadastros** preencha com o número máximo de registros que deseja filtrar e clique em Salvar:

Configuração da quantidade de registros

Os botões de navegação somente estarão habilitados na barra de ferramentas quando a quantidade de registros que estiver cadastrado for superior ao limite cadastrado na tela acima.

informando que não foi possível remover o registro, seguida do motivo e registro associado.

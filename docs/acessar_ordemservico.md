# Como filtrar Ordens de Serviço

Caminho: Guia para Solucionadores > Workspace  > Workspace Ordens de Serviço > Como filtrar Ordens de Serviço

A formação do filtro de Ordens de Serviço do Workspace é realizada pelo preenchimento dos seguintes controles destacados na figura abaixo:

Filtros do Workspace Ordens de Serviço

Veja na tabela abaixo o detalhamento de cada opção no modo filtro da tela acima.

| **Modo Filtro** | **Descrição** |
|---|---|
| Responsável atual | Recupera todas as Ordens de Serviço no qual o responsável corrente é aquele selecionado na árvore de Grupos de Trabalho e solucionadores. |
| Aprovador com pendências | Recupera todas as Ordens de Serviço onde o solucionador selecionado na árvore é um aprovador com pendência de aprovação. |
| Responsável inicial | Recupera todas as Ordens de Serviço onde o primeiro responsável foi aquele selecionado na árvore de Grupos de Trabalho e solucionadores |
| Pessoa envolvida | Recupera todas as Ordens de Serviço onde o solucionador selecionado na árvore de Grupos de Trabalho e solucionadores foi, em qualquer momento, o responsável. |
| Todos | Recupera Ordens de Serviço desconsiderando filtro por responsável |

Ainda na tela acima a opção **Ocultar pendentes Aprovação** permite ocultar Ordens de Serviço que estejam pendentes de aprovação.

Além do filtro por responsabilidade é possível definir critérios de recuperação por Cliente, Processo, Serviços, Situação e diversos outros campos da Ordem de Serviço. Veja na figura abaixo como utilizar o filtro:

Adicionando filtro em um campo

Para saber mais sobre como adicionar campos no grid, remover campos ou criar agrupamentos acesse o tópico de [Configurações do Grid de Ordens de Serviço](configuracao_do_grid_de_ordens).

Após utilização do filtro desejado pode ser necessário a remoção de filtros, para remover filtros clique novamente no filtro desejado e depois na opção indicada na figura abaixo (Repare que os campos que possuem filtro exibem o ícone de filtro diferente dos demais):

Removendo filtros

No filtro por Situação definimos os estado atual da Ordem de Serviço. Se a situação da Ordem de Serviço no qual deseja buscar for diferente de Aberta é necessário a definição de uma faixa de data: início e fim.

Filtros por situação

Para localizar o texto desejado é possível utilizar a ferramenta de localização. Repare que além do filtro a palavra de busca "SQL" fica em destaque:

Localizar texto

Além do filtro definidos nesta tela são aplicadas regras de autorização conforme descrito no tópico [Autorização e Processos](autorizacao_e_processos).

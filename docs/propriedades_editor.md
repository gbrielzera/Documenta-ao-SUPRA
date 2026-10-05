# Propriedades

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Propriedades

A janela de **Propriedades** é o recurso disponível no **Editor de Processos** para configurar os diversos elementos do BPMN adicionados ao fluxo de processos em edição.

Veja na figura abaixo que ao selecionar uma tarefa qualquer, são exibidas as configurações correspondentes na janela de **Propriedades**.

Tela de Propriedades da tarefa

Determinadas propriedades abrem novas janelas para edição de conteúdos, como por exemplo a tarefa de documentação de processo. Veja o exemplo abaixo:

Propriedades com opção de edição de conteúdo

Existem também Propriedades do tipo Booleano com as opções True (verdadeiro) ou False (falso). No exemplo abaixo as Propriedades do campo Exige apontamento são do tipo Booleano:

Propriedade do tipo Booleana

Quando selecionamos mais de um elemento no diagrama a janela de **Propriedades** passa a exibir os atributos que são comuns. Veja na figura abaixo que selecionando a tarefa **Solicitar aprovação da TI** e selecionamos também o **iniciador** do fluxo são exibidos os campos em comum:

Edição de vários elementos com propriedades comuns

É importante observar que quando modificamos uma **Propriedade** de várias tarefas selecionadas, a mudança é aplicada em bloco, ou seja em todas as tarefas selecionadas. Desta forma poderíamos, por exemplo, atualizar de uma única vez a propriedade **Papel Responsável** de várias tarefas selecionadas.

Determinadas **Propriedades** são constituídas de coleções de itens e são editadas por um diálogo aberto e para editarmos estes itens basta clicar no botão e abriremos o diálogo de edição . Veja a figura abaixo que ilustra a configuração de campos para uma regra de **Entrada de Dados**:

Edição de coleções

No exemplo acima ao acionarmos o botão , aparecerá um diálogo com a relação de todos os campos que devem ser preenchidos:

Diálogo de edição de campos

Eventualmente, itens contidos no diálogo de **Propriedades** podem ser do tipo coleção e neste caso a edição é feita por outro diálogo, ou seja, o comportamento de exibição é recursivo:

Diálogo de edição do tipo coleção

Outra característica interessante deste recurso é a capacidade de edição de sub-propriedades. Veja na figura abaixo que é possível editar a configuração de preenchimento de um campo utilizando a janela de propriedades principal, sem a necessidade de clicar no botão dos campos.

Edição de objetos aninhados

**Importante: a remoção e inclusão de novos itens necessariamente deve ser feita pelos diálogos de edição de coleções conforme apresentado anteriormente.**

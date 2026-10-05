# Atualização de aprovações

Caminho: Guia para Solucionadores > Workspace  > Workspace Ordens de Serviço > Visualizar e editar uma Ordem de Serviço > Atualização de aprovações

A Atualização de aprovadores é uma funcionalidade do Supravizio que possibilita atualizar a lista de aprovadores Ordens de Serviço pendentes de aprovação em casos que o aprovador tenha sido trocado e não seja mais membro integrante do Papel associado à aprovação.

Esta atualização pode ser realizada de 2 formas:

| 1. | Manual para uma Ordem de Serviço utilizando o botão Atualizar lista de aprovadores da tela de Ordem de Serviço. Esta situação será descrita adiante neste tópico. |
|---|---|

Atualização de uma única Ordem de Serviço

| 2. | Utilizando a listagem de Ordens de Serviço do Workspace, pode ser realizada a de uma única Ordem de Serviço ou várias ao mesmo tempo. Veja a figura abaixo: |
|---|---|

Atualização aprovadores em Ordens de Serviço

| 3. | Automática a cada intervalo de uma hora por meio do job **Máquina de Processos** disponível na tela de **Gerenciamento de Ambiente** (na versão **Windows**, menu **Utilitários \| Gerenciamento de Ambiente**): |
|---|---|

Atualização automática

## Atualização manual em uma Ordem de Serviço

No exemplo abaixo, iremos alterar o Aprovador da Ordem de Serviço, realizando uma mudança em seu respectivo papel (neste caso, Gerente de TI):

Nome do aprovador

Através do menu principal do Supravizio Windows, no Editor De Processos | Papéis selecionamos o papel Gerente de TI que tem como solucionador João Silva, que é atualmente aprovador da Ordem de Serviço pendente de aprovação. Trocamos o solucionador para Joana Castro:

Troca de papéis

Retornando na tela de Edição Ordem de Serviço que estava com pendência de aprovação. Na aba Dados Principais será exibida uma mensagem que informa que o solucionador foi trocado e que para efetivar esta mudança é necessário clicar no botão Atualizar lista de aprovadores na aba de Aprovações:

Aviso de troca de papéis

Na aba Aprovações da Ordem de Serviço com pendência de aprovações, basta atualizar as modificações clicando no botão Atualizar lista de aprovadores:

Atualização de modificações

### Atenção: Observe que ao ativar a lista a primeira versão foi cancelada e foi gerada uma nova versão com o nome dos atuais aprovadores.

### Se existir mais de um aprovador será necessário que ocorra a atualização do aprovador que foi trocado para que seja finalizada a aprovação:

### Situação com mais de um aprovador

### Também é possível registrar um substituto para o aprovador. Obtenha ajuda para registrar um substituto clicando no link [Workspace Opções.](workspace_opcoes)

Ao registrar um substituto retorne na tela Edição de Ordens de Serviço e observe que é possível ver o novo aprovador na aba Dados Principais:

Aprovador Ativo

# Critérios para Abertura de Ordens de Serviço

Caminho: Guia para Solucionadores > Workspace  > Workspace Ordens de Serviço > Critérios para Abertura de Ordens de Serviço

### Critérios para Abertura de Ordens de Serviço pelo Workspace

Ao clicar no botão "Nova" do Workspace, são verificados alguns critérios para que possa ser exibido o Subprocesso ao usuário conectado, como o Grupo de Trabalho do usuário, se o processo está ativo, se há versão ativa do processo e se há um iniciador manual disponível no Workspace:

Processos disponíveis para abertura de Nova Ordem de Serviço

| **1.** | **Usuário conectado pertence à um Grupo de Trabalho envolvido:** |
|---|---|

Para verificar os grupos de trabalho envolvidos no Macroprocesso, no Editor de Processos, Utilize o botão de Editar Macroprocesso do Process Explorer:

Editar Macroprocesso

E então selecione a aba de Grupos envolvidos:

Grupos envolvidos

É importante ressaltar que na inclusão de um Grupo de Trabalho (Como no Exemplo Gerência de TI), automaticamente adiciona as permissões também aos Grupos de Trabalho "filhos" do mesmo.

| **2.** | **Processo Ativo:** |
|---|---|

Todos processos ativos ficam claramente visíveis no Process Explorer:

**Process Explorer**

Caso um processo não esteja ativo, ele não irá aparecer claramente, ficará disponível apenas no Histórico de Versões juntamente com as versões anteriores dos processos ativos (Veja o exemplo no caso de desativar o processo de Atendimento):

Processo de Atendimento Inativo

Clique com o botão direito no processo, selecione a opção "Modificar Processo" e modifique a propriedade "Ativo".

Modificar Processo

| **3.** | **Versão de Processo Ativa:** |
|---|---|

No editor de processos, verifique se o subprocesso em questão existe apenas na versão Em edição do processo:

Processo com versão em edição

Caso seja necessário, ative a versão em edição para que o subprocesso fique disponível para abertura no Workspace:

Ativar versão do processo

| **4.** | **Iniciador manual disponível no Workspace:** |
|---|---|

Na versão **ativa **do processo, deve existir ao menos um iniciador manual com disponibilidade no Workspace:

Iniciador manual disponível no Workspace

É importante ressaltar que nas propriedades do iniciador a propriedade Ativo deve estar marcada como "True" em ao menos um dos iniciadores manuais e também que deve ser verificado se a propriedade "Permissão restrita Papel Responsável" estiver marcada como "True" o solucionador deve pertencer ao papel definido como Responsável:

Propriedades do iniciador manual

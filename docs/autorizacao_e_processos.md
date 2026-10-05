# Autorização e Processos

Caminho: Guia para Administradores > Configurando Processos > Autorização e Processos

O mecanismo de autorização permite configurar regras de visibilidade para Ordens de Serviço x Processos. Este mecanismo possui uma configuração global de autorização definida na tela de Configurações (opções de menu** Utilitários | Configurações**) e permite redefinir esta configuração para cada [Tipo de Subprocesso](classesubprocesso_sub) (opções de menu **Processo | Processos | Tipos de Subprocessos**).

**Importante: **a segunda forma de configuração, por Tipo de Subprocesso, possui maior prioridade sobre o valor encontrado na tela Configurações.

## Regras de Autorização

A seguir veremos quais são estas opções de configuração, para saber sobre outras autorizações no processo consulte [Restringindo Ações para Grupos de Trabalho](workspace_restricao_grupos).

Público

A Ordem de Serviço pode ser **lida** e **editada** pelo responsável corrente ou um dos seus coordenadores. Também pode ser acessada para **leitura** por qualquer outro solucionador.

### Visível somente para o responsável atual ou anterior

A Ordem de Serviço pode ser **lida** e **editada** pelo responsável corrente ou um dos seus coordenadores. Também pode ser acessada para **leitura** por um solucionador anterior (independente do seu grupo de trabalho). Visualize as [Histórico de Responsáveis na Ordem de Serviço](autorizacao_e_processos) para saber sobre o responsável corrente, grupo de trabalho (para saber o coordenador) e também os responsáveis anteriores.

### Visível para solucionadores do grupo do responsável

A Ordem de Serviço pode ser **lida** e **editada** pelo responsável corrente ou um dos seus coordenadores. Também pode ser acessada para **leitura** por outros solucionador do mesmo grupo.

### Visível para solucionadores do grupo do responsável ou para o responsável anterior

A Ordem de Serviço pode ser **lida** e **editada** pelo responsável corrente ou um dos seus coordenadores. Também pode ser acessada para **leitura** por outros solucionador do mesmo grupo ou por um solucionador anterior independente do seu grupo de trabalho. Visualize as [Histórico de Responsáveis na Ordem de Serviço](autorizacao_e_processos) para saber sobre o responsável corrente, grupo de trabalho (para saber o coordenador) e também os responsáveis anteriores.

### Visível para solucionadores envolvidos no Macroprocesso

A Ordem de Serviço pode ser **lida** e **editada** pelo responsável corrente ou um dos seus coordenadores. Também pode ser acessada para **leitura** por outros solucionadores que atuam no mesmo macroprocesso da Ordem de Serviço. Para determinar os solucionadores do mesmo macroprocesso o sistema recuperará todas as pessoas lotadas em alguma das áreas proprietárias de subprocessos contidos no mesmo macroprocesso.

### Visível somente para o responsável

Somente o responsável corrente ou um dos seus coordenadores pode acessar e editar a Ordem de Serviço.

## Acesso total para Administradores

Para usuários que possuem o perfil de acesso Admin (veja o cadastro de [Usuários](user_sub)) é possível autorizar no cadastro de Tipos de Subprocessos o acesso total incluindo possibilidade de edição de Ordens de Serviço.

No exemplo abaixo Ordens de Serviço do subprocesso podem ser lidas e editadas por usuários que contenham o perfil Admin:

O usuário com perfil Admin pode ler e editar Ordens de Serviço

Na situação abaixo não existe acesso especial para usuários administradores valendo então a regra de autorização global ou por tipo de Subprocessos apresentada no início deste tópico.

Não existe exceção para o usuário com perfil Admin

## Substitutos

Outra exceção para as regras de autorização está na configuração de substituto, que neste caso também possui acesso a **leitura** e **edição** em todas as Ordens de Serviço sob responsabilidade do solucionador substituído (este deve registrar a substituição na tela [Opções do Workspace](workspace_opcoes)).

## Histórico de Responsáveis na Ordem de Serviço

Para visualizar as pessoas envolvidas na Ordem de Serviço, na tela da Ordem de Serviço utilize a aba "Informações sobre Processo" e nela "Pessoas Envolvidas:

Visualizar pessoas envolvidas

Repare que quando não há conformidade de papel, o responsável aparece em cor diferenciada. Repare também que há uma associação abaixo entre os papéis envolvidos no subprocesso e os participantes (É feita verificação entre os papéis envolvidos nas tarefas realizadas e todos integrantes dos papéis).

# Visualizar e editar uma Ordem de Serviço

Caminho: Guia para Solucionadores > Workspace  > Workspace Ordens de Serviço > Visualizar e editar uma Ordem de Serviço

Neste tópico ensinaremos como visualizar e editar uma Ordens de Serviço através da tela **Edição de Ordens de Serviço. **É importante que a Ordem de Serviços já esteja criada de acordo com o passo a passo do tópico [Criando uma Ordem de Serviço.](criando_uma_nova_ordem_de_serv)

Para exibir a Edição da Ordem de Serviço, clique com o botão direito em cima da Ordem de Serviço e selecione a opção 'Visualizar' ou realize um duplo clique na Ordem de Serviço apresentada na tabela.

Visualizando Tela de Edição de Ordens de Serviço

Na tela Edição de Ordens de Serviço é possível que o responsável possa editar suas Ordens de Serviço ou no caso de coordenadores de Grupos de Trabalho possam editar as Ordens de Serviço de seus coordenados.

## Dados Principais

A aba **Dados principais** contém os principais campos da Ordem de Serviço e o Assistente de Processos, que auxiliará o usuário na execução passo-a-passo de todas as atividades do processo da Ordem de Serviço.

Nesta tela podemos observar os campos que são preenchidos na [Criação da Ordem de Serviço:](acessar_ordemservico)

Dados Principais

Em **Itens de Configuração associados **será apresentado todos os itens de configuração associados na Ordem de Serviço através da aba **Itens de Configuração**:

Itens de Configuração

Em Comentários e mensagens é possível visualizar um comentário ou adicionar um novo comentário na Ordem de Serviço:

Comentários

É possível também incluir e visualizar comentários através do Portal na tela de consulta da Ordem de Serviço:

Consulta de Ordem de Serviço

Ao clicar em adicionar comentário é exibido o seguinte diálogo:

Adicionar Comentário

Repare que pode ser adicionado comentário por todos que podem visualizar a Ordem de Serviço, porém caso seja adicionado por alguém que não seja o responsável atual, automaticamente a Ordem de Serviço é atualizada para o estado de "Não Lida":

,

Ordem de Serviço não lida

À esquerda da tela "**Dados principais**" podemos visualizar o número e o status da Ordem de Serviço e podemos verificar também o andamento do [Acordo de Nível de Serviço](acordointerrupcaosla_sub):

Status da Ordem de Serviço e ANS interrompido

Para iniciar o atendimento de uma Ordem de Serviço clique no botão Iniciar localizado no Assistente de Processos da tela:

Iniciando o atendimento da Ordem de Serviço

Abaixo dos botões de navegação de Processos (Iniciar, Avançar e Voltar e Finalizar) são exibidas as atividades do Processo em **Dados requeridos para Iniciar**. Cada atividade é exibida em um agrupamento e no seu conteúdo pode variar em função das ações configuradas para o Processo no [Editor de Processos](editor_de_processo).

Para iniciar um atendimento é importante verificar quais são os dados requeridos para prosseguir, caso contrário será exibido uma tela de críticas com uma mensagem de pendência.

Se faltar alguma atividade a ser realizada antes de prosseguir com o andamento da Ordem de Serviço será destacado de vermelho um link em **Dados requeridos para Iniciar **e ao clicar neste link será exibido uma opção oferecendo a possibilidade de cumprir com esta atividade.

Na figura abaixo podemos observar uma atividade que demanda uma a Associação de Ativos para continuidade do atendimento. Ao clicar no link em vermelho o usuário é remetido a aba Itens de configuração:

Associação de ativos

Após executar todos os dados requeridos podemos iniciar a Ordem de Serviço clicando no botão Iniciar.

Após concluir a atividade o usuário deve clicar no botão Avançar. Ao clicar neste botão pode ocorrer o encaminhamento automático da Ordem de Serviço.

No exemplo abaixo foi estabelecido em atividades do Subprocesso que a Ordem de Serviço seja encaminhada para uma aprovação de um responsável com o Papel de Gerente de TI:

Avançando para Aprovação de acordo com fluxo do Processo

Para localização do atendimento no processo, clique na aba Informações sobre o Processo.

Observe na figura que será exibido detalhes do fluxo do subprocesso e aparecerá em destaque azul o andamento do processo.

Ao avançar a Ordem de Serviço será exibido em azul o andamento do Processo de acordo com a imagem abaixo:

Informações sobre o Processo

## Reabrindo Ordens de serviço:

É possível reabrir uma Ordem de Serviço já finalizada ou cancelada por qualquer motivo. Para isso basta clicar no botão Reabrir:

**Aprovações:**

Na aba **Aprovações** podemos verificar as autorizações para execução de Serviços de TI configuradas em [Atividades de Processos](editor_de_processo). Durante a execução de uma Ordem de Serviço estas aprovações podem ser:

| 1. | Enviadas automaticamente para os respectivos aprovadores assim que a Ordem de Serviço inicia a execução da Atividade (botão "Avançar" por exemplo). |
|---|---|

| 2. | Configuradas e enviadas manualmente pelo usuário responsável pela Ordem de Serviço. |
|---|---|

Para cada solicitação existe um Assunto e diversas versões, sendo válida somente a última versão.

Na figura abaixo podemos observar o layout da tela de aprovação:

Os aprovadores são definidos no processo em função de Papéis enquanto os Itens de Configuração são configurados como [Classes de Configuração e/ou Super Classes de Configuração](classeconfiguracao_sub).

A solicitação de aprovação só pode ser enviada se todas as restrições de configuração forem atendidas. Exemplo: vamos assumir um processo de instalação de Artefato onde é necessária a aprovação do Gestor do favorecido (um papel configurado no sistema), então ao configurarmos uma nova versão para aprovação do assunto "Aprovação do Gestor do Favorecido" o sistema automaticamente preenche como aprovador o superior do solicitante da Ordem de Serviço. Se o usuário tentar modificar esta pessoa (clicar em remover e em seguida adicionar uma outra pessoa) então não será possível iniciar a aprovação.

Para iniciar a aprovação é necessário clicar no botão Iniciar.

Para verificar se a solicitação está correta quanto a configuração basta clicar no botão Validar.

### Como Cancelar uma Aprovação:

Se por algum motivo for necessário cancelar uma aprovação e enviar uma nova versão execute os seguintes passos:

1) Selecione a versão para cancelamento

2) Clique no botão Cancelar.

3) Para gerar uma nova versão clique no botão Nova Versão e em seguida selecione o Assunto para a solicitação. Os Assuntos são configurados no processo e já definem os aprovadores e os itens de configuração que farão parte da aprovação.

4) De acordo com a configuração do processo são exibidos botões com os Itens de Configuração para associação na solicitação de aprovação. Veja a figura abaixo:

Cancelamento de uma Aprovação

**Importante:** Dependendo de como foi configurado o processo a associação de Itens de Configuração pode ser automática. No exemplo acima o Artefato Gravação-Obras é vinculado automaticamente a versão de aprovação devido ao fato de já estar relacionado na Ordem de Serviço e esta associação automática também configurada no processo.

5) Após configurar a aprovação clique em Iniciar para enviar a solicitação para os aprovadores.

## Itens Configuração:

Nesta aba são associados os Itens de Configuração necessários para execução da Ordem de Serviço. A associação destes itens também é configurada no processo da Ordem de Serviço.

É possível associar os seguintes tipos de itens:

| **Campos ** | **Descrição** |
|---|---|
| Equipamento | Todo e qualquer equipamento disponível na infra-estrutura de informática. Exemplos: Computadores de mesa, Notebooks, Servidores, Projetores, Impressoras etc. |
| Artefatos/Arquivo | São documentos ou objetos de propósito geral e normalmente são dados gerados como saída de processos. Exemplos: especificações, atas de reunião, perfis de sistemas etc. |
| Software | Software, licenciado ou não, instalado em equipamentos. |
| Dispositivos | São documentos ou objetos de propósito geral e normalmente são dados gerados como saída de processos. |

Estes itens podem ser cadastrados no módulo de [Ativos](supravizio_configuracao) ou então gerados durante a execução de uma Ordem de Serviço. Também durante a execução de uma Ordem de Serviço é possível a modificação destes itens:

**Comunicados:**

Na aba **Comunicados **ficam registrados os comunicados que são encaminhados para os usuários, como por exemplo aprovações. É possível também encaminhar e administrar o envio de comunicados para usuários de acordo com a imagem abaixo:

Após realizar os preenchimentos acima clique no botão enviar na parte superior à direita.

**Informações sobre Processo:**

Ao clicar na aba **Informações sobre Processo** podemos visualizar várias informações adicionais sobre o processo da Ordem de Serviço. Estas informações são dividas em cinco novas abas:

## 1 - Fluxo:

Na aba **Fluxo **é possível visualizar o fluxo do processo da Ordem de Serviço. Ao usar os botões de navegação do Processo (Iniciar, Avançar, Voltar e Finalizar) na aba Dados principais, são exibidas na aba **Fluxo** as atividades que já foram ou estão sendo executadas com margens na cor azul:

## Pessoas envolvidas:

Na aba **Pessoas envolvidas **podemos visualizar o histórico de todas as pessoas que foram responsáveis pela Ordem de Serviço além da data e hora do encaminhamento. É possível também selecionar o papel para identificar o Ator deste papel e o motivo por este Ator ter sido o responsável pela Ordem de Serviço.

Na última coluna à direita obtemos informações da aderência do responsável ao processo da Ordem de Serviço:

## Eventos:

Em **Eventos **podemos visualizar com hora e data todos passos do andamento da Ordem de Serviço desde a abertura até sua finalização.

No exemplo abaixo podemos verificar eventos como comentários, aprovações, reprovações e encaminhamentos de uma Ordem de Serviço. Na última tabela à direita é possível identificar o responsável por cada evento:

## Atividades executadas:

Nesta aba são apresentadas todas as atividades já executadas do Processo. Na tabela abaixo podemos identificar a data e hora desta execução, responsável que iniciou e finalizou a atividade e conformidade do finalizador com o Papel do Processo:

## Atividades canceladas:

Nesta aba é possível verificar todas as atividades estabelecidas no Processo que foram canceladas com data e hora de início e fim, relatório e responsável que iniciou a atividade. Neste exemplo abaixo o responsável executou o cancelamento da atividade listada na tabela:

# Acordo de Nível Operacional

Caminho: Guia para Administradores > Roteiro de implantação > Realizando cadastros > Cadastros Adicionais > Acordos > Acordo de Nível Operacional

O Acordo de Nível Operacional é composto por um conjunto de regras configuradas no fluxo do subprocesso definindo tempo para finalização da tarefa. Estas regras podem ser definidas em função do ANS (indicação de um percentual do tempo total de atendimento), como tempo constante (em minutos) ou por horas apontadas.

A figura abaixo ilustra a configuração de ANO (Acordo de Nível de Operacional) para um fluxo de guarda de documentos:

Configuração de ANO em tempo constante

Na figura abaixo podemos verificar o comportamento da tela de Ordem de Serviço quando for executada a tarefa acima:

Tempo do Acordo de Nível Operacional

O Acordo de Nível Operacional pode ser utilizado como uma ferramenta para garantia de cumprimento do Acordo de Nível de Serviço. No exemplo abaixo definimos uma meta de ANO em função do tempo de atendimento do ANS:

Configuração de ANO em função do ANS

Quando executamos uma Ordem de Serviço do subprocesso acima podemos observar o seguinte resultado:

Tempo restante calculado em 15% do ANS

**Importante: No caso de acordos definidos em função de ANS, quando ocorre a interrupção de ANS o ANO também é paralisado.** 

Repare que no mesmo subprocesso podemos mesclar diferentes critérios de configuração de ANO. Nos exemplos acima configuramos uma tarefa com tempo constante e outra em função do ANS.

O terceiro critério de configuração de ANO é feito por horas apontadas na Ordem de Serviço. Veja o exemplo seguinte:

Configuração de ANO em função de apontamentos

No exemplo acima utilizamos um único campo nativo denominado Estimativa de esforço. Poderíamos também criar campos para cada atividade do fluxo e depois criar uma regra para cada atividade. Exemplo: tempo previsto para construção, tempo previsto para testes, tempo previsto para homologação etc. Na configuração do ANO bastaria utilizar fórmulas recuperando o campo customizado correspondente. Exemplo: OrdemServico.GetCustom("TEMPO_TESTES").

**Importante: O tempo previsto no ANO é aquele necessário para execução da tarefa durante todo o atendimento. Se uma tarefa for cancelada pelo comando Voltar e depois executada novamente ao avançar o processo o tempo contabilizado é o somatório das duas execuções. Se uma tarefa for executada várias vezes o tempo contabilizado é o somatório de todos os intervalos de execução.**

## Configuração de Períodos úteis

Esta configuração define os períodos de disponibilidade dos solucionadores e influenciam no cálculo de tempo do Acordo de Nível Operacional. Estes períodos estão presentes no cadastro de Calendários que podem ser associados a solucionadores da seguinte forma:

### 1o Critério: associação de um Calendário no registro do solucionador (cadastro de Grupo de Trabalho)

Neste caso quando vinculamos uma pessoa em um Grupo de Trabalho definimos o seu calendário de trabalho. Esta associação não é obrigatório e se não for realizada é utilizado o segundo critério de seleção de calendário.

Cadastro do calendário no registro de Solucionador

### 2o Critério: Calendário da Unidade de Negócio da localidade do solucionador

Se não for informado o calendário do solucionador conforme a figura acima, então o sistema verifica o calendário da Unidade de negócio onde está localizado o solucionador.

Calendário obtido no cadastro de Pessoa

Além de associarmos um calendário aos solucionadores precisamos definir a relação de períodos úteis (disponibilidade de recursos). Isto é feito no cadastro do calendário conforme a figura abaixo:

Configuração dos períodos úteis

Assim como a configuração de períodos de disponibilidade de serviços do ANS, nesta tela informamos períodos indicando o dia da semana e o início/fim em horas e minutos. Neste cadastro ainda contamos com uma coluna extra indicando a validade da regra, que pode ser aplicada em todas as semanas, somente semanas pares ou semanas ímpares. O uso de regras por semanas pares e ímpares permite configurar situações de alternância de disponibilidade.

## Executando Ordens de Serviço com ANO

Durante a execução da Ordem de Serviço o solucionador pode visualizar o tempo restante do ANO na parte superior do assistente de processo. No exemplo abaixo o ANO foi excedido em 315% enquanto o ANS possui um tempo restante de 36 minutos.

ANO não atendido pelo solucionador

Na tela de **Informações sobre Processo** e aba **Atividades executadas** o solucionador pode acessar um resumo dos tempos de ANO e respectivo indicador de cumprimento. Veja a figura abaixo:

Resultados do Acordo de Nível Operacional das atividades do processo

Por default o sistema atribui a responsabilidade do ANO ao solucionador com maior tempo de responsabilidade durante a execução da tarefa e permite ao coordenador deste mesmo solucionador reatribuir a responsabilidade de acordo com critério da sua gestão. Repare que o solucionador Ana Beatriz teve a Ordem de Serviço sob sua responsabilidade por 17 minutos e com isto ela foi selecionada como responsável.

Registro de responsável por ANO

Para indicar um outro solucionador responsável (descartando critério automático de tempo de responsabilidade) o coordenador do solucionador deve clicar no botão "**Definir responsabilidade**" e indicar outro solucionador da sua própria equipe.

Indicação de responsável pelo ANO

Outra ferramenta importante no gerenciamento do Acordo de Nível Operacional são as colunas de tempo restante de ANO e ANS da listagem de Ordens de Serviço da tela Workspace.

Ordenação do grid de Ordens de Serviço no Workspace

## Agrupamento de tarefas

Em determinadas situações pode ser interessante agrupar uma ou mais tarefas em um mesmo ANO compartilhando o mesmo tempo de atendimento, unidade de tempo e alertas.

## Seleção de uma tarefa pertencente ao grupo Primeiro nível

## Seleção da segunda tarefa do grupo Primeiro nível

Quanto executamos uma Ordem de Serviço do fluxo acima encontramos o seguinte resultado:

Resultado apurado para um agrupamento ANO

Repare que as duas tarefas compartilham o mesmo prazo de atendimento e a seleção do solucionador responsável leva em consideração o tempo total de responsabilidade durante a execução das duas tarefas.

Outra característica observada na configuração das tarefas pertencentes ao agrupamento é a facilidade na manutenção das propriedades **Prazo para finalização**, **Ações** e **Unidade para definição do Acordo de Nível Operacional**: sempre que ocorrer a mudança destas propriedades em uma tarefa do agrupamento a mesma mudança é replicada nas demais tarefas do grupo.

## Alertas e Encaminhamentos automáticos

A propriedade Ações pode ser utilizada para envio de e-mails e encaminhamentos automáticos em função do percentual do tempo total previsto no ANO. Na figura abaixo, por exemplo, um será enviado um e-mail para o Coordenador do solucionador se for atingido 40% do prazo do ANO. Se for atingido 70% deste prazo então é realizado um encaminhamento para o mesmo Coordenador.

Ações configuradas em um ANO

Na figura abaixo podemos verificar a execução da primeira ação configurada acima. Repare que podemos acessar o comunicado utilizando a aba de Comunicados da tela de Ordens de Serviço. Também é possível reenviar a mensagem ou incluir novos destinatários.

Comunicado enviado por uma ação do ANO

Clicando no botão de histórico de responsáveis (veja figura acima) podemos visualizar a explicação para o encaminhamento automático:

Explicação do encaminhamento

### Temporalidade

A temporalidade configurada em uma ação do tipo E-mail é um prazo em dias de permanência da mensagem no banco de dados. Ao terminar o prazo da temporalidade a mensagem será removida automaticamente.

O seu uso é indicado para redução de uso de espaço em disco após um período no qual a sua manutenção já não é mais necessária.

## Cálculo de ANO em função de prazos

Um Acordo de Nível Operacional também pode ser definido de acordo com uma data e/ou horário estipulado na Ordem de Serviço, sendo este o resultado de um cálculo em relação ao prazo final.

Realizando o cálculo desta forma, é possível ter uma maior flexibilidade nos prazos de ANO, visto que alguns projetos podem sofrer modificações em suas datas durante o desenvolvimento.

Para melhor entendimento, seguiremos com um exemplo:

Fluxo do Processo

Neste processo, depois de definido um prazo, inserimos um script para calcular o ANO da tarefa, de acordo com a data anteriormente preenchida.

Utilizamos um código que retornará o valor em minutos.

Script para o cálculo do ANO

Abrindo uma Ordem de Serviço, preenchendo o campo Data de Conclusão e após avançando para a respectiva tarefa com ANO, o sistema irá calcular o prazo (em minutos) de acordo com o horário atual e a data definida.

ANO calculado pelo sistema

Ao voltar à tarefa anterior, acrescentar um dia ao prazo e avançar novamente, o sistema irá calcular o ANO de acordo com esta nova data, sempre levando em consideração a Data da Primeira Execução da respectiva tarefa.

Novo ANO calculado

## Gestão do Acordo de Nível Operacional

Para gestão dos acordos podemos utilizar o relatório Análise de Acordo Operacional. Veja na figura abaixo um exemplo de saída deste relatório:

Gráfico de Análise do relatório de Acordo de Nível Operacional

No mesmo relatório podemos visualizar a relação de Ordens de Serviço onde o ANO foi violado:

Relatório analítico para Ordens de Serviço que violaram o ANO

Para Gestão do Acordo de Nível Operacional é possível também utilizar colunas no grid do Workspace de visualização de Ordens de Serviço com o progresso do ANO (para saber como adicionar ou remover colunas do grid do Workspace veja o tópico [Configuração do grid de Ordens de Serviço](configuracao_do_grid_de_ordens)), no exemplo a seguir podemos ver em porcentagem o restante do ANO e numericamente tanto o prazo quanto o restante do ANO:

**Colunas no Workspace para gestão do ANO**

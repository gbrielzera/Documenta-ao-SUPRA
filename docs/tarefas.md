# Tarefas

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Atividades > Tarefas

Tarefas são atividades manuais ou automatizadas realizadas por um Solucionador. Uma Tarefa consome um tempo para ser executada, envolve um ou mais recursos da organização, requer algum tipo de entrada e produz uma ou mais saídas.

Tarefa

Assim como acontece em iniciadores, podemos adicionar a uma tarefa Data Objects que representam entradas e saídas de um fluxo.

O **Motivo de interrupção de ANS** indica que ao iniciar a execução da Tarefa ocorrerá uma paralisação na contagem do tempo de atendimento previsto no Acordo de Nível de Serviço e esta suspensão ocorrerá até que a mesma atividade seja finalizada.

As propriedades **Ações**, **Grupo**, **Prazo para finalização** e** Unidade para definição de Acordo de Nível Operacional** definem prazos para conclusão da tarefa e podem ser utilizados para gestão de equipes e/ou Acordos de Nível de Serviço. Para mais detalhes sobre este assunto veja [Acordo de Nível Operacional](acordo_de_nivel_operacional).

A propriedade **Exige apontamento** não permite que o solucionador avance para a próxima atividade se não existirem apontamentos associados com a tarefa. Veja na figura abaixo como o apontamento é associado com a tarefa no momento de registro:

Informação da tarefa no apontamento

A propriedade **Permite voltar **habilita o comando Voltar do assistente de processos. Veja na figura abaixo que esta opção não é exibida:

Comando Voltar desabilitado pelo processo

O **Responsável** é configurado como um Papel de Processo que representa um grupo de pessoas (denominados Atores) que podem executar a Tarefa. Durante a execução de uma Ordem de Serviço a Máquina de Processos utilizará esta configuração de responsabilidades para realizar encaminhamentos automáticos. A responsabilidade configurado em Responsável também está relacionada com per missionamento na execução da atividade e este permissionamento pode ser restritivo quando ativamos a opção **Permissão restrita Papel responsável**. Quando esta opção estiver desativada qualquer pessoa pode realizar a Tarefa e neste caso será gravado na base de dados que houve uma não-conformidade com a configuração de responsabilidade; quando esta opção estiver habilitada somente usuários que atendam ao papel terão ação sobre a Ordem de Serviço, cuja tela de edição passa a ter todos os campos configurados como somente-leitura e com uma única operação de Encaminhamento disponível. Veja o comportamento do sistema com estas duas opções:

Tarefa com responsável em não-conformidade com papel de processo

Na consulta de pessoas envolvidas podemos observar o indicador de que o encaminhamento não está em conformidade com a responsabilidade configurada no processo:

Registro de não-conformidade

A gestão de não-conformidades pode ser feita utilizando o relatório** Análise de Melhorias em Processos** conforme ilustrado na figura abaixo:

Gestão de não-conformidades

A propriedade **Confirmar responsabilidade** pode ser utilizado para confirmar a responsabilidade de uma Ordem de Serviço em transições manuais de tarefas onde o solucionador conectado e responsável faz parte do papel da nova tarefa. No exemplo abaixo Pedro Santos faz parte do grupo Service desk e ele é também o especialista. Ao realizarmos o escalonamento para a atividade Restabelecer serviço do Especialista é apresentado um diálogo de encaminhamento onde podemos confirmar Pedro Santos ou escolher outro solucionador.

O usuário Pedro Santos escalona para o Especialista

Na figura abaixo podemos observar o comportamento do sistema quando o usuário responde **Não** na pergunta acima:

Confirmação da responsabilidade de Pedro Santos

A propriedade **Permite cancelamento pelo Portal** quando ativada permite que o próprio cliente realize o cancelamento utilizando o site de Portal.

Propriedade que permite ao cliente realizar o cancelamento via Portal

Quando esta propriedade possui o valor True (verdadeiro), passa-se a ser exibido no Portal (caso a atividade em execução seja a que configuramos) um comando para o cancelamento da Ordem de Serviço no canto superior direito da página de detalhes da Ordem de Serviço, na seção Consulta, caso o usuário logado seja o Cliente da Ordem de Serviço:

Botão de cancelamento disponível para o cliente no Portal

Clicando no botão "Cancelar" é exibida uma janela para a descrição do motivo:

Motivo de cancelamento

Clicando botão "Cancelar Ordem de Serviço" a Ordem de Serviço é cancelada:

Visualização do cancelamento no Workspace

Outra característica importante é a capacidade de implementarmos scripts para automatizar uma Tarefa. Estes scripts são implementados com a linguagem IronPython que possui sintaxe herdada de Python e inclui a biblioteca de objetos do Microsoft .NET. Existem 3 eventos que podemos codificar:

**Evento**

**Quando é disparado**

**Script Início**

Ocorre quando a Tarefa é iniciada e pode ser utilizado para preparação ou automatização de uma atividade. No exemplo abaixo podemos verificar um script de inicialização que executa uma ação e em seguida notifica a Máquina de Processos que é possível avançar automaticamente para a próxima Tarefa:

```
    LDAP.AddUserToGroup(OrdemServico.Favorecido.UsuarioRede, "Pasta-Suprimentos")
    AvancaProximaAtividade = True
```

**Script Validação**

Ocorre imediatamente antes do fim da Tarefa é utilizado para consistir o trabalho realizado. Esta verificação pode incluir testes em bases diversas, campos da própria Ordem de Serviço, consultas ao Serviço de Diretórios etc.

No script de validação é possível adicionar pendências e avisos importantes. Se existir no mínimo uma pendência então a Máquina de Processos não permitirá a transição para a próxima atividade.

**Importante:** O Script Validação, por padrão, também é executado ao final de todo o processo. No entanto, esta configuração pode ser alterada através do parâmetro **Executar Script de validação na finalização**, visível apenas nas tarefas que possuem Script Validação.

**Script Fim**

Ocorre quando a Tarefa é finalizada e pode ser utilizado para executar alguma ação de complemento para a Tarefa.

Lembre-se que a finalização pode ocorrer de forma automática, após uma aprovação por exemplo, ou manual quando o usuário clica no botão** Avançar** do Assistente de Processos. O Script Fim será chamado em todos os casos possíveis.

**Script Volta**

Ocorre ao voltar a tarefa de uma Ordem de Serviço para a anterior.

Após implementação de um dos scripts, um novo ícone será marcado na tarefa:

Indicador de Script

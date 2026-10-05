# Execução de Tarefa do Processo

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Papéis e responsabilidades > Tipos de Papéis > Execução de Tarefa do Processo

Este tipo de papel permite recuperar a pessoa responsável pelo início ou finalização de uma ou mais tarefas no processo.

Para isso, é importante configurar um código para cada uma das tarefas:

Definição de código para as tarefas

Após, configure um novo papel com seguinte formato, alterando o preenchimento conforme a necessidade, como por exemplo, os campos **Código da atividade** e **Tipo de envolvimento na atividade**.

Configuração de um novo papel

Importante: Quando existem duas ou mais atividades a terem suas pessoas recuperadas, o código de suas tarefas devem estar separados por ;(ponto e vírgula) e sem espaçamento no campo Código da atividade.

Abaixo, iremos introduzir sobre cada Tipo de Envolvimento a ser recuperado no papel:

## Aprovadores da Atividade

Neste tipo de recuperação de papel, também é possível recuperar Pessoas envolvidas em **Aprovações **de tarefas.

Recuperação de aprovadores

Vale ressaltar que nestas situações, será levada em conta a situação da aprovação e não da versão.

Como na situação abaixo, uma aprovação foi aprovada e logo após a Versão 1 cancelada.

Aprovação foi aprovada e após cancelada

Na recuperação do papel, serão retornados os **Aprovadores da Atividade**. Como a aprovação já está com a situação aprovada, será retornado **Augusto Magalhães** no papel, descartando a situação da versão.

## Responsável pelo ANO

Recupera a Pessoa responsável pelo [Acordo de Nível Operacional](acordo_de_nivel_operacional) da tarefa.

Pessoa responsável pelo ANO

## Iniciador ou Finalizador da tarefa

Recupera a Pessoa que iniciou ou finalizou a respectiva tarefa indicada no campo Código da Atividade.

Solucionadores da atividade

Dentre os parâmetros para as configurações acima, há uma denominada **Somente última execução**. Habilitando como True, o critério de recuperação passa a considerar apenas a última passagem pela tarefa, caso haja mais de uma pela mesma.

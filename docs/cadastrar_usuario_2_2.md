# Papéis e responsabilidades

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Papéis e responsabilidades

O Supravizio permite determinar dinamicamente os atores que poderão interagir de forma direta ou indireta na execução de etapas de um processo. Para isso, utilizamos o conceito de Papéis.

A configuração de papéis do Supravizio é o conceito chave para determinar responsabilidades nos fluxos de processo. Este recurso é representado pelo cadastro de Papéis que está disponível no Editor de Processos no comando Papeis.

Cadastro de papéis

Estes papéis são utilizados em diversos elementos e recursos da modelagem de fluxos de processo. Nos próximos tópicos veremos algumas de suas aplicações.

### Responsável por Atividades

Esta é a aplicação mais comum da utilização de papéis de processo e define um "performer" para alguma tarefa, subprocesso ou evento do processo. Veja na figura abaixo como realizar esta configuração:

Configuração de responsável por Atividade

A configuração de responsabilidade define o comportamento de coordenação do fluxo de trabalho. A partir da responsabilidade o sistema será capaz de provocar os encaminhamentos entre as pessoas que participam do processo.

Na figura abaixo, por exemplo, podemos observar que as tarefas **Construir** e **Testar** possuem diferentes responsáveis: **Implementador **e** Testador.** Estes, por sua vez, são papéis que foram definidos no sistema. Isto significa que quando o usuário Implementador utilizar o botão **Avançar** do [Assistente de Processos](editar_ordemservico) a Máquina de Processos do Supravizio selecionará, de forma automática, a pessoa responsável pela tarefa** Testar** com base na configuração do papel** Testador**. Neste caso específico se existir somente uma pessoa testadora então o encaminhamento é feito automaticamente, mas se existirem várias então o implementador deve selecionar uma para encaminhamento:

Exemplo de fluxo com responsabilidades configuradas

Sempre que ocorrem transições entre atividades com diferentes responsabilidades o Supravizio entra em ação realizando o devido** encaminhamento automaticamente** e troca de responsabilidade.

Também utilizamos o recurso de responsabilidade para a configuração do iniciador de um subprocesso, onde é utilizado para seleção de responsáveis quando a Ordem de Serviço é aberta pelo Portal. Neste caso específico precisamos de um papel que corresponda sempre a uma única pessoa. Para mais detalhes sobre estes critérios, leia [Tipos de Papéis](tipos_papeis).

### Clientes Autorizados

Esta configuração está presente em iniciadores manuais e é utilizada para restringir a abertura para determinadas pessoas que possuam o papel configurado. Para mais detalhes veja [Responsabilidades e autorizações do iniciador manual](bpmn_iniciadores).

### Aprovadores

Papéis são utilizados também na configuração de aprovações para determinar os aprovadores da solicitação. Para mais detalhes leia [Data Objects Aprovação](bpmn_data_objects).

### Destinatários em comunicados

É possível definir as pessoas destinatárias de um comunicado, seja este configurado via [Tipo de Evento](tipoevento_sub) ou [Eventos intermediários de Mensagem](bpmn_eventos_intermediarios), utilizando o recurso de papéis.

Veja também:

- [Tipos de Papéis](tipos_papeis)
- [Criando e adicionando uma fila compartilhada no Grupo de Trabalho](cadastrar_fila)
- [Obtém Ordens de Serviço a partir de filas compartilhadas](cadastrar_usuario_2_2_2_2)
- [Redefinição de papéis por Serviços e Itens de Configuração](redefinindo_papeis)

# Toolbox e elementos do BPMN

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN

**Toolbox** é uma barra de ferramentas que contêm ferramentas BPMN - Business Process Modeling Notation - disponíveis para a modelagem de processos. Veja a figura abaixo:

Janela Toolbox

Para adicionar uma destas ferramentas em um diagrama de processo basta executar um clique no objeto desejado (não é necessário manter o botão do mouse apertado) e depois clicar novamente no ponto adequado do diagrama de processos. Determinados elementos exigem que o clique no diagrama seja dado sobre o outro elemento que será relacionado. Por exemplo: para adicionarmos uma Aprovação clique primeiro no elemento "Aprovação" do Toolbox e em seguida clique em uma Tarefa que receberá a configuração de Aprovação.

O elemento Point possui a função de cancelar um modo de inserção de outros elementos e permite selecionarmos outros elementos já colados no diagrama.

A tabela abaixo apresenta um sumário de todas as ferramentas BPMN disponíveis no Supravizio:

|  | **Iniciador manual**: inicia um processo manualmente utilizando a tela Workspace ou Portal de Processos. O ícone indica que o iniciador está disponível no Portal e o ícone indica que estará disponível no Workspace. |
|---|---|
|  | Inicia um processo utilizando um temporizador: neste caso as Ordens de Serviço são geradas automaticamente pela máquina de processo com base em um ciclo. |
|  | Inicia um processo quando for satisfeita uma regra (fórmula): neste caso as Ordens de Serviço são geradas automaticamente pela máquina de processos sempre que for satisfeita a fórmula. É possível, por exemplo, incluir na fórmula um comando SQL e para cada registro retornado é gerada uma Ordem de Serviço. Também podemos utilizar como fórmula um valor lógico e quando este valor for verdadeiro é gerada uma Ordem de Serviço. |
|  | Inicia um processo a partir de outro processo: este iniciador é importante quando realizamos uma chamada de subprocesso. É um recurso importante para configurar a interface entre subprocessos. |
|  | Representa uma tarefa manual ou automatizada: esta tarefa pode conter entradas e gerar saídas. |
|  | Fluxo de Tarefas com entradas e saídas e sob responsabilidade de uma ou mais pessoas na organização. |
|  | Decisão baseada em Pergunta/resposta: neste caso o operador visualiza uma pergunta e com base em sua resposta a máquina de processos desvia a execução do processo. |
|  | Decisão baseada em dados (fórmula): a decisão é tomada por uma fórmula que pode conter um valor lógico e fazer acesso a base de dados. |
|  | Evento intermediário baseado em temporizador: permite a transição para outra atividade ou decisão com base em um temporizador. Transições deste tipo são executadas automaticamente pela máquina de processos. |
|  | Evento intermediário baseado em regra (fórmula): permite a transição para outra atividade ou decisão com base em uma fórmula. Transições deste tipo são executadas automaticamente pela máquina de processos. |
|  | Eventos intermediários do tipo mensagem: faz o envio de uma mensagem para destinatário configurado no próprio evento. |
|  | Finalizador de um processo: marca o fim do processo. |
|  | Finalizador de um processo seguido de chamada para outro fluxo. |
|  | Cancelamento de processo. |
|  | Raia: Elementos associados passam a ser de responsabilidade do Papel definido (exceto caso a responsabilidade atual seja definida como Sistema ou uma fila) |
|  | Data Object do tipo Entrada de dados: permite especificar campos que devem ser preenchidos pelo usuário. |
|  | Data Object do tipo Aprovação: permite configurar uma aprovação. |
|  | Data Object do tipo Item de Configuração (associação ou geração): permite relacionar o processo com o banco de dados de itens de configuração, incluindo a criação ou mera associação. Importante: artigos da base de conhecimento são tratados como itens de configuração. Portanto sua manutenção pode ser governada por este tipo de recurso. |
|  | Data Object genérico utilizado para representar documentos diversos no fluxo. |
|  | Comentário utilizado para documentar graficamente o fluxo de um subprocesso. É possível publicar um comentário no Portal. Quando publicados o elemento ganha um ícone . |

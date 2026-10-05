# Desvio por Evento

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Desvios > Desvio por Evento

Neste tipo de desvio o usuário solucionador deve responder uma pergunta. Baseado na sua resposta o fluxo sofre um desvio:

A pergunta acima foi configurada no processo utilizando o Desvio por Evento. Preenchemos no campo Descrição o texto para tomada de decisão do usuário que geralmente é uma pergunta e as alternativas que serão exibidas como fluxos do processo:

No exemplo acima quando respondemos a opção **Não** o fluxo é remetido para a tarefa **Executar atualização**. Veja o resultado abaixo exibido na tela de detalhes de execução do fluxo:

O texto exibido nas alternativas é configurado no fluxo de cada alternativa. Para isso, selecione o fluxo da alternativa e modifique a propriedade Texto:

Um Desvio por Evento quando exibido para o solucionador, dispõe de um campo para que este descreva alguma observação relevante, com rótulo **Motivo ou comentário**. É possível configurar a obrigatoriedade do preenchimento deste campo através da propriedade **Motivo obrigatório**. É possível também modificar o rótulo do texto do campo Motivo ou comentário para cada alternativa possível através da propriedade **Rótulo do motivo**. Repare no exemplo abaixo que configuramos o motivo como obrigatório e redefinimos o rótulo apresentado na pergunta:

Ao responder uma pergunta, caso o solucionador preencha o campo Motivo ou comentário, o texto é exibido nos comentários da Ordem de Serviço, junto com o texto da pergunta:

Nesse tipo de desvio também temos a opção publicar a resposta do solucionador na alternativa no Portal de Processos através da propriedade **Publicar resposta no Portal de Processos**:

Propriedades do fluxo

No exemplo abaixo, publicaremos a resposta do solucionador no Portal de Processos. Se o solucionador tomar a decisão "Sim, é o primeiro registro da falha", por exemplo, a resposta e o motivo serão publicados como um comentário no Portal.

Respondendo a decisão

Resposta no Portal de Processos

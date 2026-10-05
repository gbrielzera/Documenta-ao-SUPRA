# Suspendendo o prazo definido no ANS

Caminho: Guia para Solucionadores > Workspace  > Workspace Ordens de Serviço > Visualizar e editar uma Ordem de Serviço > Suspendendo o prazo definido no ANS

Uma interrupção é uma paralisação na contagem do tempo de atendimento ([no ANS](acordo_de_nivel_servico)) em decorrência de uma situação de exceção prevista no acordo. Esta situação pode ser registrada de forma manual ou prevista em processo.

Para interromper um ANS (Acordo de Nível de Serviço) siga os passos abaixo:

1. Abra a tela de Edição da Ordem de Serviço e selecione a aba ANS e Priorização de acordo com a imagem abaixo:

Aba 'ANS e Priorização'

2. Clique em Nova para gerar uma Nova interrupção de Acordo de Nível de Serviço:

Nova interrupção de ANS

3. Selecione a Data/hora início da interrupção (esta Data/hora início deve ser maior ou igual a data hora de solicitação da interrupção):

Data/hora início

4. Escolhendo o Motivo da Interrupção:

O motivo da interrupção deve ser cadastrado em Recurso | Motivos de Interrupção de SLA:

Motivos de Interrupção de SLA

Clique em **Novo** para gerar um novo motivo de interrupção de SLA:

Novo Motivo de Interrupção de SLA

Também é possível incluir o Motivo de interrupção também no cadastro de ANS. Selecione em Recurso | Acordo de nível de Serviço | Acordo de Nível de Serviço:

Cadastro de Acordo de Nível de Serviço

Selecione o Acordo de Nível de Serviço que deseja alterar e após, em Interrupções, selecione Novo:

Interrupções

Selecione um dos Motivos de Interrupção existes e clique em Salvar e Voltar.

Após inserir o Motivo de Interrupção é possível visualizá-lo na janela de Nova interrupção de nível de serviço:

Motivo de Interrupção

Pode ser incluído um Comentário ou Justificativa:

Comentário ou Justificativa

5. Escolha a Data/hora prevista para a finalização:

Data/hora previsto para finalização

O mensagem do aviso que será encaminhada deve ser definida em Tipos de Eventos. Selecione no menu do Supravizio, clique em Processo | Processos | Tipos de Eventos e selecione o tipo de evento Aviso Fim Interrupção ANS:

Aviso Fim Interrupção ANS

Em Mensagens crie uma mensagem:

Mensagem Evento

6. Ao realizar a interrupção a janela de Priorização e ANS será apresentada a situação da interrupção na janela de Priorização e ANS:

Priorização e ANS

7. Na janela de Edição de Ordens de Serviço ficará disponível um botão onde poderemos finalizar a interrupção, uma mensagem com dados da interrupção e em comentários e mensagens também aparecem os dados da interrupção:

Janela de Edição de Ordens de Serviço

Na tela do Ordens de Serviço do Workspace, é possível identificar quando uma Ordem de Serviço teve seu ANS interrompido através de símbolo no grid de Ordens de Serviço:

Interrupção de ANS

Ou pode significar também que a Data/Hora de entrega de serviço, chegou ao fim. Esta Data/Hora da entrega do serviço é configurada no processo através de uma entrada de dados:

Data/Hora de entrega do serviço

Importante: Após registrar a data/hora de entrega do serviço não é mais permitido ao usuário adicionar interrupções de ANS. Se for realmente necessário adicionar a interrupção então será necessário acessar o campo em questão e limpar a data informada. Em seguida adicione a interrupção e, se necessário, volte a registrar a data/hora de entrega de serviço que deve ser posterior ao final de todas as interrupções válidas.

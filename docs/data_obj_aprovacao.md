# Aprovação

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Data Objects > Aprovação

Como o próprio nome sugere este Data Object está relacionado com solicitações de aprovação que podem ser introduzidos em um fluxo de processo.

Para adicionar um Data Object deste tipo basta selecionar o item **Aprovação** do **Toolbox** e em seguida clicar na Tarefa que receberá a aprovação. Cliques em qualquer outro objeto que não seja uma Tarefa cancelará a inclusão da aprovação.

Elementos Data Object

O primeiro passo para configuração de uma aprovação é definir a lista de aprovadores da solicitação. Esta configuração é feita em função de papéis de processo que é o mecanismo para determinar responsabilidades (neste caso para selecionar pessoas para a aprovação). Para adicionar aprovadores clique no botão da propriedade **Aprovadores** e será exibida o seguinte diálogo:

Configuração do papel responsável pela aprovação

Por default uma solicitação de aprovação só é efetivamente encerrada como **Aprovada** se todas as pessoas indicadas nos papéis realizarem a aprovação. Também no comportamento padrão se uma das pessoas reprovar então toda a solicitação é encerrada como **Reprovada**. Utilizando as propriedades **Mínimo aprovadores** podemos indicar um número mínimo de pessoas necessárias para aprovação e, neste caso, a reprovação de uma pessoa só resulta na reprovação total se não for possível, a partir deste momento, obter o mínimo necessário de aprovações. Neste último caso podemos utilizar a propriedade **Reprovar imediatamente** para reprovar totalmente a solicitação após a primeira reprovação, ignorando o parâmetro **Mínimo aprovadores**. A propriedade **Reprovar imediatamente** só é utilizada e exibida quando for preenchida a propriedade **Mínimo aprovadores**.

Após definir os aprovadores devemos incluir os dados que estão sujeitos a aprovação que podem ser: campos da Ordem de Serviço, Itens de Configuração anexados na Ordem de Serviço e apropriações de horas trabalhadas. Estes dados podem ser configurados manualmente utilizando a janela de propriedades ou a partir de menus de contexto disponíveis em Data Objects que já configuram estes dados.

Para configurar manualmente um campo para aprovação utilize o botão da propriedade Campos para Aprovação do Data Object de Aprovação que deve estar selecionado no editor. Veja a figura abaixo:

Configuração de campos da Ordem de Serviço para Aprovação

No diálogo de edição de campos de aprovação informe campos customizados ou nativos para aprovação.** É importante observar que após a aprovação de um campo este não pode mais ser modificado pelo usuário utilizando a tela de edição de Ordens de Serviço. **Na figura abaixo podemos observar a configuração de um campo para aprovação:

Configuração de um campo para aprovação

Na tela abaixo podemos observar o resultado final desta configuração na página de aprovação do Portal:

Exibição de campo configurado para aprovação

E após a aprovação o campo que fez parte da requisição não pode mais ser modificado:

Campo aprovado e somente-leitura

Neste último caso basta utilizar o comando **Aprovar em**. Para isso selecione um Data Object de Entrada de Dados ou de Associação de Itens de Configuração, clique com o botão direito e no menu de contexto selecione **Mais Ações | Aprovar em | [atividade que será gerada a aprovação]**:

Facilitador para configuração de aprovação

Este acelerador configura todos os dados que precisam ser aprovados na solicitação incluindo campos e itens de configuração.

Um outro recurso de muita utilidade neste Data Object são os Campos para Preenchimento. Através deles é possível o aprovador realizar o preenchimento de alguma informação sobre a aprovação/reprovação.

Campos que serão preenchidos na aprovação

Podemos solicitar através deste recurso que o aprovador preencha um ou mais campos que podem ser campos nativos da Ordem de Serviço ou campos customizados. Podemos indicar também a obrigatoriedade do preenchimento data a operação que o aprovador efetuará, se ele realizar uma aprovação, uma reprovação, ambas, ou nenhuma obrigatoriedade, através da propriedade** Obrigatoriedade**. Os campos para preenchimento em aprovações são exibidos abaixo do campo Motivo/Observação:

Campos preenchidos durante a aprovação

### Modificação de informações aprovadas

Quando qualquer campo da Ordem de Serviço é aprovado, ele fica bloqueado não permitindo modificações:

Campo Aprovado

O símbolo de cadeado demonstra que o campo não pode mais ser alterado pois está bloqueado. Para desbloquear o campo, é necessário cancelar a aprovação relacionada com o campo, modificar o conteúdo para então solicitar novamente a aprovação. Portanto na aba de Aprovações, cancele a versão de aprovação:

Cancelar versão de aprovação

Então após editar o campo, crie uma nova versão da mesma aprovação e então inicie novamente a aprovação. Após aprovar novamente verifique que o campo volta a conter o símbolo de cadeado (e está novamente bloqueada para edições):

Campo modificado

Uma outra maneira de poder editar o campo já aprovado é na configuração do Subprocesso permitir tal ação. No Editor de Processos, no processo desejado verifique que no Elemento de Aprovação, tanto no Campo para Aprovação quanto no Campo para preenchimento, há uma propriedade chamada Permitir modificação após aprovação, basta definir esta propriedade como "True" para o campo desejado que é possível modificar este campo mesmo após aprovação:

**Permitir modificação após aprovação** 

### Geração automática da solicitação versus configuração manual

Por padrão toda solicitação de aprovação é iniciada automaticamente pelo sistema quando o processo inicia a execução da tarefa onde a aprovação está configurada. Este comportamento pode ser modificado atribuindo o valor Falso para a propriedade **Iniciar automaticamente**. Nesta situação o usuário solucionador responsável pela ocorrência deve indicar os aprovadores e eventuais arquivos para aprovação.

Na figura abaixo podemos observar a mensagem exibida para o solucionador orientando sobre o preenchimento manual da aprovação.

Mensagem orientado o usuário solucionador na configuração da aprovação

### Pré-aprovação

O recurso de pré-aprovação permite acelerar o andamento do processo baseado em informações previamente fornecidas e aprovadas.

### Propriedades relacionadas com pré-aprovação

Existem duas possibilidades de pré-aprovação:

- Reutilizar aprovações anteriores: realiza a aprovação automática por uma determinada pessoa se esta já realizou uma aprovação prévia na mesma Ordem de Serviço. É recomendado ativar esta versão desde que entre a aprovação alvo e a anterior não tenha ocorrida nenhuma modificação nos dados sujeitos a validação.
- Utilizar identidade do solicitante: realiza a aprovação automática para uma determinada pessoa desde que esta tenha sido a responsável pela abertura da Ordem de Serviço via Portal ou Workspace.

**Importante: a aprovação automática não está disponível para aprovações incrementais por hierarquia.**

Para mais detalhes sobre pré-aprovação veja [Tutorial 8: Pré-aprovação de Ordens de Serviços](tutorial_8_preaprovacao).

### Assinatura Digital do Aprovador

Através do parâmetro "Assinatura Digital" nas propriedades da Aprovação, temos um método de autenticação de informação digital comparável a uma assinatura física em papel.

Propriedade relacionada

Quando habilitada esta função, ao realizar uma aprovação/reprovação, será exibida uma mensagem:

Diálogo de confirmação

Ao confirmar, será exibido um diálogo para escolha do certificado.

Tela de seleção de certificado

Para realizar a validação do certificado, o sistema utilizará o certificado configurado no [Cadastro de Pessoas](cadastro_de_pessoas):

Cadastro da Pessoa

**Importante**: Para executar o recurso de assinatura digital, é necessário que o site esteja rodando em protocolo https. Também vale ressaltar que a estação de trabalho do aprovador deverá possuir instalado Java Runtime Edition 8 (JRE) Update 25 ou superior.

**Envio de Comunicado de Aprovação** Utilizando o parâmetro "Frequência de reenvio do email em horas", nas propriedades do elemento Aprovação, podemos definir uma quantidade em horas para o reenvio do comunicado que avisará o Aprovador que há alguma pendência de aprovação.

Ao definir um valor, a cada intervalo desse tempo, o Aprovador receberá um comunicado referente a Aprovação pendente até que seja aprovada, ou seja, enquanto a Aprovação estiver pendente ele receberá os comunicados de aviso da pendência.

**Importante: Será enviado um email para cada aprovação pendente.**

**Configuração do rótulo dos Botões de Aprovar e Reprovar** No Supravizio há a possibilidade de alterar o rótulo dos botões de Aprovar e Reprovar do Portal.

Na modelagem do processo o elemento Aprovação possui duas propriedades, **Rótulo do botão Aprovar** e **Rótulo do botão 'Reprovar'**, podemos definir um novo texto para mesmos, no site do Portal (como na figura abaixo), caso permaneça vazio, por padrão serão exibidos com o texto Aprovar e Reprovar.

Propriedades da Aprovação

Ao atribuir um novo texto nas propriedades, temos que salvar o processo.

Podemos visualizar no Portal que o rótulo dos botões estão com os valores definidos anteriormente:

Aprovação no Portal de Processos

# Campos para preenchimento em aprovações

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 3: Incluindo aprovações > Campos para preenchimento em aprovações

Os campos para preenchimentos nas aprovações possibilita que o aprovador possa preencher campos que serão apresentados na aba Dados principais da tela de Edição de Ordens de Serviço. A configuração destes campos pode auxiliar os aprovadores e os solucionadores da Ordem de Serviço que terão disponível para visualização na Ordem de Serviços os campos preenchidos na Aprovação ou Reprovação.

Neste tópico iremos configurar Campos para Preenchimento nas aprovações e apresentaremos um passo a passo do preenchimento dos campos na aprovação de uma Ordem de Serviço:

### 1. Neste exemplo estamos criando Campos para preenchimento em uma aprovação. Selecione a Aprovação no Processo de exemplo Adquirir Suprimentos e na janela de Propriedades adicione Campos para preenchimento:

### Campos para preenchimento em Aprovações

Ao selecionar os campos para preenchimento é necessário selecionar o Obrigatoriedade que indica o preenchimento do campo para as situações de Aprovações, Nenhuma, Reprovação Todas:

### Campos exibidos para o aprovador com possibilidade de preenchimento/modificação

### Em casos de dúvidas para adicionar os Campos para preenchimento clique no link [Propriedades](propriedades_editor).

### 2. Após adicionar os Campos para preenchimento da Aprovação, selecione o subprocesso Adquirir Suprimentos no Process Explorer e valide o subprocesso clicando no botão Validar fluxos do diagrama . Clique em Salvar no Process Explorer para salvar as modificações do processo. Acesse a tela Workspace e a partir do botão Novo selecione o subprocesso Adquirir Suprimentos e crie uma nova Ordem de Serviço:

Criando Nova Ordem de Serviço

Observe na tela abaixo que ao criar e avançar a Ordem de Serviço a aprovação ficará pendente:

### Nova Ordem de Serviço

### 3. Ao selecionar a aba de Aprovações é possível observar os Campos para preenchimento que foram adicionados na aprovação:

### Campos para preenchimento na aba Aprovações

### 4. Acessando o Portal de Processos, o aprovador poderá Aprovar/Reprovar e então preencher os campos para preenchimento da Aprovação. No nosso exemplo a Ordem de Serviço será aprovada e os campos obrigatórios para preenchimento em casos de Aprovações serão preenchidos:

Aprovação no Portal

**Observação:** Também é possível realizar a aprovação pelo Supravizio Web, clicando no botão **Aprovar** da aba de aprovações:

### Aprovação ou Reprovação

Observe que ocorreu a aprovação da ordem de Serviço:

### Ordem de Serviço Aprovada

### Após a aprovação os campos preenchidos aparecerão na tela Dados Principais da Ordem de Serviço com ícones de "cadeados", informando que estes campos estão desabilitados devido a aprovações realizadas. Ao passar com o mouse por cima destes campos, será exibido um tooltip com uma mensagem referente ao motivo destes campos estarem bloqueados:

### Campos desabilitados após Aprovações

### 5. Em casos de necessidades de modificações será necessário o cancelamento da aprovação que contém os campos desabilitados. Para isto selecione a aba Aprovações, identifique as aprovações que tem o campo bloqueado e cancele a versão:

### Cancelamento de Aprovação

### 6. Retorne na aba Dados Principais e realize as modificações necessárias dos campos:

### Modificando os campos para preenchimento

### 7. Retorne na tela de Aprovações e crie uma nova versão para aprovação, clique em Aprovar/Reprovar e observe que os campos estão com novo preenchimento que são os preenchimentos feitos na aba Dados Principais no passo anterior:

### Aprovação/Reprovação

### 8. Clique em OK para realizar nova Aprovação.

### 9. Ao finalizar altere novamente o papel e a tarefa para as configurações de aprovação do Presidente como era anteriormente.

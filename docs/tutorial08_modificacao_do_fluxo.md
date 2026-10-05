# Modificar o Subprocesso

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 8: Pré-aprovação de Ordens de Serviço > Modificar o Subprocesso

Vamos agora modificar o **subprocesso** de **Aquisição de suprimentos** que ao término do tópico terá as seguintes características:

Versão final do novo fluxo

### 1. No Editor de Processos selecione a janela Process Explorer e gere uma nova versão do processo Administrativo:

Geração de nova versão

### 2. Selecione o fluxo de Aquisição de Suprimentos na versão em edição:

Seleção do fluxo que será modificado

### 3. Adicione uma tarefa denominada "Solicitar aprovação do Gerente do Cliente" e configure o fluxo conforme a figura:

Adição da aprovação

### 4. Copie a aprovação da tarefa "Solicitar aprovação do Presidente"

### Copiando a aprovação

### 5. Cole a aprovação copiada na tarefa "Solicitar aprovação do Gerente do Cliente":

Colando a aprovação

Cadastro do novo papel inserido no processo de Atendimento

### 6. Selecione novamente a nova aprovação e no diálogo de propriedade modifique o aprovador para Gerente do Cliente:

### Propriedade que deve ser modificada

### Propriedade já modificada

### 7. Selecione novamente a tarefa de aprovação e modifique o código para APROV_GER_CLI:

### Alteração no código da tarefa com aprovação

### 8. Adicione uma decisão baseada em dados e configure o fluxo conforme a figura abaixo:

Decisão para avaliar resultado da aprovação

Na propriedade **Fórmula critério** da decisão **Gerente aprovou? **informe a fórmula **OrdemServico.PossuiAprovacao("APROV_GER_CLI")**

Edição da fórmula de decisão

Nesta mesma decisão selecione a alternativa que leva ao evento de cancelamento e faça a seguinte configuração na janela de propriedades:

Configuração do fluxo de reprovação

Novamente na decisão** Gerente aprovou?** selecione a alternativa que leva a tarefa **Realizar compra** e faça a seguinte configuração:

Configuração do fluxo de aprovação

### 9. Selecione novamente a aprovação do Gerente do Cliente e atribua o valor True para as propriedades "Reutilizar aprovações anteriores" e "Utilizar identidade do solicitante":

Configuração da pré-aprovação

A opção **Reutilizar aprovações anteriores** será útil quando o Gerente do cliente for também o Presidente, cuja aprovação já foi realizada no início do processo. Já a opção **Utilizar identidade do solicitante** considerará aprovada se o usuário aprovador foi o responsável pela abertura utilizando a aplicação do Portal de Processos.

### 10. Selecione a aprovação do presidente e atribua o valor True para a opção "Utilizar identidade do solicitante":

Configuração da pré-aprovação do Presidente

Com a configuração acima quando o próprio presidente realizar a abertura desta Ordem de Serviço pelo Portal o sistema considerará aprovada pelo próprio presidente.

### 11. Salve todas as modificações pendentes e ative a versão:

Ativação da nova versão

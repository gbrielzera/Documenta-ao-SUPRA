# Desenho do fluxo

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 1: Construindo o primeiro Processo > Desenho do fluxo

O objetivo deste tópico é construir o fluxo de um subprocesso simples utilizando os principais elementos do BPMN para esta finalidade. Ao término do tópico teremos o seguinte fluxo para o novo subprocesso:

Fluxo que será criado

## Adicionar um Iniciador

A primeira tarefa na elaboração do fluxo de um Subprocesso é adicionar um evento iniciador. Este tipo de evento determina regras aplicadas a abertura de uma Ordem de Serviço deste tipo.

No nosso exemplo utilizaremos um Iniciador Manual que corresponde ao ícone presente na janela Toolbox. Siga os seguintes passos para adicionar o iniciador:

| **1.** | Selecione a janela Toolbox: |
|---|---|

Janela Toolbox

| **2.** | Na janela Toolbox clique no ícone Evento Inicial: |
|---|---|

Seleção do Evento inicial da janela Toolbox

| **3.** | Sobre o diagrama do fluxo utilize um clique simples para incluir o iniciador: |
|---|---|

Inclusão do Evento inicial no fluxo

## Adicionar uma Tarefa

No próximo passo vamos adicionar uma atividade do tipo Tarefa onde será configurada uma ação e responsabilidade do processo.

1. Selecione a janela Toolbox:

Janela Toolbox

### 2. Na janela Toolbox clique no ícone Tarefa:

Seleção de tarefa na janela Toolbox

### 3. Sobre o diagrama do fluxo utilize um clique simples para incluir a tarefa:

Inclusão de tarefa no fluxo

### 4. Preencha o descritivo com o texto Realizar compra e depois clique em algum ponto do diagrama para finalizar o modo de edição:

### Alteração no descritivo de tarefa

Seguindo o objetivo de montar um fluxo simples vamos agora adicionar um Evento Finalizador seguindo os seguintes passos:

1. Selecione a janela Toolbox:

Janela Toolbox

### 2. Na janela Toolbox clique no ícone Evento Final:

Seleção de evento final na janela Toolbox

### 3. Sobre o diagrama do fluxo utilize um clique simples para incluir o finalizador:

Inclusão do evento final no fluxo

## Correlacionando os elementos do fluxo

Vamos agora configurar os fluxos entre estes 3 elementos adicionados ao fluxo. Para isto siga os seguintes passos:

### 1. Na janela Toolbox clique no ícone Fluxo:

Seleção de Fluxo na janela Toolbox

### 2. Clique sobre um dos conectores do evento inicial com o botão esquerdo do mouse e mantendo este botão pressionado arraste a nova linha até um dos conectores da tarefa Realizar compra:

### Inclusão de fluxo relacionando evento inicial e tarefa no fluxo

### 3. Crie o fluxo entre a tarefa Realizar compra até o finalizador utilizando o mesmo procedimento acima:

### Inclusão de link de fluxo relacionando tarefa e evento final no fluxo

## Definindo a Entrada de Dados

Nosso fluxo terá como entrada o descritivo da solicitação e uma justificativa que serão informados no início do processo. Siga os próximos passos para configurar esta entrada de dados:

### 1. Na janela Toolbox selecione o ícone Entrada de Dados:

Seleção de entrada de dados no Toolbox

### 2. Clique sobre o iniciador manual para incluir o Data Object de Entrada de Dados:

Inclusão de entrada de dados no fluxo

### 3. Selecione o novo objeto de Entrada de dados e com o botão direito do mouse acesse a opção Propriedades do menu de contexto:

Propriedades da entrada de dados

4. Na janela de Propriedades clique no botão para configurar os campos da entrada de dados:

Configuração dos campos de preenchimento nas entradas de dados

### 5. No diálogo de configuração de campos clique no botão Adicionar localizado no canto inferior esquerdo:

Campos que devem ser preenchidos pelo usuário ou solicitante

### 6. No campo adicionado pelo passo anterior selecione o item Descrição detalhada no campo Nome:

Seleção do nome do campo da entrada de dados

### 7. Adicione um novo campo conforme a figura abaixo:

Inclusão de outro campo para entrada de dados

### Após finalizar todos os passos com sucesso teremos o seguinte resultado parcial do nosso fluxo:

Fluxo ao final da configuração

**Importante**: a entrada configurada nesta etapa será exibida na tela de criação de solicitações valendo a mesma regra para as telas de Portal e Workspace (aplicação Windows):

Resultado esperado no Portal para a configuração de Entrada de dados

## Configuração de Responsabilidades

A configuração de responsabilidade permite definir pessoas ou equipes que devem realizar atividades diversas no processo. A partir da configuração de responsabilidades a Máquina de Processos do Supravizio orquestrará o fluxo de trabalho entre estes indivíduos.

No BPMN a configuração de responsabilidades é realizada por uso de Papéis de Processos. No Supravizio podemos criar um papel da seguinte forma:

### 1. Selecione a tarefa Realizar compra, na janela de Propriedades acesse as opções do campo Responsável e neste campo selecione o item <Novo...>:

Especificar novo tipo de responsável para tarefas

### Observação: o cadastro de papéis também poderá ser realizado através do botão Papéis:

Acesso ao cadastro de Papéis

### Para adicionar um novo papel através desta tela, clique em Novo:

Inclusão de novo papel

### 2. Configure o novo papel com o seguinte conteúdo:

### 2.1. Configure o Nome do papel e o Tipo:

### Novo Papel

### 2.2. Configure a referência (documentação):

### Adicionando Referência ao novo Papel

### 2.3. Configure os Grupos Relacionados:

Relação de grupos que define a regra de recuperação de solucionadores

### 2.4. Configure o Critério de Seleção:

Novo Papel

### 3. Retorne ao Editor de Processos, selecione a tarefa Realizar Compra do processo, visualize a janela de Propriedades e acesse as opções do campo Papel responsável:

Adicionar o papel no processo

No combobox da figura anterior selecione o item **Comprador com menor carga**.

### 4. Retorne ao diagrama do subprocesso e selecione o iniciador e em seguida acesse a janela de Propriedades:

Configuração do responsável inicial

Finalizada a configuração do fluxo partiremos para a próxima etapa que é a [ativação do processo](ativando_processo).

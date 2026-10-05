# Criar um Macroprocesso

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 10: Macroprocessos e Tipos de solicitação > Criar um Macroprocesso

### Crie um Macro-processo seguindo os seguintes passos:

### 1. No Editor de Processos selecione a janela Process Explorer e selecione no topo da janela o botão Novo Macroprocesso:

No topo do Process Explorer é possível visualizar o cadastro de Macroprocessos Tecnologia da Informação:

Selecionando o botão Novo Macro Processo

Macroprocesso

Será aberta então a janela Novo Macroprocesso, em "Dados principais" preencha como na figura abaixo:

Novo Macro Processo

### 2. Adicionar os Grupos de Trabalho que poderão abrir novas Ordens de Serviço dos processos deste Macroprocesso.

É necessário determinar quais Grupos de Trabalho poderão realizar a abertura de novas Ordens de Serviço definidos no Macroprocesso. Para isso, no próprio cadastro do Macroprocesso, selecione a aba "Grupos envolvidos". Clique em "Novo" para inserir um Grupo de Trabalho envolvido. É importante ressaltar que na inclusão de um Grupo de Trabalho (como no exemplo abaixo, Gerência Administrativa) implica na permissão de abertura de novas Ordens de Serviço aos Grupos de Trabalho de subníveis (nível inferior ao do informado):

Adicionar Grupo Envolvido

### 3. Clique em Confirmar e Fechar para salvar as alterações:

### Gerenciando Macro Processos

A descrição para clientes é apresentada no ato de abertura de Ordens de Serviço no Portal.

Caso o usuário seja um administrador, aparecerá ao lado os botões para inclusão, edição e remoção de macro-processos.

É possível mover um Processos de um macro-processo para outro selecionando a opção **Mover para...**:

Movendo Processos entre Macro Processos

Obs: Após mover um processo é necessário salvar para que as modificações tenham efeito.

### 4. Vamos agora criar o processo de Faturamento e um subprocesso Liberação de notas conforme o modelo para o macro-processo Administrativo:

### Obs: Acesse [Criar um Processo](criando_um_processo) e [Criar um Subprocesso](criar_um_sub-processo) para eventuais dúvidas.

### Modelo de Subprocesso Liberação de Notas

### Ativar nova versão

### 5. Escolha a Área proprietária do subprocessos para determinar sua exibição no Workspace. Acesse o cadastro do Subprocesso através do menu Processo | Processos | Tipos de Subprocessos:

### Determinando órgão proprietário do Subprocesso

### 6. Acesse o Supravizio Web com um usuário que pertença ao Grupo de Trabalho escolhido (Gerência Administrativa):

Login no Supravizio Windows

7. Acesse a tela Workspace, neste caso estamos usando a usuária maria.jose:

Workspace com o novo Subprocesso incluído

Desta forma só terão acesso aos Processos e poderão abrir Ordens de Serviço pessoas que pertençam aos grupos de trabalho em questão (no caso o Grupo de Trabalho Gerência Administrativa).

### 8. Acesse novamente o Supravizio Windows porém com o usuário joao.silva (pertence ao grupo de trabalho Gerência de TI) e acesse o Workspace novamente:

Workspace sem possibilidade de ver novo Subprocesso

Utilizando um usuário que não pertence ao grupo de trabalho em questão (gerência administrativa) não é possível visualizar o Subprocesso de Faturamento.

Consulte o tópico para saber mais sobre os [Critérios para Abertura de Ordens de Serviço](criterios_para_abertura_de_ord).

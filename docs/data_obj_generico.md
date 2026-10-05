# Genérico

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Data Objects > Genérico

Este tipo de Data Object representa um documento modificado por um fluxo podendo servir apenas para documentação, ou criar um link podendo ser utilizado por exemplo como um elemento para auxiliar o solucionador a acessar outro sistema de informação.

Link criado

**Importante**: Vale ressaltar que esta funcionalidade de links está disponível apenas na versão Web do Supravizio.

Para adicionar um elemento deste tipo basta selecionar o item **Documento** no Toolbox e em seguida clicar sobre uma Tarefa, Evento Iniciador ou Evento Finalizador contido no diagrama.

Configuração de um Data Object Genérico

Após adicionar o item, será possível editar as seguintes propriedades:

### Estado

Inidica que houve mudança de estado no documento.

### Produzido ao término

Indica que o documento é uma saída de dados.

### Requerido inicial

Indica que o documento é uma entrada de dados.

### Texto

Descritivo a ser exibido para o usuário.

### Tipo de link

Indica se o Data Object será apenas um Documento, **Botão** ou **Hyperlink**.

Campos adicionais

Ao selecionar um destes dois itens, será habilitado o preenchimento de mais dois parâmetros:

### Link

Endereço da página destino do controle.

### Script

Permite gerar links e rótulos dinâmicos, como por exemplo, incluindo campos da Ordem de Serviço no link.

Para entender melhor o uso deste script, iremos citar um exemplo, redefinindo o rótulo do botão conforme um campo customizado preenchido anteriormente:

Script para redefinição de rótulo

Assim, ao entrar na tela da atividade, o botão terá a seguinte aparência:

Botão na Ordem de Serviço

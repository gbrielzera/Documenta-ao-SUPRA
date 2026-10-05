# Criar um Subprocesso

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 9: Manipulação de Arquivos Anexos > Criar um Subprocesso

### 1. Acessando o Editor de Processos

Acesse o Editor de Processos a partir do menu utilizando as opções **Processo | Processos | Editor de Processos**.

### 2. Criar uma nova versão de um Processo existente

A primeira tarefa é criar uma nova versão para o processo **Gerenciamento de Projetos**. Sempre que for necessário alterar ou criar um novo Subprocesso é recomendado que se inicie uma nova versão do Processo.

Para isso selecione a versão corrente do processo **Gerenciamento de Projetos** e clique com o botão direito do mouse para exibir o menu de opções.

Selecionando uma versão existente

Selecione no menu o item **Nova Versão:**

Criando uma nova versão para o Processo

3. Adicionando um novo Subprocesso

Selecione a nova versão e clique com o botão direito do mouse para acessar o menu de opções, o objetivo agora é adicionar o Subprocesso nesta nova versão:

Nova versão do Processo

No menu de opções selecione **Adicionar novo Subprocesso** conforme imagem abaixo.

Adicionando um novo Subprocesso

O objetivo deste novo Subprocesso é registrar a necessidade de um cliente, armazenando um arquivo na Ordem de Serviço. Então a configuração do Subprocesso será bem simples conforme podemos observar na figura abaixo.

Cadastro do novo Subprocesso

A descrição completa dos campos desta tela pode ser vistas no tópico [Criar um Subprocesso](criando_um_sub-processo) do tutorial [Construindo o Primeiro Processo](tutorial_01).

### 4. Editar o Processo

Na ferramenta gráfica do editor de processos desenhe um fluxo adicionando um evento inicial, uma tarefa e um evento final e depois relacione estes objetos.

Defina **Gerente de TI** como o responsável pela tarefa, conforme figura abaixo. Caso tenha dúvidas de como criar e editar um Subprocesso leia o [Tutorial 1: Construindo o primeiro Processo](tutorial_01):

Desenho de Subprocesso

### 5. Adicionar e Configurar um Item de Configuração

Para adicionar a entrada de um Arquivo é simples, basta selecionar o objeto da ToolBox chamado **Item de Configuração** e clicar sobre a tarefa:

Adicionando um Item de Configuração

Selecione o elemento **Item de Configuração** para acessar suas propriedades:

Selecionando o Item de Configuração

Na janela de propriedades acesse o editor de **Itens para Associação:**

Propriedades do Item de Configuração

No novo diálogo devemos configurar as regras para geração do arquivo. Neste ponto serão necessárias duas mudanças básicas:

1) Mude a propriedade** Produzido ao término** para True

2) Clique no botão de edição da coleção **Tipos/Super tipos para associação** e indique o tipo de documento que será anexado.

Lista de Classes de Configuração e suas propriedades

No diálogo de Tipos e super tipos para associação encontramos uma propriedade que define o Tipo de **Item de Configuração.** Assim como na figura abaixo informe o super tipo de **Item de Configuração** igual a **Artefato** e abaixo selecione o tipo **Especificação Técnica**.

Tipos e Super Tipos

Feche as janelas de configuração utilizando o botão **OK** e salve o Processo:

Botão Salvar

### 6. Ativar a Nova Versão

Para utilizarmos o Subprocesso criado, precisamos ativar a versão em edição, para isso acesse o menu de opções da nova versão clicando com o botão direito do mouse sobre a nova versão.

Process Explorer

Para ativar basta selecionar a opção **Ativar:**

Menu de opções, Ativar em destaque

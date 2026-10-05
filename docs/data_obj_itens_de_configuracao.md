# Itens de Configuração

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Data Objects > Itens de Configuração

Um Data Object do tipo Item de Configuração define uma regra de associação de um Item já existente (uma entrada) ou a geração de um novo Item de Configuração (saída).

Para adicionar um elemento deste tipo basta selecionar o item **Item de Configuração** no Toolbox e em seguida clicar sobre uma Tarefa, Evento Iniciador ou Evento Finalizador contido no diagrama. Após adicionar o item, há duas maneiras de inserir o item de configuração, manualmente e utilizando o assistente de configuração de associação de arquivo.

Para inserir manualmente um tipo de item para associação selecione a janela de propriedades e clique no botão que aciona o diálogo de configuração da coleção **Itens para Associação** (veja figura abaixo).

Como configurar regras de associação/geração de Itens de Configuração

Na janela de configuração de regras (veja a figura abaixo) clique no botão **Adicionar** para criar uma nova regra e depois utilize suas propriedades para finalizar a

configuração.

Configuração do Data Object de Itens de Configuração

Em **Tipos/Ação de configuração de usuário** relacionamos a relação de tipos de Itens de Configuração que devem ser associados ou gerados pelo Data Object. Para adicionar itens é necessário clicar no botão da propriedade e editor em um segundo diálogo a relação de Classes de Configuração. Veja a figura abaixo:

Relação de tipos de itens de configuração para associação

Para visualizar o comportamento do Assistente de Processos verifique o exemplo abaixo.

O atributo** Descrição** é utilizado para orientar o Solucionador na informação do item de configuração. Neste caso será exibido na aba de Itens de Configuração da Ordem de Serviço um botão com o mesmo rótulo configurado aqui. Veja a figura abaixo:

Resultado da configuração na tela de Ordem de Serviço

O atributo **Escopo por Serviços** indica para quais serviços esta regra terá validade. Neste exemplo a associação só será válida se o campo** Serviço** da Ordem de Serviço for preenchido como o valor **Software**.

Os parâmetros **Exibir itens automaticamente na procura do Portal** e **Permitir vários Itens na abertura do Portal** são aplicáveis quando o Data Object estiver associado a iniciadores e quando o fluxo estiver disponível para o usuário no Portal de Processos. O primeiro faz com que a janela de busca de itens liste automaticamente todas as opções assim que for exibida não exigindo que o usuário digite um critério de busca. Esta opção é interessante para tipos que possuem uma quantidade reduzida de itens e não é recomendada para grandes quantidades. O segundo permite que o usuário selecione no quarto passo da abertura mais de um Item de Configuração.

Os parâmetros **Produzido ao término** e **Requerido inicialização** dizem respeito a configuração como entrada ou saída da Tarefa ou Evento associado. Se **Produzido término** for verdadeiro então o item será uma saída e com isto será cadastrado um novo item de configuração ou um novo arquivo (dependendo do tipo de item). Se **Requerido inicialização** for verdadeiro então será necessário adicionar um item já existente considerado uma entrada na Tarefa ou Evento. Quando os dois forem falso então a regra será uma associação (entrada) não obrigatória.

Os exemplos adiante ilustrarão a utilização deste importante elemento do BPMN.

### Criando tipos de Arquivos

Para** inserir utilizando o assistente de configuração de associação arquivo**, clique com o botão direito no Data Object e selecione a opção "Configurar Associação de Arquivo":

Utilizar o configurador de associação de arquivo

Em seguida, na nova janela exibida selecione o tipo existente de arquivo que deseja usar ou caso seja necessário, selecione "Criar um novo Tipo de Arquivo" e especifique os dados do novo tipo:

Criação de novo tipo de arquivo através do assistente

Salve e atualize as informações do editor de processos. Veja que o novo tipo de arquivo já é automaticamente associado ao Data Object, também repare que o novo "Tipo de Arquivo" foi criado nos Tipos de Itens de Configuração (Ativos | Tipos de Itens de Configuração) como um Artefato, que foi criada uma situação inicial (Anexado) e que as configurações conferem com o definido no assistente:

Item de configuração definido

Dados Principais do novo Item de Configuração

Situações do novo Item de Configuração

Definições de transferência do novo Item de Configuração

### Exemplo 1: Associação de Itens de Configuração

Data Object Item de Configuração como entrada

A configuração de associação de Item de Configuração do subprocesso acima aparece no Assistente de Processos como um comando "Selecionar Desktop" visto na figura abaixo. Enquanto não for associado o item não é possível avançar no processo (botão "Avançar").

Comportamento do Assistente de Processos com a entrada de um Item de Configuração

Clicar em "Selecionar Desktop" é apresentado o diálogo de busca de itens de configuração do tipo Desktop. O usuário então informa um registro e com isto consegue avançar no processo:

Seleção de um Item de Configuração

### Exemplo 2: Geração de Itens de Configuração

Neste exemplo veremos um fluxo que gera um registro do tipo Item de Configuração (o item é uma saída da tarefa de processo):

Item de Configuração como saída de uma Tarefa

A opção de "geração" de item de Configuração foi configurada no Data Object Item de Configuração conforme a figura abaixo:

Configuração do item como saída

Quando executamos uma Ordem de Serviço referente ao fluxo acima é exibido um link "Cadastrar Software" no Assistente de Processos. Veja a figura abaixo:

Comportamento do Assistente de Processos para geração de um Item de Configuração

Ao clicar no link "Cadastrar Software" é exibido o diálogo de novo Software para inclusão do novo registro:

Tela de cadastro do novo Item de Configuração

### Exemplo 3: Anexar um arquivo em uma tarefa de processo

Arquivos podem ser anexados em Ordens de Serviço da mesma forma que criamos Itens de Configuração (veja exemplo anterior). A única diferença está na configuração da regra de geração que deve conter uma Tipo de Configuração (tipo de Item de Configuração) do tipo Artefato configurado como arquivo. Veja na sequência de telas abaixo como é feita esta configuração:

Primeiro passo para criação de uma Tipo de Configuração

Configuração do tipo de Artefato como um arquivo

Configuração do Data Object que será responsável por gerar o arquivo anexo

### Exemplo 4: Cadastrar um artigo de Base de Conhecimento

Também podemos realizar a configuração de um Data Object para que o mesmo seja utilizado para a criação de um novo artigo na Base de Conhecimento.

A seguir, iremos ilustrar um modelo de Processo utilizado para realizar o cadastro:

Exemplo de configuração para cadastro

Ao realizar a abertura de uma Ordem de Serviço deste Subprocesso, haverá a possibilidade de realizar o cadastro diretamente:

Link para a página de cadastro

Ao clicar no texto, haverá um redirecionamento para a página de cadastro do artigo na Base de Conhecimento:

Página para inclusão do artigo

**Observação**: Também podemos ao final do processo, inserir uma etapa para que seja inserido um aviso aos solucionadores sobre o cadastro do novo artigo:

Tarefa de divulgação do artigo

**Processo: Criação de Artigos para a Base de Conhecimento**

**Evento: Script Início**

```
#Carrega os Grupos de Trabalho e insere em uma lista
grupos = ArrayList()
grupos.Add(GrupoTrabalho.Carrega("Descricao","Gerência de TI"))
grupos.Add(GrupoTrabalho.Carrega("Descricao","Infraestrutura"))
#Gera um aviso no mural do solucionador
conhecimento = OrdemServico.ObtemConhecimento()
OrdemServico.GeraAvisoMural("Novo Artigo Cadastrado: " + conhecimento.Titulo, GrupoTrabalho.Carrega("Descricao","Gerência de TI"), grupos, True, True, DateTime.Now, DateTime.Now.AddDays(1), String.Empty, conhecimento)
AvancaProximaAtividade = True
```

Sendo assim, quando uma Ordem de Serviço iniciar esta atividade, será criado um novo aviso no Mural, conforme a imagem abaixo:

Mensagem publicada no mural

Para mais informações sobre o Mural de Avisos, visite o tópico [Publicando um aviso no Mural](publicando_um_aviso_no_mural).

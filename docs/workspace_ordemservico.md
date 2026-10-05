# Workspace  > Workspace Ordens de Serviço

Caminho: Guia para Solucionadores > Workspace  > Workspace Ordens de Serviço

O modo de visualização Ordens de Serviço permite que o usuário solucionador gerencie suas ocorrências de processo e também de seus solucionadores subordinados. Na figura abaixo podemos observar o layout comentado deste modo do Workspace:

Layout comentado do modo Ordens de Serviço

Para mais detalhes sobre as diversas opções de filtro veja [Filtro avançado de Ordens de Serviço](acessar_ordemservico). Para mais informações sobre Filas na Estrutura do Grupo de Trabalho do usuário conectado acesse [Obtendo Ordens de Serviço a partir de filas compartilhadas](cadastrar_usuario_2_2_2_2).

No grid de Ordens de Serviço da tela acima existe um menu de contexto que pode ser acionado com o clique com o botão direito do mouse. Veja na figura abaixo o conteúdo deste menu:

Menu de contexto com comandos adicionais

Observe na figura acima o comando **Visualizar** que permite acessar o diálogo de edição da Ordem de Serviço selecionada. O mesmo diálogo pode ser acessado com um duplo clique na Ordem de Serviço.

Visualização da Ordem de Serviço

Outra forma de acesso a uma Ordem de Serviço é por meio do campo texto localizado na barra de ferramentas do Workspace. Neste campo digite o número da Ordem de Serviço e depois clique no botão conforme a figura abaixo:

Retornando nossa atenção para a relação de Ordens de Serviço do Workspace podemos observar que um dos registros é apresentado em negrito e ícone . Isto significa que o responsável atual ainda não fez a leitura (visualizou a Ordem de Serviço pelo diálogo acima).

Ordem de Serviço não lida pelo responsável corrente

## Abertura de Ordens de Serviço

A abertura de Ordens de Serviço pode ser feita por meio do botão **Nova** localizado na barra de ferramentas da janela Workspace. Quando clicamos no botão **Nova** é exibido um menu com todos os **processos** cadastrados e ao selecionar um destes processos é exibido um segundo menu com os **subprocessos** disponíveis. Observe na figura abaixo que ao selecionarmos o processo **Incidente** é exibidas apenas a opção **Incidente**. Selecionando **Incidente**, por exemplo, é exibido o diálogo de edição de Ordem de Serviço onde podemos preencher os dados requeridos para abertura e iniciar o atendimento da solicitação.

Abertura de uma Ordem de Serviço de Incidente

Ao selecionar a opção Guarda de documentos é apresentada a tela de Ordem de Serviço:

Abertura de uma Ordem de Serviço

Para informar o assunto basta selecionar o campo de mesmo nome e digitar um texto sucinto sobre a Ordem de Serviço. Para informação do **Cliente** e clique em Selecionar para exibição do diálogo de procura de clientes. Confira esta operação observando a figura abaixo:

Seleção de Cliente para a nova Ordem de Serviço

Ao clicar no botão de procura é apresentado o diálogo abaixo onde devemos selecionar um cliente para a Ordem de Serviço.

Seleção do Cliente da Ordem de Serviço

Após informar o Cliente, o Assunto e o Serviço (este último pode ser preenchido automaticamente dependendo de configuração do processo) clique no botão Salvar e será exibido o número da nova Ordem de Serviço:

Nova Ordem de Serviço

Na figura acima podemos observar que após salvar a Ordem de Serviço foram exibidos campos referentes a regras configuradas no iniciador do processo. Estas regras podem ser visualizadas graficamente no painel localizado no canto inferior direito.

A classificação inicial de processo (campo Subprocesso) pode ser modificada a qualquer momento utilizando a função de Classificação disponível na tela de Ordem de Serviço e na barra de ferramentas do Workspace Ordens de Serviço. Veja [Classificação de Ordens de Serviço](classificacao_os) para mais detalhes. A gestão da reclassificação pode ser realizada com uso do relatório [Reclassificação de Ordens de Serviço](reclassificacao_ordens_servico).

Uma outra forma de criação de Ordens de Serviço no Workspace é por meio do botão **Clonar nova** disponível no menu de contexto do grid de Ordens de Serviço. Este comando gera uma nova Ordem de Serviço a partir de uma existente copiando todos os campos existentes.

Clonar uma Ordem de Serviço

Para mais detalhes sobre clonagem de Ordens de Serviço veja [Clonar uma Ordem de Serviço](clonar_ordem_servico).

## Anexando arquivos utilizando o recurso "arrastar e soltar"

A tela Workspace permite anexar um arquivo em uma Ordem de Serviço utilizando arraste de arquivos a partir do Windows Explorer.

Na figura abaixo podemos observar o arraste de um arquivo texto:

Arquivo arrastado a partir do Windows Explorer

Após soltar o arquivo sobre uma Ordem de Serviço é apresentado um diálogo onde o usuário deve informar o tipo de arquivo:

Informação do tipo de arquivo que será anexado

Se existir na atividade corrente alguma regra de anexação de arquivo então esta configuração é utilizada para pré-selecionar o campo** Tipo novo Item** do diálogo acima.

## Anexando links para páginas web

A tela de Edição de Ordens de Serviço também possibilita o anexo de links externos para páginas web.

Para isso, é necessário que na configuração do Tipo de Item de Configuração, esta opção esteja habilitada, conforme a imagem a seguir:

Aba Artefatos no cadastro de Tipo de Configuração

Ao abrir uma Ordem de Serviço e clicar na opção para anexar o arquivo, será disponibilizado um campo que permite o preenchimento do endereço:

Anexo de Arquivo

Anexado o arquivo, haverá um link para acesso a respectiva página na tela da Ordem de Serviço.

Tela de Edição de Ordem de Serviço

## Adicionando comentários em Ordens de Serviço

Repare na figura abaixo que podemos adicionar comentários em Ordens de Serviço. Estes comentários são exibidos na tela de Ordem de Serviço no canto inferior direito:

Registro de comentários

Com um clique com o botão direito do mouse sobre o grid de comentários podemos acessar um menu de contexto onde encontraremos um comando para publicação do comentário no Portal. Veja a figura abaixo:

Publicação de comentários no Portal

Após selecionar a opção Publicar comentário no Portal de Processos e salvar a Ordem de Serviço podemos visualizar o mesmo na página de consultas aplicação web destinada ao cliente.

Visualização de comentários no Portal

Utilizando a listagem de Ordens de Serviço do Workspace podemos adicionar um comentário em várias Ordens de Serviço. Para isto selecione vários registros no grid, clique com o botão direito do mouse e no menu de contexto selecione a opção

Adicionar comentário em várias Ordens de Serviço

Após selecionar o comando de adicionar comentários é exibido um diálogo onde podemos informar um texto e selecionar a publicação no Portal de Processos.

Novo comentário publicado no Portal

## Restrição de quantidade de Ordens de Serviço para consulta

Este recurso permite limitar a quantidade de Ordens de Serviço recuperadas em resposta ao critério de filtro selecionado na interface do Workspace. Este recurso é necessário pois a seleção de um filtro muito abrangente pode resultar na recuperação de uma quantidade muito grande de registros prejudicando o trabalho dos demais usuários e provocando lentidão no sistema.

A quantidade máxima de registros é definida na tela de Configurações do Supravizio que está acessível pelo menu **Utilitários | Configurações**.

Ao acessar a tela de Configurações, selecione a aba Processo. Após, basta informar a quantidade máxima de Ordens de Serviço que serão recuperadas no Workspace de acordo com a imagem abaixo:

Configuração da quantidade máxima para recuperação

Se a quantidade de Ordens de Serviço correspondente ao filtro do Workspace for maior que o limite cadastrado na tela de Configurações, serão listados apenas a quantidade de registros definida na tela de Configurações.

Diálogo de confirmação de limitação

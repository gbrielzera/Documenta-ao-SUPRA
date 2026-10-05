# Criando processos

Caminho: Guia para Administradores > Inventário de Hardware e Software > Criando processos

Neste tutorial vamos criar um processo contendo subprocessos específicos para tratamento de eventos relacionados a integração com Inventariado de Hardware e Software.

Recomendável o estudo prévio do capítulo [Configuração de Processos](editor_de_processo) e seus tutoriais antes da execução deste tutorial.

Inicialmente vamos criar um Processo chamado "Gerenciamento de Configuração". Para isso, vá em Processo | Processos | Editor de Processos. No Editor de Processo, na aba "Process Explorer" clique no comando para criação de um novo Processo:

No formulário de cadastro do novo processo preencha as seguintes informações:

Clique em Confirmar e Fechar.

Após isso vamos criar 1 novo subprocesso que criará Ordens de Serviço para a retirada de memória em uma estação de trabalho.

## Retirada de Componentes

Selecione a versão em edição do processo Gerenciamento de Configuração e clique em "Adicionar novo Subprocesso":

Preencha o cadastro do novo Tipo de Subprocesso com as seguintes informações:

Na aba "Serviços disponíveis (se existir restrição)" selecione o serviço adequado para este processo. Para este tutorial vamos utilizar o serviço Estação de Trabalho. Mantendo apenas um Serviço disponível em um subprocesso este é assumido automaticamente em aberturas de Ordens de Serviço automáticas (Mais informações leia [Eventos Iniciadores](bpmn_iniciadores)).

Após confirmar o cadastro do Tipo de Subprocesso selecione no Toolbox o elemento "Evento Inicial por Mensagem" clicando no diagrama em seguida. Mude a propriedade Tipo de mensagem para "Importação Hardware e Software":

Na propriedade NomeEventoOCS é possível determinar qual evento será tratado por este iniciador. Nosso exemplo tratará inicialmente redução de memória:

Inclua em seguida um elemento intermediário por mensagem clicando no Toolbox e em seguida no diagrama. Ligue o iniciador por mensagem no novo elemento. Este novo elemento permitirá que o analista de infra seja notificado:

Mais informações sobre a criação de comunicados em processos leia o [Tutorial 12: Envio de Comunicados](envio_de_comunicados).

Da mesma forma que criamos um iniciador para a redução de memória, podemos também inserir um iniciador para cada caso que for necessário.

Ao ser reduzida a memória, o Supravizio abrirá automaticamente uma nova Ordem de Serviço para tratamento do evento:

## Instalação de Software em Blacklist

Vamos neste subprocesso criar um fluxo para tratamento de softwares em Blacklist. Uma Blacklist contem softwares que não são permitidos em uma determinada rede, tanto por questões de segurança quanto por políticas internas da própria empresa. Um software em Blacklist pode ser determinado no Supravizio a partir do seu Tipo de Item de Configuração. Vamos criar um novo Tipo de Item de Configuração chamado "Software em Blacklist".

Acesse no menu principal Ativos | Tipos de Itens de Configuração. Na barra de ferramentas clique em Novo e preencha o novo tipo de item com as seguintes informações:

Na aba Situações crie a seguinte Situação:

Confirme a criação da Situação "Bloqueado" e clique em Salvar.

Repare no cadastro do tipo de item, na aba Dados principais que marcamos a opção "Incluir itens em uma Blacklist":

Após criado o novo tipo de item, vamos agora no cadastro de Softwares e listar todos os softwares que são do tipo cadastrado na rotina de importação (em nosso exemplo, o nome do tipo é "Licença de Software"). No campo de procura digite o nome do tipo de item:

Reparem que na listagem encontram-se aplicativos comumente não autorizados em uma rede empresarial. Veja por exemplo o software "Call of Duty: Black Ops". Para os conhecedores de jogos ele é um clássico dos jogos de tiro. Não gostaria que seus colaboradores utilizassem este tipo de aplicativo, correto? Então vamos mudar o tipo de item deste software para o tipo Software em Blacklist. Dê um duplo clique no cadastro e mude a propriedade Tipo de Item de Configuração:

Vamos agora construir um fluxo para o tratamento de detecção de novas instalações de aplicativos deste tipo. No processo Gerenciamento de Configuração clique em "Adicionar novo Subprocesso":

Preencha o cadastro do novo Tipo de Subprocesso com as seguintes informações:

Na aba "Serviços disponíveis (se existir restrição)" selecione o serviço adequado para este processo. Para este tutorial vamos utilizar o serviço Estação de Trabalho. Mantendo apenas um Serviço disponível em um subprocesso este é assumido automaticamente em aberturas de Ordens de Serviço automáticas (Mais informações leia [Eventos Iniciadores](bpmn_iniciadores)).

Criado o novo Tipo de Subprocesso, selecione no Toolbox o Evento Inicial por Mensagem e cole no diagrama. Modifique as propriedades Tipo de Mensagem para "Importação Hardware e Software" e NomeEventoOCS para "Nova instalação de software em Blacklist":

Como no exemplo anterior, crie um Evento Intermediário por Mensagem com o modelo de comunicado adequado e uma atividade para o responsável pela averiguação da instalação conforme fluxo abaixo:

Caso uma nova instalação de um software em Blacklist seja identificada, durante a importação será aberta uma nova OS para tratamento:

**Importante**: O controle de Blacklist de software é realizado através do nome deste. Portanto, caso seja identificado um novo software com o mesmo nome e em nova versão, ele será classificado automaticamente.

Observe no exemplo acima, que foi necessário um procedimento de checagem na listagem de Softwares no sistema para uma reclassificação de Tipo de Item de Configuração (de Licença de Software para Software em Blacklist). Aqui poderíamos utilizar um outro processo para tratamento de novos softwares instalados utilizando o mesmo elemento Evento Inicial por Mensagem com as configurações abaixo:

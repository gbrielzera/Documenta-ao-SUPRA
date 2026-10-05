# Iniciador por Mensagem

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Eventos Iniciadores > Iniciador por Mensagem

Um iniciador por mensagem permite que sejam abertas novas Ordens de Serviço através de envio de emails ou realizando uma chamada à webservice.

Iniciador por mensagem

### Realizando abertura automática de Ordens de Serviço através de emails

Para realizar uma abertura por email, por exemplo, clique no símbolo do Evento Inicial por Mensagem na barra de ferramentas clicando no desenho do processo e em seguida clique com o botão direito no iniciador selecionando a opção "Propriedades". Após isso, no grupo de propriedades "Mensagem geradora", indique a opção "Email" na propriedade "Tipo de mensagem":

Configurando tipo de mensagem

Após isso, selecione uma caixa de email (que será monitorado pela Máquina de Processos) onde serão recebidos os emails deste tipo solicitação. O cadastro de caixas de mensagens se encontra em Processo | Processos | Caixas de Mensagem. Para cadastrar uma caixa de mensagem você deve preencher informações básicas sobre a conta:

Cadastro de Caixa de email

Para o caso de solicitações abertas através de iniciadores por mensagem baseados em emails, o cliente da Ordem de Serviço é uma pessoa do cadastro de Pessoas que possua o mesmo email do remetente do email coletado pela Máquina de Processos no instante em que estiver processando os emails:

**Edição de Email no cadastro de Pessoas**

O assunto da nova Ordem de Serviço é exatamente o assunto do email. O corpo do email passa a ser a descrição detalhada da Ordem de Serviço:

**Envio de Email para abertura de OS**

Uma outra informação de extrema importância é em relação à determinação automática do Serviço da Ordem de Serviço pela Máquina de Processo no instante da abertura. Para determinarmos um serviço específico para um subprocesso, podemos incluir na lista de restrição de serviços do tipo de subprocesso associado ao fluxo:

Associação de Serviço para tipo de subprocesso

Caso o tipo de subprocesso associado ao fluxo do iniciador por mensagem possua um único serviço restrito (Serviços disponíveis) então automaticamente este serviço é associado à Ordem de Serviço durante a sua abertura pela Máquina de Processos.

Caso queira determinar o serviço via script IronPython, basta modificar a propriedade "Serviço inicial" do iniciador por mensagens:

Definição de Serviço por Script

Após processar a caixa de mensagens indicada no iniciador por mensagens, a Máquina de Processos exclui os emails que foram processados originaram novas Ordens de Serviço.

### Realizando abertura automática de Ordens de Serviço através de webservice

Uma outra forma de realizar a abertura de Ordens de Serviço através do evento inicial por mensagens é através de webservice. Esta é uma boa opção para integrar o Supravizio com outros sistemas para que estes realizem aberturas de Ordens de Serviço, por exemplo, ao ser diagnosticado um incidente.

A solução Supravizio disponibiliza o Supravizio Service Bus como mecanismo webservice para realizar esta tarefa. Para efetuar uma chamada a webservice para abertura e processamento de Ordens de Serviço acesse [http://[nome_do_host]/SupravizioWeb/ServiceBus/Processo/Processo.asmx.](http://%5Bnome_do_host%5D/SupravizioWeb/ServiceBus/Processo/Processo.asmx.) Este webservice dispõe do método** ProcessaMensagem**. Os parâmetros deste método são:

WebService

No parâmetro **dominio** indicamos o domínio dos processos de interesse. Para obter esta informação acesse Utilitários | Domínios.

No parâmetro** username** e **password** indicamos o usuário de contexto que efetuará conexão no serviço SV Service Services (Servidor de Aplicações do Supravizio).

ATENÇÃO: A conexão do usuário é contabilizada como um acesso concorrente no controle de licenças, caso o limite de usuários concorrentes tenha sido atingido a sessão mais antiga será finalizada para ser substituída pela do webservice no momento e o seguinte erro é registrado no log de erros:

Mensagem de Log de Erros

No parâmetro **nomeMensagem** indicamos os eventos iniciadores e intermediários por mensagens do tipo webservices que possuem a propriedade Nome da Mensagem respectiva:

Configuração do iniciador por WebService

É possível fornecer parâmetros para a realização da abertura da Ordem de Serviço fornecendo um XML na propriedade conteudoXML, submetendo um XML com a seguinte estrutura:

<MENSAGEM>

<PARAMETROS>

<PARAMETRO>

<NOME>Parametro1</NOME>

<VALOR>Valor do parâmetro 1</VALOR>

</PARAMETRO>

<PARAMETRO>

<NOME>Parametro2</NOME>

<VALOR>Valor do parâmetro 2</VALOR>

</PARAMETRO>

</PARAMETROS>

</MENSAGEM>

Você poderá incluir quantos parâmetros forem necessários para realizar a sua solicitação. Ao realizar a abertura, podemos recuperar estes parâmetros no Script Evento do iniciador por mensagem por webservices, atraves do objeto** Parametros** (que é um hashtable):

Script para recuperação de Parâmetros

Da mesma forma que o evento iniciador por email, para determinarmos um serviço para a nova Ordem de Serviço aberta através da chamada ao método ProcessaMensagem via webservices, podemos incluir no tipo de subprocesso relacionado com o iniciador um único Serviço disponível ou determinarmos o serviço no Script Evento do iniciador.

Script para associação de serviço

Existem também, algumas palavras reservadas que são os parâmetros responsáveis para definir alguns dados sobre a Ordem de Serviço que será aberta. São elas:

- ASSUNTO = Assunto da OS
- CLIENTE = Cliente da OS (Usuário de rede da pessoa)

Para fazer uso delas, ao lado direito do editor de script, há uma paleta que contém todos os parâmetros que poderão ser manipulados. É possível expandir e visualizar os parâmetros clicando no botão (+). Para facilitar a edição do script, pode-se utilizar o duplo-clique no parâmetro desejado, e o mesmo será incluído no editor, no local onde se localiza o cursor.

Pode-se utilizar os parâmetros acima como no exemplo:

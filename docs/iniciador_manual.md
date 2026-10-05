# Iniciador manual

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Eventos Iniciadores > Iniciador manual

Este evento representa o início de um fluxo a partir de uma ação manual que pode ser uma solicitação realizada através do Portal de Processos ou uma nova Ordem de Serviço criada a partir do Workspace. Na sequência de figuras abaixo podemos observar as diversas possibilidades de disponibilização destes iniciadores:

| Iniciador manual disponível apenas na tela Workspace | Iniciador manual disponível apenas no Portal de Processos | Iniciador manual disponível na tela Workspace e também na aplicação web de Portal de Processos |
|---|---|---|

Na figura abaixo podemos notar a disponibilidade de iniciadores manuais na função de abertura de Ordem de Serviços do Workspace.

Comportamento do Workspace para fluxos com iniciadores manuais

Outra forma de iniciar manualmente um subprocesso é por meio do Portal. Neste portal são exibidos no segundo passo da abertura de Ordens de Serviço todos subprocessos que possuem um iniciador manual que possua a propriedade **Visibilidade em aplicações** igual a **Todas as aplicações** ou **Somente Portal de Processos**. Veja a figura abaixo:

**Importante: o produto permite a criação de Macroprocessos e também permite a classificação dos subprocessos em Tipos de Solicitações. Quando utilizamos estes recursos a funcionalidade de abertura do Portal ganha um quinto passo e as opções apresentadas na figura abaixo passam a compor o terceiro passo.**

Comportamento do iniciador manual no Portal

Observação: Quando um iniciador está disponível somente no Workspace o Campo Cliente é preenchido automaticamente com o usuário conectado na aplicação. Para modificar este comportamento desative a opção "Preencher cliente com solucionador".

Assim como os demais iniciadores disponíveis no Supravizio, podemos configurar neste elemento características de entrada de dados, tais como campos da Ordem de Serviço que devem ser preenchidos, Itens de configuração que precisam ser anexados etc. Esta configuração é realizada por uso dos Data Objects que no Supravizio são representados pelas especializações Entrada de dados, Aprovações e Itens de Configuração. Veja o exemplo abaixo de uma entrada de dados e o comportamento do sistema na abertura de uma Ordem de Serviço pelo Portal e pelo Workspace:

Configuração de Entrada de dados para o iniciador

Na tela abaixo podemos verificar o resultado final desta configuração. Repare que os campos configurados no editor são apresentados como um formulário no assistente de processos. Repare também que o rótulo vermelho indica que o preenchimento é obrigatório e até o momento não foi concluído. Desta forma, se o usuário tentar iniciar o processo (clique no botão **Iniciar**) ele não consiguirá, pois existe a pendência de preenchimento.

Comportamento da configuração de Entrada de Dados no Workspace

Na figura abaixo podemos observar que a mesma entrada configurada para a tela Workspace está presente também no Portal de Processos. Repare que no último passo de abertura são apresentados os campos configurados no iniciador manual e que são aplicadas também todas as regras de preenchimento obrigatório conforme a tela anterior.

Comportamento da configuração de Entrada de Dados no Portal

### Responsabilidades e autorizações do iniciador manual

A configuração de responsabilidade para o iniciador manual pode ser utilizada para definição do responsável inicial pela Ordem de Serviço e também restringir a permissão de abertura utilizando regras de autorização. Veja na figura abaixo as propriedades relacionadas com este assunto:

Responsabilidade e autorizações do iniciador manual

O parâmetro **Clientes Autorizados** é uma relação de papéis de processos que definem as pessoas autorizadas a gerar uma solicitação pelo iniciador. Esta configuração é aplicada ao site de Portal filtrando os iniciadores onde o usuário conectado está autorizado. Se, por exemplo, um analista de RH entrar no site de Portal ele não visualizará o iniciador do fluxo acima, pois este está acessível somente para o Presidente.

A autorização também é validada tela Workspace, onde é feita a restrição para preenchimento do campo Cliente. Veja na figura abaixo a ilustração da abertura do processo configurado anteriormente. Repare que é exibida uma mensagem de informação no diálogo de busca e também não é possível selecionar outra pessoa que não atenda o papel.

Abertura de uma Ordem de Serviço com regra de autorização por cliente

O parâmetro **Permissão restrita Papel responsável** deve ser utilizado em conjunto com a propriedade **Responsável** para definir regras de autorização para solucionadores que acessam a tela Workspace. Na figura abaixo, por exemplo, existe um iniciador disponível somente para solucionadores que atendam ao papel **Gerente de TI**.

Configuração de um fluxo com um iniciador com regra de autorização por solucionador

Considerando o processo acima, quando um usuário que possui o papel Gerente de TI aciona o comando de nova Ordem de Serviço é apresentado um diálogo onde ele seleciona a forma de início mais adequada. Veja a figura abaixo:

Responsabilidade e autorizações no Workspace

No exemplo acima para qualquer outro usuário a simples seleção do comando **Nova | Incidente | Incidente** no Workspace já iniciará o incidente pelo único Evento iniciador que não possui a configuração de autorização.

Fluxo

# Envio de Mensagens em Processo

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 11: Envio de Comunicados > Envio de Mensagens em Processo

Um Evento Intermediário baseado em Mensagem realiza o encaminhado automaticamente de uma mensagem a um ou mais destinatários.

### Criando um fluxo conforme a figura abaixo

No nosso exemplo vamos trabalhar um fluxo de Incidentes assim descrito: primeiramente é iniciado pelo Service Desk, no instante em que ele avança o especialista deve preencher o campo com Descrição da falha (Detalhes da configuração abaixo) e ao avançar é encaminhada uma mensagem para o suporte e o Especialista aguarda resposta deste:

Fluxo

### 1. Criar um campo customizado para descrever uma falha:

No data object entrada de dados da atividade selecionar nome "Customizado" e em campo customizado "Novo":

Incluir Campo Customizado

Adicione um campo customizado, Descrever Falha, conforme especificado na figura abaixo, não esqueça de preencher os campos em destaque :

Novo campo customizado

### 2. Inclua o campo na entrada de dados:

Novo campo na entrada de dados

### 3. Adicione um evento intermediário de mensagem e o configure conforme a figura abaixo:

Evento intermediário

No campo "Tipo do arquivo retornado" indicamos o Tipo de Item que será criado dado o(s) arquivo(s) que será(ão) retornado(s) do e-mail de resposta. O campo "Tipos de arquivos anexados" indicamos quais os Tipos de Itens de arquivos da Ordem de Serviço poderão ser anexados na mensagem que será enviada. O campo "Finalizar interrupção de ANS em resposta" faz com que a interrupção de ANS que esteja acionada (caso exista) na Ordem de Serviço seja finalizada.

No campo Destinatário podemos selecionar um Papel de Processo para determinarmos o(s) destinatário(s). Em situações onde for necessário incluir mais de um destinatário podemos fazer o uso de papéis compostos. Exemplo: para enviar email para o cliente e seu gerente poderíamos usar um papel "Cliente e Gerente do Cliente" cujo cadastro possui a aba de papéis para composição preenchida com os papéis "Cliente" e "Gerente do Cliente". No campo Listagem de destinatários podemos determinar de forma fixar a lista de destinatários da mensagem. A lista final de destinatários é composta pelos emails das pessoas retornadas pelo papel (propriedade não obrigatória) mais a lista de emails constantes da propriedade **Listagem de destinatários**.

**Importante: as pessoas recuperadas por meio de papéis são incluidas na lista de destinatários se, e somente se, possuirem o campo email cadastradado.**

No campo Modelo de comunicado indicamos qual Modelo de Comunicado será adotado para a geração da mensagem. Crie um novo modelo de comunicado.

Novo Modelo de Comunicado

Para este exemplo utilizamos o seguinte modelo de comunicado, para mais informações de como criar modelos de comunicados acesse o tópico [Modelos de Comunicados](modelos_de_comunicados):

Modelo de comunicados

### 4. Abrir uma Ordem de Serviço e avançar no processo

Ative o processo criado e, usando a tela Workspace, abra uma nova Ordem de Serviço do subprocesso em questão. Nesta nova Ordem de Serviço avance no processo até que o Especialista seja interrogado se "A falha foi resolvida em definitivo", respondendo não, sendo o Serviço como Banco de Dados, avançará para a atividade "Descrever falha" onde o Especialista vai detalhar a falha. Observe no modelo de comunicado acima que indicamos a descrição da falha através do campo customizado INC_DESC_FALHA.

Ordem de Serviço

### 5. Após descrever a falha avance no processo

Avançando no processo, é enviada uma mensagem para os destinatários (neste exemplo utilizamos Listagem de destinatários, mas poderia ser um papel de processo). Para visualizar a mensagem acesse a aba de comunicados da tela de edição de Ordem de Serviço ou clique com botão direito no ícone de comunicado do fluxo e selecione o comunicado desejado.

Visualização do comunicado pelo fluxograma

Mensagem encaminhada

Após enviar o comunicado, ao listar as Ordens de Serviço no Workspace, haverá um novo ícone apontando que foi enviado um comunicado nesta OS.

Para mais informações sobre estes indicadores, visite o tópico [Acompanhando respostas de Comunicados](indicadores_comunicado).

### Temporalidade

A temporalidade é um prazo em dias de permanência da mensagem no banco de dados. Ao terminar o prazo da temporalidade a mensagem será removida automaticamente.

O seu uso é indicado para redução de uso de espaço em disco após um período no qual a sua manutenção já não é mais necessária. Exemplo: após 6 meses de envio já não seria mais necessário manter no banco uma mensagem solicitando aprovação de uma Ordem de Serviço ou avisando algum solucionador sobre a chegada de uma Ordem de Serviço em sua fila.

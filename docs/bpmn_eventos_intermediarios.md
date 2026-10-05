# Eventos Intermediários

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Eventos Intermediários

Os Eventos intermediários, ao contrário dos eventos iniciadores e finalizadores, são executados entre as atividades de um determinado fluxo de processo. Os eventos intermediários contemplados no Supravizio são:

## Evento Intermediário por Regra

Um **Evento Intermediário por Regra** é executado sempre que uma fórmula de critério estabelecida indique uma condição verdadeira. Para utilizar este objeto no Editor de Processos basta clicar no objeto "**Evento Intermediário por Regra**" no Toolbox e, caso seja um evento associado a uma atividade, clicar na atividade. Caso seja um evento não associado a uma atividade, basta clicar no objeto no Toolbox e depois clicar em qualquer região do desenho.

Evento intermediário baseado em regra

O **Evento Intermediário por Regra** tem as mesmas características do **Evento Iniciador por Regra**, porém, é "disparado" no meio de um processo, ao contrário de seu similar iniciador, que é disparado apenas no início de um processo.

Assim também como o [Iniciador por Regra](bpmn_iniciadores), o evento Intermediário por Regra é acionado sempre que o job de "Máquina de Processos" for executado.

Existem basicamente duas formas de se utilizar este tipo de evento. Uma das formas é adicioná-lo ao fluxo do processo como fazemos com uma atividade simples:

Evento intermediário como restrição no fluxo

Observe no exemplo acima que existe um evento intermediário baseado em regra "Aguardando entrada em estoque" e este possui a seguinte condição:

Configuração de uma regra utilizando comando SQL

O fluxo do processo só prosseguirá caso a regra estabelecida indicar uma condição verdadeira (após uma execução do job "Máquina de Processos"). Caso contrário, se um solucionador tente avançar em uma ordem de serviço deste processo, será exibida uma mensagem:

Mensagem de erro

A outra forma de utilização deste tipo de evento (e mais comum) é associá-lo a uma atividade:

Transição automática via evento

Observe que neste caso a atividade "Procurar por medidas de recuperação" assumirá dois caminhos possíveis. Um deles é o avanço manual acionado pelo solucionador (ou se uma atividade automática, com avanço automático):

Transição da atividade

O outro caminho é adotado caso a condição estabelecida pela Regra configurada no evento associado tenha resultado verdadeiro após a execução do job "Máquina de Processos":

Regra configurada para o evento

No exemplo acima, caso o Nível de SLA tenha sido recalculado e este em uma determinada ocorrência deste fluxo que esteja nessa atividade seja incrementado, avança automaticamente para a atividade "Restabelecer o serviço" para o Especialista.

Durante a configuração do evento é possível definir a quantidade máxima de execuções por meio da propriedade **Quantidade máxima execuções**. Se este parâmetro for preenchido com o valor 0 significa que ele nunca será executado, tornando o evento inativo. Quando não for preenchido então o evento pode ocorrer sempre que for satisfeita a condição.

## Evento Intermediário por Temporizador

O que diferencia o **Evento intermediário por Temporizador** do **Evento Intermediário por Regra **é o fato utilizar um intervalo limite em minutos iniciando no instante em que a ocorrência inicia a atividade associada como temporizador. Repare no exemplo do fluxo de processo abaixo:

Tempo configurado para o evento

Se o Service Desk não finalizar a atividade "Procurar por medidas de recuperação" em 180 minutos (3 horas), automaticamente a Máquina de Processos avança para a atividade "Restabelecer o serviço" cujo responsável é o Especialista.

Caso contrário, avança naturalmente para a pergunta "A solução é de domínio do Service Desk?".

Durante a configuração do evento é possível definir a quantidade máxima de execuções por meio da propriedade **Quantidade máxima execuções**. Se este parâmetro for preenchido com o valor 0 significa que ele nunca será executado, tornando o evento inativo. Quando não for preenchido então o evento pode ocorrer sempre que for satisfeita a condição.

## Evento Intermediário de Mensagens

O evento intermediário de mensagens pode ser utilizado para envio de comunicados durante a execução do processo ou para comunicação com WebServices.

Evento intermediário por mensagem - WebServices

Para que o Evento Intermediário seja associado ao WebService o Nome da Mensagem deve estar configurado, o script evento são as ações que o evento deve realizar ao ser executado. Para saber mais sobre WebServices leia os tópicos "[Iniciador por Mensagem](iniciador_por_mensagem)" e "[Tutorial 16: Integração de Instalações Supravizio](tutorial_16_integracao_de_inst)".

Como visto no tópico "Iniciador por Mensagem", podemos abrir novas Ordens de Serviço utilizando o SV Service Bus. Também é possível configurarmos eventos Intermediários por Mensagem, acionados a partir do webservice.

Evento Intermediário por Mensagem usando Webservices

Também podem ser fornecido parâmetros da mesma forma que no Iniciador por Mensagem. Porém, aqui podemos ter dois comportamentos distintos. Podemos "avançar" uma Ordem de Serviço específica, ou podemos avançar TODAS as Ordens de Serviço que estiverem na atividade que contem o intermediário. Caso queira que apenas uma Ordem de Serviço específica seja "afetada", eu obrigatoriamente devo informar qual será. Para isso, basta inserir na lista de parâmetros (conteudoXML) o parâmetro OrdemServico. Nele eu informo o Número da Ordem de Serviço.

<MENSAGEM>

<PARAMETROS>

**<PARAMETRO>**

**<NOME>OrdemServico</NOME>**

**<VALOR>81717993278</VALOR>**

**</PARAMETRO>**

<PARAMETRO>

<NOME>Parametro2</NOME>

<VALOR>Valor do parâmetro 2</VALOR>

</PARAMETRO>

</PARAMETROS>

</MENSAGEM>

Repare no exemplo acima, no xml de parâmetros informamos que queremos afetar APENAS a Ordem de Serviço 81717993278. Isso é importante caso necessite de integração com outros sistemas, armazenando a Ordem de Serviço relacionada com a transação.

Caso eu queira que todas as Ordens de Serviço que estejam em uma atividade que contem o Intermediário por Mensagem, basta não fornecer o parâmetro OrdemServico.

Observe na mensagem abaixo que o evento **Análise de backup** enviará um e-mail para o Gerente de TI, um para "supervisor@empresa.com.br" e outro para "tecnico@empresa.com.br" informando que houve falha na execução de backup. Repare que serão enviados três emails individualmente (não apenas um com todos os destinatários como destinatário do email) pois a opção "Enviar uma mensagem para cada destinatário" está definida como "True" ou verdadeira. Também podemos redefinir o remetente da mensagem através do campo "Nome do remetente" e seu respectivo e-mail no campo "E-mail do remetente".

Evento intermediário de mensagem

O conteúdo da mensagem é definido em um Modelo de Comunicado que pode ser criado a partir da própria janela de propriedades do editor de processos ou pelas opções de menu **Processo | Processos | Modelos de Comunicados**. Veja na figura abaixo um exemplo de modelo editado no cadastro em questão:

Configuração de um Modelo de Comunicados

Para mais detalhes sobre criação de modelos veja [Tutorial 12: Modelos de Comunicados](modelos_de_comunicados).

As propriedades **Anexar todos os documentos** indica que todos os itens de configuração do tipo Artefato e configurados como arquivos serão anexados no comunicado. Já a opção **Tipos de arquivos anexados** permite especificar e restringir os tipos de artefatos que serão realmente anexados na mensagem. Também é possível anexar um relatório com dados da Ordem de Serviço através da opção **Anexar relatório de impressão**. Para saber mais, leia o tópico [Impressão da Ordem de Serviço](impressao_da_ordem_de_servico).

Quando preenchido a propriedade **Tipo de arquivo retornado** então o sistema anexa na Ordem de Serviço todos os arquivos anexados em comunicados de resposta utilizando o tipo informado. É importante observar que a resposta deve seguir a regra documentada em [Comunicados e Ordens de Serviço](comunicados).

O campo **Descrição** é opcional na grande maioria dos elementos porém no evento intermediário de mensagens é de suma importância pois é utilizado como texto do assunto do comunicado.

A opção **Finalizar Interrupção de ANS** indica que se existir alguma interrupção de ANS em curso e existir uma resposta com e-mail igual ao do cliente, então esta interrupção é finalizada automaticamente.

Além da configuração via propriedades é possível ajustar o evento via script. Neste caso o usuário deve fazer uso do Script Evento e seguir as orientações do tópico [Tutorial 12: Script de mensagem](envio_de_mensagens_em_eventos). No instante de envio da mensagem são aplicadas inicialmente as configurações de propriedades e em seguida é executado o script. Portanto, as propriedades do script são opcionais e prevalecem sobre a configuração de propriedades.

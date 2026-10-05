# Acordo de Nível de Serviço

Caminho: Guia para Administradores > Roteiro de implantação > Realizando cadastros > Cadastros Adicionais > Acordos > Acordo de Nível de Serviço

Acordos de Nível de Serviço são registrados no sistema por meio da tela de mesmo nome disponível nas opções de menu **Recurso | Acordos de Nível de Serviço | Acordos de Nível de Serviço **conforme a figura abaixo:

Acesso a tela de Acordo de Nível de Serviço

Acessando o cadastro de ANS podemos observar os seguintes campos na figura abaixo:

Dados principais do cadastro de ANS

Podemos observar que o ANS possui uma data de início e fim de validade.

Quando marcamos o campo **Considerar feriados da localidade do cliente no cálculo de tempo**, os dias dos feriados no calendário do cliente são excluídos da contagem de tempo, ou seja, nestes dias o ANS permanece suspenso.

Para consultar o Calendário do cliente acesse o cadastro da Unidade onde está localizado o Cliente (campo Local no cadastro da Pessoa).

O campo **Publicar informações no Portal de Processos** quando marcado exibe informações do ANS na página de consulta do Portal. Veja dois exemplos nas figuras abaixo:

Informação de prazo na consulta

Ainda na tela de dados principais podemos informar um plano de gestão que define indicadores utilizados para monitorar objetivos do ANS.

### Registrar Áreas atendidos

Para registrar os Órgãos que serão atendidos, acesse a aba e Áreas Atendidas e clique em novo:

Inclusão de Áreas Atendidas pelo ANS

No exemplo acima, o campo de área atendida é a Presidência e repare que a opção de incluir sub-áreas está marcada, portanto o acordo atende desde a Presidência até os últimos níveis na estrutura (todos os sub-níveis). No exemplo abaixo podemos observar um ANS que atende uma determinada área:

Acordo para área específica

## Tempos de Atendimento

A aba **Tempos de Atendimento** define as regras e tempos em **minutos** acordados para realizar o atendimento de um cliente (finalizar o atendimento). Para entender a utilização destas regras é importante conhecer o mecanismo de atribuição de ANS que é disparado na criação de uma nova Ordem de Serviço ou na modificação da informação de Cliente, Itens de Configuração associados ou classificação de processos. Neste instante o sistema recupera todos os ANS que podem atender o cliente tomando como base sua lotação e **pré-seleciona todas regras de atendimento que se enquadram no preenchimento da Ordem de Serviço** (campo Serviço, tipo de cliente, prioridade etc).

Tempos de atendimento de um ANS

Na figura acima, por exemplo, a primeira regra significa: para** todos os tipos de serviços, serviços, perfis e graus de prioridade** atender em **90** minutos.

## Critérios para a seleção da ANS

- São comparados os critérios **Tipo de Serviço** e **Serviço**, logo, o ANS com mais afinidade em relação a estes termos será atendido;
- Caso as regras tenham os mesmos critérios, o sistema selecionará aquela que apresentar o **menor tempo de atendimento**;
- Na edição da regra, a ausência de preenchimento de qualquer coluna indica que a regra será atendida para qualquer conteúdo.

Para facilitar o entendimento destas regras vamos utilizar alguns exemplos de Ordens de Serviço e observar o ANS selecionado.

### Exemplo 1: Uma Ordem de Serviço aberta por um usuário VIP

No exemplo da figura selecionamos como cliente uma pessoa que possui o perfil VIP. Podemos observar na figura acima que neste caso existe existem duas regras atendendo a Ordem de Serviço

Regra 1: para** todos os tipos de serviços, serviços, perfis e graus de prioridade** atender em **90** minutos

Regra 2: para** clientes do perfil VIP** atender em **30** minutos.

Como a Regra 2 possui o menor tempo de atendimento ela foi utilizada como tempo de atendimento para a Ordem de Serviço. Configura na figura abaixo:

Regra por perfil de Cliente

### Exemplo 2: Uso de uma regra genérica

Neste caso nossa Ordem de Serviço é atendida por uma regra genérica que define apenas o tempo de atendimento. A regra utilizada foi a seguinte:

Regra 1: para** todos os tipos de serviços, serviços, perfis e graus de prioridade** atender em **90** minutos

Correspondente ao seguinte registro:

Na figura abaixo podemos observar o resultado final:

Atendimento por uma regra genérica no ANS

É importante observar que no instante em que o sistema está selecionando uma regra são considerados todos os acordos cadastrados e válidos de acordo com sua lotação.

### Exemplo 3: Uso da regra mais específica

Neste exemplo, foram utilizadas os seguintes Tempos de Atendimento:

Tempos de Atendimento

Note que neste caso, o ANS utilizado foi o mais específico e com menor **Tempo de Atendimento**:

Atendimento por regra mais específica

Vamos criar uma nova Ordem de Serviço, desta vez, utilizando um **Serviço** diferente do especificado, porém, com o mesmo **Tipo de Serviço**:

Atendimento pela regra de Tipo de Serviço

Nesta Ordem de Serviço, foi utilizado o ANS com a mesma especificação de **Tipo de Serviço**, mas como o **Serviço **era diferente, este **Tempo de Atendimento** não foi utilizado.

### Exemplo 4: Exceções em dias do mês

Neste exemplo foi aplicada uma regra que define um período de exceção que vale para o período do dia 20 até o dia 30 de cada mês. Veja o cadastro desta exceção:

Regra de atendimento

Na figura podemos observar a regra para atendimento de solicitações de **Folha de Pagamento**. Acessando a aba **Períodos de Exceção** podemos verificar que existe uma exceção entre os dias 1 e 10 de cada mês:

Exceção do ANS

### Exemplo 5: Tempos específicos para Clientes (uso de fórmulas)

Neste exemplo criamos um campo customizado no cadastro de pessoas onde informamos o tempo de atendimento. No cadastro da regra informamos uma fórmula que recupera este tempo ou, caso não exista informação no cadastro do Cliente, retorna um valor default.

No cadastro do cliente informamos o tempo:

Tempo de atendimento do cliente Carlos Morais

Para mais informações sobre criação de campos customizados veja [Propriedades Customizadas](campos_customizados).

No cadastro da regra utilizamos a seguinte regra:

Regra por fórmula

O resultado final do exemplo pode ser observado na figura abaixo:

## Horários de Serviço

Esta aba configura os intervalos em dias das semana nos quais existe disponibilidade de serviço e nos quais será contabilizado tempo de atendimento (exceto em caso de feriados quando estes forem considerados no ANS).

No preenchimento desta configuração indicamos o dia da semana e as horas/minutos de início e fim. É possível relacionar vários períodos para um mesmo dia da semana. Exemplo: na segunda existe disponibilidade de 08:00 até 12:00 e de 14:00 até 18:00:

Dois períodos no mesmo dia da semana

### Interrupções

Uma [interrupção](ans_parado) é uma paralisação na contagem do tempo de atendimento em decorrência de uma situação de exceção prevista no acordo. Esta situação pode ser registrada de forma manual ou prevista em processo. Na figura abaixo podemos observar uma interrupção sendo inserida manualmente pelo solucionador:

Acessando o diálogo de Priorização e interrupções

Após acessar o diálogo de priorização podemos registrar a interrupção:

Adicionando uma interrupção

No exemplo abaixo informamos um motivo que está condicionado a aprovação pelo cliente. Veja na figura abaixo como foi feita a configuração desta aprovação:

Aprovação para paralisação do tempo de ANS

Registro da nova interrupção

Para realizar a aprovação acima o cliente pode utilizar a tela de aprovações do Portal.

Outra forma de trabalho com interrupções é indicando um motivo de interrupção no desenho do processo. No exemplo abaixo ao entrarmos na atividade "Solicitar recolhimento das caixas" o ANS será interrompido até que seja feita a transição para a próxima atividade.

Interrupção prevista em processo

Veja o resultado desta configuração na figura abaixo:

Interrupção configurada no processo

Ao contrário da interrupção manual a prevista em processo não pode ser encerrada ou cancelada pelo usuário. Veja na figura abaixo o resultado quando o usuário tenta cancelar a interrupção do processo acima:

Tentativa de cancelamento de interrupção previsa no processo

É importante observar que a interrupção prevista em processo só é efetivamente aplicada se o ANS prevê sua existência na aba de **Interrupções**.

**Importante**: Caso a interrupção seja configurada em um [Evento Finalizador](bpmn_eventos_finalizadores), será gerada uma interrupção que será encerrada assim que o usuário reabrir a Ordem de Serviço. Sendo assim, o periodo em que a Ordem de Serviço estiver finalizada não será incluído no cálculo do Acordo de Nível de Serviço.

A interrupção do ANS pode ter configurado um tempo limite máximo e também exigir do usuário informação de um comentário, estes itens podem ser configurados em **Recursos | Acordos de Nível de Serviço | Motivos de Interrupção de ANS**:

**Motivos de Interrupção de ANS**

Com duplo clique no Motivo desejado (ou novo motivo) pode se configurar se é necessário informar comentário com o checkbox e definir o tempo máximo em horas na caixa de texto, por exemplo para definir o tempo máximo de 10 horas e obrigar a informação de comentário para o motivo "Aguardando fornecedor":

Preenchimento dos campos

Com essas configurações, ao fazer uma nova interrupção com o motivo "Aguardando fornecedor" acontece o seguinte:

Nova Interrupção ANS

Note que o campo Comentário ou justificativa passou a ser obrigatório e que a Data/hora previsto para finalização já foi preenchida automaticamente com o tempo máximo, porém se o usuário tentar modificar a previsão para finalização para um período maior que o tempo máximo ocorre o seguinte erro:

Modificação da data de entrega prevista

## Processos acordados

A aba Processos acordados contém os subprocessos para os quais o ANS é válido.

Subprocessos onde o ANS será aplicado

## Charge-back

A aba de Charge-back define regras de cobrança por serviços relativos ao ANS. No exemplo abaixo será cobrada uma taxa mensal de 2.000 pela manutenção do ANS.

Cobrança por taxa mensal

No exemplo abaixo será cobrada uma taxa de 50 reais por Ordem de Serviço registrada e atendida pelo ANS:

Cobrança por Ordem de Serviço

## Início e fim do período de atendimento

### Solicitação de Serviço

Quando uma Ordem de Serviço é criada, a data e hora da solicitação recebe por padrão mesma data e hora de criação (abertura) mas é importante lembrar que é possível modificar tal campo na Ordem de Serviço.

**Data/Hora da Solicitação**

Importante: Data/Hora da Solicitação somente fica disponível se houver ANS.

### Entrega de Serviço

Quando a Ordem de Serviço é finalizada, por padrão a Data/Hora da Entrega é definida, mas este valor pode ser definido antecipadamente. A Data/Hora de Entrega é o valor que define quando o Tempo de ANS deve parar de ser contabilizado.

Data/Hora de Entrega definida por finalização

### Definindo início e fim via processo

No Editor de Processos pode ser incluído um [Data Object de Entrada de Dados](criando_fluxos_de_processos) no qual pode ser definido o preenchimento da Data/Hora de Entrega de Serviço e também pode ser preenchido a Data/Hora de Solicitação de Serviço. Como a única maneira de alterar a Data/Hora de Entrega é definir previamente, o exemplo criará uma Entrada de Dados deste tipo.

Campos de Entrada de Dados

Processo com preenchimento de Data/Hora de Entrega

Após inclusão do campo Data/Hora entrega serviço, na Ordem de Serviço ao atingir a etapa "Aguardar Resposta e executar solução apresentada" ocorrerá a seguinte tela:

Ordem de Serviço com Entrada de Dados para definição de Data/Hora de entrega

Ao clicar em Definir data/hora de entrega o seguinte diálogo será apresentado:

Registrar Entrega Serviço

Repare que o checkbox do controle de data permite que a data/hora seja "zerada", ou seja, se o problema ainda não foi resolvido e é necessário retomar a contagem do tempo restante de ANS.

### Cálculo de tempo por campos da Ordem de Serviço

Também é possível realizar a criação de um **Acordo de Nível de Serviço** que calcula o tempo de acordo com uma data inserida na Ordem de Serviço, porém, respeitando a disponibilidade da respectiva **Pessoa**.

Como exemplo, utilizaremos um [Tempo de Atendimento](acordo_de_nivel_servico) calculado de acordo com a seleção do campo **Data fim previsto**.

Para isso, devemos realizar as seguintes alterações no fluxo.

Fluxo no Editor de Processos

Feita a alteração, crie um **Acordo de Nível de Serviço** com o seguinte [Tempo de atendimento](acordo_de_nivel_servico):

```
AcordoNivelServico.ObtemTempoDisponibilidade(OrdemServico.DataHoraCriacao, OrdemServico.DataHoraFimPrevisto ife OrdemServico.DataHoraFimPrevisto !=
None else OrdemServico.DataHoraCriacao, Cliente)
```

Configuração do Tempo de Atendimento

Inicie uma nova Ordem de Serviço, utilizando o mesmo **Serviço** selecionado anteriormente, e selecione uma** Data/hora fim previsto**.

Seleção da data prevista

Após, note que o **Acordo de Nível de Serviço** será calculado de acordo com a data selecionada.

Tempo calculado na Ordem de Serviço

### Impacto no Cálculo da disponibilidade de serviço

No [Relatório de Disponibilidade de Serviços](disponibilidade_servicos), o inicio de períodos de indisponibilidade são contados a partir da Data/Hora de solicitação e o fim pela Data/Hora de entrega de serviço. Ao alterar a Data/Hora de entrega ou Data/Hora de Solicitação, os resultados também serão alterados.

### Gestão do Acordo de Nível de Serviço

Para Gestão do Acordo de Nível de Serviço é possível utilizar colunas no grid do Workspace de visualização de Ordens de Serviço com o progresso do ANS (para saber como adicionar ou remover colunas do grid do Workspace veja o tópico [Configuração do grid de Ordens de Serviço](configuracao_do_grid_de_ordens)), no exemplo a seguir podemos ver em porcentagem o restante do ANS e numericamente tanto o prazo quanto o restante do ANS:

Colunas no Workspace para Gestão do ANS

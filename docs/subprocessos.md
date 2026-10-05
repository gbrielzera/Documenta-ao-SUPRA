# Subprocessos

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Atividades > Subprocessos

A chamada de subprocesso é um recurso que permite invocar um outro fluxo de processo gerando uma nova Ordem de Serviço. O subprocesso invocado pode ser do mesmo processo ou de outro processo através de [Associações](associacao_sub). É possível determinar se o fluxo do processo seguirá adiante independente da conclusão ou não desta nova Ordem de Serviço (denominada "chamada assíncrona") ou não permitir avançar a atividade do subprocesso enquanto a nova Ordem de Serviço não estiver concluída. É possível também determinar se a Ordem de Serviço chamadora será cancelada caso a nova Ordem de Serviço seja cancelada (mais informações leia [Sincronização de Cancelamentos](tutorial_5)).

Chamadas de Subprocessos

A figura abaixo ilustra a configuração de dois fluxos utilizando uma chamada de Subprocesso. Observe que no primeiro fluxo da figura existe uma chamada para o subprocesso Mudança. Na segunda figura encontramos o fluxo da ocorrência originada da execução do chamador iniciada a partir de um** [Link inicial](bpmn_iniciadores)**. Como pode ser observado para cada fluxo executado existirá uma Ordem de Serviço e entre as duas ocorrências pode ocorrer troca de dados e diferentes responsabilidades.

Chamadas de fluxos

A principal configuração de uma chamada de Subprocesso é a Associação:

Configuração da chamada de Subprocesso

Uma Associação permite configurar um relacionamento entra processos fontes e processos alvo. Para mais informações sobre interface entre processos leia o [Tutorial 4: Interface entre Processos](tutorial_04).

Uma outra propriedade muito importante é a Chamada assíncrona. Com ela podemos avançar a Ordem de Serviço chamadora sem necessidade de finalização da Ordem de Serviço invocada.

O parâmetro **Sincronizar cancelamento** indica que se a Ordem de Serviço chamadora for cancelada, todas as Ordens de Serviço invocadas também serão canceladas e vice-versa. Durante a execução do processo são exibidos alertas no assistente de processos quando ocorrer algum cancelamento. Veja no exemplo abaixo que a Ordem de Serviço 51 foi cancelada em virtude do cancelamento da Ordem de Serviço 52.

Resultado do sincronismo de cancelamento

Para mais informações sobre sincronismo de cancelamento leia o [Tutorial 5: Sincronização de Cancelamentos](tutorial_5).

### Passagem de parâmetros

A passagem de valores e itens de configuração entre processos é um recurso muito importante para construção de fluxos "parametrizáveis", ou seja, fluxos que podem ter aplicação em diversos processos.

Quando um subprocesso invoca um outro é possível fornecer dados como parâmetros. Estes dados podem ser constituídos de campos da Ordem de Serviço (poderíamos por exemplo fornecer o campo Assunto modificado) ou Itens de Configuração (poderíamos por exemplo passar um documento anexado ou o cadastro de Equipamento). Nas próximas figuras podemos verificar o que deve ser feito para configurar esta passagem de parâmetros.

Configuração de passagem de Itens de Configuração

**Passagem e retorno de Itens de Configuração**

Podemos passar itens de configuração utilizando o atributo** Passar todos os Itens de Configuração**, que fornecerá para a ocorrência invocada todos os itens anexados no chamador, ou então podemos relacionar os tipos que devem ser transferidos para o chamado preenchendo a coleção **Passagem de Itens de Configuração**.

A regra de retorno de itens de configuração possui configuração similar fazendo uso dos parâmetros **Retornar todos os Itens de Configuração** e **Retorno de Itens de Configuração**. O retorno de itens ocorre quando finalizamos a ocorrência invocada, quando todos os itens anexados neste registro são anexados também na chamadora.

**Passagem e retorno de campos da ocorrência**

Nesta situação os dados fornecidos e retornados como parâmetros são campos nativos ou customizados da ocorrência e são configurados no elemento chamador da seguinte forma:

- Parâmetros de entrada: são valores fornecidos para a ocorrência invocada no instante em que esta é criada. Para configurar estes parâmetros utilize a coleção **Parâmetros de entrada**. Veja o exemplo abaixo:

Acessando o editor de parâmetros

Editor de parâmetros

Na figura abaixo podemos visualizar o novo parâmetro configurado.

Configuração do Parâmetro de Entrada

Para especificar um parâmetro foi necessário selecionar uma propriedade nativa ou um campo customizado (é permitida a seleção de apenas uma das opções) e em seguida definimos uma fórmula para recuperação do valor. Clicando no ícone é apresentado o diálogo de edição de fórmulas conforme a figura abaixo:

Parâmetro de entrada montado com texto constante e Assunto do chamador

Quando executamos uma Ordem de Serviço conforme a configuração acima a nova Ordem de Serviço gerada pela chamada recebe o novo conteúdo do assunto conforme a figura abaixo:

Resultado da passagem do parâmetro Assunto

- Parâmetros de saída: são valores retornados para a ocorrência chamadora no instante em que a invocada é finalizada. Para especificar estes parâmetros precisamos configurar o fluxo que é invocado e nele definir os parâmetros de saída. Veja na figura abaixo a sequência de comandos para realizar esta configuração:

Fluxo chamador

Acessar o cadastro do Subprocesso

Configuração dos parâmetros de saída

Ainda no exemplo anterior podemos marcar a opção **Transição automática** no elemento chamador. Desta forma a liberação seria finalizada, o campo Solução retornado para o chamador (a Mudança), que sofreria uma transição para o finalizador que encerraria automaticamente a mudança pois já existe informação da Solução.

Transição automática após finalizar a Liberação

**Observação**: Há a opção de desativar a geração manual de associadas durante a edição da Ordem de Serviço, através da opção **Permitir geração manual.**

Propriedade do subprocesso

Caso a propriedade seja definida como **False**, a opção de abertura não será exibida:

Edição de Ordem de Serviço

### Chamadas Assíncronas

### É possível determinar se o fluxo do processo seguirá adiante independente da conclusão ou não desta nova Ordem de Serviço (denominada "chamada assíncrona") ou não permitir avançar a atividade do subprocesso enquanto a nova Ordem de Serviço não estiver concluída.

### Caso a propriedade seja definida como False, a tarefa só poderá ser avançada quando todas as ocorrências geradas tiverem sido finalizadas.

Propriedade Chamada assíncrona

Caso contrário, a atividade será avançada independentemente de os subprocessos terem sido finalizados. Neste caso, será habilitada uma nova opção para escolha sobre qual o momento a atividade poderá avançar:

Opções de sincronismo com a atividade

- **Finalização da ocorrência** - A ocorrência principal só poderá poderá ser finalizada assim que todas as geradas pela mesma estiverem na mesma situação;
- **Finalização de tarefa ou evento** - Só será possível avançar determinada atividade assim que as Ordens de Serviço geradas estiverem finalizadas;
- **Nenhuma restrição** - Não haverá sincronia entre as duas ocorrências. A ocorrência principal poderá ser finalizada, mesmo que os subprocessos ainda estejam pendentes.

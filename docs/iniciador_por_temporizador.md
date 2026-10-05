# Iniciador por Temporizador

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Eventos Iniciadores > Iniciador por Temporizador

O início por temporizador permite a geração de Ordens de serviço por configuração de ciclo de repetição baseado em tempo. Este tipo de iniciador pode ser utilizado, por exemplo, nas seguintes situações:

- Semanalmente precisamos verificar os níveis de estoque e, se necessário, providenciar resuprimento;
- Mensalmente realizaremos uma reunião de monitoria de processos e, quando necessário, será gerada uma nova versão de processo;
- Diariamente precisamos conferir o backup do servidor de arquivos.

Evento inicial por temporizador

Para utilizar um iniciador por temporizador é necessário primeiramente definir o tipo de ciclo que pode ser diário, semanal, mensal ou anual. Para cada tipo de ciclo existem parâmetros adicionais que são editados na janela de Propriedades do Editor. Utilizando estes parâmetros é possível construir ciclos derivados tais como bimestrais (habilitando determinados meses para execução de ciclos mensais), semestrais etc.

**Importante: um fluxo que contenha somente iniciadores por temporizador não estará disponível no Portal de Processos ou no Workspace.**

Outro parâmetro requerido para configuração deste iniciador é a de responsável feita pela propriedade de mesmo nome. Sem esta configuração o iniciador é desconsiderado pela máquina de processos e não gerará Ordens de serviço.

A propriedade Regra é uma fórmula que determina o resultado da geração da seguinte forma:

- Se for retornado um valor lógico então este valor é utilizado para** confirmar a geração da Ordem de Serviço**. Exemplo: se especificarmos a fórmula **DateTime.Now.Year < 2012** então só serão geradas Ordens de Serviço até o ano de 2012.
- Se for retornado um array ou lista então será gerada** uma Ordem de Serviço para item retornado**.
- Se for retornado um objeto DataTable do Microsoft .Net então é retornado **uma Ordem de Serviço para data DataRow**. Neste caso o iniciador por timer passa a se comportar de forma muito semelhante ao iniciador por regra. A diferença fundamental é que no caso do iniciador por regra o comando SQL é executado repetidas vezes em função da configuração de ciclo da máquina de processos, enquanto no iniciador por timer é repetido apenas no ciclo do timer e pode se tornar uma opção mais interessante em termos de desempenho do sistema.

Prorpiedade de Regra para Iniciador por Timer

### Considerações sobre ativação de iniciadores por timer

Após a ativação de um iniciador este só pode gerar Ordens de Serviço referente a uma configuração de ciclo que retorne uma data maior ou igual a data/hora corrente. Se, por exemplo, um iniciador for configurado para iniciar no dia 1 do mês corrente e se o dia corrente for igual a 5 então não é gerada a Ordem de Serviço. Esta só será gerada no início do próximo mês.

Outra situação de exceção é quando uma nova versão de um processo é ativada e no mesmo dia da ativação já tenha ocorrido a geração de uma Ordem de Serviço por iniciador do tipo timer. Nesta situação a nova versão não gerará nova Ordem de Serviço.

# Configuração de Contratos

Caminho: Guia para Administradores > Roteiro de implantação > Realizando cadastros > Cadastros Adicionais > Cadastrar Tipos de Apontamento > Configuração de Contratos

O Supravizio também possibilita a criação de apontamentos de diferentes tipos. Um apontamento pode assumir um determinado valor dado o seu tipo de apontamento. Por exemplo, o solucionador pode criar um apontamento do tipo "Hora Trabalhada", um apontamento do tipo "Treinamento", um apontamento do tipo "Deslocamento", ou outros. Para cada tipo de apontamento, pode haver um valor diferenciado, de acordo com o que é definido no [Contrato](contrato_sub) associado à Ordem de Serviço do apontamento que queremos criar ou modificar.

Para criar tipos de apontamento, selecione no menu principal as opções** [Recurso | Tipos de Apontamento](tipoapontamento_sub)**:

Após cadastrar os nomes dos tipos de apontamento adotados, o usuário deve incluí-los no [Contrato](contrato_sub) desejado. Para isso, selecione **Recurso | Contrato**, selecionando o [Contrato](contrato_sub) na listagem e clique na aba **Apontamentos**. Nesta aba é possível incluir os tipos de apontamentos desejados e cadastrar uma **Variação**. Esta Variação é um percentual do Valor/Hora contratado de um determinado Recurso Aplicado.

Clicando na aba **Recursos Aplicados**, selecione um registro e observe que podemos determinar o valor/hora deste tipo de recurso através do campo **Valor hora** além de registrarmos um valor mensal de custo deste recurso, um saldo de horas por mês e a validade deste saldo em meses:

Na aba **Solucionadores** incluímos os grupos de trabalho que são daquele tipo de Recurso Aplicado.

É importante ressaltarmos as seguintes informações:

- Em um contrato podemos inserir apenas um Recurso Aplicado sem nenhum grupo de trabalho definido. Em um cálculo de saldo de horas ou de apropriações de horas trabalhadas, os valores e saldos deste Recurso Aplicado serão utilizados como padrão.
- Um grupo de trabalho não pode constar em dois Recursos Aplicados diferentes em um contrato.

**Observação**: Também podemos associar um Serviço a um Contrato através da aba **Serviços do Contrato**. Estes serviços também são utilizados como filtro no módulo de Abertura do Portal de Processos, caso o solicitante esteja associado ao contrato. Leia o tópico [Configuração do módulo de Abertura](portal_abertura_configuracao_assist) para saber mais sobre a configuração necessária.

Com as três informações de: variação do [tipo de apontamento](tipoapontamentocontrato_sub), valor hora do recurso aplicado e o solucionador sendo um integrante de um grupo de trabalho que esteja contido no recurso aplicado, é possível realizar o cálculo da somatória do valor financeiro do trabalho do solucionador.

No preenchimento de um apontamento, você pode indicar agora o tipo do apontamento:

**Tipos de apontamento para um apontamento**

Caso não exista um [Contrato](contrato_sub) associado ou, se existir um [Contrato](contrato_sub), este não houver [Tipos de apontamento](tipoapontamentocontrato_sub) previstos, não é possível atribuir um tipo de apontamento no cadastro do apontamento.

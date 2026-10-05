# Bandas de um Relatório

Caminho: Guia para Administradores > Editor de Relatórios > Bandas de um Relatório

A organização de bandas de exibição de relatórios do Editor de Relatórios do Supravizio é semelhante aos editores de relatório mais comuns do mercado. É possível criarmos bandas para cabeçalho de relatórios, rodapés, repetições de topos ou rodapés de relatórios, banda de listagem de dados e bandas internas. Os tipos disponíveis são:

### TopMargin

Esta uma das bandas mais simples. Sua finalidade é determinar o espaçamento da margem superior do relatório. Seu espaçamento é aplicado todas as páginas. Sua principal propriedade é Height, que determina em pixels o tamanho da margem:

Esta é uma região ideal para inclusão de logotipos e/ou títulos para o relatório:

### BottomMargin

Assim como o TopMargin determina o espaçamento superior de uma página de relatório, o BottomMargin determina o espaçamento inferior.

Também utilizamos esta região quando necessitamos incluir um rodapé:

### Detail

Nesta banda determinamos como serão exibidos os campos de uma consulta. Esta é a banda principal de um relatório. Nela nós adicionamos os campos, determinando suas formatações. Observe no exemplo abaixo que temos um relatório que listará, baseado em uma consulta, todas as Ordens de Serviço ordenadas por Número e Assunto:

Para este exemplo utilizamos a seguinte consulta:

Durante a renderização (impressão em tela ou outro meio) do relatório, para cada registro retornado pela consulta, o conteúdo da banda Detail se repete:

### Report Header

Este é o cabeçalho do relatório. É uma região ideal para incluirmos campos adicionais caso iremos listar dados através da banda Detail.

### Report Footer

Esta banda é utilizada quando finalizamos a impressão de um relatório. É muito utilizada caso o usuário queira listar totais gerais sobre o relatório elaborado.

### Page Header

Esta banda é repetida todas as vezes em que uma nova página do relatório é exibida.

### Page Footer

Esta banda é repetida todas as vezes em que uma nova página do relatório é exibida.

Group Header

Esta banda é utilizada quando necessitamos agrupar alguns dos valores da consulta. Por exemplo, quando necessitamos agrupar Ordens de Serviço por Serviço. Podemos utilizar esta região para realizar o agrupamento. Para realizarmos estes agrupamentos, basta no Grid de Propriedades da banda selecionarmos a propriedade Campos do Agrupamento.

Esta é uma banda que pode possuir outros Group Headers se forem necessários sub-agrupamentos para o relatório.

### Group Footer

Esta banda é utilizada ao final da impressão de um agrupamento realizado por um Group Header.

## Ajustando Tipo e Tamanho e Margens de Papeis

Para modificar o tipo de papel que será definido na impressão do seu relatório, basta selecionar o relatório na barra de propriedades e na propriedade KindPaper selecionar uma das opções.

Para ajustar as margens do papel, selecione a propriedade Margens. Expandido esta propriedade verá que poderá alterar os tamanhos das margens (em pixels).

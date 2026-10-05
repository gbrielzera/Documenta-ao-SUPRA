# Tabelas Dinâmicas

Caminho: Relatórios > Tabelas Dinâmicas

### Uma tabela dinâmica é uma estrutura de dados que utilizando os filtros determinados pelo usuário visa criar tabelas de modo versátil e proporcionar melhor entendimento dos dados gerados no sistema Supravizio.

## Entendendo uma tabela dinâmica

Uma tabela dinâmica é composta basicamente de 4 regiões: Linhas, Colunas, Área de Filtro e Área de dados (Totalizadores):

Layout de consulta

Selecionando um campo na lista de campos disponíveis e soltando na região das Linhas, são listados os registros agrupados relacionados com o campo selecionado. Veja por exemplo, se selecionarmos campo "Solucionador" e soltando na região das Linhas, são listados todos os Solucionadores responsáveis pelas Ordens de Serviço filtradas no período determinado na barra de ferramentas da transação:

Arraste de colunas

Da mesma forma, vamos selecionar o mesmo campo Solucionadores e arrastá-lo agora para a região das colunas:

Configuração de colunas

Repare que agora a lista de solucionadores responsáveis por Ordens de Serviço no período selecionado é exibida em forma de colunas.

Vamos detalhar a utilização da região dos Totalizadores no item seguinte:

### Totalizando Informações

Arrastando novamente o campo Solucionadores para a região das Linhas, vamos agora incluir totais relacionados com os solucionadores em questão. Selecione na lista de campos o campo "Quantidade" e arraste-o e em seguida solte-o na região dos Totalizadores. Observe que são exibidos os totais de Ordens de Serviço em que cada Solucionador é responsável:

Totalizadores

### Dividindo totais

Dando continuidade no assunto anterior, desejamos agora contabilizar os totais de Ordens de Serviço abertas por cada solucionador dividindo-os pelas suas Situações. Ainda com o campo Solucionador inserido na região das linhas e o campo Quantidade como totalizador, vamos agora selecionar o campo "Situação" arrastando-o em seguida para a região das colunas:

Tabela Dinâmica Solucionador x Situação com total de quantidade

Observe que os totais foram divididos pelas situações existentes nas Ordens de Serviço recuperadas através do filtro por período exibindo como última coluna o total de cada solucionador. Se invertermos as posições dos campos Solucionador e Situação, temos a seguinte configuração:

Tabela Dinâmica Situação x Solucionador com total de quantidade

Concluímos que podemos organizar nossa consulta configurando as linhas e colunas da forma mais adequada para nosso relatório.

### Subdividindo Totais

Vamos agora realizar uma outra consulta inserindo subdividindo campos. Queremos exibir as situações das Ordens de Serviço filtradas, porém dividindo-as por cada Solucionador responsável. Para isso basta arrastar o campo "Solucionador" para a região das linhas, porém do lado direito do campo Situação:

Subdivisão de Situação, Solucionador

Invertendo a ordem dos campos Situação e Solucionador temos o seguinte resultado:

Subdivisão de Solucionador, Situação

A tabela dinâmica possibilita por sua vez também subdividir informações por colunas. Observe o caso abaixo. Vamos agrupar os tempos brutos gastos por cada solucionador em cada subprocesso, dividindo os totais por situação em Tipos de Serviço:

Tabela dinâmica Solucionador subdividido em Subprocesso x Situação subdividida em Tipo de Serviço com total em Tempo Bruto Total

## Lista de Campos

O menu lista de campos é útil para melhor organização ou mesmo fácil implementação de colunas, linhas e totalizadores de maneira organizada.

Clique em Mais Campos na barra de ferramentas para exibir a lista de campos disponíveis.

Exibir lista de Campos

Uma nova caixa aparecerá, clique e arraste os campos desejados para dentro da nova caixa para retirar o campo.

**Arraste os campos desejados**

Para adicioná-los, basta arrastar o campo para o local desejado:

Local para adicionar campo

É importante ressaltar o significado de cada campo de adição:

| **Linha** | Insere o campo na área de linhas. |
|---|---|
| **Coluna** | Insere o campo na área de colunas. |
| **Área de filtro** | Insere o campo na área de filtro de campos. |
| **Área de dados** | Insere o campo na área de totalizador. |

Especificação dos regiões de adição

## Filtros

As informações de tabelas dinâmicas podem ser muito amplas, por isso o recurso de filtros possibilita que a tabela seja focada nos propósitos necessários ao usuário. O comando de filtro é bem simples de ser utilizado, coloque o ponteiro do mouse sobre o campo que deseja que seja filtrado (por exemplo Solucionador), um ícone de filtro aparecerá, clique nele.

Filtro

Os possíveis campos de resultados irão aparecer, junto com a opção Show All, caso queira exibir os resultados de apenas alguns Solucionadores, marque apenas os desejados. Por exemplo apenas Tarefa de Projeto e Tarefa de Apoio em mudança:

Filtro definido com exemplo

Agora em qualquer tipo de tabela dinâmica elaborada os resultados serão filtrados apenas com informações de Ordens de Serviço nas quais o Tipo de Subprocesso são um dos indicados acima.

**Tabela Dinâmica com filtro**

Repare que mesmo não participando das colunas, linhas ou totais o filtro é utilizado. Verifique a mesma tabela sem o filtro:

**Tabela Dinâmica sem filtro**

## Ordenando os Campos

Os campos podem ser ordenados de variadas formas para melhor compreensão da tabela, há diversas maneiras de realizar tal ordenação e este tópico pretende apresenta-las ao usuário.

A ordenação alfabética pode ser realizada em qualquer campo de linha ou de coluna, e pode ser feito combinações das mais variadas de ordenações dos submenus pois cada submenu ordena seus resultados independente dos demais, para modificar a ordenação basta clicar nos campos em destaque:

Tabela Dinâmica Ordenação Alfabética

## Exportar Tabela Dinâmica

Para realizara exportação de uma tabela dinâmica basta utilizar o botão Exportar e selecionar o formato de exportação desejado:

**Tabela dinâmica de Ordem de Serviço - Exportação**

Ao clicar no formato desejado um novo diálogo será exibido automaticamente com a extensão desejada para selecionar a pasta onde o arquivo de exportação deve ser salvo. Por exemplo uma exportação para Excel:

Exportação de Tabela dinâmica

## Tabelas Dinâmicas Disponíveis

[Tabela Dinâmica de Apontamentos](tabela_dinamica_de_apontamento)

[Tabela Dinâmica de Atividades Executadas](tabela_dinamica_de_atividades_)

[Tabela Dinâmica de Interrupção de ANS](tabela_dinamica_ans)

[Tabela Dinâmica de Ordens de Serviço](tabela_dinamica_de_ordens_de_s)

[Tabela Dinâmica de Pesquisas Respondidas](tabela_dinamica_de_pesquisas_r)[ ](tabela_dinamica_de_itens_de_co)

[Tabela Dinâmica de Itens de Configuração](tabela_dinamica_de_itens_de_co)

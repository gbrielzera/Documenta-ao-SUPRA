# Seções de Dados

Caminho: Guia para Administradores > Editor de Dashboard > Seções de Dados

Os dados utilizados em um dashboard podem ser organizados em "dimensões" específicas que chamamos de Seções de Dados. As principais Seções de Dados são:

- Argumentos (Arguments)
- Séries (Series)
- Valores (Values)

## Áreas de dados disponíveis

## Argumentos (Arguments)

Argumentos (Arguments) representa a classificação/divisão dos dados que queremos exibir. Pode ser considerado, por exemplo, como um eixo X num plano cartesiano ou as fatias de um gráfico pizza.

Valores (Values) Valores (Values) representam as proporções (em número) de um determinado argumento/série. Em um gráfico pizza, por exemplo, representa o tamanho das fatias. Num gráfico de barras equivale a um "eixo Y".

Séries (Series) Através das Séries é possível inserirmos "subdivisões" nas medidas dos argumentos. Por exemplo, em um gráfico de barras, é possível dividirmos os dados por anos específicos (através de Argumentos) e em seguida subdividir este ano em barras com outras classificações:

f

## Casos especiais

Em alguns tipos de gráficos, há algumas particularidades em relação a estas áreas a serem utilizadas.

### Pivot

Para gráficos do tipo Pivot, estão disponíveis as seguintes seções:

- **Values**

Contém os dados que serão utilizados para realizar o calcular os valores exibidos na tabela.

- **Columns**

Contém os itens os quais seus valores serão utilizados para o rótulo das colunas.

- **Rows**

Contém os itens os quais seus valores serão utilizados para o rótulo das linhas.

### Grid

Para gráficos do tipo Grid, está disponível apenas a seção **Columns**. No entanto, estas colunas podem ser de três tipos diferentes:

**Importante**: Para alterar o tipo da coluna, clique sobre o símbolo da mesma, conforme serão indicadas nas imagens.

- **Dimension**

Exibe os descritivos dos itens a serem vinculados aos valores.

- **Measure**

Exibe os valores calculados de acordo com o item de dados vinculado.

- **Delta**

Calcula um valor de acordo com duas medidas e exibe a diferença entre estas duas. Este exibe a diferença de valores em números, seguido de um triângulo indicando se houve um aumento ou diminuição de valores.

## Campos Ocultos

Também podem ser criados campos que podem ser utilizados em lugares como filtros ou ordenações, porém, não aparecerão nos gráficos. Para estes campos, existem duas áreas específicas:

- Dimensions

Podem ser utilizados ao criar um critério de filtro no Dashboard.

- Measures

Estes itens aparecerão ao se realizar uma ordenação em **Sort By **na coluna ou em **Top N values**.

## Funções de Cálculo

Estão disponíveis para uso em conjunto com os campos recuperados, algumas funções de cálculo:

Funções disponíveis

Abaixo, vamos descrever brevemente cada função:

- **Count** - Quantidade de valores (exceto quando for retornado Null e DBNull);
- **Sum** - Soma de todos os valores;
- **Min** - Menor valor;
- **Max** - Maior valor;
- **Average** - Média entre todos os valores;
- **StdDev** - Uma estimativa do desvio padrão de uma população, onde a amostra é apenas uma parte da população;
- **StdDevP** - O desvio padrão de uma população, onde a população são todos os dados recuperados;
- **Var** - Uma estimativa da variação de uma população, onde a amostra é apenas uma parte da população;
- **VarP** - A variação de uma população, onde a população são todos os dados recuperados.

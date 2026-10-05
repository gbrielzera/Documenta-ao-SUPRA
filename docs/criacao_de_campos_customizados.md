# Criação de Campos Customizados

Caminho: Guia para Administradores > Roteiro de implantação > Propriedades Customizadas > Criação de Campos Customizados

A criação de uma propriedade customizada não se limita apenas a [cadastros](criando_propriedade_customizada), pois possibilita também ao customizador incluir novas propriedades que poderão ser utilizadas em implementações de script, novos campos e propriedades em Ordens de Serviço, dentre outras.

Neste tópico descrevemos o que ocorre no sistema quando criamos um novo campo customizado:

### Propriedades do campo customizado

Nos próximos parágrafos vamos detalhar cada parâmetro a ser inserido durante a criação de um novo campo.

## Nome

Nome do campo customizado. Possui formato de nome de coluna de tabela de banco de dados, conforme descrito acima. Sendo assim, esteja atento a limitações de quantidade de caracteres em nomes de colunas determinados pelo seu sistema gerenciador de banco de dados.

## Descrição resumida

Podemos definir um descritivo mais amigável para nosso campo customizado através da propriedade Descrição resumida. Este é o rótulo de exibição de um campo customizado.

## Descrição

Para indicar detalhadamente uma propriedade utilizamos a propriedade Descrição.

Além de visualizar a Descrição do campo, também visualizamos detalhes de armazenamento em banco de dados pois são exibidos a tabela da propriedade e o campo da tabela que ela faz parte. Este recurso pode ser utilizado caso seja necessário gerar algum relatório que dependa desta informação, utilização em elaboração de scripts, dentre outros.

## Tipo

Quando criamos um campo customizado devemos indicar de qual tipo esta será. Para isso utilizamos a propriedade Tipo. Os tipos possíveis são:

- **Alfanumérico**: admite letras e números.
- **Data e Hora**: data/hora.
- **Decimal**: admite números decimais contendo 15 dígitos e duas casas decimais.
- **Inteiro**: admite números inteiros, sem casas decimais e limitados a valores na faixa de -999999 até 999999 em bases Oracle ou na faixa -2^31 (-2,147,483,648) até 2^31-1 (2,147,483,647) no caso de banco SQL Server.
- **Listagem de Objetos**: lista de objetos de uma determinada classe pertencente ao Dicionário de Classes do sistema. Equivale ao conceito de identificador e chave estrangeira para outra tabela.
- **Listagem de Registros**: lista de registros referentes a valores inseridos dentro de campos presentes na listagem. Estes campos podem ser de qualquer Tipo, exceto a própria e Listagem de Objetos.
- **Lógico**: verdadeiro (True) ou falso (False)

## Permitir inclusão em listagens de edição

Habilita a inclusão do campo na exibição de colunas em Telas de Listagem, como Telas de Cadastro ou na exibição de Ordens de Serviço.

Podemos determinar a forma de exibição de um campo customizado através do grupo de propriedades **Controle Edição**. Vamos agora detalhar sobre cada propriedade deste grupo.

## Ordem de Exibição

Ao exibir os controles em uma tela de exibição de campos customizados estes obedecem uma ordenação de exibição. Esta ordenação é determinada pela propriedade Ordem Exibição. Consiste em um número inteiro para esta ordenação.

## Controle

Indica qual controle será exibida para edição daquele campo customizado. Para mais informações, leia o tópico [Tipos de Controle](tipos_de_controle_os_2).

## Cadastro associado

É possível também criar propriedades customizadas que são registros de outros cadastros, de outras classes. Podemos fazer isto preenchendo o campo Classe referência. Vamos exemplificar mais adiante neste tópico sobre este assunto quando criamos controles do tipo ComboBox.

## Script para a recuperação de opções

Este script python pode ser utilizado para recuperar dados que serão exibidos na listagem de opções para seleção. Neste script devemos preencher uma lista de objetos denominada Itens (disponível no script) com estes valores de opções. Para realizar este preenchimento podemos utilizar, por exemplo, a função **Utils.ExecuteDataTable **para recuperar dados a partir de banco via comando SQL.

## Habilitado

Indica se é permitida ou não a edição das informações do controle.

## Visível

Indica se será exibido ou não o controle.

## Largura

Determina a largura de exibição do controle em pixels.

## Altura

Determina a altura de exibição do controle em pixels.

## Listagem itens

Em muitos casos, o usuário necessita apenas selecionar um item de uma lista predefinida. Neste caso, basta inserir os valores neste campo, separados por ponto-e-vírgula (;), sem espaçamentos, como por exemplo, três opções: Criação, Modificação ou Remoção. Devemos inserir no campo "Criação;Modificação;Remoção".

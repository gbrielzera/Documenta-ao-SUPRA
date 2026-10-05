# Criação de Campos Customizados

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Data Objects > Entrada de Dados > Criação de Campos Customizados

A criação de Campos Customizados através do Editor de Processos é realizado através da seguinte opção, que se encontra no barra de menus. Neste tópico descrevemos a criação, edição ou exclusão de um novo campo customizado.

Menu Campos

Ao clicar sobre o botão, será exibida uma tela contendo todos os campos cadastrados.

Tela de campos customizados

Ao clicar para obter mais detalhes do campo, serão exibidas as especificações do campo:

### Propriedades do campo customizado

Nos próximos parágrafos vamos detalhar cada parâmetro de cada campo.

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
- **Lógico**: verdadeiro (True) ou falso (False). Por padrão, este campo tem o valor False.

## Permitir inclusão em listagens de edição

Habilita a inclusão do campo na exibição de colunas em Telas de Listagem, como Telas de Cadastro ou na exibição de Ordens de Serviço.

Podemos determinar a forma de exibição de um campo customizado através do grupo de propriedades **Controle Edição**. Vamos agora detalhar sobre cada propriedade deste grupo.

## Ordem de Exibição

Ao exibir os controles em uma tela de exibição de campos customizados estes obedecem uma ordenação de exibição. Esta ordenação é determinada pela propriedade Ordem Exibição. Consiste em um número inteiro para esta ordenação.

## Controle

Indica qual controle será exibida para edição daquele campo customizado. Para mais informações, leia o tópico [Tipos de Controle](tipos_de_controle_os).

## Cadastro associado

É possível também criar propriedades customizadas que são registros de outros cadastros, de outras classes. Podemos fazer isto preenchendo o campo Classe referência. Vamos exemplificar mais adiante neste tópico sobre este assunto quando criamos controles do tipo ComboBox.

## Script para a recuperação de opções

Este script python pode ser utilizado para recuperar dados que serão exibidos na listagem de opções para seleção. Neste script devemos preencher uma lista de objetos denominada Itens (disponível no script) com estes valores de opções. Para realizar este preenchimento podemos utilizar, por exemplo, a função **DB.ExecuteDataTable **para recuperar dados a partir de banco via comando SQL.

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

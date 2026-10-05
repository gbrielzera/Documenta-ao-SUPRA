# Controles pré-definidos para customização

Caminho: Guia para Administradores > Portal de Processos > Customizações de aparência > Skins de páginas > Criando uma Skin > Controles pré-definidos para customização

Existem alguns controles pré-definidos para customização do skin: o controle de menu, texto, logotipo, link de conexão e um controle genérico.

Neste tópico, explicaremos mais detalhadamente sobre cada um destes:

## Menu

O menu exibe as páginas criadas do portal, o usuário conectado, um botão para retornar para o Workspace e um botão para se desconectar.

Controle Menu

O controle de menu permite definir a utilização do modo de abas, a exibição do link de conexão e a orientação do menu:

Propriedades do Controle

### UtilizaModoAbas

Modifica o modo de exibição dos itens de menu na barra, que pode ser por abas ou, por padrão, botões. Exemplos:

- UtilizaModoAbas=”True”:

Modo Abas

- UtilizaModoAbas=”False”:

Modo de Botões

ExibeLinkConexao Determina a visibilidade do botão Conectar/Desconectar. Exemplos:

- ExibeLinkConexao=”True”:

Exibindo botão Desconectar

- ExibeLinkConexao=”False”:

Botão oculto

OrientacaoVertical Modifica a disposição do menu superior, podendo ser disposto verticalmente ou horizontalmente. Exemplos:

- OrientacaoVertical=”True”:

Menu horizontal

- OrientacaoVertical=”False” e movendo o controle menu do PANEL_HEADER para o PANEL_LEFT:

Menu vertical

## Controle de Texto

Esse controle exibe um texto pré-defino conforme o exemplo:

Controle Texto

O controle permite a redefinição das propriedades de texto, negrito, tamanho da fonte, cor e classe css.

Propriedades do Controle

As propriedades que este controle possui são:

- **Texto** (string): Texto que será exibido na tela.
- **Negrito** (boolean): Aceita valores “True” e “False”
- **TamanhoFonte** (FontUnit): Modifica o tamanho da fonte do texto. Aceita valores como: “Large”, “Larger”, “Medium”, “Small”, ”Smaller”, “XLarge”, “XSmall”, “XXLarge”, “XXSmall”.
- **Cor** (Hexadecimal): Modifica a cor do texto e seu valor deverá ser preferencialmente em hexadecimal, exemplo: “#000FFF”, mas pode ser pelo nome da cor em inglês, como por exemplo: “Black”, “Orange”, “Blue”, etc.
- **ClasseCss** (string): Todas as opções do controle de texto podem ser modificadas também via css. Após criar um estilo e adicioná-lo em algum lugar visível à página, basta preencher essa propriedade com o nome da classe css.

## Logotipo

O Logotipo exibe a imagem da empresa que foi configurada no Supravizio.

Controle Logotipo

Esse controle permite a alteração da altura e largura:

Propriedades do controle

- **Altura** (inteiro): Define a altura do logotipo, o valor dado será convertido em pixels;
- **Largura** (inteiro): Define a largura do logotipo, o valor dado será convertido em pixels.

## Link de Conexão

Controle Link

Para utilizar o link de conexão na página é necessário adicionar o seguinte código no começo do arquivo da skin:

<%@ Register src="../Controles/LinkConexao.ascx" tagname="LinkConexao" tagprefix="uc4" %>

Código de Importação do Controle

O controle de link de conexão pode ser configurado para exibir uma imagem para desconectar/conectar e um texto para conectar/desconectar.

Propriedades do Link

**Importante**: Ao adicionar um novo controle na página, é necessário verificar se o tagprefix já está sendo utilizado em outro controle, devido a possíveis conflitos causados por tais duplicidades.

Exemplo de código

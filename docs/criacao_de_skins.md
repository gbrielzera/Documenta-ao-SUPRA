# Criando uma Skin

Caminho: Guia para Administradores > Portal de Processos > Customizações de aparência > Skins de páginas > Criando uma Skin

Neste tutorial, vamos criar uma nova skin a partir dos arquivos da skin padrão.

Criando novos arquivos

Neste primeiro momento, iremos multiplicar os arquivos já existentes para utilizarmos como base nas alterações. Para isso, acessamos o caminho: "[diretório do site do Supravizio]/Portal/Classico/Skin", onde se encontram os arquivos:

Pasta dos arquivos

Duplique a pasta e altere o nome da nova para diferenciar da já existente:

Nova pasta clonada

Após a criação dos arquivos da skin, é necessário executar um comando SQL na base de dados para cadastrar a nova skin, assim como no exemplo abaixo:

Exemplo de comando

A Tabela **SKIN** possui as seguintes colunas:

- **ID_SKIN**: Essa coluna deverá conter apenas valores inteiros e únicos, para preencher adicione +1 ao maior número da coluna ID_SKIN + 1;
- **ID_DOMAIN**: Identificador do domínio do Supravizio, o valor é alterado apenas quando o Supravizio possui mais que um domínio, se não houver, preencher com o valor padrão;
- **DESCRICAO**: Representação textual da skin;
- **URL**: Nome da pasta criada que contém os arquivos da nova skin;
- **SIGLA**: Identificador textual da skin, deve ser única em toda a tabela.

## Alterando o arquivo

A customização da skin que está sendo criada pode ser no arquivo Skin.ascx, que contém o html do layout da página, localizado dentro da pasta da skin:

Arquivo a ser alterado

Abrindo o arquivo Skin.ascx com um editor de texto, vamos ter o seguinte resultado:

Arquivo da skin padrão

### Divisões do layout

O PANEL_HEADER é composto por três controles: Controle de texto do portal, logotipo e o menu com as páginas:

Controle PANEL_HEADER

O PANEL_LEFT e o PANEL_RIGHT, exibidos abaixo, possibilitam configurar as margens laterais da página:

Controle PANEL_LEFT

Controle PANEL_RIGHT

O PANEL_CONTENT é o container de todos os módulos da página:

Controle PANEL_CONTENT

O PANEL_FOOTER é o rodapé da página:

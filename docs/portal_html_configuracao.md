# Configurando o Módulo

Caminho: Guia para Administradores > Portal de Processos > Módulos > Módulo de Conteúdo HTML > Configurando o Módulo

Para este módulo, podem ser configurados os seguintes parâmetros:

Configurador do módulo Editor HTML

## Título

Define o descritivo da página HTML, será exibida na parte superior do módulo.

## Exibição do conteúdo

- **Expandido** - permitirá a expansão do conteúdo e virá como padrão o conteúdo por completo;
- **Retraído** - idem ao anterior, porém, virá como padrão apenas o título do conteúdo, sendo necessário clicar no item para exibir o conteúdo;
- **Nenhum** - Será exibido o título, seguido do conteúdo, sem possibilidade de expandir nem retrair.

Na aba conteúdo, há um Editor HTML comum, com todas as possibilidades de inserção de conteúdo que a linguagem permite inserir.

Apenas duas particularidades sobre o uso deste editor merecem algum maior esclarecimento.

## Redirecionamento para páginas do próprio Portal

Ao clicar no ícone **Inserir Link**, será exibido um popup e em Page serão listadas as páginas disponíveis.

Através deste facilitador, o configurador irá montar a tag HTML com o link diretamente para a respectiva página.

Inserção de links para páginas do Portal ou externas

Outra funcionalidade em especial é a possibilidade de inserção de textos dinâmicos definidos por script.

No combo indicado abaixo, há cinco opções de complementos para serem inseridos no HTML.

Conteúdo de texto dinâmico

Na aba Conteúdo Dinâmico, é possível definir o valor deste complemento (no caso abaixo, o nome da pessoa conectada).

Script para definição do conteúdo dinâmico

Neste script, é possível também recuperar parâmetros passados pelo link da página, em casos por exemplo, de links recebidos em comunicados de Ordens de Serviço.

Script recuperando parâmetro

Ao acessar a página com a passagem do parâmetro, terá o seguinte conteúdo:

Texto com valor recuperado

Importante: Caso haja necessidade de ocultar o conteúdo no link, é possível utilizar os métodos **Utils.EncryptUrl** para criptografar os parâmetros na geração do link e **Utils.DecryptUrl **durante a recuperação.

# Bibliotecas de Scripts

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Bibliotecas de Scripts

Em muitos casos, precisamos usar uma função em vários scripts ou a mesma utilizada em um mesmo diversas vezes, tornando necessário copiá-los toda vez que precisarmos em algum script. Esta repetição torna ainda mais difícil tarefas como manutenção de scripts em caso de falhas e alterações, até mesmo por conta do versionamento de fluxos, devido a necessidade de manutenção também em versões anteriores.

Para evitar estes problemas, podemos utilizar bibliotecas de scripts, que são coleções de funções e importá-las para serem reutilizadas em outros scripts.

O acesso às bibliotecas está disponível no menu do [Editor de Processos](editor_de_processo). Para acessar os scripts existentes ou criar uma nova, basta clicar sobre o mesmo:

Opção no Editor de Processos

A seguir, iremos seguir com um exemplo na criação de uma função e como reutilizá-la no processo.

Para adicionar uma nova biblioteca, clique em **Novo**.

Criação de nova biblioteca

Neste caso, criaremos uma biblioteca com funções relativas a serviço de diretório, o qual vamos chamar de "Active Directory".

Nome da Biblioteca

Logo, será aberta uma nova aba no **Editor de Processos** para que edição do script:

Editor de Scripts

O script a ser inserido deve possuir apenas as definições das funções, assim como os parâmetros a serem recebidos.

Função criada

Terminada a edição, clique em **Salvar**.

Botão Salvar

Criada a biblioteca, vamos utilizar a função no **Script Início** de uma atividade de um processo.

Script Início

Será aberta uma nova aba contendo o editor. Nela, clique com o botão direito do mouse e em seguida, em **Importar bibliotecas de scripts **no menu aberto:

Importação de bibliotecas

Clicando nesta opção, será aberto um diálogo contendo as opções de seleção de scripts a serem utilizados. Selecione a biblioteca que criamos para ser importada.

Tela de seleção de bibliotecas

Clique em **Concluir** para finalizar a seleção. Assim, as funções da biblioteca importada estarão disponíveis para uso também no script em edição.

Script criado

**Observação:** O cabeçalho inserido é somente-leitura, caso seja necessário remover alguma biblioteca ou fazer alterações, basta entrar na tela de seleção de bibliotecas e remover as que não forem utilizadas.

Removendo biblioteca importada

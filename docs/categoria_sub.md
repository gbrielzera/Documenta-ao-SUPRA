# Categoria

Caminho: Janelas > Processo > Categoria

Classificação manual atribuída a Ordens de Serviço associadas com uma cor e com possibilidade de exibição na barra de rolagem de Ordens de Serviço. Para definição das cores é utilizado o modelo RGB que é baseado na teoria de visão colorida tricromática.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Processo | Processos | Categorias**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Descrição** | Descrição detalhada da Categoria Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRICAO da tabela [CATEGORIA](dados_categoria). |
|---|---|
| **Ativo** | Indica que a Categoria está ativa no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ATIVO da tabela [CATEGORIA](dados_categoria). |
| **Vermelho** | Fator vermelho para formação da cor da categoria. Para definição das cores é utilizado o modelo RGB que é baseado na teoria de visão colorida tricromática. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna VERMELHO da tabela [CATEGORIA](dados_categoria). |
| **Verde** | Fator verde para formação da cor da categoria. Para definição das cores é utilizado o modelo RGB que é baseado na teoria de visão colorida tricromática. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna VERDE da tabela [CATEGORIA](dados_categoria). |
| **Azul** | Fator azul para formação da cor da categoria. Para definição das cores é utilizado o modelo RGB que é baseado na teoria de visão colorida tricromática. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna AZUL da tabela [CATEGORIA](dados_categoria). |
| **Visível Painel Alertas do Workspace** | Indica que Ordens de Serviço desta categoria serão visíveis na barra de rolagem localizada na parte inferior da tela Workspace (Painel de Alertas). Esta configuração ainda está condicionada a regra de visualização do Grupo de Trabalho (veja as configurações do Grupo de Trabalho do solucionador). Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna VISIVEL_PAINEL_WS da tabela [CATEGORIA](dados_categoria). |

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Categoria a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Categoria se este for utilizado em um dos cadastros abaixo:

- Ordem de Serviço

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

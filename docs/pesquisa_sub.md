# Pesquisa

Caminho: Janelas > Processo > Pesquisa

Uma Pesquisa de Satisfação é composta por um formulário enviado para Clientes após finalização de uma Ordem de Serviço. As respostas coletadas destas pesquisas podem ser utilizadas para construção de Indicadores de Desempenho - KPI's.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Processo | Processos | Pesquisa de Satisfação | Pesquisas geradas**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Identificador** | Identificador da Pesquisa de Satisfação. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ID_PESQUISA da tabela [PESQUISA](dados_pesquisa). |
|---|---|
| **Assunto** | Assunto abordado pela Pesquisa de Satisfação Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ASSUNTO da tabela [PESQUISA](dados_pesquisa). |
| **Ordem de Serviço** | Uma Ordem de Serviço é uma ocorrência de Processo em atendimento a uma solicitação de serviço de Tecnologia da Informação. Ordens de Serviço podem ser abertas na aplicação do Portal de Processos ou na transação Workspace do sistema Supravizio. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Avaliador** | Avaliador da Pesquisa de Satisfação Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Situação** | Indica a Situação da Pesquisa de Satisfação. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna SITUACAO da tabela [PESQUISA](dados_pesquisa). |
| **Data/hora criação** | Data e hora que a Pesquisa de Satisfação foi gerada. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DATA_HORA_CRIACAO da tabela [PESQUISA](dados_pesquisa). |
| **Data/hora resposta** | Data e hora em que foi respondida a Pesquisa |
| **Respondida no Autoatendimento** | Indica que a Pesquisa de Satisfação foi respondida pelo Cliente utilizando a aplicação de Autoatendimento. |
| **Comentário avaliador** | Comentário gravado pelo Avaliador no instante em que a Pesquisa é respondida |
| **Motivo cancelamento** | Motivo de Cancelamento da Pesquisa |
| **Responsável cancelamento** | Pessoa responsável pelo Cancelamento da Pesquisa de Satisfação Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Classe Pesquisa Satisfação** | Uma Classe de Pesquisa de Satisfação define um conjunto de configurações utilizado para geração de Pesquisas de Satisfação enviadas para clientes após finalização de uma Ordem de Serviço. O envio da pesquisa está condicionado ao evento terminador utilizado na definição do processo aplicado em Ordens de Serviço alvo da pesquisa. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |

| **Item de Pesquisa** | Item a ser avaliado em uma Pesquisa Todos os registros desta coleção de dados são mantidos na tabela [ITEM_PESQUISA](dados_item_pesquisa). |
|---|---|

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Pesquisa a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

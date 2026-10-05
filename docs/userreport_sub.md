# Relatórios

Caminho: Janelas > Utilitários > Relatórios

Relatório criado pelo usuário utilizando o Editor de Relatórios

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Utilitários | Editor de Relatórios**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Descrição** | Descrição detalhada do Report Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRIPTION da tabela [SV_REPORT](dados_sv_report). |
|---|---|
| **Ativo** | Indica que o Report está ativo no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ENABLED da tabela [SV_REPORT](dados_sv_report). |
| **Data/hora criação** | Data/hora de criação do relatório Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna CREATION_DATE da tabela [SV_REPORT](dados_sv_report). |
| **Criado por** | Usuário que criou o relatório Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Bloqueado por** | Usuário que bloqueou o relatório para edição. Durante a existência do bloqueio somente este usuário pode realizar modificações. O desbloqueio pode ser desfeito pelo criador do relatório, autor do bloqueio ou qualquer outro que possua o perfil 'Admin' Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Desbloqueado por** | Pessoa que realizou o desbloqueio na edição do relatório. Somente o criador do relatório, o responsável pelo bloqueio e usuários com o perfil 'Admin' estão autorizados a desbloquear o relatório. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Comentário de bloqueio** | Comentário registrado pelo usuário que realizou ou cancelou o bloqueio de edição |

| **Parâmetros** | Parâmetros do relatório Todos os registros desta coleção de dados são mantidos na tabela [SV_REPORT_PARAM](dados_sv_report_param). |
|---|---|

| **Layout do relatório** | Layout do relatório mantidos em um controle Report serializado |
|---|---|

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Relatórios a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

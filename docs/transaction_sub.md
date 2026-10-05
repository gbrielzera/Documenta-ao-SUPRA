# Transação

Caminho: Janelas > Utilitários > Transação

Uma Transação representa o ponto de entrada para uma funcionalidade do sistema (Tela de sistema, Web Services, etc). Para cada Transação é possível a configuração de autorização por Perfil de acesso.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Utilitários | Segurança | Transações**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Código** | Código da transação utilizado para acesso via barra de ferramentas. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Todos os caracteres preenchidos são convertidos automaticamente para minúsculo - Não é permitida duplicidade de valores Este campo é mantido na coluna SHORT_NAME da tabela [SV_TRANSACTION](dados_sv_transaction). |
|---|---|
| **Descrição resumida** | Descrição resumida da Transação. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna TEXT da tabela [SV_TRANSACTION](dados_sv_transaction). |
| **Descrição** | Descrição detalhada sobre a transação. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRIPTION da tabela [SV_TRANSACTION](dados_sv_transaction). |
| **Ativo** | Indica que a Transação está ativa. Quando desativada a Transação não é mais visível para o usuário. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ENABLED da tabela [SV_TRANSACTION](dados_sv_transaction). |
| **Url** | Caminho para objeto inicial da Transação Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Não é permitida duplicidade de valores Este campo é mantido na coluna URL da tabela [SV_TRANSACTION](dados_sv_transaction). |
| **Module** | System Module Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Descrição resumida original** | Descrição resumida original Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ORIGINAL_TEXT da tabela [SV_TRANSACTION](dados_sv_transaction). |
| **Descrição original** | Descrição detalhada original. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ORIGINAL_DESCRIPTION da tabela [SV_TRANSACTION](dados_sv_transaction). |

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Transação a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Transação se este for utilizado em um dos cadastros abaixo:

- [Comando](command_sub)
- Autorização de Perfil
- Acesso a Transações

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

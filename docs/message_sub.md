# Mensagens

Caminho: Janelas > Utilitários > Mensagens

Mensagens enviadas em resposta a Eventos ou ferramentas de comunicação do sistema.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Utilitários | Mensagens**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Identificador** | Identificador da Mensagem. Este valor é acrescentados no Subject da mensagem. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ID da tabela [SV_MESSAGE](dados_sv_message). |
|---|---|
| **Assunto** | Campo Assunto da Mensagem. Em mensagens de respostas o assunto é acrescido do ID da Mensagem. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna SUBJECT da tabela [SV_MESSAGE](dados_sv_message). |
| **Corpo** | Corpo da mensagem para envio. O formato pode ser configurado pela propriedade Mime-Format. |
| **Situação** | Situação da Mensagem Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna STATUS da tabela [SV_MESSAGE](dados_sv_message). |
| **Data/hora requisição** | Data e hora em que a Mensagem foi registrada Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna REQUEST_DATE da tabela [SV_MESSAGE](dados_sv_message). |
| **Remetente** | Endereço de email remetente da mensagem. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna FROM_ADDRESS da tabela [SV_MESSAGE](dados_sv_message). |
| **Mensagem original** | Mensagem inicial da comunicação. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Detalhes sobre erros de envio** | Relatório contendo detalhes sobre erros ocorridos durante o envio da mensagem. |
| **Registro associado** | Representação textual do objeto de negócio associado com a Mensagem. |
| **Data de expiração para temporalidade** | Após a data de expiração o registro de mensagem é excluído do sistema. |
| **Endereço de reply** | Conta utilizada para reply quando o destinatário responder o comunicado. Quando não informada é utilizada a conta configurada no job de envio de emails. |

| **Destinatários** | Destinatários da Mensagem Todos os registros desta coleção de dados são mantidos na tabela [SV_RECIPIENT](dados_sv_recipient). |
|---|---|

| **Anexos** | Arquivos anexados na Mensagem Todos os registros desta coleção de dados são mantidos na tabela [SV_MESSAGE_ATTACH](dados_sv_message_attach). |
|---|---|

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Mensagens se este for utilizado em um dos cadastros abaixo:

- [Mensagens](message_sub)

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

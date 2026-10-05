# Mensagem Evento

Caminho: Janelas > Processo > Tipo Evento > Mensagem Evento

Mensagens programadas para um determinado Evento.

Na tabela abaixo temos os principais campos deste cadastro:

## Campos do cadastro

| **Descrição** | Descrição detalhada sobre a Mensagem do Evento Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRICAO da tabela [MENSAGEM_EVENTO](dados_mensagem_evento). |
|---|---|
| **Modelo de comunicado** | Template utilizado para montar o corpo do email. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Destinatários** | Papel de processo que define os destinatários da mensagem Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Processo alvo** | O envio da mensagem ocorre somente para Ordens de Serviço deste Processo. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Temporalidade (em dias)** | Define após quantos dias a mensagem será excluída da base de dados. Se for 0 (zero) ela será excluída assim que o email for enviado. Se estiver sem preenchimento a mensagem não será excluída. Para este campo existem as seguintes regras: - A temporalidade deve ser maior ou igual a 0 Este campo é mantido na coluna TEMPORALIDADE da tabela [MENSAGEM_EVENTO](dados_mensagem_evento). |
| **Endereço de reply** | Endereço configurado para reply na mensagem enviada. Se não for configurado então será utilizada a caixa de email do job de envio de mensagens. |
| **Listagem de destinatários** | Relação de endereços de emails separados por ponto e vírgula que são utilizados como destinatários do comunicado. Pode ser preenchido em conjunto com o papel de processo de Destinatários. |

| **Script** | Script para montagem da Mensagem a ser enviada. Neste script são preenchidos atributos do objeto Mensagem. Se não for preenchido qualquer um destes atributos então a mensagem não é enviada. |
|---|---|

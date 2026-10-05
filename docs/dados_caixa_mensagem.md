# CAIXA_MENSAGEM

Caminho: Customização > Modelo de dados > Processo > CAIXA_MENSAGEM

Caixas de mensagens (email por exemplo) que são monitoradas pela máquina de processos e geram alguma ação configurada em eventos. No caso de caixas de emails o acesso é realizado via protocolo POP3. Após processamento a mensagem é removida do servidor.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CAIXA_MENSAGEM** | Número sequencial gerado automaticamente pelo sistema para Identificar um CaixaEmail | int | number(6,0) | Não |
| **NOME** | Nome da caixa de mensagem que será monitorada pela máquina de processos. Não é permitido o uso da caixa utilizada pela rotina de envio de emails e redirecionamentos. | varchar(100) | varchar(100) | Não |
| **SENHA** | Senha da caixa de mensagem monitorada. Esta senha é necessária para acessar a caixa. | varchar(500) | varchar(500) | Sim |
| **PORTA_POP3** | Porta do protocolo TCP/IP utilizada para acesso ao servidor de email via POP3. Se não for preenchida então será utilizada o padrão 110. | int | number(6,0) | Sim |
| **SERVIDOR_POP3** | Servidor POP3 onde está localizada a caixa de email configurada. | varchar(500) | varchar(500) | Sim |
| **TIPO_CAIXA** | Tipo de caixa de mensagem | varchar(250) | varchar(250) | Não |

Tabelas que dependem de CAIXA_MENSAGEM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **CAIXA_MENSAGEM** \| \|---\|---\| \| ID_CAIXA_EMAIL \| ID_CAIXA_MENSAGEM \| |

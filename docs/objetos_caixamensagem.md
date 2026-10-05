# CaixaMensagem

Caminho: Customização > Modelo de objetos > Processo > CaixaMensagem

Caixas de mensagens (email por exemplo) que são monitoradas pela máquina de processos e geram alguma ação configurada em eventos. No caso de caixas de emails o acesso é realizado via protocolo POP3. Após processamento a mensagem é removida do servidor.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um CaixaEmail | Inteiro |
| **NomeCaixa** | Nome da caixa de mensagem que será monitorada pela máquina de processos. Não é permitido o uso da caixa utilizada pela rotina de envio de emails e redirecionamentos. | String |
| **PortaPOP3** | Porta do protocolo TCP/IP utilizada para acesso ao servidor de email via POP3. Se não for preenchida então será utilizada o padrão 110. | Inteiro |
| **Senha** | Senha da caixa de mensagem monitorada. Esta senha é necessária para acessar a caixa. | String |
| **ServidorPOP3** | Servidor POP3 onde está localizada a caixa de email configurada. | String |
| **TipoCaixa** | Tipo de caixa de mensagem | [TipoCaixaMensagem](enum_tipocaixamensagem) |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | CaixaMensagem Carrega(int i); |
| **Novo** | Cria um novo registro do tipo CaixaMensagem | CaixaMensagem Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | CaixaMensagem Carrega(string nomePropriedade, object valorPropriedade); |

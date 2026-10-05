# Caixas de mensagem monitoradas

Caminho: Janelas > Processo > Caixas de mensagem monitoradas

Caixas de mensagens (e-mail por exemplo) que são monitoradas pela máquina de processos e geram alguma ação configurada em eventos. No caso de caixas de emails o acesso é realizado via protocolo POP3. Após processamento a mensagem é removida do servidor.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Processo | Processos | Caixas de Mensagens**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Nome** | Nome da caixa de mensagem que será monitorada pela máquina de processos. Não é permitido o uso da caixa utilizada pela rotina de envio de emails e redirecionamentos. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Não é permitida duplicidade de valores Este campo é mantido na coluna NOME da tabela [CAIXA_MENSAGEM](dados_caixa_mensagem). |
|---|---|
| **Tipo** | Tipo de caixa de mensagem Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna TIPO_CAIXA da tabela [CAIXA_MENSAGEM](dados_caixa_mensagem). |
| **Senha** | Senha da caixa de mensagem monitorada. Esta senha é necessária para acessar a caixa. Para este campo existem as seguintes regras: Este campo é mantido na coluna SENHA da tabela [CAIXA_MENSAGEM](dados_caixa_mensagem). |
| **Servidor POP3** | Servidor POP3 onde está localizada a caixa de e-mail configurada. |
| **Porta POP3** | Porta do protocolo TCP/IP utilizada para acesso ao servidor de e-mail via POP3. Se não for preenchida então será utilizada o padrão 110. |

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Caixas de mensagem monitoradas a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Caixas de mensagem monitoradas se este for utilizado em um dos cadastros abaixo:

- Atividade

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

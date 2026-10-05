# Tipo Evento

Caminho: Janelas > Processo > Tipo Evento

Um Tipo de Evento define um marco (evento) ocorrido em uma Ocorrência de Processo. Este evento pode ser publicado para o Cliente para que este realize o acompanhamento da sua solicitação. Um Tipo de Evento pode representar também uma ferramenta de envio de comunicados para Pessoas diversas.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Processo | Processos | Tipos de Eventos**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Código** | Código que identifica o Evento Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Todos os caracteres preenchidos são convertidos automaticamente para minúsculo - Não é permitida duplicidade de valores Este campo é mantido na coluna CODIGO da tabela [TIPO_EVENTO](dados_tipo_evento). |
|---|---|
| **Nome** | Nome Abreviado do Tipo de Evento Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna NOME da tabela [TIPO_EVENTO](dados_tipo_evento). |
| **Descrição** | Texto que descreve claramente quando um Evento deste Tipo ocorre. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRICAO da tabela [TIPO_EVENTO](dados_tipo_evento). |
| **Ativa mensagens** | Ativa ou desativa o Envio de Mensagens na ocorrência de eventos deste Tipo Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ATIVA_MENSAGENS da tabela [TIPO_EVENTO](dados_tipo_evento). |
| **Tipo mensagem** | Tipo de Mensagem gerada Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna TIPO_MENSAGEM da tabela [TIPO_EVENTO](dados_tipo_evento). |
| **Script mensagem** | Script para determinar a mensagem gerada no Evento |

| **Mensagens** | Template de mensagens que serão enviadas quando ocorrer um Evento deste Tipo Todos os registros desta coleção de dados são mantidos na tabela [MENSAGEM_EVENTO](dados_mensagem_evento). |
|---|---|

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Tipo Evento a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Tipo Evento se este for utilizado em um dos cadastros abaixo:

- Eventos Ocorrências
- Classe Apontamento
- Gatilho de Associação

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

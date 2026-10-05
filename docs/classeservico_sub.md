# Tipo de Serviço

Caminho: Janelas > Processo > Tipo de Serviço

Um Tipo de Serviço define classificações para Serviços. Registros deste cadastro são utilizados em diversas configurações do sistema incluindo durante a definição de Processos.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Processo | Serviços | Tipos de Serviços**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Descrição** | Descrição detalhada do Tipo de Serviço Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRICAO da tabela [CLASSE_SERVICO](dados_classe_servico). |
|---|---|
| **Sigla** | Nome resumido (código) que identifica unicamente um Tipo de Item de Configuração Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Todos os caracteres preenchidos são convertidos automaticamente para minúsculo - Não é permitida duplicidade de valores - A Sigla deve conter somente letras maiúsculas Este campo é mantido na coluna SIGLA da tabela [CLASSE_SERVICO](dados_classe_servico). |
| **Ativo** | Indica que o Tipo de Serviço está ativa no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ATIVO da tabela [CLASSE_SERVICO](dados_classe_servico). |
| **Grupo de Serviços** | Segundo nível hierárquico de classificação no qual o tipo de Serviço está inserido. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Fator Prioridade** | Fator utilizado no cálculo de Prioridade. É utilizado como valor default quando não for informado no nível de Serviço. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Tipo de Serviço a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Tipo de Serviço se este for utilizado em um dos cadastros abaixo:

- [Serviço](servico_sub)
- Restrições de Serviços em Subprocessos
- Restrições Anexos por Serviço
- Restrições Itens Aprovação por Serviço

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

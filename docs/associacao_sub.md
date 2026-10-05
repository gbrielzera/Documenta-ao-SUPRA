# Associação

Caminho: Janelas > Processo > Associação

Uma Associação define um relacionamento entre duas Ocorrências de Processo. Estas associações podem ser estabelecidas pelo usuário na tela de edição de Ordens de Serviço ou automaticamente por configuração de Processo. Para criação de uma Associação é necessário definir: um Tipo de Subprocesso para cada uma das ocorrências, uma frase para leitura da Associação, outra fase para leitura inversa da Associação e finalmente a cardinalidade desejada.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Processo | Processos | Associações**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Nome** | Nome para identificação e recuperação da Associação. O nome não pode conter espaços e deve conter apenas caracteres alfanuméricos. Também deve ser único entre todas as Associações e utilizado em scripts para recuperação da Associação. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Todos os caracteres preenchidos são convertidos automaticamente para minúsculo - Não é permitida duplicidade de valores Este campo é mantido na coluna NOME da tabela [ASSOCIACAO](dados_associacao). |
|---|---|
| **Subprocesso chamador** | Tipo de Subprocesso de Ocorrências que são fonte (iniciadores) em Associações. Indica que podemos ter várias ou uma única ocorrência como Fonte no relacionamento. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Subprocesso invocado** | Tipo de Subprocesso de Ocorrências que é alvo (terminador) em Associações. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Frase Associação** | Frase utilizada para estabelecer a Associação. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna FRASE_ASSOC da tabela [ASSOCIACAO](dados_associacao). |
| **Frase Inversa** | Frase utilizada para representar o sentido inverso da Associação. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna FRASE_INV_ASSOC da tabela [ASSOCIACAO](dados_associacao). |
| **Ativo** | Indica que a Associação está ativa no Sistema. Se estiver inativa então não é possível a criação de novas associações desta natureza. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ATIVO da tabela [ASSOCIACAO](dados_associacao). |
| **Cardinalidade Fonte** | Cardinalidade da Associação no sentido Alvo para Fonte Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna CARD_FONTE da tabela [ASSOCIACAO](dados_associacao). |
| **Cardinalidade Alvo** | Cardinalidade da Associação no sentido Fonte para Alvo. Indica que podemos ter várias ou uma única ocorrência como Alvo no relacionamento. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna CARD_ALVO da tabela [ASSOCIACAO](dados_associacao). |

| **Gatilhos** | Eventos que são disparados pelo sistema na ocorrência de um determinado Tipo de Evento. Todos os registros desta coleção de dados são mantidos na tabela [GATILHO_ASSOC](dados_gatilho_assoc). |
|---|---|

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Associação a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Associação se este for utilizado em um dos cadastros abaixo:

- Associação Ocorrência
- Atividade
- Associação com Subprocesso

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

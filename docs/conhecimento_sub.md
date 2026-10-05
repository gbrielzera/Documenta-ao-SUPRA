# Conhecimento

Caminho: Janelas > Ativos > Conhecimento

Artigo de Base de Conhecimento

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Ativos | Base de Conhecimento**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Identificador** | Número sequencial gerado automaticamente para Identificar um Item de Configuração Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ID_ITEM da tabela [ITEM](dados_item). |
|---|---|
| **Tipo Item Configuração** | Tipo de Item de Configuração associado Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Situação** | Configura todos os Estados possíveis para um Item do Tipo de Item de Configuração associada. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Título** | Título Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna TITULO da tabela [CONHECIMENTO](dados_conhecimento). |
| **Sumário** | Sumário Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna SUMARIO da tabela [CONHECIMENTO](dados_conhecimento). |
| **Palavras chave** | Palavras Chave para pesquisa |
| **Data cadastro** | Data em que o Item de Configuração foi cadastrado no sistema. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DATA_CADASTRO da tabela [ITEM](dados_item). |
| **Usuário responsável** | Usuário responsável pelo Item de Configuração. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Fator Prioridade** | Fator utilizado para cálculo de Prioridade em Ocorrências. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |

| **Tópicos** | Tópicos que compõem o artigo. Estes tópicos são ordenados pelo sequencial cadastrado do tipo de artigo. Todos os registros desta coleção de dados são mantidos na tabela [TOPICO_ARTIGO](dados_topico_artigo). |
|---|---|

| **Dependências** | Itens de configuração que possuem relação de Dependência. Todos os registros desta coleção de dados são mantidos na tabela [ITEM_DEPENDENCIA](dados_item_dependencia). |
|---|---|

| **Observações** | Observações a respeito do Item de Configuração Todos os registros desta coleção de dados são mantidos na tabela [OBSERVACAO_ITEM](dados_observacao_item). |
|---|---|

| **Redefinição de Papéis** | Atores Todos os registros desta coleção de dados são mantidos na tabela [ATOR_ITEM](dados_ator_item). |
|---|---|

| **Serviços onde o artigo será aplicado** | Regras de utilização do artigo em função de Serviços e Tipos de Serviços. Estas regras influenciarão o mecanismo de recuperação de artigos durante a busca manual ou automática. Todos os registros desta coleção de dados são mantidos na tabela [APLIC_CONH_SERV](dados_aplic_conh_serv). |
|---|---|

| **Restrição de acesso** | Composição entre permissão e conhecimento Todos os registros desta coleção de dados são mantidos na tabela [PERM_CONH_PAPEL](dados_perm_conh_papel). |
|---|---|

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Conhecimento a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Conhecimento se este for utilizado em um dos cadastros abaixo:

- Uso de Conhecimento

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

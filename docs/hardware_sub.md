# Equipamento

Caminho: Janelas > Ativos > Equipamento

Itens de Configuração do tipo 'Equipamento'

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Ativos | Equipamentos**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Identificador** | Número sequencial gerado automaticamente para Identificar um Item de Configuração Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ID_ITEM da tabela [ITEM](dados_item). |
|---|---|
| **Tipo Item Configuração** | Tipo de Item de Configuração associado Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Situação** | Configura todos os Estados possíveis para um Item do Tipo de Item de Configuração associada. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Etiqueta identificação** | Número da Etiqueta de Identificação do Equipamento pela equipe de suporte. Este número pode ser utilizado pelo Solucionador durante o atendimento de um chamado. |
| **Número série** | Número de série do Item |
| **Patrimonio** | Identificação de Patrimonio |
| **Descrição** | Descrição detalhada sobre o Item de configuração Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRICAO da tabela [ITEM](dados_item). |
| **Usuário responsável** | Usuário responsável pelo Item de Configuração. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Local** | Localização do Equipamento Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Tipo posse** | Tipo de Posse Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Fornecedor** | Fornecedor para o Item. Se for mantido por equipe própria então não preencher. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Modelo** | Modelo de Item de Configuração segundo especificação de um Fabricante. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Comentários para Cliente** | Comentário sobre o Item destinados ao Cliente. Para histórico de observações utilize a relação de Observações. |
| **Fator Prioridade** | Fator utilizado para cálculo de Prioridade em Ocorrências. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Código OCS** | Código do hardware original do banco de dados OCS |
| **Tamanho da memória em MB** | Tamanho da memória detectada pelo OCS NG em megabytes |

| **Dependências** | Itens de configuração que possuem relação de Dependência. Todos os registros desta coleção de dados são mantidos na tabela [ITEM_DEPENDENCIA](dados_item_dependencia). |
|---|---|

| **Componentes** | Componentes de um Item de Configuração Todos os registros desta coleção de dados são mantidos na tabela [ITEM_COMPONENTE](dados_item_componente). |
|---|---|

| **Redundâncias** | Redundâncias existentes do Ativo. Todos os registros desta coleção de dados são mantidos na tabela [ITEM_COPIA](dados_item_copia). |
|---|---|

| **Observações** | Observações a respeito do Item de Configuração Todos os registros desta coleção de dados são mantidos na tabela [OBSERVACAO_ITEM](dados_observacao_item). |
|---|---|

| **Usuários** | Usuários do Item de Configuração Todos os registros desta coleção de dados são mantidos na tabela [USUARIO_ITEM](dados_usuario_item). |
|---|---|

| **Redefinição de Papéis** | Atores Todos os registros desta coleção de dados são mantidos na tabela [ATOR_ITEM](dados_ator_item). |
|---|---|

| **Data cadastro** | Data em que o Item de Configuração foi cadastrado no sistema. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DATA_CADASTRO da tabela [ITEM](dados_item). |
|---|---|
| **Data entrega** | Data em que o Item foi entregue |
| **Data aceite** | Data de aceite do Item |
| **Data entrada produção** | Data de entrada em Produção. |
| **Data expiração garantia** | Data para Expiração de uma eventual garantia |
| **Data desativação** | Data de desativação do Item. |

| **Custo aquisição** | Custom total de aquisição do Item |
|---|---|
| **Custo manutenção mensal** | Valor do Custo de Manutenção Mensal do Item |
| **Preço aquisição** | Preço de aquisição do Item para demonstrativo de custeio pela rotina de Charge-back. O valor de aquisição é lançado no charge-back de competência relativa a Data de Entrega do Ativo. |
| **Preço manutenção mensal** | Preço de Charge-back de manutenção mensal |
| **Critério charge-back** | Critério para destino de custo no cálculo de Charge-back. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna CRIT_CHARGE_BACK da tabela [ITEM](dados_item). |

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Equipamento a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

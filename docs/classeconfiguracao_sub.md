# Tipo Item Configuração

Caminho: Janelas > Ativos > Tipo Item Configuração

Um Tipo de Item de Configuração é utilizado para classificar Itens de Configuração, que são ativos sujeitos a alteração (como entrada ou saída) em processos de negócio.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Ativos | Tipos de Itens de Configuração**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Descrição** | Texto que descreve claramente a classificação de um Item de Configuração. No caso de tipos que representam arquivos este descritivo não pode conter os caracteres \\ / : > ? * " pois este descritivo é utilizado para nomear pastas no repositório de arquivos. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRICAO da tabela [CLASSE_CONFIGURACAO](dados_classe_configuracao). |
|---|---|
| **Sigla** | Nome abreviado (código) utilizado para recuperar um Tipo de Item de Configuração em comandos SQL de relatórios ou scripts de customização. Esta sigla deve contar apenas números e letras. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Todos os caracteres preenchidos são convertidos automaticamente para minúsculo - Não é permitida duplicidade de valores - A Sigla deve conter somente números e letras maiúsculas Este campo é mantido na coluna SIGLA da tabela [CLASSE_CONFIGURACAO](dados_classe_configuracao). |
| **Super tipo** | Nome do Super Tipo associado que pode ser um Equipamento, Software, Dispositivo telefônico, Artigo da Base de Conhecimento ou Artefato (tipo genérico). Para cada Super tipo existe uma tela de cadastro no módulo de Ativos. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna SUPER_CLASSE da tabela [CLASSE_CONFIGURACAO](dados_classe_configuracao). |
| **Ativo** | Indica que o Tipo de Item de Configuração está ativo no sistema. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ATIVO da tabela [CLASSE_CONFIGURACAO](dados_classe_configuracao). |
| **Fator Prioridade** | Fator utilizado para cálculo de Prioridade em Ocorrências. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Habilita redefinição de Papéis** | Habilita a redefinição de Papéis por Itens da Classe. Papéis possuem uma definição global de Atores que pode ser sobreposta por um Serviço. Este parâmetro indica que Itens de Configuração desta Classe podem acumular um segundo nível de redefinição de Papéis, que ainda está condicionada a parametrização do Serviço. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna HAB_REDEF_PAPEIS da tabela [CLASSE_CONFIGURACAO](dados_classe_configuracao). |
| **Filtrar itens por Serviço na associação com Ordens de Serviço** | Sempre que um item deste tipo for associado a uma Ordem de Serviço (na tela de edição ou Portal) existirá um filtro implícito por componentes do Serviço informado na ocorrência de processo. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna FILTRO_SERVICO da tabela [CLASSE_CONFIGURACAO](dados_classe_configuracao). |
| **Incluir itens em uma Blacklist** | Indica que itens deste tipo fazem parte de um Blacklist Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna INC_BLACK_LIST da tabela [CLASSE_CONFIGURACAO](dados_classe_configuracao). |

| **Situações** | Situações possíveis para Itens da Classe Todos os registros desta coleção de dados são mantidos na tabela [SITUACAO_CLASSE](dados_situacao_classe). |
|---|---|

| **Tipos componentes** | Tipos de Itens de Configuração que podem ser utilizadas como Componentes. Todos os registros desta coleção de dados são mantidos na tabela [CLASSE_COMPONENTE](dados_classe_componente). |
|---|---|

| **Tipos dependentes** | Tipos de Itens de Configuração que podem ser associados como Dependências Todos os registros desta coleção de dados são mantidos na tabela [CLASSE_DEPENDENCIA](dados_classe_dependencia). |
|---|---|

| **Fonte dados** | Fonte de dados (válido somente para Artefatos) Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna FONTE_DADOS da tabela [CLASSE_CONFIGURACAO](dados_classe_configuracao). |
|---|---|
| **Forma de acesso** | Define o mecanismo utilizado para acessar o arquivo, que pode ser por Compartilhamento de rede ou pelo mecanismo de Download/upload. No segundo caso o arquivo é transferido para a máquina local e, após modificações, deve ser enviado para atualização no servidor. O valor default deste campo está condicionado a configuração do tipo de acesso default existente na tela de Configurações (grupo Configuração) Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna TIPO_ACESSO da tabela [CLASSE_CONFIGURACAO](dados_classe_configuracao). |
| **Tamanho máximo (em MB)** | Tamanho máximo (em megabytes) permitido por arquivo deste tipo. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna TAMANHO_MAXIMO da tabela [CLASSE_CONFIGURACAO](dados_classe_configuracao). |
| **Exigir comentário** | Determina se o Item pertencente a esta Classe de Configuração terá o campo Comentário como Obrigatório Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna COMENT_OBRIGATORIO da tabela [CLASSE_CONFIGURACAO](dados_classe_configuracao). |

| **Template Tópicos** | Tópicos que devem ser preenchidos na criação de artigos para a Base de Conhecimento. Quando um artigo é criado todos os tópicos são inicializados com o Template. Todos os registros desta coleção de dados são mantidos na tabela [TOPICO_CONH](dados_topico_conh). |
|---|---|

| **Valor custo** | Valor do Custo de Aquisição Padrão para Itens do tipo. Este valor pode ser redefinido com o campo correspondente no Item. |
|---|---|
| **Custo manutenção mensal** | Valor do Custo de Manutenção Mensal Padrão para Itens da Classe. Este valor pode ser redefinido com o campo correspondente no Item. |
| **Critério Charge-back** | Critério para destino de custo no cálculo de Charge-back. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna CRIT_CHARGE_BACK da tabela [CLASSE_CONFIGURACAO](dados_classe_configuracao). |
| **Agrupamento em Charge-back** | Define a forma como itens de charge-back apurado são agrupados no relatório apresentado para gestores de áreas clientes. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna AGRUP_ITENS da tabela [CLASSE_CONFIGURACAO](dados_classe_configuracao). |

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Tipo Item Configuração a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Tipo Item Configuração se este for utilizado em um dos cadastros abaixo:

- Item Configuração
- Tipo Componente
- Tipo Depedência
- Tipo redundância
- Componentes

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

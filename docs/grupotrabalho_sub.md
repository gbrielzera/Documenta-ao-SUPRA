# Grupo Trabalho

Caminho: Janelas > Recurso > Grupo Trabalho

Um Grupo de Trabalho define uma estrutura hierárquica de equipes contendo um coordenador e um ou mais solucionadores. O coordenador de um Grupo de Trabalho possui atribuições especiais podendo realizar diversas ações sobre Ordens de Serviço sob responsabilidade de seus subordinados. Um Grupo de Trabalho pode corresponder a um nível na hierarquia de Órgãos, porém não existe uma relação automática com este cadastro.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Recurso | Grupos de Trabalho**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Descrição** | Texto que descreve claramente o objetivo do Grupo de Trabalho. Este texto é utilizado em diversas telas e relatórios da aplicação Supravizio. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRICAO da tabela [GRUPO_TRABALHO](dados_grupo_trabalho). |
|---|---|
| **Sigla** | Nome resumido (código) utilizado para identificar um Grupo de Trabalho. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Todos os caracteres preenchidos são convertidos automaticamente para minúsculo - Não é permitida duplicidade de valores Este campo é mantido na coluna SIGLA da tabela [GRUPO_TRABALHO](dados_grupo_trabalho). |
| **Grupo Trabalho Pai** | Grupo de Trabalho que é o Ancestral na hierarquia. A hierarquia de Grupos de Trabalho não corresponde necessariamente a Estrutura Organizacional da Empresa. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Coordenador** | Coordenador do Grupo de Trabalho Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Ativo** | Indica que o Grupo de Trabalho está ativo. Quando ativo o Grupo de Trabalho pode ser utilizado na implementação de Papéis de Processo ou para lotação de profissionais. Quando um Grupo de Trabalho se torna Inativo automaticamente todos os profissionais associados também são desativados. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ATIVO da tabela [GRUPO_TRABALHO](dados_grupo_trabalho). |
| **Visualizar outros Grupos de Trabalho na tela Workspace** | Permite visualizar outros Grupos de Trabalho na árvore de Grupos de Trabalho. Caso esta propriedade seja desmarcada o solucionador deste grupo poderá visualizar apenas o seu grupo de trabalho e sub-grupos. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna PERMITE_VER_GRUPOS da tabela [GRUPO_TRABALHO](dados_grupo_trabalho). |
| **Painel de Alertas do Workspace** | Regra de autorização para exibição de Ordens de Serviço no Painel de Alertas do Workspace. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna EXIBE_ALERTA_OS_GRUPO da tabela [GRUPO_TRABALHO](dados_grupo_trabalho). |
| **Cancelar** | Regra de autorização para execução da operação de Cancelamento de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna PERMITE_CANCELAR da tabela [GRUPO_TRABALHO](dados_grupo_trabalho). |
| **Encaminhar** | Regra de autorização para execução da operação de Encaminhamento de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna PERMITE_ENCAMINHAR da tabela [GRUPO_TRABALHO](dados_grupo_trabalho). |
| **Classificar** | Regra de autorização para execução da operação de Classificação de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna PERMITE_CLASSIFICAR da tabela [GRUPO_TRABALHO](dados_grupo_trabalho). |
| **Reabrir** | Regra de autorização para execução da operação de Reabertura de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna PERMITE_REABRIR da tabela [GRUPO_TRABALHO](dados_grupo_trabalho). |
| **Interromper ANS** | Regra de autorização para execução da operação de adicionar uma Interrupção de ANS de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna PERMITE_INTERROMPER_ANS da tabela [GRUPO_TRABALHO](dados_grupo_trabalho). |
| **Priorizar** | Regra de autorização para execução da operação de Priorização de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna PERMITE_PRIORIZAR da tabela [GRUPO_TRABALHO](dados_grupo_trabalho). |

| **Solucionadores e Filas** | Pessoas ou Filas do Grupo de Trabalho que atuam no atendimento de Ordens de Serviço Todos os registros desta coleção de dados são mantidos na tabela [TECNICO](dados_tecnico). |
|---|---|

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Grupo Trabalho a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Grupo Trabalho se este for utilizado em um dos cadastros abaixo:

- [Grupo Trabalho](grupotrabalho_sub)
- Contratação de Solucionadores

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

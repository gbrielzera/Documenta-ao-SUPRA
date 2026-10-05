# Indicador

Caminho: Janelas > Processo > Indicador

Um Indicador de Desempenho, também conhecido como KPI (Key Performance Indicator), define uma medição realizada sobre a execução de Processos ou base de Ativos. Indicadores representam uma importante ferramenta para monitoramento e gerenciamento dos Serviços.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Processo | Monitoramento | Indicadores**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Código** | Código de identificação do Indicador Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Todos os caracteres preenchidos são convertidos automaticamente para minúsculo - Não é permitida duplicidade de valores Este campo é mantido na coluna CODIGO da tabela [INDICADOR](dados_indicador). |
|---|---|
| **Descrição** | Texto que descreve claramente a finalizada de um Indicador de Desempenho. Este texto é utilizado na publicação do Indicador na página Executive Dashboard da tela Workspace. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRICAO da tabela [INDICADOR](dados_indicador). |
| **Referência do cálculo** | Texto explicativo sobre como o Indicador é calculado. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna REFER_CALCULO da tabela [INDICADOR](dados_indicador). |
| **Grupo Indicador** | Um Grupo de Indicadores é utilizado para classificar um Indicador de Desempenho. Também permite que Indicadores relacionados sejam agrupados na exibição feita pelo Executive Dashboard. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Provedor** | Banco de dados utilizado para apuração do Indicador. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna PROVEDOR da tabela [INDICADOR](dados_indicador). |
| **Função agregação** | Função de agregação utilizada para apuração de Indicador. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna AGREGACAO da tabela [INDICADOR](dados_indicador). |
| **Melhor desempenho** | Indica o melhor desempenho para um valor apurado em relação a Meta estipulada para o Indicador. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna SENTIDO_MELHOR da tabela [INDICADOR](dados_indicador). |
| **Fórmula valor** | Fórmula para determinar o Valor do Indicador. Se não for preenchido é assumida a Projeção de Contagem de registros que atendam Fórmula de Seleção. A Fórmula de Valor deve ser utilizada em conjunto com a função de Agregação para determinar o valor final de apuração do Indicador. |
| **Fórmula seleção** | Fórmula para seleção de registros baseados no Provedor do Indicador. Indicadores do tipo Percentual devem obrigatoriamente definir uma fórmula de seleção. |

| **Processo** | Seleciona Ordens de Serviço do Processo Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
|---|---|
| **Tipos Subprocesso Filtro** | Tipos de Subprocesso utilizados como filtro na recuperação de Ocorrências. Esta relação de Tipos de Subprocesso só faz sentido para Indicadores apurados a partir da base de dados de Ocorrências de Processos. Todos os registros desta coleção de dados são mantidos na tabela [CLASSE_SUBPROC_INDICADOR](dados_classe_subproc_indicador). |
| **Abertas** | Seleciona Ordens de Serviço Abertas no Período de apuração do Indicador Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna OS_FILTRO_ABERTA da tabela [INDICADOR](dados_indicador). |
| **Canceladas** | Seleciona Ordens de Serviço Canceladas no Período de apuração do Indicador Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna OS_FILTRO_CAN da tabela [INDICADOR](dados_indicador). |
| **Finalizadas com Sucesso** | Seleciona Ordens de Serviço Finalizadas como Sucesso no Período de apuração do Indicador. Para determinar a finalização no período é utilizada a Data/hora de Execução de Mudança. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna OS_FILTRO_FIN_SUC da tabela [INDICADOR](dados_indicador). |
| **Finalizadas como Falha** | Seleciona Ordens de Serviço Finalizadas como Falha no Período de apuração do Indicador. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna OS_FILTRO_FIN_FALHA da tabela [INDICADOR](dados_indicador). |
| **Finalizada Não-realizada** | Seleciona Ordens de Serviço Finalizadas como Não-realizada no Período de apuração do Indicador. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna OS_FILTRO_FIN_NREAL da tabela [INDICADOR](dados_indicador). |

| **Tipo/Super tipos** | Tipos ou super tipos de Itens de Configuração utilizados como filtro na recuperação de Ativos. Esta relação só faz sentido para Indicadores apurados a partir da base de dados de Itens de Configuração. Todos os registros desta coleção de dados são mantidos na tabela [CLASSE_CONF_INDICADOR](dados_classe_conf_indicador). |
|---|---|

| **Pesquisa de satisfação** | Tipo de pesquisa de satisfação que será considerada no cálculo do indicador. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
|---|---|
| **Questões** | Grupos de Questões para Filtro durante a Apuração de Pesquisas de Satisfação Todos os registros desta coleção de dados são mantidos na tabela [GRUPO_QUESTAO_INDICADOR](dados_grupo_questao_indicador). |
| **Concluída** | Seleciona Pesquisas de Satisfação respondidas por Clientes Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna PESQ_FILTRO_CONC da tabela [INDICADOR](dados_indicador). |
| **Cancelada** | Seleciona Pesquisas de Satisfação canceladas Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna PESQ_FILTRO_CAN da tabela [INDICADOR](dados_indicador). |
| **Andamento** | Seleciona Pesquisas de Satisfação não respondidas Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna PESQ_FILTRO_AN da tabela [INDICADOR](dados_indicador). |

| **Fórmula para filtro complementar** | Fórmula para filtro complementar |
|---|---|
| **Fórmula para recuperação de Responsável** | Fórmula para recuperação responsável por uma Ordem de Serviço ou Pesquisa de Satisfação. |

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Indicador a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Indicador se este for utilizado em um dos cadastros abaixo:

- Apuração Indicador
- Indicador de Plano de Gestão

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

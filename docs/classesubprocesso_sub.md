# Tipo de Subprocesso

Caminho: Janelas > Processo > Tipo de Subprocesso

Um Tipo de Subprocesso mantém características de um fluxo que são invariáveis entre suas diversas versões.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Processo | Processos | Tipos de Subprocessos**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Identificador** | Número sequencial gerado automaticamente pelo sistema para identificar um Tipo de Subprocesso. Um Identificador não pode ser modificado pelo usuário. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ID_CLASSE_SUB_PROCESSO da tabela [CLASSE_SUB_PROCESSO](dados_classe_sub_processo). |
|---|---|
| **Descrição** | Texto que descreve claramente a utilização de um Tipo de Subprocesso Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRICAO da tabela [CLASSE_SUB_PROCESSO](dados_classe_sub_processo). |
| **Descritivo cliente** | Descritivo apresentado para o Cliente. Se não for preenchido é apresentado o Descritivo padrão do Tipo de Subprocesso. |
| **Nome abreviado** | Nome abreviado (código) que identifica um Tipo de Subprocesso. Este código pode ser utilizado em scripts para automatismo de processos. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Todos os caracteres preenchidos são convertidos automaticamente para minúsculo - Não é permitida duplicidade de valores - O Nome Abreviado deve conter somente letras maiúsculas Este campo é mantido na coluna SIGLA da tabela [CLASSE_SUB_PROCESSO](dados_classe_sub_processo). |
| **Método Priorização** | Método utilizado para Priorizar Ocorrências do Subprocesso. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Documentação** | Texto de Referência sobre o Objetivo do Tipo de Subprocesso |
| **Ativo** | Indica que o Tipo de Subprocesso está Ativo. Quando ativo o tipo é visível em formulários de entrada de dados para Ordens de Serviço ou Consultas diversas. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ATIVO da tabela [CLASSE_SUB_PROCESSO](dados_classe_sub_processo). |
| **Disponível para consulta como Base de Conhecimento** | Ordens de Serviço deste Subprocesso podem ser recuperadas pela ferramenta de busca de base de conhecimento. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DISP_CONS_CONH da tabela [CLASSE_SUB_PROCESSO](dados_classe_sub_processo). |
| **Habilita consulta automática de Base de Conhecimento** | Indica que Ordens de Serviço deste Subprocesso acionam a busca automática de artigos da Base de Conhecimento a partir dos campos Assunto, Descrição detalhada ou Sintoma analisado. Esta busca ocorre quando o usuário visualiza a tela de edição da Ordem de Serviço, quando os campos citados são utilizados como critério de recuperação por palavras-chave. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna HAB_CONS_AUTO_CON da tabela [CLASSE_SUB_PROCESSO](dados_classe_sub_processo). |
| **Regra de visualização de Ordens de Serviço** | Regra de autorização para visualização de Ordens de Serviço do Subprocesso. Se este campo não for preenchido o sistema utilizará o parâmetro default cadastrado na tela de Configurações. |
| **Acesso total para usuários com perfil Administrador** | Indica que usuários com o perfil Administrador possuem acesso total em ocorrências do Subprocesso. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ACESSO_ADMIN da tabela [CLASSE_SUB_PROCESSO](dados_classe_sub_processo). |
| **Órgão proprietário** | Órgão responsável pelo Subprocesso. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Responsável** | Pessoa responsável pelo Subprocesso Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Fator Prioridade** | Fator utilizado no cálculo de Prioridade Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Valor Charge-back** | Valor para cobrança pela rotina de Charge-back. Se o critério de charge-back for 'Hora' então o valor total é obtido pela multiplicação do 'Valor' pela quantidade de horas apontadas no período de apuração. Se o critério de charge-back for 'Ocorrência' então o total é obtido pela multiplicação do 'Valor' pela quantidade total de ocorrências finalizadas no período de apuração. |
| **Critério Charge-back** | Forma de Charge-back para Ocorrências do Subprocesso. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna CRIT_CHARGE_BACK da tabela [CLASSE_SUB_PROCESSO](dados_classe_sub_processo). |
| **Emails para cópia em comunicado manual** | Serão enviados para este(s) e-mail(s) os emails enviados manualmente relacionados com este Tipo de Subprocesso. Separar por ponto-e-vírgula (;). |

| **Serviços disponíveis (se existir restrição)** | Serviços que estarão disponíveis para o Subprocesso. Deve ser preenchido somente quando for necessário restringir os Serviços. Se não for preenchido então todos os Serviços estarão disponíveis. Tomar como exemplo o passo 3 do Autoatendimento. Todos os registros desta coleção de dados são mantidos na tabela [REST_SERVICO](dados_rest_servico). |
|---|---|

| **Permitir reabertura** | Permite que clientes reabram a Ordem de Serviço utilizando a página de consulta do Autoatendimento. Esta permissão também está condicionada ao parâmetro 'Máximo dias para reabertura' da tela de Configurações. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna REABERTURA_AA da tabela [CLASSE_SUB_PROCESSO](dados_classe_sub_processo). |
|---|---|
| **Visibilidade** | Indica o tipo de visibilidade das ocorrências deste tipo de subprocesso no Autoatendimento, levando em consideração o cliente ou favorecido como referência Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna VISIBILIDADE_AA da tabela [CLASSE_SUB_PROCESSO](dados_classe_sub_processo). |
| **Publicação de Apontamentos** | Indica a regra de publicação de apontamentos de horas trabalhadas no Autoatendimento Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna PUBLIC_APONTAMT_AA da tabela [CLASSE_SUB_PROCESSO](dados_classe_sub_processo). |
| **Ordem de exibição na abertura** | Ordem de exibição da Solicitação na página de Abertura de Ordens de Serviço da aplicação de Autoatendimento. Quando preenchido a Solicitação é exibida em um grupo denominado "Principais solicitações", caso contrário é agrupado em "Demais solicitações". Em caso de empate por ordenação deste campo então é adotado como segundo critério a ordenação alfabética por Descritivo do Cliente |

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Tipo de Subprocesso a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Tipo de Subprocesso se este for utilizado em um dos cadastros abaixo:

- Subprocesso
- Ocorrências
- Ocorrências
- Tipos de Subprocesso para recuperação
- [Associação](associacao_sub)
- [Associação](associacao_sub)
- Atividade

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

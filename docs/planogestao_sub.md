# Plano Gestão

Caminho: Janelas > Processo > Plano Gestão

O Plano de Gestão é utilizado para gerenciar Indicadores de Desempenho. Este plano pode ser utilizado para gestão de Indicadores de Desempenho Chave da área ou indicadores associados a Acordos de Nível de Serviço.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Processo | Monitoramento | Planos de Gestão**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Descrição** | Descrição detalhada do Plano de Gestão. Esta descrição é utilizada para seleção do Plano de Gestão na aplicação Executive Dashboard. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRICAO da tabela [PLANO_GESTAO](dados_plano_gestao). |
|---|---|
| **Data início** | Data de início do plano. Quando modificado é atualizada a coleção de períodos de todos os Indicadores associados ao plano. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - O campo 'Data início' deve ser menor que o campo 'Data fim' Este campo é mantido na coluna DATA_INICIO da tabela [PLANO_GESTAO](dados_plano_gestao). |
| **Data fim** | Data fim do plano. Quando modificado é atualizada a coleção de períodos de todos os Indicadores associados ao plano. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DATA_FIM da tabela [PLANO_GESTAO](dados_plano_gestao). |
| **Visibilidade restrita ao usuário conectado** | O solucionador logado só visualiza suas informações ou informações de subordinados. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna INFO_RESTRITAS da tabela [PLANO_GESTAO](dados_plano_gestao). |

| **Indicadores** | Indicadores associados ao Plano de Gestão. Para cada indicador existe um desdobramento de vários Períodos. Possui também uma Meta geral e redefinições por período. Todos os registros desta coleção de dados são mantidos na tabela [INDICADOR_PLANO](dados_indicador_plano). |
|---|---|

| **Grupos Autorizados** | Grupos de Trabalho que estão autorizados a visualizar o resultado da apuração de indicadores. Todos os registros desta coleção de dados são mantidos na tabela [GRUPO_TRABALHO_AUTORIZADO](dados_grupo_trabalho_autorizado_). |
|---|---|

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Plano Gestão a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Plano Gestão se este for utilizado em um dos cadastros abaixo:

- Apuração Indicador

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

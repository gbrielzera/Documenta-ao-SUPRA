# Serviço

Caminho: Janelas > Processo > Serviço

Um Serviço pode ser definido como um sistema composto por Tecnologia, Facilidades, Processos e Pessoas que habilitam um processo de negócio.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Processo | Serviços | Serviços**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Identificador** | Identificador do Serviço Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ID_SERVICO da tabela [SERVICO](dados_servico). |
|---|---|
| **Descrição** | Descrição detalhada do Produto Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRICAO da tabela [SERVICO](dados_servico). |
| **Descrição cliente** | Descritivo apresentado para Cliente no Catálogo de Serviços. Se não for preenchido é utilizado a Descrição padrão do Serviço |
| **Nome abreviado** | Nome resumido do Serviço Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Todos os caracteres preenchidos são convertidos automaticamente para minúsculo - Não é permitida duplicidade de valores - O Nome Abreviado deve conter somente números e letras maiúsculas Este campo é mantido na coluna SIGLA da tabela [SERVICO](dados_servico). |
| **Documentação** | Texto de Referência para utilização do Produto |
| **Ativo** | Define se o Serviço está Ativo. Por padrão o valor inicial é sempre Verdadeiro. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ATIVO da tabela [SERVICO](dados_servico). |
| **Solucionador responsável** | Solucionador responsável pelo Serviço Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Responsável área negócio** | Gerência responsável pelo Serviço na área de negócio cliente do Serviço Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Tipo de Serviço** | Classificação do Serviço. Este atributo é utilizado pelo Cliente na aplicação de Autoatendimento Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Fator Prioridade** | Fator utilizado no cálculo de Prioridade. Se não for preenchido é utilizado o valor atribuído a Classe do Serviço quando preenchido. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Redefinição de Papéis por Itens de Configuração** | Define o comportamento da rotina de resolução de Atores quando existirem redefinições de Papéis em Itens de Configuração associados em uma Ordem de Serviço. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna REDEF_PAPEIS_ITEM da tabela [SERVICO](dados_servico). |
| **Disponibilidade no Autoatendimento** | Configuração da disponibilidade do Serviço na aplicação de Autoatendimento. Alguns Serviços são utilizados internamente pela área de Tecnologia da Informação e por isto nunca serão visíveis para o Cliente. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DISP_AA da tabela [SERVICO](dados_servico). |

| **Redefinição de Papéis** | Sobrepõe a configuração global de Papéis em ocorrências do Serviço. Todos os registros desta coleção de dados são mantidos na tabela [ATOR_SERVICO](dados_ator_servico). |
|---|---|

| **Componentes** | Itens de Configuração que compõem o Serviço. Todos os registros desta coleção de dados são mantidos na tabela [COMP_SERVICO](dados_comp_servico). |
|---|---|

| **Pré-requisitos/Dependências** | Pré-requisitos ou Dependências para o perfeito funcionamento do Serviço. |
|---|---|
| **Benefícios** | Benefícios oferecidos pelo Serviço |
| **Disponibilidade** | Disponibilidade que pode ser esperada pelo Cliente incluindo horários. |
| **Programação manutenção** | Detalhes sobre a Programação de Manutenção do Serviço incluído janelas semanais de paradas. |
| **Solicitação Serviços** | Detalhes sobre procedimento de abertura de Chamados. Se não for preenchido é estabelecido o procedimento padrão por meio do Catálogo de Serviços. |

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Serviço a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Serviço se este for utilizado em um dos cadastros abaixo:

- Ordem de Serviço
- Apuração Indicador Ordem Serviço
- Apuração Indicador Pesquisa
- Restrições de Serviços em Subprocessos
- Restrições Anexos por Serviço
- Restrições Itens Aprovação por Serviço

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

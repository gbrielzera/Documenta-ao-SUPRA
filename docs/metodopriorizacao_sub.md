# Métodos de Priorização

Caminho: Janelas > Processo > Métodos de Priorização

Define uma Metodologia para Priorização de Ocorrências e cálculo de ANS.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Processo | Processos | Métodos de Priorização**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Descrição** | Descrição detalhada da ClasseSeveridade Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRICAO da tabela [METODO_PRIORIZACAO](dados_metodo_priorizacao). |
|---|---|
| **Referência** | Texto de referência sobre o Método de Priorização. Procure especificar neste campo qual o propósito e a aplicação deste Método de Priorização. |
| **Expressão cálculo** | Expressão utilizada para determinar a base de cálculo utilizada para seleção do Grau de Prioridade a partir. Para seleção do Grau de Prioridade é selecionado aquele com Limite Superior maior que o valor resultante na Expressão. A expressão deve retornar obrigatoriamente um número Inteiro não negativo. |
| **Cálculo automático** | Indica que o cálculo é automático sempre que ocorrer modificação no campos Cliente, Serviço ou quando for adicionado ou removido um Item de Configuração. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna CALCULO_AUTOMATICO da tabela [METODO_PRIORIZACAO](dados_metodo_priorizacao). |

| **Variáveis** | Variáveis utilizada para compor a Prioridade da Ocorrência. Todos os registros desta coleção de dados são mantidos na tabela [VARIAVEL_PRIORIZACAO](dados_variavel_priorizacao). |
|---|---|

| **Graus de Prioridade** | Graus de Pririodade Todos os registros desta coleção de dados são mantidos na tabela [GRAU_PRIORIDADE](dados_grau_prioridade). |
|---|---|

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Métodos de Priorização a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Métodos de Priorização se este for utilizado em um dos cadastros abaixo:

- [Tipo de Subprocesso](classesubprocesso_sub)
- Ordem de Serviço

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

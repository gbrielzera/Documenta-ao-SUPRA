# Classe Pesquisa Satisfação

Caminho: Janelas > Processo > Classe Pesquisa Satisfação

Uma Classe de Pesquisa de Satisfação define um conjunto de configurações utilizado para geração de Pesquisas de Satisfação enviadas para clientes após finalização de uma Ordem de Serviço. O envio da pesquisa está condicionado ao evento terminador utilizado na definição do processo aplicado em Ordens de Serviço alvo da pesquisa.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Processo | Processos | Pesquisa de Satisfação | Classes de Pesquisa de Satisfação**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Descrição** | Descrição detalhada da ClassePesquisaSatisfacao Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRICAO da tabela [CLASSE_PESQ_SATISF](dados_classe_pesq_satisf). |
|---|---|
| **Ativo** | Indica que a ClassePesquisaSatisfacao está ativa no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ATIVO da tabela [CLASSE_PESQ_SATISF](dados_classe_pesq_satisf). |
| **Percentual envio** | Número percentual entre 0 e 100 que indica a probabilidade de envio de Pesquisa de Satisfação. O valor 0 indica que nenhuma Pesquisa será enviada enquanto 100 estabelece que sempre será enviada Pesquisa de Satisfação |
| **Fórmula para percentual de envio** | Fórmula que é avaliada para determinar o Percentual de Envio de Pesquisas de Satisfação. Quando preenchido será desconsiderado o campo 'Percentual envio'. |

| **Questões** | Questões que farão parte da Pesquisa de Satisfação Todos os registros desta coleção de dados são mantidos na tabela [QUESTAO_CLASSE_PESQ](dados_questao_classe_pesq). |
|---|---|

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Classe Pesquisa Satisfação a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Classe Pesquisa Satisfação se este for utilizado em um dos cadastros abaixo:

- Atividade
- Ordem de Serviço
- [Pesquisa](pesquisa_sub)
- [Indicador](indicador_sub)

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

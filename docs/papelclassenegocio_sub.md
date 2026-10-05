# Papéis

Caminho: Papéis

Um Papel representa uma importante ferramenta para configuração de responsabilidades em um Processo. Com este recurso é possível definir no Processo quem será, por exemplo, o responsável por uma determinada tarefa, quem realizará uma determinada aprovação e assim por diante. O Papel pode ser definido por referências de equipes, solucionadores, por scripts (recuperando registros do banco de dados) e também por composição de Papéis. Também é possível a redefinição de Atores de um Papel por Serviço.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Processo | Processos | Papéis**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Nome** | Descritivo utilizado para nomear um Papel. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Não é permitida duplicidade de valores Este campo é mantido na coluna NOME da tabela [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio). |
|---|---|
| **Ativo** | Indica que o Papél está ativo no Sistema. Quando inativo o Papel é ignorado pela rotina de cálculo de Atores. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ATIVO da tabela [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio). |
| **Solucionador** | Solucionador configurado como Ator para o Papel. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Referência** | Descritivo completo do Papel. Este descritivo é utilizado na geração de documentação de Processos. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna REFERENCIA da tabela [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio). |
| **Grupo de Trabalho** | Grupo de Trabalho utilizado para seleção de Ator Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Critério seleção Ator** | Critério para seleção de Atores obtidos a partir de Grupos de Trabalho (exige o preenchimento do campo 'Grupo de Trabalho') Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ATOR_GRUPO_TRABALHO da tabela [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio). |
| **Inclui Coordenador (somente Todos os Membros e Menor Carga)** | Inclui seleção do Coordenador do Grupo de Trabalho. Se o critério de seleção de solucionadores do grupo for Coordenador então este campo é desconsiderado. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna INC_COORDENADOR da tabela [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio). |
| **Exclui Aprovações (somente Menor Carga)** | Exclui da contagem de Ocorrências aquelas que estiveram Pendentes de Aprovação. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna EXC_APROVACAO da tabela [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio). |
| **Somente usuários conectados** | Somente usuários conectados na aplicação Supravizio estão habilitados como Atores do Papel. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna USU_CONECTADO da tabela [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio). |

| **Papéis para composição** | Relação de papéis de processo que serão utilizados para compor este papel. O papel resultante é formado pela soma de todas as pessoas sem ocorrência de duplicidades. Todos os registros desta coleção de dados são mantidos na tabela [PAPEL_COMP](dados_papel_comp). |
|---|---|

| **Script Seleção Atores** | Script para seleção de Atores de um Papel de Processo |
|---|---|

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Papéis a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Papéis se este for utilizado em um dos cadastros abaixo:

- Papéis de Processo
- Atores de Serviço
- Atores de Serviço
- Composição de Papéis
- Mensagem Evento

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

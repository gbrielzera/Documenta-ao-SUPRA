# Órgão

Caminho: Janelas > Recurso > Órgão

Diretoria, Gerência, Departamento ou Área que compõe a estrutura organizacional. Em um Órgão, também denominado Área, podemos associar empregados ou terceiros (lotação). Um Órgão pode possuir uma associação com outro Órgão denominado "Pai". Esta associação "pai-filho" define a hierarquia de órgãos de uma Empresa.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Recurso | Órgãos**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Identificador** | Identificador do Órgão Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ID_ORGAO da tabela [ORGAO](dados_orgao). |
|---|---|
| **Descrição** | Texto que descreve claramente a função do Órgão. Este texto é utilizado por profissionais e clientes para busca por itens da estrutura organizacional. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRICAO da tabela [ORGAO](dados_orgao). |
| **Sigla** | Nome resumido (código) utilizado para identificar um Órgão. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Todos os caracteres preenchidos são convertidos automaticamente para minúsculo Este campo é mantido na coluna SIGLA da tabela [ORGAO](dados_orgao). |
| **Ativo** | Indica que o Órgão está Ativo Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ATIVO da tabela [ORGAO](dados_orgao). |
| **Gestor** | Gestor responsável pelo Órgão Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Órgão pai** | Diretoria, Gerência, Departamento ou Área que compõe a estrutura organizacional. Em um Órgão, também denominado Área, podemos associar empregados ou terceiros (lotação). Um Órgão pode possuir uma associação com outro Órgão denominado \"Pai\". Esta associação \"pai-filho\" define a hierarquia de órgãos de uma Empresa. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Empresa** | Empresa ao qual pertence o Órgão. Se preenchido é anulado o campo Unidade de Negócio. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Órgão a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Órgão se este for utilizado em um dos cadastros abaixo:

- [Pessoa](pessoa_sub)
- [Órgão](orgao_sub)
- Charge-Back de Órgão
- Histórico Órgão
- Histórico Órgão
- Órgão atendido por ANS

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

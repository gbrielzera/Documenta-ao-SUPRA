# Pessoa

Caminho: Janelas > Recurso > Pessoa

Uma Pessoa pode representar um Cliente, um Solucionador ou uma fila de atendimento. Um registro do tipo Pessoa deve obrigatoriamente estar associado a um Órgão, e por meio desta associação é possível determinar seu gestor. No cadastro de uma Ordem de Serviço encontramos os campos Cliente e Responsável que representam a pessoa que solicitou e a responsável pelo atendimento respectivamente.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Recurso | Pessoas**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Identificador** | Número sequencial gerado automaticamente pelo sistema para identificar uma Pessoa. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ID_PESSOA da tabela [PESSOA](dados_pessoa). |
|---|---|
| **Nome** | Nome completo da Pessoa Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna NOME da tabela [PESSOA](dados_pessoa). |
| **Nome abreviado** | Nome abreviado da Pessoa Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna NOME_ABREVIADO da tabela [PESSOA](dados_pessoa). |
| **Usuário rede** | Nome do usuário de rede utilizado pela Pessoa para acesso a ambiente de rede Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Não é permitida duplicidade de valores Este campo é mantido na coluna USUARIO_REDE da tabela [PESSOA](dados_pessoa). |
| **Tipo de colaborador** | Tipo de Colaborador que pode ser Empregado ou Terceiro. No caso de Terceiro é necessário informar a Empresa Fornecedora Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna TIPO_COLABORADOR da tabela [PESSOA](dados_pessoa). |
| **Órgão** | Órgão onde a Pessoa está lotada. A lotação é de grande importância em processos que envolvem aprovações de chefias e hierárquica. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Ativo** | Indica que a Pessoa está Ativa no sistema. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ATIVO da tabela [PESSOA](dados_pessoa). |
| **Cargo** | Descrição do Cargo da Pessoa |
| **Fornecedor** | Empresa Fornecedora responsável pelo Terceiro. Preencher este campo somente quando a Pessoa for um Terceiro. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Fator Prioridade** | Fator utilizado para cálculo de Prioridade em Ocorrências. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Perfil Cliente** | Perfil especial concedido a um Cliente para atendimento diferenciado Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Local de trabalho** | Local de trabalho da Pessoa Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Cultura Cliente** | Cultura preferencial do Cliente. Esta Cultura é utilizada pela aplicação de Autoatendimento para configuração de idioma do usuário. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Senha de Autoatendimento** | Senha do usuário formada por no mínimo 4 caracteres que podem ser somente números ou letras. A comparação é insensível a letras minúsculas ou maiúsculas. Quando preenchida ignora validação de senha no Active Directory. Para este campo existem as seguintes regras: Este campo é mantido na coluna SENHA da tabela [PESSOA](dados_pessoa). |
| **Último acesso Autoatendimento** | Data/hora do último acesso ao Autoatendimento. |

| **Substituto para aprovações** | Pessoa autorizada a realizar aprovações como substituto. O Substituto pode ser registrado na aplicação Supravizio ou pelo próprio Cliente pelo site de Autoatendimento. A autorização de substituição em aprovações é válida por um período com data de início e data de fim que são obrigatórios no registro da substituição. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
|---|---|
| **Data Inicio Substituição Aprovação** | Data de Início de validade para a autorização de substituição. Importante: a data de início não está associada a data de início de aprovação (instante em que solicitação de aprovação é enviada para o aprovador) e sim com a data instantânea em que a página de aprovação é exibida para o Cliente. |
| **Data Fim Substituição Aprovação** | Data de Fim de validade para a autorização de substituição. Importante: a data de fim não está associada a data de início de aprovação (instante em que solicitação de aprovação é enviada para o aprovador) e sim com a data instantânea em que a página de aprovação é exibida para o Cliente. |
| **Responsável substituto** | Pessoa que realizou o registro do Substituto pela aprovação. Este pode ser o próprio Cliente quando realizado pelo site de Autoatendimento ou um Profissional utilizando a aplicação Supravizio. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |

| **Telefone** | Número do Telefone (ramal) de contato. |
|---|---|
| **Celular particular** | Telefone Celular particular da Pessoa |
| **Celular empresa** | Telefone Celular fornecido pela empresa |
| **E-mail** | E-mail da Pessoa Para este campo existem as seguintes regras: - E-mail inválido Este campo é mantido na coluna EMAIL da tabela [PESSOA](dados_pessoa). |
| **E-mail alternativo** | E-mail alternativo de contato para a Pessoa |
| **Segundo contato** | Segunda Pessoa para contato |
| **Telefone segundo contato** | Telefone da Segunda Pessoa de contato |

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Pessoa a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

### Importante

Não é possível remover um registro de Pessoa se este for utilizado em um dos cadastros abaixo:

- Solucionador
- [Grupo Trabalho](grupotrabalho_sub)
- [Órgão](orgao_sub)
- [Contrato](contrato_sub)
- Ausência Temporária
- Ausência Temporária
- [Pessoa](pessoa_sub)
- [Pessoa](pessoa_sub)
- Histórico de Usuários
- Histórico Órgão
- Histórico de Pessoas
- Histórico de Item em Charge-back
- Item de Charge-back apurado

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).

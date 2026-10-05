# Serviço de Diretório

Caminho: Guia para Administradores > Configurações do Sistema > Serviço de Diretório

Um Serviço de Diretório é um serviço que armazena e organiza as informações sobre os recursos e os usuários de uma rede de computadores, e que permite os administradores de rede, gerenciar o acesso dos usuários e sistemas a esses recursos.

Para visualizar a configuração do Serviço de Diretório no Supravizio, é preciso acessar as Configurações no Menu Principal (**Utilitários | Configurações**) e clicar na aba **Serviço de Diretório** em Utilitários:

- No campo "Endereço Domínio", deve ser inserido o endereço do domínio que os usuários estão alocados.
- Em "Tipo de autenticação", é possível selecionar entre Active Directory(AD) e OpenLDAP/Novell. Caso o Tipo de Autenticação seja OpenLDAP ou Novell, será necessária a configuração de mais alguns parâmetros, conforme detalharemos neste tópico;
- Em "Criação de novo Usuário: A nova conta deve iniciar com a seguinte senha", pré-estabelece uma senha padrão aos usuários que serão cadastrados.
- Se o campo "Criação de novo Usuário: Usuário deve trocar senha no primeiro Logon" for selecionado, o Usuário terá que alterar a senha de acesso após o primeiro Logon.
- Se o campo "Criação de novo Usuário: A senha do usuário nunca expira" for selecionada, a senha do usuário nunca expirará.
- Se o campo "Criação de novo Usuário: A nova conta deve iniciar desabilitada" for selecionada, no momento que for criada a conta de usuário, ela iniciará desabilitada.

Os campos com o termo "Criação de novo usuário" são utilizados pelo método **CreateUser** para a criação de um novo usuário no Serviço de Diretório.

Através do Supravizio, também é possível realizar interações com o Serviço de Diretórios. Podemos, por exemplo, criar, remover ou desabilitar usuários, gerenciar grupos, dentre outras funcionalidades. Para mais informações leia o tópico [Recursos Avançados](recurso_avancado).

## Configurações para OpenLDAP e Novell

Caso o Tipo de Autenticação utilizado seja OpenLDAP ou Novell, além do **Endereço do Domínio**, será necessário o preenchimento de parâmetros adicionais:

Parâmetros adicionais

### Credenciais admin

Credenciais do usuário que tem permissões de adicionar, remover, alterar e consultar o serviço de diretório.

Exemplo de preenchimento

Em Tipo de Autenticação, caso seja utilizado o método Samba, basta selecioná-la dentre as opções listadas. Caso contrário, é possível realizar a criação de um método customizado através de um script na linguagem Iron Python.

Script para customização de autenticação

Nesse script são disponibilizadas três variáveis:

- **AtributosUsuarioLDAP** - Possui todas os atributos do usuário que está tentando se conectar, em um objeto do tipo Hashtable;
- **Autenticado** - Resultado do script, se o usuário deve ser autenticado então deve-se preencher a variável com True, caso contrário, False;
- **MensagemDeErro** - Mensagem a ser exibida ao usuário em caso de falha de autenticação, em formato String.

**Importante**: Caso esteja vazio, o sistema realizará o login normalmente, porém, validando apenas o usuário e a senha. Informações de usuário e senha ainda são tratadas pelo código nativo do sistema, esse script destina-se a complementar a autenticação com propriedades relevantes ao ambiente.

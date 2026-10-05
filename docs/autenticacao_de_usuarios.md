# Autenticação de usuários

Caminho: Guia para Administradores > Configurações do Sistema > Configurações do Autoatendimento e Portal de Processos > Autenticação de usuários

A autenticação de usuários se refere ao mecanismo de validação de usuários e senha do Autoatendimento. Esta configuração é determinada pelo campo **Forma de autenticação de usuários **que pode ser preenchido com uma das seguintes opções:

### Cadastro de Pessoas

Nesta situação o Portal utiliza uma senha configurada no cadastro de Pessoas conforme a figura abaixo:

Configuração da senha

A senha do usuário também poderá ser alterada, acessando o Portal haverá um link para a alteração de senha:

### Mudar Senha

Quando utilizamos esta forma de autenticação a página de logon passa a exibir a opção de recuperação de senha. Veja a figura abaixo:

Opções de recuperação de senha

Quando o usuário realiza a troca de senha é feita uma modificação no campo **Senha de Autoatendimento** do [cadastro de Pessoas](cadastro_de_pessoas).

### Serviço de diretório (usuário de rede)

Nesta situação a autenticação do usuário é feita no Serviço de diretório, ou seja, o usuário deve utilizar usuário e senha de rede para acessar o Autoatendimento ou Portal de Processos.

Nesta opção de configuração a tela de logon não apresenta as opções de troca e recuperação de senha. Para esta demanda o usuário deve utilizar recursos do sistema operacional para realizar a troca ou solicitar o reset para a equipe que mantém o Serviço de diretório.

### Autenticação de usuários

O Supravizio permite que o usuário logado na máquina seja reconhecido e autenticado no serviço de diretório automaticamente, porém a configuração do IIS deve ser modificada para permitir reconhecimento do usuário logado na máquina. Para efetuar essa modificação, acesse o IIS da máquina e então verifique as propriedades do Portal:

Modificação de Autenticação - IIS 6.0

Integração com Autenticação do Windows - IIS 6

Modificação de Autenticação - IIS 7

Integração com Autenticação do Windows - IIS 7

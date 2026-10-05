# Criar um subprocesso chamador de WebServices

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 14: Integração de Instalações Supravizio via WebService > Criar um subprocesso chamador de WebServices

Vamos criar o seguinte exemplo: o Subprocesso Incidente do SV1 chamará o Subprocesso Tratamento de Falha do SV2 caso o serviço requerido tenha um webservice indicado e aguardará resposta por WebService.

### Cadastrando o campo customizado para endereço de WebService:

Utilize o Menu Utilitários | Dicionário de Classes | Dicionário de Classes:

Acessar Dicionário de Classes

Procure pela classe "Venki.Supravizio.Processo.Servico, Supravizio" e selecione com duplo clique (ou clique em modificar):

Selecionar Classe específica

Selecione Propriedades customizadas:

Selecionar Propriedades Customizadas

Em seguida clique em Novo e preencha os seguintes campos:

Propriedades Customizadas

Clique em "Confirmar e Fechar" e salve as configurações.

Para preencher o campo "WEBSERVICE" de algum serviço, entre em Processo | Serviços, Serviços:

Serviços

Vamos por exemplo, editar o serviço de Banco de Dados com duplo clique (ou botão modificar):

Clique em Mais Campos:

Preencha o campo, salve e feche, e salve as alterações no serviço:

Voltando agora ao processo, foi criado um novo campo customizado cujo nome é "WEBSERVICE", agora tudo que precisa ser feito é verificar se ele foi preenchido ou não.

No Editor de Processos, crie uma nova versão para o subprocesso de incidente, e então na tarefa "Restabelecer o Serviço" edite o Script Início:

Editor de Processos

Adicione o Seguinte código:

#verificar se existe endereço de webservice cadastrado no serviço

if not String.IsNullOrEmpty(OrdemServico.Servico.GetCustom("WEBSERVICE")):

#definir os campos de usuario, senha, instancia para efetuar logon no serviço

usuario = "admin"

senha = "x"

instancia = 1

#definir nome da mensagem para identificação na OS

nome = "INICIAOSX2"

#definir url para comunicação com webservice

url = OrdemServico.Servico.GetCustom("WEBSERVICE")

#definir parâmetros xml que serão enviados

xmlparam = "<MENSAGEM><PARAMETROS><PARAMETRO><NOME>NUMERO</NOME><VALOR>"+

OrdemServico.Numero +"</VALOR> </PARAMETRO><PARAMETRO><NOME>Descricao</NOME><VALOR>"+

OrdemServico.DescricaoDetalhada+"</VALOR></PARAMETRO></PARAMETROS></MENSAGEM>"

#estabelecer conexão com o webservice e enviar as informações definidas

ws = Utils.LoadWebService(url)

mensagem = ws.ProcessaMensagem(instancia,usuario,senha,nome, xmlparam)

Utils.LogInformation(mensagem.ToString(), "Acesso SVServiceBus")

Script Início

Este código pode ser interpretado da seguinte forma: Na primeira linha é verificado se há endereço de WebService configurado no campo customizado "WESERVICE", se existir ele determina que o usuário do sistema é o "admin" (Utilitários | Segurança | Usuários), a senha é "x", a variável instancia é 1 e o nome da mensagem é "INICIAOSX2" além de recuperar do campo que a url do WebService é o conteúdo do campo customizado e recuperar o número da OS e a descrição detalhada para ser enviado como parâmetro.

A partir dessas informações, o comando Utils.LoadWebService carrega o WebService e as informações são enviadas.

Voltando ao Editor de processos, adicione também na tarefa um Evento intermediário de mensagem e defina os campos Nome da Mensagem e Script evento:

Evento intermediário por mensagem

O Nome da Mensagem, vamos determinar como "CONTINUAOSX1" e o Script Evento vamos definir:

OrdemServico.Solucao = Parametros["Solucao"]

Script Evento

Nesse script é recuperado o Parâmetro "Solucao" da OS do SV2.

Adicione ao Iniciador por gerente de TI o mesmo campo de preenchimento de descrição detalhada que do iniciador pelo service desk:

Campo Descrição Detalhada

Complete o fluxo do evento intermediário por mensagem, salve as alterações e ative a versão para finalizar a configuração do SV1:

Configuração Subprocesso

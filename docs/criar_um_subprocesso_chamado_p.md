# Criar um subprocesso chamado por WebServices

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 14: Integração de Instalações Supravizio via WebService > Criar um subprocesso chamado por WebServices

Agora é necessário configurar o SV2, no editor de processos do outro servidor vamos criar um Subprocesso de Tratamento de Falha no novo processo "Falhas":

Fluxo do Tratamento de Falha

Crie um novo processo com o nome "Falhas" (caso não saiba leia o [tutorial 1, criando processos](criando_um_processo)), crie um Subprocesso "Tratamento de Falhas" (caso não saiba leia o [tutorial 1, criando subprocessos](criar_um_sub-processo))

No iniciador por mensagem é utilizado um campo customizado, vamos inserir este campo. Em propriedades do iniciador, edite os campos para preenchimento. Adicione o campo de descrição detalhada e mais um campo customizado (no customizado clique em novo):

Campos necessários

Então preencha os seguintes campos:

Novo Campo

Configure para utilização do novo campo:

Configuração Campos

Agora vamos verificar as propriedades do iniciador por mensagem, configure o Nome da Mensagem como "INICIAOSX2" e o Script Evento:

OrdemServico.SetCustom("OS_SIS_CHAMADOR",Parametros["NUMERO"])

OrdemServico.DescricaoDetalhada = Parametros["Descricao"]

Script Evento

Propriedades

Também é importante definirmos um Serviço inicial para o iniciador. Neste caso, selecionamos "Chave de rede":

Propriedade Serviço inicial

Vamos configurar também o Script Fim da Tarefa "Correção da falha com apresentação de solução":

Tarefa

#verificar se existe endereço de webservice cadastrado no serviço

if not String.IsNullOrEmpty(OrdemServico.GetCustom("OS_SIS_CHAMADOR")):

#definir os campos de usuário, senha, instancia para efetuar logon no serviço

usuario = "admin"

senha = "x"

instancia = 1

#definir nome da mensagem para identificação na OS

nome = "CONTINUAOSX1"

#definir url para comunicação com webservice que iniciou esta ocorrência

url = http://[ip_ou_nome_do_servidor_CHAMADOR]/supravizioweb/servicebus/processo/processo.asmx/

#definir parâmetros xml que serão enviados

xmlparam = "<MENSAGEM><PARAMETROS> <PARAMETRO><NOME>Solucao</NOME><VALOR>"+

OrdemServico.Solucao +"</VALOR></PARAMETRO><PARAMETRO><NOME>OrdemServico</NOME><VALOR>"+ OrdemServico.GetCustom("OS_SIS_CHAMADOR")+"</VALOR></PARAMETRO></PARAMETROS></MENSAGEM>"

#estabelecer conexão com o webservice e enviar as informações definidas

ws = Utils.LoadWebService(url)

ws.ProcessaMensagem(instancia,usuario,senha,nome, xmlparam)

Script Fim

Repare que o Parâmetro "OrdemServico" não foi recuperado em nenhum script do chamador, ele só foi enviado, isto ocorre porque o sistema utiliza este parâmetro para associar a resposta com cada Ordem de Serviço e caso este campo seja nulo todas Ordens de Serviço que contenham o nome de mensagem "CONTINUAOSX1" serão associadas.

Salve e ative a versão e pronto, agora os servidores se comunicam entre si.

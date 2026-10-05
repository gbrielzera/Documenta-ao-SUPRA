# Envio de Mensagens WebServices

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 13: Abertura de Ordem de Serviço por WebService > Envio de Mensagens WebServices

Para execução deste tutorial, utilize uma ferramenta de abertura de Ordens de Serviço por Web Services desenvolvida para exemplificar maneiras de implementar o WebService em Windows Application. A aplicação pode ser obtida no seguinte site: http://www.venki.com.br/downloads/SupravizioServiceBusUtilitario.zip

Faça download da aplicação, descompacte e execute. A seguinte tela estará disponível:

Página principal da aplicação

E na aba configurações:

**Aba de Configurações**

Preencha as configurações com campos válidos. Para o exemplo o preenchimento será o seguinte [http://localhost/supravizioweb/servicebus/processo/processo.asmx/](http://localhost/supravizioweb/servicebus/processo/processo.asmx/)

Configurações utilizadas

O usuário e senha é o configurado no próprio supravizio, o Nome Mensagem deve ser o mesmo que o configurado no [tópico anterior](criar_um_subprocesso_iniciado_) e o site deve ser o equivalente ao de instalação do SVServiceBus. Configurado, podemos ir ao preenchimento da mensagem:

Corpo da mensagem utilizado

Ao clicar em enviar a seguinte tela ocorrerá:

Confirmação de criação

E consultando a OS 9 no Workspace podemos visualizar, repare que o assunto e a descrição detalhada são correspondentes:

Ordem de Serviço

Abaixo podemos observar o código (Linguagem C#) do botão enviar da aplicação:

private void buttonEnviar_Click(object sender, EventArgs e)

{

1 ProcessaMensagem.Processo processo = new ProcessaMensagem.Processo();

2 processo.Url = textBoxSite.Text;

3 string mensagem = "<MENSAGEM><PARAMETROS><PARAMETRO><NOME>ASSUNTO</NOME><VALOR>"+ textBoxAssunto.Text+"</VALOR></PARAMETRO><PARAMETRO><NOME>DESC</NOME><VALOR>"+

textBoxDescricao.Text+"</VALOR></PARAMETRO></PARAMETROS>";

4 string domain1 = textBoxDominio.Text;

5 try

6 {

7 string xml = processo.ProcessaMensagem(Int32.Parse(domain1), textBoxLogin.Text, textBoxSenha.Text, textBoxNomeMensagem.Text, mensagem);

8 string texto = String.Empty;

9 StringReader sr = new StringReader(xml);

10 DataSet ds = new DataSet();

11 ds.ReadXml(sr);

12 texto = "Número da OS: " + ds.Tables[0].Rows[0].ItemArray[1] + " \n " + "Assunto: " +

ds.Tables[0].Row[0].ItemArray[2];

13 MessageBox.Show(texto);

14 }

15 catch

16 {

17 MessageBox.Show("Erro ao acessar o WebService.");

18 }

19 }

**Código do botão enviar do programa**

Como é apresentado no código acima queremos demonstrar apenas como devem ser passados os parâmetros para o WebService. Na linha 3, podemos verificar que o seguinte modelo é utilizado:

<MENSAGEM>

<PARAMETROS>

<PARAMETRO>

<NOME>

ASSUNTO

</NOME>

<VALOR>

"Texto equivalente ao assunto digitado"

</VALOR>

</PARAMETRO>

<PARAMETRO>

<NOME>

DESC

</NOME>

<VALOR>

"Texto equivalente a descrição digitada"

</VALOR>

</PARAMETRO>

</PARAMETROS>

</MENSAGEM>

**XML para envio de parâmetros**

Este modelo permite que os campos ASSUNTO e DESC sejam recuperado na Ordem de Serviço em que for utilizada pelo script.

OrdemServico.Assunto = Parametros["ASSUNTO"]

OrdemServico.DescricaoDetalhada = Parametros["DESC"]

**Recuperação de parâmetros na OS**

Com este script, é possível recuperar o Assunto e a Descrição Detalhada através dos parâmetros passados.

Caso o usuário que está acessando esteja utilizando a máquina em que o SVServiceBus esteja instalada, o usuário pode também utilizar o WebService diretamente pela url da web, o padrão é [http://localhost/supravizioweb/servicebus/processo/processo.asmx/](if)

WebService no localhost

O WebService ProcessaMensagem aparece disponível, ao clicar nele disponibilizam as seguintes opções:

Chamada pelo WebService

Conclusão, o WebService também pode ser chamado pelo próprio processo.asmx

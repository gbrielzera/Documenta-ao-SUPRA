# Web Services

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Web Services

Através da Biblioteca de Scripts, podemos realizar a criação web services dinamicamente através de scripts Iron Python.

Para ativar esta funcionalidade, basta habilitar a opção **Visível em chamadas web service **ao criar a biblioteca.

Propriedade no cadastro

**Observação**: Caso a opção **Generate web service log **esteja marcada, serão gerados arquivos contendo o log de execução.

Após criada a biblioteca, estas opções poderão ser alteradas na barra de ferramentas através dos botões indicados na figura abaixo:

Botão na barra de ferramentas

Neste tópico, criaremos um exemplo de web service que retornará as Ordens de Serviço usando como parâmetro o cliente das mesmas.

Para isso, utilizamos o seguinte código:

**Biblioteca de Scripts: Web Service**

**Método: ObtemOSPorCliente**

```
import clr
from System import *
from System.Text import StringBuilder
clr.AddReference("Supravizio.Custom")
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import OrdemServico
def ObtemOSPorCliente(usuarioRede):
    xml = StringBuilder()
    try:
        cliente = Pessoa.Carrega("UsuarioRede", usuarioRede)
        if cliente != None:
            dt = DB.ExecuteDataTable("SELECT ID_OCORRENCIA FROM OCORRENCIA WHERE ID_CLIENTE = " + cliente.Id.ToString() + " AND SITUACAO = 'Aberto'")
            if dt.Rows.Count > 0:
                xml.AppendLine("<ORDEMSERVICO>")
                for dr in dt.Rows:
                    os = OrdemServico.Carrega(Convert.ToInt32(dr["ID_OCORRENCIA"]))
                    xml.AppendFormat("<NUMERO>{0}</NUMERO>", os.Numero)
                    xml.AppendFormat("<ASSUNTO>{0}</ASSUNTO>\r\n", os.Assunto)
                xml.AppendLine("</ORDEMSERVICO>")
            else:
                xml.Append("Não foi encontrada nenhuma Ordem de Serviço")
        else:
            xml.Append("Usuário não encontrado")
    except Exception, e:
        xml.Append("Erro ao executar Web Service")
    return xml.ToString()
```

Ao salvar o script, será gerado um arquivo de extensão** .asmx **na pasta do Supravizio Web, no caminho** /ServiceBus/Custom/SOAP**:

Arquivo gerado na pasta do Supravizio Web

Ao acessarmos o endereço através do navegador, serão apresentados os métodos disponíveis e seus respectivos parâmetros:

Página no navegador

É importante que ao realizar a chamada do Web Service seja passado como primeiro parâmetro o token do usuário que será utilizado para acesso e realizar a chamada do web service.

Para gerar um novo token, basta clicar em **Novo **na aba **Token Web Services **no Cadastro de Usuários.

Token passado na chamada

Para realizar o acompanhamento da execução do Web Service, basta acessarmos o caminho **Utilitários | Gerenciamento de Ambiente **e em seguida ir clicar em **Web Services**:

Log de execução

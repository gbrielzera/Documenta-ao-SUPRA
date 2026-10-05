# Ambiente de Qualidade

Caminho: Guia para Administradores > Configurações do Sistema > Ambiente de Qualidade

Comumente utilizamos o ambiente de qualidade para a realização de testes dos processos. Inicialmente criamos o processo e depois é validado, migrando-o para o ambiente de produção.

Podemos configurar os ambiente de duas formas, pelo **Configurador do Supravizio Server** e através do arquivo SVServer.exe.config:

**Na tela de Configurações do Supravizio Server**

Temos que acessar Windows | Todos os programas | Venki Tecnologia | Utilitários | Configurador do Supravizio Server. Basta alterar a caixa de seleção para Qualidade:

Configurador Supravizio Server

Através do arquivo SVServer.exe.config

Temos que acessar o arquivo SVServer.exe.config localizado no diretório em quem o Supravizio Server está instalado.

Geralmente instalamos no local padrão:

C:\Program Files\Venki Tecnologia\Supravizio Server\SVServer.exe.config

Abra o arquivo com um editor de texto e localize a tag "<add key="Ambiente" value="Producao"/>". Temos que alterar a propriedade "value" para "Qualidade", desta forma: <add key="Ambiente" value="Qualidade"/>.

SVServer.exe.config

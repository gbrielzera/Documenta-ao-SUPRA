# LoadWebService

Caminho: Recursos Avançados > Objeto Webservices > LoadWebService

Acessa um webservice e retorna um objeto proxy que podemos utilizar para realizar chamadas usando sintaxe da linguagem IronPython.

Repare no script abaixo que recuperamos o proxy do webservice e o armazenamos em uma variável denominada ws. Em seguida fizemos uma chamada para o método Process desta variável.

Script para chamada Webserivce

Acessando** [http://www.osmobile.com.br/integrador/integrator.asmx?op=Process](http://www.osmobile.com.br/integrador/integrator.asmx?op=Process)**, podemos consultar os parâmetros.

Assinatura do Webservice

Assinatura

public object LoadWebService(string url)

### url

Caminho do Webservice para acesso.

### Retorno

### Objeto proxy que pode ser utilizado para invocar métodos.

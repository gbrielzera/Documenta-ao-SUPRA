# Realizando chamadas Web Service

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Web Services > Realizando chamadas Web Service

No exemplo abaixo, mostraremos como consumir um WebService através de uma página Web. Utilizaremos como exemplo o script criado anteriormente no tópico [Web Services](web_services).

Realizamos a criação de uma página na linguagem PHP com o seguinte código-fonte:

**Exemplo de página PHP**

**Chamada Método: ObtemOSPorCliente**

```
<!DOCTYPE html>
<html>
<body>
<?php
$client = new SoapClient("http://localhost/SupravizioWeb/ServiceBus/Custom/SOAP/WebService.asmx?wsdl"); // Endereço do wsdl correspondente ao serviço a ser utilizado
try {
  $obj = $client->ObtemOSPorCliente(array("usuarioRede" => "ana.beatriz"));
   $myxml = simplexml_load_string ($obj -> ObtemOSPorClienteResult);
   echo $obj -> ObtemOSPorClienteResult;
  } catch (Exception $e) {
  echo "ERRO: " . $e->getMessage();
}
?>
</body>
</html>
```

Ao acessar a página, teremos o seguinte resultado:

Retorno exibido pela página

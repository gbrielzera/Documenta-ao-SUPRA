# ParamInfo

Caminho: Customização > Modelo de objetos > Utilitários > Message > ParamInfo

Descritivo dos parâmetros de envio em formato legível pelo usuário.

**Exemplo 1: modificação da propriedade ParamInfo**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade ParamInfo
message.ParamInfo = "Informações sobre parâmetros de envio";
# salva modificação da propriedade ParamInfo
Message.Salva(message)
```

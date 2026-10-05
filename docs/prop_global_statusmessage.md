# StatusMessage

Caminho: Customização > Modelo de objetos > Utilitários > Global > StatusMessage

Mensagem para esclarecimento sobre a situação. Se a situação for Erro, por exemplo, esta mensagem contém a mensage de Exceção.

**Exemplo 1: modificação da propriedade StatusMessage**

```
# carrega objeto Global de identificador 1
global = Global.Carrega(1)
# modifica a propriedade StatusMessage
global.StatusMessage = "Mensagem associadao a situação";
# salva modificação da propriedade StatusMessage
Global.Salva(global)
```

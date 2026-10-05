# ExpressaoMensagem

Caminho: Customização > Modelo de objetos > Processo > TipoEvento > ExpressaoMensagem

Script para determinar a mensagem gerada no Evento

**Exemplo 1: modificação da propriedade ExpressaoMensagem**

```
# carrega objeto TipoEvento de identificador 1
tipoEvento = TipoEvento.Carrega(1)
# modifica a propriedade ExpressaoMensagem
tipoEvento.ExpressaoMensagem = "Script mensagem";
# salva modificação da propriedade ExpressaoMensagem
TipoEvento.Salva(tipoEvento)
```

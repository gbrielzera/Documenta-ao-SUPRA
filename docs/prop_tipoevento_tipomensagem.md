# TipoMensagem

Caminho: Customização > Modelo de objetos > Processo > TipoEvento > TipoMensagem

Tipo de Mensagem gerada

**Exemplo 1: modificação da propriedade TipoMensagem**

```
# carrega objeto TipoEvento de identificador 1
tipoEvento = TipoEvento.Carrega(1)
# modifica a propriedade TipoMensagem
tipoEvento.TipoMensagem = "Informacao";
# salva modificação da propriedade TipoMensagem
TipoEvento.Salva(tipoEvento)
```

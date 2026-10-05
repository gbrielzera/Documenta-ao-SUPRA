# Descricao

Caminho: Customização > Modelo de objetos > Processo > TipoEvento > Descricao

Texto que descreve claramente quando um Evento deste Tipo ocorre.

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto TipoEvento de identificador 1
tipoEvento = TipoEvento.Carrega(1)
# modifica a propriedade Descricao
tipoEvento.Descricao = "Descrição";
# salva modificação da propriedade Descricao
TipoEvento.Salva(tipoEvento)
```

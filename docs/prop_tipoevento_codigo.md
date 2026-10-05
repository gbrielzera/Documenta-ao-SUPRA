# Codigo

Caminho: Customização > Modelo de objetos > Processo > TipoEvento > Codigo

Código que identifica o Evento

**Exemplo 1: modificação da propriedade Codigo**

```
# carrega objeto TipoEvento de identificador 1
tipoEvento = TipoEvento.Carrega(1)
# modifica a propriedade Codigo
tipoEvento.Codigo = "Código";
# salva modificação da propriedade Codigo
TipoEvento.Salva(tipoEvento)
```

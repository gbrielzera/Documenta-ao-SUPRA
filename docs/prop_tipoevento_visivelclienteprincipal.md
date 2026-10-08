# Propriedade VisivelClientePrincipal

Caminho: Propriedade VisivelClientePrincipal

Indica que um Evento do Tipo é visível para o Cliente na aplicação de Auto-atendimento quando a Ocorrência relacionada for Principal

**Exemplo 1: modificação da propriedade VisivelClientePrincipal**

```
# carrega objeto TipoEvento de identificador 1
tipoEvento = TipoEvento.Carrega(1)
# modifica a propriedade VisivelClientePrincipal
tipoEvento.VisivelClientePrincipal = true;
# salva modificação da propriedade VisivelClientePrincipal
TipoEvento.Salva(tipoEvento)
```

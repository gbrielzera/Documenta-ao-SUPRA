# Propriedade VisivelClienteDerivada

Caminho: Propriedade VisivelClienteDerivada

Indica que um Evento do Tipo é visível para o Cliente na aplicação de Auto-Atendimento quando a Ocorrência relacionada for uma Derivada

**Exemplo 1: modificação da propriedade VisivelClienteDerivada**

```
# carrega objeto TipoEvento de identificador 1
tipoEvento = TipoEvento.Carrega(1)
# modifica a propriedade VisivelClienteDerivada
tipoEvento.VisivelClienteDerivada = true;
# salva modificação da propriedade VisivelClienteDerivada
TipoEvento.Salva(tipoEvento)
```

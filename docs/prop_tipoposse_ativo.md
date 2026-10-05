# Ativo

Caminho: Customização > Modelo de objetos > Ativos > TipoPosse > Ativo

Indica que o Tipo de Posse está ativo no sistema

**Exemplo 1: modificação da propriedade Ativo**

```
# carrega objeto TipoPosse de identificador 1
tipoPosse = TipoPosse.Carrega(1)
# modifica a propriedade Ativo
tipoPosse.Ativo = true;
# salva modificação da propriedade Ativo
TipoPosse.Salva(tipoPosse)
```

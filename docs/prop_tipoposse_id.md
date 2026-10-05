# Id

Caminho: Customização > Modelo de objetos > Ativos > TipoPosse > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Tipo de Posse

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto TipoPosse de identificador 1
tipoPosse = TipoPosse.Carrega(1)
# modifica a propriedade Id
tipoPosse.Id = 1;
# salva modificação da propriedade Id
TipoPosse.Salva(tipoPosse)
```

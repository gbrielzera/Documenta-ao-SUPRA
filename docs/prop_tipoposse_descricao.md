# Descricao

Caminho: Customização > Modelo de objetos > Ativos > TipoPosse > Descricao

Descrição detalhada para o Tipo de Posse

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto TipoPosse de identificador 1
tipoPosse = TipoPosse.Carrega(1)
# modifica a propriedade Descricao
tipoPosse.Descricao = "Descrição";
# salva modificação da propriedade Descricao
TipoPosse.Salva(tipoPosse)
```

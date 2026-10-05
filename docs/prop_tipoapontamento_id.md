# Id

Caminho: Customização > Modelo de objetos > Recurso > TipoApontamento > Id

Identificador do Tipo de Apontamento

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto TipoApontamento de identificador 1
tipoApontamento = TipoApontamento.Carrega(1)
# modifica a propriedade Id
tipoApontamento.Id = 1;
# salva modificação da propriedade Id
TipoApontamento.Salva(tipoApontamento)
```

# Descricao

Caminho: Customização > Modelo de objetos > Recurso > TipoApontamento > Descricao

Descrição do Tipo de Apontamento

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto TipoApontamento de identificador 1
tipoApontamento = TipoApontamento.Carrega(1)
# modifica a propriedade Descricao
tipoApontamento.Descricao = "Descrição";
# salva modificação da propriedade Descricao
TipoApontamento.Salva(tipoApontamento)
```

# Nome

Caminho: Customização > Modelo de objetos > Processo > TipoEvento > Nome

Nome Abreviado do Tipo de Evento

**Exemplo 1: modificação da propriedade Nome**

```
# carrega objeto TipoEvento de identificador 1
tipoEvento = TipoEvento.Carrega(1)
# modifica a propriedade Nome
tipoEvento.Nome = "Nome";
# salva modificação da propriedade Nome
TipoEvento.Salva(tipoEvento)
```

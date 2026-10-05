# Id

Caminho: Customização > Modelo de objetos > Processo > TipoEvento > Id

Número sequencial gerado automaticamente pelo sistema para identificar um Tipo de Evento. Este número não pode ser modificado pelo usuário.

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto TipoEvento de identificador 1
tipoEvento = TipoEvento.Carrega(1)
# modifica a propriedade Id
tipoEvento.Id = 1;
# salva modificação da propriedade Id
TipoEvento.Salva(tipoEvento)
```

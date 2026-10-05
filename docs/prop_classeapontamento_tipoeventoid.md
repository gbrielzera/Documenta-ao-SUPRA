# TipoEventoId

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > TipoEventoId

Identificador do TipoEvento associado

**Exemplo 1: modificação da propriedade TipoEventoId**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade TipoEventoId
classeApontamento.TipoEventoId = 1;
# salva modificação da propriedade TipoEventoId
ClasseApontamento.Salva(classeApontamento)
```

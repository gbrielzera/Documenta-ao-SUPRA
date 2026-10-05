# TipoEventoGerado

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > TipoEventoGerado

Tipo de Evento gerado na ocorrência de um Apontamento

**Exemplo 1: modificação da propriedade TipoEventoGerado**

```
# carrega objeto ClasseApontamento de identificador 78
classeApontamento = ClasseApontamento.Carrega(78)
# modifica a propriedade TipoEventoGerado
classeApontamento.TipoEventoGerado = TipoEvento.Carrega(23);
# salva modificação da propriedade TipoEventoGerado
ClasseApontamento.Salva(classeApontamento)
```

# DataHoraInicio

Caminho: Customização > Modelo de objetos > Recurso > Ausencia > DataHoraInicio

Data e hora de início de validade para a regra de Ausência Temporária

**Exemplo 1: modificação da propriedade DataHoraInicio**

```
# carrega objeto Ausencia de identificador 1
ausencia = Ausencia.Carrega(1)
# modifica a propriedade DataHoraInicio
ausencia.DataHoraInicio = DateTime;
# salva modificação da propriedade DataHoraInicio
Ausencia.Salva(ausencia)
```

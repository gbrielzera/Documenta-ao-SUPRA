# DataHoraRegistro

Caminho: Customização > Modelo de objetos > Recurso > Ausencia > DataHoraRegistro

Data e hora de registro da Ausência Temporária

**Exemplo 1: modificação da propriedade DataHoraRegistro**

```
# carrega objeto Ausencia de identificador 1
ausencia = Ausencia.Carrega(1)
# modifica a propriedade DataHoraRegistro
ausencia.DataHoraRegistro = DateTime;
# salva modificação da propriedade DataHoraRegistro
Ausencia.Salva(ausencia)
```

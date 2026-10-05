# DataHoraPrevisaoRetorno

Caminho: Customização > Modelo de objetos > Recurso > Ausencia > DataHoraPrevisaoRetorno

Data e hora para Previsão de retorno do Solucionador

**Exemplo 1: modificação da propriedade DataHoraPrevisaoRetorno**

```
# carrega objeto Ausencia de identificador 1
ausencia = Ausencia.Carrega(1)
# modifica a propriedade DataHoraPrevisaoRetorno
ausencia.DataHoraPrevisaoRetorno = DateTime;
# salva modificação da propriedade DataHoraPrevisaoRetorno
Ausencia.Salva(ausencia)
```

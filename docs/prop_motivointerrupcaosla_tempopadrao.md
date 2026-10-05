# TempoPadrao

Caminho: Customização > Modelo de objetos > Recurso > MotivoInterrupcaoSLA > TempoPadrao

Tempo máximo (em horas) para finalização de interrupção manuais (exclui interrupções configuradas no processo).

**Exemplo 1: modificação da propriedade TempoPadrao**

```
# carrega objeto MotivoInterrupcaoSLA de identificador 1
motivoInterrupcaoSLA = MotivoInterrupcaoSLA.Carrega(1)
# modifica a propriedade TempoPadrao
motivoInterrupcaoSLA.TempoPadrao = 1;
# salva modificação da propriedade TempoPadrao
MotivoInterrupcaoSLA.Salva(motivoInterrupcaoSLA)
```

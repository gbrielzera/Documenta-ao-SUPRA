# CriterioChargeBack

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > CriterioChargeBack

Forma de Charge-back para Ocorrências do Subprocesso.

**Exemplo 1: modificação da propriedade CriterioChargeBack**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade CriterioChargeBack
classeSubProcesso.CriterioChargeBack = "Hora";
# salva modificação da propriedade CriterioChargeBack
ClasseSubProcesso.Salva(classeSubProcesso)
```

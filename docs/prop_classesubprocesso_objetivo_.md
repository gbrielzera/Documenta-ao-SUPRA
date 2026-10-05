# Objetivo

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > Objetivo

Texto de Referência sobre o Objetivo do Tipo de Subprocesso

**Exemplo 1: modificação da propriedade Objetivo**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade Objetivo
classeSubProcesso.Objetivo = "Documentação";
# salva modificação da propriedade Objetivo
ClasseSubProcesso.Salva(classeSubProcesso)
```

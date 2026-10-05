# Sigla

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > Sigla

Nome abreviado (código) que identifica um Tipo de Subprocesso. Este código pode ser utilizado em scripts para automatismo de processos.

**Exemplo 1: modificação da propriedade Sigla**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade Sigla
classeSubProcesso.Sigla = "INCIDENTE";
# salva modificação da propriedade Sigla
ClasseSubProcesso.Salva(classeSubProcesso)
```

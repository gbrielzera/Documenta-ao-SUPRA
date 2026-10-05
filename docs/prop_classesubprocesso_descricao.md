# Descricao

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > Descricao

Texto que descreve claramente a utilização de um Tipo de Subprocesso

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade Descricao
classeSubProcesso.Descricao = "Incidente";
# salva modificação da propriedade Descricao
ClasseSubProcesso.Salva(classeSubProcesso)
```

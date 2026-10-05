# ResponsavelId

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > ResponsavelId

Identificador da Pessoa associada

**Exemplo 1: modificação da propriedade ResponsavelId**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade ResponsavelId
classeSubProcesso.ResponsavelId = 1;
# salva modificação da propriedade ResponsavelId
ClasseSubProcesso.Salva(classeSubProcesso)
```
